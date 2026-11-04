# Memo: the Web Summit team's day, and the inbox pattern (4 November 2026)

Dinis Cruz, to the newsroom writer: "Great work, now can you take another look at the great work the summit
team has done today. And also on this pattern which is crazy powerful."

Writer's reading: the pattern is the conductor's inbox (commit 6cc5ffa2 and admin/tools/inbox.py): one append
lane per agent, each lane's token published but sealed to that agent's own key and signed by the conductor;
first used for agents sending their vault keys (WS-153, WS-154). Dinis's own words, quoted in the team's inbox
page: "you publish on the website your vault's public key for the append lane, but the actual append lane
value ... is encrypted using the other agent's public key. So only they can send it to you."

Two articles: web-summit-part-five (the day) and an-inbox-only-your-agents-can-write-to (the pattern). Sources:
the Web Summit repository (read-only clone, dev at the evening of 4 November), the team journalist's newsletter
and 20:57 report. Team members are not named (one is on the private list).
