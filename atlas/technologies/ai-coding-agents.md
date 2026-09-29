\# AI Coding Agents



\*\*ID:\*\* `TECH-AI-CODING-AGENTS`



\*\*Category:\*\* Developer Security



\*\*Status:\*\* Active



\## Description



AI coding agents are AI-powered systems that can inspect software projects, generate or modify code, execute development tools, run tests, and interact with development environments.



Their ability to perform actions beyond code generation introduces security considerations around repository access, command execution, credentials, dependency changes, and modifications to development infrastructure.



\## Security Questions



Important security questions include:



\- Which files and repositories can the agent access?

\- Which commands can the agent execute?

\- What credentials or secrets are available to the agent?

\- Can untrusted repository content influence agent behavior?

\- Are generated changes reviewed before execution or deployment?

\- How are dependency and supply-chain risks handled?

\- Are agent actions logged and attributable?



\## Security Areas



Relevant areas include:



\- Repository compromise

\- Command execution

\- Prompt injection

\- Secret exposure

\- Dependency manipulation

\- Supply-chain security

\- Credential misuse

\- CI/CD security

\- Sandbox isolation

\- Code review

\- Agent action auditing



\## References



Further references should be added as the Atlas develops.



\## Related Threats



\- `THREAT-PROMPT-INJECTION`

\- `THREAT-EXCESSIVE-AGENT-PERMISSIONS`

\- `THREAT-AGENT-TOOL-ABUSE`

