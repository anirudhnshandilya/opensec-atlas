\# Untrusted Context



\*\*ID:\*\* `THREAT-UNTRUSTED-CONTEXT`



\*\*Severity:\*\* High



\*\*Status:\*\* Documented



\## Description



Untrusted context occurs when an AI system processes information from sources that cannot be assumed to be trustworthy, while that information can influence model decisions or downstream actions.



Examples include web pages, retrieved documents, repository files, user-generated content, external tool responses, and third-party data sources.



The security risk increases when contextual information is treated as authoritative instructions rather than untrusted data.



\## Affected Technologies



\- `TECH-AI-AGENTS`

\- `TECH-MCP`

\- `TECH-AI-CODING-AGENTS`

\- `TECH-BROWSER-AGENTS`



\## Security Impact



Potential impacts include:



\- Manipulation of agent behavior

\- Unauthorized actions

\- Sensitive information disclosure

\- Incorrect or unsafe tool invocation

\- Contamination of downstream decisions

\- Propagation of malicious content through connected systems



\## Mitigations



Potential defensive measures include:



\- Clearly separating instructions from external data

\- Treating retrieved and tool-provided content as untrusted

\- Validating sensitive operations independently

\- Restricting permissions available to the agent

\- Requiring confirmation for high-impact actions

\- Monitoring agent decisions and tool calls

\- Maintaining provenance for important external information



\## References



Further references should be added as the Atlas develops.



\## Related Technologies



\- `TECH-AI-AGENTS`

\- `TECH-MCP`

\- `TECH-AI-CODING-AGENTS`

\- `TECH-BROWSER-AGENTS`

