# OpenSec Atlas Roadmap

OpenSec Atlas is building an open security knowledge layer for technologies whose security practices are still being discovered.

The roadmap is intentionally directional. Priorities may change as technologies, research, and the contributor community evolve.

The project is currently in the **foundation stage**.

---

## 1. Foundation

**Status: In progress**

Build the repository and data model needed for the Atlas to grow without becoming an unstructured collection of links.

### Repository

* [x] Establish repository structure
* [x] Define licensing model
* [x] Add contribution guidelines
* [x] Add governance documentation
* [x] Add security reporting guidance
* [x] Add Code of Conduct
* [x] Add pull request and issue templates
* [x] Add automated repository validation
* [ ] Add contributor ownership documentation
* [ ] Add project citation metadata

### Atlas model

* [x] Define technology schema
* [x] Define threat schema
* [x] Define attack schema
* [x] Define defense schema
* [x] Define detection schema
* [x] Define benchmark schema
* [x] Define research schema
* [x] Define lab schema
* [ ] Define relationships between Atlas objects more formally
* [ ] Define object lifecycle and status rules
* [ ] Define evidence and confidence metadata
* [ ] Define versioning strategy for Atlas objects

### Initial knowledge

* [x] AI Agents
* [x] Model Context Protocol
* [x] AI Coding Agents
* [x] Browser Agents
* [x] Prompt Injection
* [x] Excessive Agent Permissions
* [x] Agent Tool Abuse
* [x] Untrusted Context
* [ ] Add initial attacks
* [ ] Add initial defenses
* [ ] Add initial detections
* [ ] Add initial research records
* [ ] Add initial reproducible labs
* [ ] Add initial benchmarks

---

## 2. Build the Initial Atlas

**Status: Next**

Turn the initial taxonomy into a useful body of connected security knowledge.

### Expand the agent-security area

Priorities include:

* prompt injection;
* indirect prompt injection;
* tool abuse;
* excessive agency;
* credential exposure;
* sensitive-data exfiltration;
* malicious tool behavior;
* insecure tool authorization;
* agent-to-agent trust;
* memory and context manipulation;
* untrusted retrieved content;
* supply-chain risks;
* unsafe autonomous actions.

Each major area should connect relevant:

**Technology → Threat → Attack → Defense → Detection → Research → Lab**

### Expand technology coverage

Initial areas to investigate:

* RAG systems
* AI assistants
* browser automation agents
* software engineering agents
* agent protocols
* tool-use frameworks
* model gateways
* local AI runtimes

Later areas may include:

* Edge AI
* WebAssembly
* eBPF
* Confidential Computing
* Post-Quantum Cryptography
* Robotics
* Autonomous Systems

New technologies should be added when there is enough security substance to justify an Atlas entry.

---

## 3. Reproducible Security Research

**Status: Planned**

Move beyond documenting security knowledge toward making security claims easier to test.

### Research records

Build a consistent format for recording:

* research question;
* hypothesis;
* methodology;
* environment;
* dependencies;
* configuration;
* datasets;
* commands;
* measurements;
* results;
* limitations;
* reproduction status.

### Reproduction infrastructure

Develop reusable mechanisms for:

* environment capture;
* dependency pinning;
* experiment configuration;
* result recording;
* artifact storage;
* reproduction instructions;
* independent verification.

The objective is not merely to collect papers.

It is to make meaningful security claims **testable**.

---

## 4. Security Labs

**Status: Planned**

Create controlled environments where contributors can reproduce security behavior safely.

Labs should provide:

* isolated environments;
* explicit prerequisites;
* setup instructions;
* reproducible procedures;
* expected results;
* cleanup instructions;
* safety boundaries;
* references to the relevant Atlas objects.

Possible early labs:

* prompt-injection demonstrations;
* agent tool authorization failures;
* malicious tool scenarios;
* browser-agent manipulation;
* insecure coding-agent workflows;
* data-exfiltration scenarios.

Labs should prioritize educational and defensive value and remain within authorized testing environments.

---

## 5. Detection Engineering

**Status: Planned**

Build a detection layer connected directly to documented threats and attacks.

Explore support for:

