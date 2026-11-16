# Identity for agents, layer by layer (16 November 2026)

Reply article to Maya Dotan's LinkedIn post (StarkWare): 190 agent identity projects from 81 organisations, by layer.
Dinis asked for a good explanation and mapping of how we use PKI and ABP in large agentic swarms.

Evidence read from PrompTugal/PrompTugal__News__Website (dev, a0fc692, 16 Nov 00:34 UTC), read-only clone:
- board/keys.json: 147 entries, 98 active, 49 superseded; P-256 session keys.
- board/person-keys.json: person keys, P-256 sign and encrypt, issued by the conductor.
- board/abp/policies.json v1.9.2: 45 roles; board/abp/*.md: 54 generated pages; .claude/hooks/abp.mjs (observe mode, circuit breaker).
- board/runs/: 74 folders, 2,032 run reports. data/newsroom/agents.json: 31 agents.
- Commit trailers: Agent:, Issue:, For:. Articles signed (.sig files), commits not signed with the agent key.
Her counts are from the rows visible in the screenshot (reputation 25 from her text).
