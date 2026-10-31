# An augmented PDF viewer: how hard is it to build one in the browser that renders any PDF and opens the provenance, the graph and the comments behind it? Less than I thought, sgit.ai

> The augmented book made me ask a question about PDF. It is a strange format: static, closed, made for a printed page, with nothing behind it. But a PDF is how most serious documents still travel, and the book will have one. So why not augment the PDF? I asked a research agent how feasible it would be to build a viewer in JavaScript, in the browser, that renders any PDF normally but also shows a layer the PDF cannot: the provenance of each claim, the nodes of the semantic graph, definitions, comments and review cards, on demand, beside the text. The answer is that most of it exists, as open source we can extend. Mozilla's PDF.js, under the Apache licence and committed to the day before we looked, already draws a page as a stack of layers, canvas, text and annotations, and announces each one as it renders, so a layer of our own fits on top. It can read a PDF's attachments, its metadata, its links and its fingerprint. And the augmented layer does not need to live in the PDF at all: the PDF only needs clues to find it, an attached file, an id in its metadata, a link, the file's own identifier, or a QR code that survives printing. Hypothesis already anchors annotations to PDFs this way, and e-invoices already carry machine-readable data inside human-readable PDFs. The hard part is not the PDF. It is the interface, anchoring claims to text reliably, and making sure the layer a viewer loads is signed by the people who made the document.

*Source: <https://newsroom.sgit.ai/articles/an-augmented-pdf-viewer.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / An augmented PDF viewer: how hard is it to build one in the browser that renders any PDF and opens the provenance, the graph and the comments behind it? Less than I thought

