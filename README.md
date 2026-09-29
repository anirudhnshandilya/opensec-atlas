# OpenSec Atlas

### Security knowledge for technology that doesn't have a security textbook yet.

[![Validate Atlas](https://github.com/anirudhnshandilya/opensec-atlas/actions/workflows/validate.yml/badge.svg)](https://github.com/anirudhnshandilya/opensec-atlas/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](LICENSE)
[![Content](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE-DOCS.md)

**OpenSec Atlas is an open, community-driven security atlas for emerging technologies.**

We map technologies to the threats, attacks, defenses, detections, research, benchmarks, and reproducible labs surrounding them — creating a connected body of security knowledge that can evolve with the technology itself.

> **Discover. Reproduce. Test. Defend. Contribute.**

---

## Why OpenSec Atlas?

Technology moves faster than security knowledge.

New protocols, AI systems, developer tools, autonomous agents, cloud primitives, computing models, and software architectures appear long before mature security guidance exists for them.

Security knowledge becomes fragmented across:

* research papers
* vulnerability disclosures
* blog posts
* threat reports
* proof-of-concepts
* detection rules
* benchmarks
* security tools
* conference talks
* internal experiments

OpenSec Atlas aims to connect those pieces into a **living, structured security knowledge base**.

---

## The Atlas

The core idea is simple:

```text
                              TECHNOLOGY
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
           THREATS             RESEARCH          BENCHMARKS
              │                   │                   │
              ▼                   ▼                   ▼
           ATTACKS             EVIDENCE          MEASUREMENTS
              │                   │                   │
              ▼                   │                   │
          DEFENSES                │                   │
              │                   │                   │
              ▼                   ▼                   ▼
         DETECTIONS          REPRODUCIBLE LABS
              │                   │
              └───────────────────┼───────────────────┘
                                  ▼
                         ATLAS KNOWLEDGE
```

Every contribution should make the Atlas more connected, more reproducible, and more useful.

---

## What lives here?

| Area             | Purpose                                                |
| ---------------- | ------------------------------------------------------ |
| **Technologies** | Emerging technologies and their security boundaries    |
| **Threats**      | Security problems affecting those technologies         |
| **Attacks**      | Documented attack techniques and abuse cases           |
| **Defenses**     | Mitigations and defensive engineering patterns         |
| **Detections**   | Detection logic, telemetry, and investigation guidance |
| **Benchmarks**   | Repeatable measurements of security properties         |
| **Research**     | Research questions, experiments, and reproductions     |
| **Labs**         | Reproducible environments for learning and testing     |

The Atlas is designed to connect these objects rather than treat them as isolated documents.

---

# Initial Focus

OpenSec Atlas begins with technologies where security knowledge is evolving particularly quickly.

### AI & Agentic Systems

* AI agents
* Model Context Protocol (MCP)
* AI coding agents
* Browser agents
* RAG systems

### Emerging Computing

* Edge AI
* WebAssembly
* eBPF
* Confidential computing
* Post-quantum cryptography

### Autonomous Systems

* Robotics
* Autonomous systems

This scope will expand as the community identifies new areas where security knowledge is fragmented or immature.

---

# Built for Reproducibility

Security knowledge is more useful when other people can verify it.

Research and technical contributions should provide enough information for others to reproduce the work where practical:

```text
Question
   ↓
Methodology
   ↓
Environment
   ↓
Experiment
   ↓
Evidence
   ↓
Reproduction
   ↓
Atlas Knowledge
```

For research, benchmarks, and labs, contributors should document relevant:

* environments
* dependencies
* configurations
* datasets
* commands
* expected results
* limitations

Reproducibility is a goal, not a claim that every experiment will reproduce perfectly across every environment.

---

# Built for the Community

OpenSec Atlas is intended to support many different kinds of contributors.

You don't need to be a security researcher to contribute.

### Security researchers

Add research, reproductions, experiments, datasets, and findings.

### Red teams

Document attack techniques, abuse cases, and controlled security experiments.

### Blue teams

Develop defenses, detections, telemetry guidance, and investigation techniques.

### Engineers

Contribute tools, benchmarks, automation, schemas, and reproducible environments.

### Students & learners

Build labs, improve documentation, reproduce existing work, and investigate open questions.

### Researchers from adjacent fields

Bring security perspectives from AI, systems, distributed computing, cryptography, robotics, and other emerging disciplines.

### Reviewers

Help verify evidence, improve technical accuracy, and connect related Atlas entries.

---

# Contribution Paths

There is no single way to contribute.

```text
                         OpenSec Atlas
                              │
        ┌─────────────┬───────┼───────┬─────────────┐
        ▼             ▼       ▼       ▼             ▼
    Technology     Threat   Attack  Defense     Research
        │             │       │       │             │
        └─────────────┴───────┴───────┴─────────────┘
                              │
                    ┌─────────┼─────────┐
                    ▼         ▼         ▼
                 Detection  Benchmark   Lab
                              │
                              ▼
                          Evidence
```

You can contribute by:

* adding a technology
* documenting a threat
* researching an attack
* proposing a defense
* writing a detection
* building a benchmark
* reproducing published research
* creating a security lab
* contributing datasets or experiments
* improving documentation
* developing Atlas tooling
* reviewing existing contributions

---

# Structured Knowledge

The Atlas uses machine-readable schemas so that security knowledge can eventually be consumed by tools as well as humans.

Current object types include:

```text
TECH-*       Technologies
THREAT-*     Threats
ATTACK-*     Attacks
DEFENSE-*    Defenses
DETECT-*     Detections
BENCH-*      Benchmarks
RESEARCH-*   Research
LAB-*        Labs
```

This enables future tooling for:

* security knowledge graphs
* cross-reference discovery
* automated validation
* benchmark aggregation
* research indexing
* detection mapping
* security analysis
* visualization
* machine-assisted research

---

# Repository

```text
opensec-atlas/
│
├── atlas/
│   ├── technologies/
│   ├── threats/
│   ├── attacks/
│   ├── defenses/
│   ├── detections/
│   ├── benchmarks/
│   └── research/
│
├── benchmarks/
├── detections/
├── labs/
├── missions/
│
├── research/
│   ├── reproductions/
│   ├── datasets/
│   └── experiments/
│
├── schemas/
├── tools/
├── docs/
│
└── .github/
    ├── ISSUE_TEMPLATE/
    └── workflows/
```

---

# Validation

Contributions are designed to be machine-checkable where structured data is involved.

Run the validator locally:

```bash
python -m pip install jsonschema
python tools/validate_atlas.py
```

Expected result:

```text
Atlas validation passed.
```

Pull requests are also checked automatically through GitHub Actions.

---

# Security Research

OpenSec Atlas is a security research project.

Security testing should be performed only against systems and environments where the contributor has appropriate authorization.

Contributions should clearly distinguish:

* demonstrated behavior
* experimental observations
* documented claims
* hypotheses
* limitations

See [SECURITY.md](SECURITY.md) for the project's security and vulnerability-reporting guidance.

---

# Roadmap

### Phase 1 — Foundation

* [x] Repository structure
* [x] Project documentation
* [x] Contribution framework
* [x] Knowledge schemas
* [x] Initial technology catalog
* [x] Initial threat catalog
* [x] Automated validation

### Phase 2 — Initial Atlas

* [ ] Attack catalog
* [ ] Defense catalog
* [ ] Detection catalog
* [ ] Research catalog
* [ ] Initial security labs
* [ ] Initial benchmarks
* [ ] Cross-linked knowledge

### Phase 3 — Reproducible Security

* [ ] Reproduction framework
* [ ] Standard experiment metadata
* [ ] Benchmark runner
* [ ] Detection testing
* [ ] Reproducible lab environments

### Phase 4 — Community

* [ ] Contributor missions
* [ ] Working groups
* [ ] Review workflows
* [ ] Community-maintained technology areas
* [ ] Contributor documentation

### Phase 5 — Atlas Platform

* [ ] Search
* [ ] Knowledge graph
* [ ] Relationship visualization
* [ ] Benchmark explorer
* [ ] Research explorer
* [ ] Detection mapping
* [ ] Programmatic API

The roadmap is intentionally evolutionary. The community should help determine what the Atlas becomes.

---

# Principles

OpenSec Atlas is built around a few principles:

**Open**
Security knowledge should be accessible and reusable.

**Evidence-driven**
Claims should be supported by evidence where practical.

**Reproducible**
Research and experiments should be repeatable where possible.

**Connected**
Threats, attacks, defenses, detections, research, and technologies should reference one another.

**Technology-neutral**
The Atlas should document security properties rather than promote specific vendors or products.

**Community-owned**
The quality and direction of the Atlas should emerge from transparent community contribution and review.

**Evolving**
The Atlas should change as technologies, threats, and defensive techniques change.

---

# Contributing

Start here:

**[CONTRIBUTING.md](CONTRIBUTING.md)**

You can also open an issue using one of the structured contribution forms.

Every contribution — from fixing a sentence to reproducing a security paper — can improve the Atlas.

---

# License

Code, tooling, schemas, and automation are licensed under the **Apache License 2.0**.

Documentation and Atlas knowledge content are licensed under **CC BY 4.0**, unless otherwise stated.

See:

* [LICENSE](LICENSE)
* [LICENSE-DOCS.md](LICENSE-DOCS.md)

---

# The Goal

OpenSec Atlas is not intended to become another list of security links.

The goal is to build **shared security infrastructure for technologies that are still emerging**.

A place where someone can discover a new technology and move from:

```text
"What is this?"
       ↓
"What can go wrong?"
       ↓
"How can it be attacked?"
       ↓
"How can I reproduce it?"
       ↓
"How can I detect it?"
       ↓
"How can I defend it?"
       ↓
"What evidence exists?"
```

And then contribute the next piece of knowledge.

> **If a technology doesn't have a security textbook yet, help build the Atlas.**
