# Contributing

Thanks for helping improve Palisade. This repo contains only plugin configuration, skills, and commands. There is no server code here.

## Adding a skill

1. Create `plugins/palisade/skills/<kebab-name>/SKILL.md`.
2. Start the file with frontmatter that includes:
   - `name`: must match the folder name exactly.
   - `description`: one or two sentences on when to use the skill (under 1024 characters).
3. Every skill defers to `patent-search-fundamentals` for the search tools, query writing, the search log, dates, patent term, citations, claim language, families and assignees, and output rules. Do not restate those rules; reference that skill instead, and add to it if a new rule applies to more than one skill.

## Adding a command

Commands live in `plugins/palisade/commands/<name>.md`. Each needs `description` and `argument-hint` frontmatter and a short body that points to a skill by name in backticks. Keep the workflow logic in the skill, not the command.

## Before opening a pull request

Run both checks from the repo root:

```
python scripts/validate.py
claude plugin validate .
```

Fix any errors. Never commit credentials, tokens, or API keys.
