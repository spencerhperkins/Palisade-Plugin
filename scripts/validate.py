#!/usr/bin/env python3
"""Validate the Palisade plugin marketplace repo.

Standard library only. Run from anywhere:

    python scripts/validate.py

Checks:
  1. marketplace.json and each local plugin.json parse and have required fields;
     marketplace and plugin names are kebab-case and match between files;
     every relative plugin source starts with ./ and contains .claude-plugin/plugin.json.
  2. Plugin versions match between marketplace.json and plugin.json.
  3. .mcp.json parses; each server is type "http" with an https:// url and no
     Authorization header.
  4. Each skills/<folder>/SKILL.md has frontmatter `name` equal to the folder name
     and a non-empty `description` under 1024 characters. A missing SKILL.md is a
     warning, not an error.
  5. Each commands/*.md has `description` frontmatter, and every backticked
     kebab-case name in the body is an existing skill.
  6. Each evals/cases/*.json contains the required keys from evals/schema.json.
  7. No tracked file contains secret-like strings.

Unfilled {{PLACEHOLDER}} values are reported as a single warning.
Exits 1 if any errors were found, 0 otherwise.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SELF = Path(__file__).resolve()

KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PLACEHOLDER = re.compile(r"\{\{[A-Z0-9_]+\}\}")
BACKTICKED_NAME = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)*)`")
SECRET_PATTERNS = [
    ("sk- API key", re.compile(r"\bsk-[A-Za-z0-9_\-]{16,}")),
    ("Bearer token", re.compile(r"\bBearer\s+[A-Za-z0-9\-._~+/]{8,}")),
    ("api_key", re.compile(r"api[_-]?key\s*[:=]\s*[\"']?[A-Za-z0-9_\-]{16,}", re.I)),
    ("PEM block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
]

errors: list[str] = []
warnings: list[str] = []


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def error(path: Path, message: str) -> None:
    errors.append(f"{rel(path)}: {message}")


def warn(path: Path, message: str) -> None:
    warnings.append(f"{rel(path)}: {message}")


def load_json(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        error(path, "file not found")
        return None
    except json.JSONDecodeError as exc:
        error(path, f"invalid JSON: {exc}")
        return None
    if not isinstance(data, dict):
        error(path, "top level must be a JSON object")
        return None
    return data


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str] | None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        error(path, "missing frontmatter (file must start with ---)")
        return None
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        error(path, "frontmatter is not closed with ---")
        return None
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.startswith((" ", "\t", "#")):
            continue
        key, sep, value = line.partition(":")
        if not sep:
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        fields[key.strip()] = value
    body = "\n".join(lines[end + 1 :])
    return fields, body


def check_plugin(entry: dict, marketplace_path: Path) -> None:
    name = entry.get("name")
    source = entry.get("source")
    if not isinstance(name, str) or not name:
        error(marketplace_path, "plugin entry is missing `name`")
        return
    if not KEBAB.match(name):
        error(marketplace_path, f"plugin name {name!r} must be kebab-case")
    if source is None:
        error(marketplace_path, f"plugin {name!r} is missing `source`")
        return
    if not isinstance(source, str):
        return
    if not source.startswith("./"):
        error(marketplace_path, f"plugin {name!r} source {source!r} must start with ./")
        return

    plugin_dir = (ROOT / source).resolve()
    manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
    if not manifest_path.is_file():
        error(marketplace_path, f"plugin {name!r} source has no .claude-plugin/plugin.json")
        return

    manifest = load_json(manifest_path)
    if manifest is None:
        return
    manifest_name = manifest.get("name")
    if not isinstance(manifest_name, str) or not manifest_name:
        error(manifest_path, "missing `name`")
    elif not KEBAB.match(manifest_name):
        error(manifest_path, f"name {manifest_name!r} must be kebab-case")
    elif manifest_name != name:
        error(manifest_path, f"name {manifest_name!r} does not match marketplace entry {name!r}")

    entry_version = entry.get("version")
    manifest_version = manifest.get("version")
    if entry_version and manifest_version and entry_version != manifest_version:
        error(
            manifest_path,
            f"version {manifest_version!r} does not match marketplace.json {entry_version!r}",
        )

    check_mcp(plugin_dir / ".mcp.json")
    skills = check_skills(plugin_dir / "skills")
    check_commands(plugin_dir / "commands", skills)


def check_mcp(path: Path) -> None:
    if not path.exists():
        return
    data = load_json(path)
    if data is None:
        return
    servers = data.get("mcpServers")
    if not isinstance(servers, dict) or not servers:
        error(path, "`mcpServers` must be a non-empty object")
        return
    for server_name, server in servers.items():
        if not isinstance(server, dict):
            error(path, f"server {server_name!r} must be an object")
            continue
        if server.get("type") != "http":
            error(path, f"server {server_name!r} must have type \"http\"")
        url = server.get("url")
        if not isinstance(url, str) or not url.startswith("https://"):
            error(path, f"server {server_name!r} url must start with https://")
        headers = server.get("headers") or {}
        if any(key.lower() == "authorization" for key in headers):
            error(path, f"server {server_name!r} must not hardcode an Authorization header")


def check_skills(skills_dir: Path) -> set[str]:
    names: set[str] = set()
    if not skills_dir.is_dir():
        return names
    for folder in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        names.add(folder.name)
        skill_path = folder / "SKILL.md"
        if not skill_path.is_file():
            warn(folder, "no SKILL.md")
            continue
        parsed = parse_frontmatter(skill_path)
        if parsed is None:
            continue
        fields, _ = parsed
        if fields.get("name") != folder.name:
            error(skill_path, f"frontmatter name {fields.get('name')!r} must equal folder name {folder.name!r}")
        description = fields.get("description", "")
        if not description:
            error(skill_path, "frontmatter `description` is empty")
        elif len(description) >= 1024:
            error(skill_path, f"description is {len(description)} characters (must be under 1024)")
    return names


def check_commands(commands_dir: Path, skills: set[str]) -> None:
    if not commands_dir.is_dir():
        return
    for path in sorted(commands_dir.glob("*.md")):
        parsed = parse_frontmatter(path)
        if parsed is None:
            continue
        fields, body = parsed
        if not fields.get("description"):
            error(path, "frontmatter `description` is missing")
        for name in sorted(set(BACKTICKED_NAME.findall(body))):
            if name not in skills:
                error(path, f"references `{name}`, which is not a skill in this plugin")


def check_evals() -> None:
    schema_path = ROOT / "evals" / "schema.json"
    cases_dir = ROOT / "evals" / "cases"
    if not schema_path.exists():
        return
    schema = load_json(schema_path)
    if schema is None:
        return
    required = schema.get("required", [])
    for path in sorted(cases_dir.glob("*.json")) if cases_dir.is_dir() else []:
        case = load_json(path)
        if case is None:
            continue
        missing = [key for key in required if key not in case]
        if missing:
            error(path, f"missing required keys: {', '.join(missing)}")


def repo_files() -> list[Path]:
    try:
        output = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        return [ROOT / line for line in output.splitlines() if line]
    except (OSError, subprocess.CalledProcessError):
        return [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]


def check_files() -> None:
    placeholder_files: list[str] = []
    for path in repo_files():
        if path.resolve() == SELF or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                error(path, f"contains a secret-like string ({label})")
        if PLACEHOLDER.search(text):
            placeholder_files.append(rel(path))
    if placeholder_files:
        warnings.append(f"unfilled {{{{PLACEHOLDER}}}} values in: {', '.join(placeholder_files)}")


def main() -> int:
    marketplace_path = ROOT / ".claude-plugin" / "marketplace.json"
    marketplace = load_json(marketplace_path)
    if marketplace is not None:
        name = marketplace.get("name")
        if not isinstance(name, str) or not name:
            error(marketplace_path, "missing `name`")
        elif not KEBAB.match(name):
            error(marketplace_path, f"name {name!r} must be kebab-case")
        owner = marketplace.get("owner")
        if not isinstance(owner, dict) or not owner.get("name"):
            error(marketplace_path, "missing `owner.name`")
        plugins = marketplace.get("plugins")
        if not isinstance(plugins, list) or not plugins:
            error(marketplace_path, "`plugins` must be a non-empty list")
        else:
            for entry in plugins:
                if isinstance(entry, dict):
                    check_plugin(entry, marketplace_path)
                else:
                    error(marketplace_path, "each plugin entry must be an object")

    check_evals()
    check_files()

    for message in warnings:
        print(f"  WARNING: {message}")
    for message in errors:
        print(f"  ERROR: {message}")
    if errors:
        print(f"Validation failed with {len(errors)} error(s).")
        return 1
    print(f"Validation passed with {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