* behavioral detections;
* telemetry requirements;
* log sources;
* detection logic;
* SIEM rules;
* endpoint signals;
* application telemetry;
* agent audit logs;
* tool invocation monitoring;
* false-positive analysis.

The long-term objective is to answer:

> **If this attack happens, what evidence should a defender expect to see?**

---

## 6. Security Benchmarks

**Status: Planned**

Create reproducible ways to measure security properties rather than relying exclusively on qualitative claims.

Potential benchmark areas:

* prompt-injection resistance;
* tool authorization;
* agent permission boundaries;
* data-exfiltration resistance;
* sandbox escape resistance;
* detection coverage;
* security-control effectiveness;
* reproducibility of published attacks.

Benchmarks should document their:

* objective;
* environment;
* metrics;
* methodology;
* limitations;
* reproduction procedure.

Benchmark results should remain traceable to the exact methodology and environment used to produce them.

---

## 7. Knowledge Graph

**Status: Planned**

The Atlas should eventually become more than a directory.

Build explicit relationships between objects:

```text
Technology
    ↓
Threat
    ↓
Attack
    ↓
Defense
    ↓
Detection
    ↓
Evidence
    ↓
Research / Lab / Benchmark
```

Potential capabilities:

* cross-reference discovery;
* attack-to-defense mapping;
* threat-to-detection mapping;
* research-to-technology mapping;
* evidence provenance;
* dependency and relationship visualization;
* machine-readable Atlas queries.

The objective is to make relationships between security knowledge discoverable.

---

## 8. Contributor Missions

**Status: Planned**

Make it easy for someone to contribute without first understanding the entire repository.

Introduce focused missions such as:

* document a technology;
* map a threat;
* reproduce an attack;
* implement a defense;
* write a detection;
* reproduce a research result;
* build a lab;
* create a benchmark;
* verify an existing Atlas entry;
* improve documentation.

Missions should have clear scopes, expected outputs, and acceptance criteria.

---

## 9. Community Review

**Status: Planned**

As the Atlas grows, establish stronger mechanisms for technical review.

Potential areas:

* domain maintainers;
* research reviewers;
* detection reviewers;
* benchmark reviewers;
* technology-area ownership;
* contributor recognition;
* review history;
* correction workflows.

The goal is to scale review without turning contribution into bureaucracy.

---

## 10. Atlas Tooling

**Status: Planned**

Build tooling around the underlying structured knowledge.

Potential tools include:

* Atlas CLI;
* schema validation;
* reference validation;
* relationship validation;
* duplicate detection;
* broken-link detection;
* evidence checks;
* Atlas search;
* object generation;
* contribution linting;
* benchmark runners;
* research artifact checks.

Eventually, the Atlas should be useful both to humans and to machines.

---

## 11. Atlas Platform

**Status: Long term**

If the underlying repository and knowledge model prove useful, build interfaces on top of them.

Potential capabilities:

* searchable Atlas;
* interactive knowledge graph;
* threat explorer;
* attack explorer;
* detection explorer;
* benchmark explorer;
* research explorer;
* technology security profiles;
* API access;
* machine-readable exports;
* contributor dashboards.

The platform should remain downstream of the open repository rather than becoming a replacement for it.

---

# What Success Looks Like

OpenSec Atlas should eventually make it possible to take an unfamiliar technology and answer:

**What is it?**

→ **What can go wrong?**

→ **How can it be attacked?**

→ **Can the behavior be reproduced?**

→ **What evidence exists?**

→ **How can it be detected?**

→ **How can it be defended?**

→ **How reliable is the evidence?**

That is the core loop of the project.

---

# Near-Term Priorities

Before expanding into dozens of technologies, the project will prioritize depth over breadth.

The immediate sequence is:

1. **Strengthen the Atlas data model**
2. **Build the first connected technology/threat/attack set**
3. **Add reproducible security labs**
4. **Add defensive detections**
5. **Add research reproductions**
6. **Add the first security benchmarks**
7. **Make contribution missions easy to discover**
8. **Improve automated validation and review tooling**

Only then should the project aggressively expand into additional technology domains.

---

# Guiding Principle

> **Don't build a catalogue of security links. Build infrastructure for security knowledge.**
