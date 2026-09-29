# OpenSec Atlas Governance

OpenSec Atlas is an open security research and engineering project.

The repository is maintained as a community project. Governance exists to keep contributions technically useful, security-conscious, and open to review while avoiding unnecessary bureaucracy.

## 1. Project Principles

OpenSec Atlas is built around a few basic principles:

* **Technical merit over status.** Contributions are evaluated on their substance, evidence, clarity, and usefulness.
* **Evidence over assertion.** Security claims should be supported by references, experiments, demonstrations, or clearly identified assumptions.
* **Reproducibility matters.** When practical, research and experiments should provide enough information for others to reproduce or challenge the result.
* **Disagreement is healthy.** Technical disagreement should be resolved through evidence and reasoning rather than authority.
* **Security research must be responsible.** Contributions must respect authorization, privacy, safety, and applicable law.
* **The Atlas belongs to its contributors.** No individual should treat the project as personal proprietary infrastructure.

## 2. Maintainers

Maintainers are trusted contributors responsible for keeping the repository healthy.

Their responsibilities include:

* reviewing pull requests;
* maintaining repository structure and schemas;
* resolving technical disagreements when necessary;
* protecting the quality and integrity of Atlas content;
* maintaining project automation;
* coordinating larger changes;
* responding to security reports;
* helping new contributors navigate the project.

Maintainers do not have unrestricted authority over technical truth. A maintainer's decision should be explainable in terms of project principles, technical evidence, repository policy, or practical project constraints.

## 3. Becoming a Maintainer

Maintainer status is earned through sustained contribution.

Relevant factors include:

* consistent high-quality contributions;
* technically sound reviews;
* familiarity with the Atlas data model;
* responsible handling of security research;
* constructive participation in discussions;
* willingness to maintain work beyond the initial contribution;
* demonstrated commitment to the project's long-term direction.

There is no fixed contribution count that automatically grants maintainer status.

Maintainers may invite established contributors to join the maintainer group when there is a clear need for additional ownership.

## 4. Decision Making

Most changes should be decided through the normal pull-request process.

For routine changes:

1. A contributor opens an issue or pull request where appropriate.
2. The change is reviewed publicly.
3. Reviewers raise technical, security, documentation, or reproducibility concerns.
4. The contributor addresses the relevant feedback.
5. A maintainer merges the change when it meets the project's standards.

For larger architectural changes, contributors should open an issue or design discussion before implementation.

Examples include:

* changing the Atlas schema;
* introducing a new top-level repository area;
* changing contribution or review policy;
* introducing significant automation;
* changing licensing;
* changing the project's security-research boundaries.

## 5. Technical Disagreements

Technical disagreement should be handled openly.

When contributors disagree, the preferred order is:

**evidence → experiment → reproducibility → technical reasoning → maintainer decision**

Where evidence is incomplete, uncertainty should be recorded rather than hidden.

A maintainer may close a discussion when a decision is required for project progress, but the reasoning should be documented when the decision has lasting technical consequences.

## 6. Atlas Content

Atlas entries should distinguish between different levels of certainty.

Contributors should avoid presenting:

* hypotheses as established facts;
* unverified claims as reproduced results;
* demonstrations as universal vulnerabilities;
* vendor claims as independent evidence;
* experimental observations as guarantees.

Where appropriate, entries should identify whether information is:

* documented;
* experimentally observed;
* independently reproduced;
* disputed;
* unresolved;
* deprecated.

The repository's schemas and contribution guidelines define the expected structure for machine-readable content.

## 7. Security Research

OpenSec Atlas supports legitimate security research.

Contributors are responsible for ensuring that their work is authorized and conducted in an appropriate environment.

Do not submit material that requires:

* unauthorized access;
* theft or disclosure of credentials;
* exposure of private information;
* destructive activity against third-party systems;
* persistence on systems without authorization;
* malware deployment outside an authorized research environment;
* disruption of production services.

Potentially sensitive vulnerabilities should be reported according to `SECURITY.md` rather than publicly disclosed through a normal pull request.

## 8. Research Integrity

OpenSec Atlas depends on contributors being precise about what their work demonstrates.

Contributors should not:

* fabricate results;
* alter measurements to support a conclusion;
* conceal material limitations;
* misrepresent a reproduction;
* claim independent validation without performing it;
* remove contradictory evidence without explanation;
* present generated or synthetic evidence as real-world evidence.

Corrections are expected and encouraged.

A correction to an earlier contribution is preferable to leaving an inaccurate security claim in the Atlas.

## 9. Conflicts of Interest

Contributors should disclose relevant conflicts of interest when they materially affect a contribution.

Examples include:

* evaluating a product developed by the contributor;
* reporting research funded by an interested organization;
* contributing on behalf of a vendor whose technology is being assessed;
* benchmarking competing technologies where the contributor has a direct interest in the outcome.

A conflict does not automatically invalidate research. Transparency allows reviewers to evaluate the work appropriately.

## 10. Content Removal and Corrections

Atlas content may be corrected, replaced, or removed when it is:

* demonstrably inaccurate;
* misleading;
* improperly sourced;
* plagiarized;
* unsafe;
* legally problematic;
* based on unauthorized disclosure of sensitive information;
* incompatible with the project's contribution standards.

Material corrections should preserve an understandable history where practical.

## 11. Changes to Governance

Governance changes should be proposed publicly and reviewed before adoption.

Changes affecting:

* licensing;
* security-research policy;
* contribution requirements;
* maintainer authority;
* project ownership;
* repository structure;

should receive particular scrutiny because they affect the long-term operation of the project.

The project should prefer incremental governance changes over unnecessary process.

## 12. Community Standards

All contributors are expected to follow the project's Code of Conduct.

Technical expertise, professional position, academic affiliation, employer, or contributor history does not exempt anyone from these standards.

See [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## 13. Project Direction

The roadmap describes the intended direction of OpenSec Atlas, but it is not a promise that every planned item will be implemented.

Priorities may change as:

* new technologies emerge;
* security research changes understanding of a threat;
* contributors identify more valuable work;
* community needs evolve;
* practical maintenance constraints become clear.

The goal is not to build the largest possible repository.

The goal is to build **useful, trustworthy, connected security knowledge for technologies whose security knowledge is still emerging.**
