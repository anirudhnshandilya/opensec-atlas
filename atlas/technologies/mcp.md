\# Model Context Protocol (MCP)



\*\*ID:\*\* `TECH-MCP`



\*\*Category:\*\* AI Infrastructure



\*\*Status:\*\* Active



\## Description



Model Context Protocol (MCP) is a protocol for connecting AI applications with external tools, resources, and contextual information.



MCP-based systems can allow an AI application to discover available capabilities and interact with external services through defined interfaces.



This creates security boundaries around tool discovery, capability exposure, authorization, input handling, output handling, and trust between clients and servers.



\## Security Questions



Important security questions include:



\- How are MCP servers authenticated?

\- Which tools and resources are exposed?

\- How are tool permissions granted and constrained?

\- How is untrusted tool output handled?

\- Can a malicious or compromised server influence an AI application?

\- How are sensitive resources protected?

\- How are tool invocations logged and audited?



\## Security Areas



Relevant areas include:



\- Tool authorization

\- Server trust

\- Capability exposure

\- Prompt injection

\- Malicious tool behavior

\- Supply-chain security

\- Credential handling

\- Data exfiltration

\- Input validation

\- Output validation

\- Audit logging



\## References



Further references should be added as the Atlas develops.



\## Related Threats



\- `THREAT-PROMPT-INJECTION`

\- `THREAT-EXCESSIVE-AGENT-PERMISSIONS`

\- `THREAT-AGENT-TOOL-ABUSE`

