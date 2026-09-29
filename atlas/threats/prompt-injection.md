\# Prompt Injection



\*\*ID:\*\* `THREAT-PROMPT-INJECTION`



\*\*Severity:\*\* High



\*\*Status:\*\* Documented



\## Description



Prompt injection occurs when untrusted instructions contained in user input, retrieved content, files, web pages, tool output, or other context influence an AI system to behave contrary to the intended instructions or security policy.



In agentic systems, successful prompt injection can potentially influence tool selection, data handling, or other actions performed by the agent.



\## Affected Technologies



\- `TECH-AI-AGENTS`

\- `TECH-MCP`

\- `TECH-AI-CODING-AGENTS`

\- `TECH-BROWSER-AGENTS`



\## Security Impact



Potential impacts include:



\- Unauthorized tool invocation

\- Sensitive information disclosure

\- Manipulation of agent decisions

\- Data exfiltration

\- Unauthorized changes to systems or repositories

\- Circumvention of intended workflow controls



Impact depends on the privileges available to the affected AI system and the controls surrounding its actions.



\## Mitigations



Potential defensive measures include:



\- Treating external content as untrusted input

\- Separating instructions from untrusted data

\- Applying least-privilege access controls

\- Requiring confirmation for high-impact actions

\- Validating tool arguments independently of model output

\- Monitoring and auditing agent actions

\- Limiting access to sensitive information



\## References



Further references should be added as the Atlas develops.



\## Related Technologies



\- `TECH-AI-AGENTS`

\- `TECH-MCP`

\- `TECH-AI-CODING-AGENTS`

\- `TECH-BROWSER-AGENTS`

