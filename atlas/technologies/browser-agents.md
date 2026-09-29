\# Browser Agents



\*\*ID:\*\* `TECH-BROWSER-AGENTS`



\*\*Category:\*\* Autonomous Systems



\*\*Status:\*\* Active



\## Description



Browser agents are AI-powered systems that interact with websites and web applications through browser interfaces.



They may navigate pages, interpret web content, fill forms, click controls, retrieve information, and perform actions on behalf of users.



Because browser agents operate across untrusted web content and potentially sensitive user sessions, their security model must account for both model behavior and the security properties of the browser environment.



\## Security Questions



Important security questions include:



\- Which websites and browser actions can the agent access?

\- How are authenticated sessions protected?

\- Can untrusted web content influence agent decisions?

\- Which actions require explicit user confirmation?

\- How are sensitive data and credentials isolated?

\- Can malicious pages manipulate agent behavior?

\- How are browser actions logged and reviewed?



\## Security Areas



Relevant areas include:



\- Web prompt injection

\- Session security

\- Credential exposure

\- Unauthorized actions

\- Data exfiltration

\- Cross-origin security

\- Malicious web content

\- Browser isolation

\- Action authorization

\- Audit logging



\## References



Further references should be added as the Atlas develops.



\## Related Threats



\- `THREAT-PROMPT-INJECTION`

\- `THREAT-EXCESSIVE-AGENT-PERMISSIONS`

\- `THREAT-AGENT-TOOL-ABUSE`

\- `THREAT-UNTRUSTED-CONTEXT`

