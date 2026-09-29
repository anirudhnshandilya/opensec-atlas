\# AI Agents



\*\*ID:\*\* `TECH-AI-AGENTS`



\*\*Category:\*\* AI Security



\*\*Status:\*\* Active



\## Description



AI agents are software systems that use AI models to reason about tasks, maintain context, select actions, and interact with external tools or environments.



Unlike a conventional model that primarily produces an output, an agent may perform multi-step operations involving APIs, files, databases, browsers, code execution, or other software systems.



This creates a security boundary between model-generated decisions and real-world actions.



\## Security Questions



Important security questions include:



\- How are agent permissions controlled?

\- How are tool calls authenticated and authorized?

\- Can untrusted content influence agent decisions?

\- How are high-impact actions confirmed?

\- How are agent actions logged and audited?

\- How is sensitive context isolated?

\- How are compromised or manipulated tools handled?



\## Security Areas



Relevant areas include:



\- Prompt injection

\- Tool abuse

\- Excessive permissions

\- Credential exposure

\- Data exfiltration

\- Agent-to-agent interaction

\- Supply-chain security

\- Action authorization

\- Observability

\- Runtime isolation



\## References



Further references should be added as the Atlas develops.



\## Related Threats



\- `THREAT-PROMPT-INJECTION`

\- `THREAT-EXCESSIVE-AGENT-PERMISSIONS`