# An augmented PDF viewer: how hard is it to build one in the browser that renders any PDF and opens the provenance, the graph and the comments behind it? Less than I thought

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-31 · [article v1.0.0](versions/an-augmented-pdf-viewer.md) · [newsroom v0.14.16](https://newsroom.sgit.ai/admin/versions.html) · pdfbookreadingprovenanceopen-sourcejavascriptresearchbriefarticle

***Abstract:** The augmented book made me ask a question about PDF. It is a strange format: static, closed, made for a printed page, with nothing behind it. But a PDF is how most serious documents still travel, and the book will have one. So why not augment the PDF? I asked a research agent how feasible it would be to build a viewer in JavaScript, in the browser, that renders any PDF normally but also shows a layer the PDF cannot: the provenance of each claim, the nodes of the semantic graph, definitions, comments and review cards, on demand, beside the text. The answer is that most of it exists, as open source we can extend. Mozilla's PDF.js, under the Apache licence and committed to the day before we looked, already draws a page as a stack of layers, canvas, text and annotations, and announces each one as it renders, so a layer of our own fits on top. It can read a PDF's attachments, its metadata, its links and its fingerprint. And the augmented layer does not need to live in the PDF at all: the PDF only needs clues to find it, an attached file, an id in its metadata, a link, the file's own identifier, or a QR code that survives printing. Hypothesis already anchors annotations to PDFs this way, and e-invoices already carry machine-readable data inside human-readable PDFs. The hard part is not the PDF. It is the interface, anchoring claims to text reliably, and making sure the layer a viewer loads is signed by the people who made the document.*

The proposed stack: PDF.js draws the page in layers, and one more layer of ours carries what the PDF cannot.

## In short

- **PDF is static,** but it is how serious documents travel, and the book will have one.
- **So: a viewer in the browser that renders any PDF and adds an augmented layer** of provenance, graph, definitions and comments.
- **Most of it exists.** PDF.js is open source, active, and already draws pages as layers we can add to.
- **The layer does not have to live in the PDF.** The PDF only needs clues: an attachment, metadata, a link, its id, a QR code.
- **There are precedents:** Hypothesis anchors notes to PDFs by fingerprint; e-invoices carry data inside a PDF.
- **The hard part is not the PDF.** It is the interface, reliable anchors, and signing the layer.

## Why augment a PDF

In [the augmented book](the-augmented-book.md) I argued that a book should be one source in layers, and that print should carry a QR code where a layer would open. That made me look at PDF differently. A PDF is a strange format: it describes a printed page, it is static, it has nothing behind it, and every reader shows it the same way. But it is also how books, papers, reports and contracts actually travel, and the book of The Ultimate Insider has two of them, the book and its review companion.

So the question is simple. If we have the layers anyway, why can't a PDF have them? Not by inventing a new format nobody can open, but with a viewer that renders any PDF normally and, when the PDF carries the right clues, shows everything behind it.

## A viewer that already exists

The research agent cloned the main open-source projects and read their code. The one to build on is [PDF.js](https://github.com/mozilla/pdf.js), Mozilla's PDF renderer, the one inside Firefox:

- **The licence is Apache-2.0,** so we can extend it and ship it.
- **It is very active.** Its latest release, 6.4.299, came out on 3 October 2026, and its last commit was on 30 October, the day before we looked.
- **It draws a page as layers:** the canvas, a text layer with the selectable words, an annotation layer for links and forms, and others for accessibility and drawing. Each announces itself when it has rendered.
- **So our layer fits on top:** when a page's text layer is ready, we add our own, positioned with the page's own coordinates. Provenance, a graph node or a comment appears beside the words it is about.
- **It reads what we need from the file:** attachments, metadata including the raw XMP, named destinations, links, the structure tree, the text with its positions, and a fingerprint of the document.

There are alternatives. EmbedPDF builds a viewer on Chrome's PDF engine compiled to WebAssembly; its licence differs between packages and needs checking. MuPDF.js is excellent and licensed under the AGPL, which would oblige us to publish our changes or buy a licence. For writing PDFs, pdf-lib can attach files and add metadata, but has not been updated since 2021; two maintained forks carry it on. And the commercial viewers, Nutrient, Apryse and Adobe's embed API, sell overlays and annotation layers, which tells us there is a market for this.

## The PDF only needs clues

Five clues, tried in order, for finding a PDF's augmented layer, and which one survives what.

The insight in the memo is that the augmented layer probably does not need to be in the PDF at all. The PDF just needs enough clues for the viewer to find it. There are five, and the viewer tries them in order:

1. **An embedded file.** A PDF can carry attachments, and PDF 2.0 can mark one as data associated with the document. We attach the layer as JSON. It is the strongest clue, and the most fragile: printing to PDF, email gateways and compressors often strip attachments.
2. **Metadata.** A PDF's XMP metadata can hold our own fields, such as the document's id and the address of its layer.
3. **A link.** An ordinary link in the PDF to the document's page on our site, which every reader can follow too.
4. **The file's own identifier.** PDFs carry an id in their trailer, which PDF.js turns into a fingerprint; the viewer can look it up on our server. It is weak on its own: it is optional, copies share it, and regenerating the file changes it.
5. **A QR code** on the page, read from the rendered image in the browser, or by a phone from a printed copy. It survives printing, which nothing else does.

## It has been done, in parts

- **Hypothesis** annotates PDFs without changing them. Its client takes the PDF.js fingerprint, turns it into an address, and anchors each note to a quote of the text, matched loosely so it survives small changes. Copies of the same PDF share their annotations.
- **The W3C's annotation model** defines how to anchor a note to text: by quote with the words around it, by position, or by a PDF fragment such as a page.
- **E-invoices** in the Factur-X and ZUGFeRD standards are PDFs a person reads with machine-readable XML attached for the accounting system, declared in the metadata. A human-readable document carrying a machine-readable one is exactly our pattern.
- **Content Credentials (C2PA)** define how to embed a signed provenance manifest in a PDF, as an associated file, and PDF signatures (PAdES) sign the document itself.

## What not to do: JavaScript inside the PDF

PDF has its own JavaScript, which Acrobat runs: it can calculate forms, open dialogs and reach the network. It is also one of the most attacked parts of PDF. Search results for this research reported an Acrobat JavaScript flaw exploited from late 2025 and patched in April 2026, and PDF.js itself had a flaw in 2024 that let malicious font data run code, fixed in version 4.2.67. Many viewers ignore PDF JavaScript or run it in a sandbox, and security teams turn it off. The augmented layer must never depend on it: the PDF carries clues, and our viewer does the work.

## How hard is it?

Less than I thought. A minimum version is:

1. **PDF.js's viewer component,** with one extra layer drawn when each page's text is ready.
2. **Discovery** through the five clues, in order.
3. **Anchors:** each claim in the layer points at a quote of the text and a page, matched against the text PDF.js extracts, the way Hypothesis does; named destinations can be firmer anchors for our own PDFs.
4. **Writing the clues** when we build the book's PDF: attach the JSON, set the metadata, add the link and stamp the QR code.
5. **Signing:** the layer is signed with the publisher's key, and the viewer checks it before showing anything.

The research agent's estimate is weeks for a prototype, with the work in the interface and the data, not in the PDF. That matches what we already have: the book's claims, sources, graph and review cards exist as files, and the newsroom's site already shows sections at more or less detail.

## The risks

- **Clues get stripped.** Attachments and metadata do not survive every pipeline; that is why there are five clues and the last is printed.
- **Anchors drift.** Text extraction differs between files and between PDF.js versions, which breaks quotes; Hypothesis has met this.
- **A layer can be faked.** Anyone can attach a JSON file to a PDF. The viewer should show only a layer signed by the document's publisher, which is where [PKI everywhere](pki-everywhere.md) comes in.
- **Loading addresses found in a document** needs care: only from domains we trust, so a PDF cannot make the viewer call anywhere it likes.
- **Licences need reading** package by package, outside PDF.js.

## What I want to try

Take the RC1 PDF of the book, attach its claims, sources and graph as a signed layer, add its id to the metadata and a QR code to a few pages, and open it in a PDF.js viewer with one extra layer. Then put the same viewer inside [the iPad app](an-ipad-to-review-the-book.md), where the review comments go on the page. The PDF still opens in Preview, in Acrobat and in a browser, exactly as before; it just has more behind it in ours.

## What this does not claim

- **It is a research brief.** Nothing is built.
- **The code was read, not run.** The research agent cloned PDF.js, pdf-lib, react-pdf, MuPDF.js, EmbedPDF, jsQR, the Hypothesis client and the C2PA specifications, and read them on 31 October 2026; it did not build a viewer.
- **Some facts are from search results only:** the W3C annotation model, Factur-X, the Acrobat vulnerability, the commercial viewers and EmbedPDF's licence per package. The pages could not be opened from here.
- **The weeks are an estimate.**
- **My interest:** I write the book and build the tools it would use.

## Where this comes from

- My message of 31 October 2026, word for word in `admin/notes/2026-10-31__augmented-pdf/memo-01.md` in this site's repository.
- Repositories cloned and read on 31 October 2026: [mozilla/pdf.js](https://github.com/mozilla/pdf.js) (`web/`, `src/display/api.js`, `src/core/document.js`), [Hopding/pdf-lib](https://github.com/Hopding/pdf-lib), [wojtekmaj/react-pdf](https://github.com/wojtekmaj/react-pdf), [ArtifexSoftware/mupdf.js](https://github.com/ArtifexSoftware/mupdf.js), [embedpdf/embed-pdf-viewer](https://github.com/embedpdf/embed-pdf-viewer), [cozmo/jsQR](https://github.com/cozmo/jsQR), [hypothesis/client](https://github.com/hypothesis/client) and [c2pa-org/specifications](https://github.com/c2pa-org/specifications); package versions and dates from the npm registry.
- Seen in search results, not opened: the [W3C Web Annotation model](https://www.w3.org/TR/annotation-model/), [RFC 8118](https://www.rfc-editor.org/rfc/rfc8118) on PDF fragments, [Hypothesis on annotating PDFs without URLs](https://web.hypothes.is/blog/annotating-pdfs-without-urls/), [Help Net Security on the Acrobat zero-day](https://www.helpnetsecurity.com/2026/04/09/acrobat-reader-zero-day/), and [Nutrient's custom overlays](https://www.nutrient.io/guides/web/samples/custom-overlay-items.md).
- Related: [the augmented book](the-augmented-book.md), [an iPad to review the book](an-ipad-to-review-the-book.md), [the book of the talk and its companion](the-book-of-the-talk-and-its-companion.md), [PKI everywhere](pki-everywhere.md).

## Threads

Site & engineeringGraphs & knowledge[This article as a graph →](graphs.md#an-augmented-pdf-viewer)

### Builds on

- [The augmented book: one source in layers, projected to the web, the iPad and print, so the reader gets the right information at the right time, and what fifty years of attempts teach](the-augmented-book.md) The augmented book: one source in layers, projected to web, iPad and print, with the right information at the right time, and what precedents teach.
- [PKI everywhere: from now on every message, secret and handover starts with a signature, and how an agent gets its first key](pki-everywhere.md) From now on every message, secret and handover is signed. The hard part is an agent's first key: two patterns, one built and one proposed.
- [An iPad to review the book: a brief for an app that reads the PDFs, shows the comments on the page, opens its vault with my passkey and carries sgit in Swift](an-ipad-to-review-the-book.md) A brief for an iPad app to review the book: PDFs, comments on the page, append lanes, a vault opened with my passkey, and sgit in Swift.
- [The book of the talk by morning: RC1 of The Ultimate Insider, written from the record, read cold by a second team, with a companion PDF that turns reviews into tick boxes](the-book-of-the-talk-and-its-companion.md) Two agent teams, one night: RC1 of the book of The Ultimate Insider, a cold read by a team that knew only the record, and a companion PDF of tick boxes.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 338 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=338)

**Posting this article on LinkedIn?** The cover is [an-augmented-pdf-viewer.jpg](banners/an-augmented-pdf-viewer.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/an-augmented-pdf-viewer.html)*
