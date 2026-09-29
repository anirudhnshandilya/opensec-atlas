# Contributing to OpenSec Atlas

OpenSec Atlas is built by people who want emerging technologies to have better security knowledge.

You can contribute through research, engineering, documentation, experimentation, review, or simply by improving something that is unclear.

> **You do not need to be an expert to contribute.**

Good questions, careful reproductions, useful references, and well-documented failures are valuable contributions.

---

# Before You Start

Please read:

* [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
* [SECURITY.md](SECURITY.md)
* [GOVERNANCE.md](GOVERNANCE.md)

For security-sensitive research, make sure you have appropriate authorization before testing a system.

---

# What Can I Contribute?

OpenSec Atlas has several contribution paths.

## Technologies

Document an emerging technology and its security boundaries.

Examples:

* AI agents
* protocols
* developer platforms
* computing environments
* infrastructure technologies
* autonomous systems

A technology contribution should explain what the technology is and why it creates interesting security questions.

---

## Threats

Document a security threat affecting a technology.

A useful threat entry should explain:

* what the threat is
* which technologies are affected
* potential security impact
* relevant mitigations
* supporting evidence

---

## Attacks

Document an attack technique, abuse case, or security experiment.

Where appropriate, include:

* prerequisites
* affected technology
* threat relationship
* attack methodology
* observed impact
* limitations
* references

Security testing must be authorized.

---

## Defenses

Document a mitigation or defensive engineering technique.

Examples include:

* authorization controls
* isolation
* input validation
* monitoring
* hardening
* secure architecture
* policy enforcement

Explain what threat or attack the defense addresses and describe relevant limitations.

---

## Detections

Contribute detection logic and investigation guidance.

Useful detection contributions may include:

* telemetry requirements
* detection logic
* queries
* behavioral indicators
* false-positive considerations
* investigation guidance

Detections should explain what they are intended to identify and under what assumptions they operate.

---

## Benchmarks

Create repeatable measurements of security properties.

A benchmark should clearly describe:

* objective
* target technology
* environment
* metrics
* methodology
* reproduction procedure
* limitations

Benchmarks should avoid ambiguous measurements where possible.

---

## Research

Research contributions can include:

* original research
* research reproductions
* experiments
* negative results
* datasets
* methodological investigations
* security analyses

A research contribution should distinguish clearly between established evidence, observations, assumptions, and conclusions.

---

## Labs

Build controlled environments where security concepts can be reproduced safely.

Labs should document:

* prerequisites
* setup
* procedure
* expected result
* cleanup
* relevant security considerations

Labs involving offensive techniques must be designed for authorized environments.

---

# Documentation Contributions

Documentation improvements are first-class contributions.

You can contribute by:

* correcting errors
* improving explanations
* adding references
* clarifying terminology
* improving examples
* fixing broken links
* improving navigation
* adding diagrams
* translating content

Small improvements matter.

---

# Machine-Readable Content

Structured Atlas objects use stable identifiers.

Current prefixes include:

```text
TECH-*       Technology
THREAT-*     Threat
ATTACK-*     Attack
DEFENSE-*    Defense
DETECT-*     Detection
BENCH-*      Benchmark
RESEARCH-*   Research
LAB-*        Lab
```

When creating a new structured object:

1. choose the appropriate object type
2. create a unique identifier
3. follow the corresponding schema
4. connect related objects where appropriate
5. provide references and evidence where applicable

---

# Evidence and References

OpenSec Atlas aims to be evidence-driven.

Useful sources may include:

* peer-reviewed research
* conference papers
* technical specifications
* standards
* security advisories
* vulnerability databases
* official technical documentation
* reproducible experiments
* well-documented security investigations

When making a security claim, provide enough information for another contributor to understand where the claim comes from.

Do not present speculation as established fact.

---

# Reproducibility

For research, experiments, benchmarks, and labs, provide reproducibility information where practical.

Useful details include:

```text
Environment
Dependencies
Versions
Configuration
Dataset
Commands
Procedure
Expected result
Observed result
Limitations
```

A failed reproduction is still useful if it is documented accurately.

---

# Local Development

Clone the repository:

```bash
git clone https://github.com/anirudhnshandilya/opensec-atlas.git
cd opensec-atlas
```

Install the validation dependency:

```bash
python -m pip install jsonschema
```

Run validation:

```bash
python tools/validate_atlas.py
```

Expected result:

```text
Atlas validation passed.
```

---

# Pull Requests

Before opening a pull request:

```bash
python tools/validate_atlas.py
git diff --check
```

Please keep pull requests:

* focused
* understandable
* reproducible where applicable
* appropriately referenced
* free of secrets
* limited to authorized security research

Avoid combining unrelated changes into one pull request.

---

# Pull Request Checklist

Before submitting, check:

* [ ] The change has a clear purpose.
* [ ] Relevant documentation has been updated.
* [ ] Structured data follows the appropriate schema.
* [ ] IDs follow Atlas conventions.
* [ ] Related entries are linked where appropriate.
* [ ] References are included where useful.
* [ ] Validation passes.
* [ ] No secrets or credentials are included.
* [ ] Security testing was authorized.
* [ ] Reproduction information is included where applicable.
* [ ] Limitations are documented where relevant.

---

# Security Research Rules

OpenSec Atlas supports security research, including offensive security research.

However, contributions must remain within authorized environments.

Do not:

* attack systems without permission
* publish credentials or secrets
* expose private information
* intentionally disrupt third-party services
* upload malware intended to harm users
* use the repository to facilitate unauthorized access

For vulnerability reports affecting OpenSec Atlas itself, follow [SECURITY.md](SECURITY.md).

---

# Review Process

Contributions may be reviewed for:

### Technical accuracy

Does the contribution accurately describe the technology, threat, attack, defense, or research?

### Evidence

Are important claims supported?

### Reproducibility

Can another contributor understand or reproduce the work?

### Security

Was the research performed appropriately and within authorization?

### Scope

Does the contribution belong in OpenSec Atlas?

### Maintainability

Is the contribution structured so that future contributors can extend it?

Reviewers may request changes before a contribution is accepted.

---

# Good Contributions

A strong contribution does not need to be large.

Examples:

> Add one well-researched threat to an emerging technology.

> Reproduce one experiment from a published paper.

> Build a small lab demonstrating a documented attack.

> Add a detection for a known behavior.

> Improve a benchmark so its measurements are reproducible.

> Connect an existing threat to relevant defenses.

> Fix an inaccurate security claim.

The objective is not to maximize the number of files.

The objective is to increase the quality and connectedness of the Atlas.

---

# Proposing Larger Changes

For substantial changes, open an issue before beginning implementation.

Examples:

* new technology domains
* new object types
* schema changes
* benchmark frameworks
* automated analysis
* major tooling
* new community workflows

This gives maintainers and contributors an opportunity to discuss the design before significant work begins.

---

# Attribution

Respect the licenses and attribution requirements of third-party research, datasets, documentation, code, and other materials.

Do not copy third-party material into the repository unless its license permits redistribution.

When reproducing research, clearly identify the original work.

---

# Community

OpenSec Atlas is intended to be community-maintained.

Contributors are encouraged to:

* review pull requests
* improve existing entries
* challenge unsupported claims
* propose research questions
* reproduce experiments
* connect related knowledge
* help new contributors

The Atlas becomes more valuable as more people independently verify and improve it.

---

# Questions

If you are unsure where a contribution belongs, open an issue and describe what you are trying to add.

A maintainer or community member can help identify the appropriate contribution path.

---

**OpenSec Atlas**

*Discover. Reproduce. Test. Defend. Contribute.*
