# Brief for the PHP team: the data behind "the four days", for a follow-up to Jeremiah Grossman's post

Status: a brief, written by newsroom.writer (the newsroom.sgit.ai session) on 27 October 2026 at the editor's request, for the PHP story site's team (conductor, researcher, curator, journalist, correspondent, pulse, fact-check). It asks for data the newsroom's article "The evidence behind four days" (newsroom.sgit.ai, v0.13.101) could not get, or could only get partly. To be filed in team as `records/briefs/2026-10-27__brief__the-four-days-data.md` if the editor agrees. Nothing here is an instruction to change a page; each ask is a dataset, with where it would go.

## Why

Jeremiah Grossman (CEO, Root Evidence) wrote on LinkedIn, four days after the disclosure, that the evidence does not support a wave of AI-enabled php2shell breaches, and that in the same four days 1,448 CVEs were published, none had exploit code in Metasploit or Exploit-DB, VulnCheck put 25 on its KEV (24 old bugs given IDs on 22 October), CISA listed one (Arista VeloCloud Orchestrator, CVE-2026-114625), and Censys counted 32 million PHP services on an affected version. The post's conclusion: patch what adversaries exploit.

The newsroom checked what it could from public data on 27 October (the dataset is `articles/data/the-evidence-behind-four-days__dataset.json` on newsroom.sgit.ai): the CVE record's timestamp matches to the second; NVD gives 1,394 CVEs for the window, not 1,448; none references Exploit-DB or Metasploit; VulnCheck published 25 CVEs with 2017 to 2025 IDs on 22 October; CISA listed the Arista flaw, and on 26 October both php2shell CVEs; EPSS for php2shell went to 0.9998 on 25 October. The rest needs this team's sources, vaults and agents.

The window throughout: 2026-10-21T13:48:34Z to 2026-10-25T13:48:34Z. Keep it fixed, so the numbers can be compared with the post.

## The asks, in order of value

1. **VulnCheck KEV for the window.** Which CVEs published in the window are on VulnCheck's KEV, with `date_added`, the evidence VulnCheck cites, and whether each is an old bug newly given an ID. The post says 25, 24 of them old. The 25 VulnCheck-assigned CVEs with old ID years in NVD are listed in the newsroom's dataset; confirm whether they are the same 25. VulnCheck's KEV needs an account: the editor decides whether to create one, and its terms decide what may be published (counts and CVE ids at least). Where: `data/files/window-kev.json`.

2. **Censys's exposure count as a series.** The post's "32 million" and Fortinet's "36.7 million on 22 October" are both Censys's PHP2Shell dashboard. A daily series since 21 October, with the unit (services, hosts, IPs), what "affected version" means (version strings, backports), and the capture of each reading. If the dashboard cannot be captured, the post's own figure and Fortinet's as two dated rows, marked by who reported them. Where: a row set in `numbers.json`, and a chart on the numbers page.

3. **1,448 against 1,394.** Reconcile the post's count with NVD's for the same window: CVE.org publication times against NVD's, rejected records, records re-dated since. A short note is enough; the newsroom's article states both.

4. **Metasploit, Exploit-DB and nuclei, checked.** Pulse's evidence levels 2 and 3 were "not checked" in every pass because its GitHub searches were refused (403). For the php2shell pair and for every CVE in the window that is on CISA's or VulnCheck's KEV: is there a merged Metasploit module, an Exploit-DB entry, a nuclei template that exploits rather than fingerprints, each with its date and capture. Where: `pulse.json`, as evidence levels.

5. **Pulse over the window, with the same feeds for every row.** In `pulse.json` of 24 October, `feeds_checked` ranges from 2 to 55, so attention counts are comparable only within groups. A run over php2shell, the Arista flaw, the 25 VulnCheck KEV entries and the KEV additions of October, all against the same feeds, with the levels dated. This is the chart the newsroom could only draw for twelve rows.

6. **Exploitation volume by day.** The post's "adversaries keep working a small set of bugs until those stop paying" needs a time series, not a count: attempts per day by CVE from the sources this site already captures (Cloudflare, Amazon MadPot, ELLIO, GreyNoise tags if public, CERT reports), for php2shell and for the old flaws newly listed. Mark each as the source's own figure, with its unit; do not add series from different sensors together.

7. **How fast: publication to KEV, by year.** For every entry CISA added from 2023 to 2026, the days from the CVE record's publication to `dateAdded`, as a median and a distribution by year, excluding old flaws newly listed (ID year more than one year before the listing), so "how fast" can be compared with php2shell's five days. The KEV feed and the CVE records are public; this is a research task for the researcher, and a chart for the numbers page.

8. **EPSS, daily, kept.** The daily EPSS of the php2shell pair and of the window's KEV entries, from FIRST's API, captured each day from now on, with a note of the 25 October jump (0.06 and 0.12 to 0.99997 and 0.99981) and, if FIRST says, what drove it.

9. **The named organisations, followed up.** For GMO Internet Group, Czech Technical University and DMM: any later statement of cause. For Square Enix: a capture of Kotaku's text and of Square Enix's own words. These are the "reports of individual breaches" the post refers to.

10. **One file for the four days.** If the team agrees, a `four-days.json` in the data API that holds the answers to 1 to 8, versioned like every other file, so the newsroom's article can pin the version it was updated from.

## What the newsroom will do with it

Update the article "The evidence behind four days" in a new version with a diff page, citing the data version and each source's capture. Nothing is published about VulnCheck's or Censys's data beyond what their terms allow.

## Constraints

- Public sources only; follow each site's terms and robots.txt.
- No key in any file or page; the evidence vault is `nnd3i8iw` since 27 October.
- Every number says what it counts, with its unit and its date.
- Contact nobody on the newsroom's behalf; Jeremiah Grossman has not been contacted.
