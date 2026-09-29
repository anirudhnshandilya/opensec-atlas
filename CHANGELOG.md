# Changelog

All notable changes to OpenSec Atlas are documented here.

The project is currently in its early foundation stage. Changes are grouped by release or development milestone rather than by every individual commit.

## [Unreleased]

### Documentation

* Refresh project documentation to better define the purpose, scope, and contribution model of OpenSec Atlas.
* Clarify expectations for security research, evidence, reproducibility, and technical review.
* Improve contributor guidance for adding and maintaining Atlas knowledge.

### Community

* Refine contribution workflows for security researchers, engineers, students, and reviewers.
* Establish clearer standards for technical evidence and responsible security research.

---

## [0.1.0] — Foundation

### Added

#### Project foundation

* Initial OpenSec Atlas repository structure.
* Project governance and roadmap documentation.
* Community Code of Conduct.
* Security reporting guidance.
* Contribution and pull request guidelines.
* Apache-2.0 license for code, tooling, schemas, and automation.
* CC BY 4.0 licensing for Atlas documentation and knowledge content.

#### Atlas schemas

Initial machine-readable schemas for:

* Technologies
* Threats
* Attacks
* Defenses
* Detections
* Benchmarks
* Research
* Labs

#### Initial technology catalog

Added initial Atlas entries covering:

* AI Agents
* Model Context Protocol (MCP)
* AI Coding Agents
* Browser Agents

#### Initial threat catalog

Added initial entries covering:

* Prompt Injection
* Excessive Agent Permissions
* Agent Tool Abuse
* Untrusted Context

#### Repository automation

* Added Atlas schema validation tooling.
* Added GitHub Actions validation workflow.
* Added issue templates for technology, research, security research, feature, and bug contributions.
* Added pull request template with evidence, validation, reproducibility, and security checks.

### Validation

The repository includes automated validation for machine-readable Atlas content using JSON Schema.

Local validation:

```bash
python -m pip install jsonschema
python tools/validate_atlas.py
```

## Versioning

OpenSec Atlas is currently pre-1.0.

Version numbers will evolve as the project moves from foundation work toward a stable contribution and knowledge model.

Until then, the changelog records meaningful project milestones rather than treating every commit as a release.

---

[Unreleased]: https://github.com/anirudhnshandilya/opensec-atlas/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/anirudhnshandilya/opensec-atlas/releases/tag/v0.1.0
