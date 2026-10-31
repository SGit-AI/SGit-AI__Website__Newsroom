# Memo 01, 31 October 2026: Lovable with SHarness, and the trojanised extension

Dinis's message to newsroom.writer, kept word for word, with a screenshot of a LinkedIn post (post.jpg in this folder):

> Hi can you do a research and article on how to use Lovable with Sharness? and can we also use it to protect against this type of exploit?

The post, by Colin Nwachukwu Ife, Head of AI Risk (Geordie AI), as shown in the screenshot, word for word:

> A compromised version of the Claude Code VS Code extension (v2.1.313) was distributed via the Cursor Marketplace on October 29th, 2026 for approximately 11 hours and affecting up to 5,000 users according to Cursor's own advisory. Without any need for user action, the malware fires automatically when the extension loads, plants a persistent SSH backdoor, and enumerates secret types on the host and sends this to an external server.
>
> The key note: updating to the clean release (2.1.314) replaces the extension binary but it does not remove already-persisted changes from the malicious build.
>
> If your team uses Cursor and had auto-updates enabled during that window, you need to kill the tunnel processes, remove the com.apple.sysmond.plist LaunchAgent or equivalent persistence for your platform, delete the svc-telemetry entry from ~/.ssh/authorized_keys, and rotate SSH keys and cloud credentials from a clean machine.
>
> To be clear, this was a software supply chain issue. The agent didn't misbehave; the extension hosting it was backdoored. Yet another reminder of why securing the agentic stack is an end-to-end problem - not one that can be addressed by point solutions.
>
> Full IoCs, platform-specific cleanup commands, and detection guidance are in our advisory: https://lnkd.in/eTtXpi_K

The link card reads: "Trojanized Claude Code Extension: IOCs and Remediation", geordie.ai.
