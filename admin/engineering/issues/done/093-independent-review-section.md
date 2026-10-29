---
id: 093
title: Independent review as a section of the site, with every public part linked and as a QR code, and the secrets as QR codes
kind: story
priority: high
created: 2026-10-27T22:00:00Z
source: Dinis, 27 October 2026: "You know the secrets you gave me above? First of all, can you give them as QR codes? Also, surely you need their QR code before you can give me this here, right? And also, all of this should be linked from the website. Like, is anything here that is private? And can't we just have a whole section on the website dedicated to this? So I can just point to it."
release: v0.13.115
estimated_effort: medium
---
# Independent review as a section of the site, with every public part linked and as a QR code, and the secrets as QR codes

## What is asked
1. The three sealed secrets as QR codes.
2. Everything about independent review linked from the website, and what of it is private.
3. A section of the site to point people to.

## Scenario
```gherkin
Given the review desk's key, the security agent's key and a reviewer's vault key, each sealed to the editor's pki.sgit.ai key
Then each sealed link fits one QR code, and the code decodes to the link

Given anyone opens newsroom.sgit.ai/reviews/
Then they see how independent review works, the queue, the brief, the criteria, the vaults and keys, the send page and the records
And Vaults and keys shows each vault's public read key and each signing key as a QR code, and names every secret and who holds it, with none of them on the page
```

## Outcome
Shipped in v0.13.115. The sealed links were 7,400 characters, past pki.sgit.ai's 2,300 for one QR code: the desk's and the security agent's secrets now carry only the signing key (they never decrypt), and the sealed text is the variable alone. As the newsroom kept no copy of the first ones, the two keys and ChatGPT's vault were made again: vault gfzbzp41, desk sha256:fb35b723a2ae8b98, security sha256:2f1a036313b78b1d; the first ones are listed as retired, with why. `review_keys.mjs` writes each sealed link's QR code beside it; each was decoded back to its link. The section: `reviews/index.html` is now *Independent review* (how it works, in six steps, then the records), with a bar across its pages (Overview, The queue, Vaults and keys, The criteria, Send a review, The records), and in the site's menu under How it runs. `reviews/vaults.html` (built by `review_queue.py`, QR codes drawn in the page by `assets/reviews/qr.js`): each vault's read key, the two signing keys as pki.sgit.ai key links with their bundles and register submissions, where the verdicts go, who does what, the table of secrets and who holds each, the review lane's public half, and the retired vaults and keys. Tests: `test_review_lane.mjs` checks the page (a QR code for every public key, nothing private, no sideways scroll).
