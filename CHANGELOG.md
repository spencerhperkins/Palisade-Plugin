# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Skill: `prosecution-history`, which reads the file wrapper of any US application from the USPTO Open Data Portal.

### Changed

- `chart` traces prosecution history for claim construction and equivalents instead of asking the user for it.
- `patent-search-fundamentals` adds a citation format for prosecution papers.

## [0.1.0] - 2026-09-24

### Added

- Initial release: Palisade MCP connector config.
- Skills: `patent-search-fundamentals`, `prior-art-search`, and `chart` (invalidity, infringement, and claim construction charts).
- Commands: `/invalidity` and `/chart`.

[Unreleased]: https://github.com/spencerhperkins/palisade-plugin/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/spencerhperkins/palisade-plugin/releases/tag/v0.1.0
