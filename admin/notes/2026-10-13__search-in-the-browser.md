# Search in the browser: an index built at release, ranked in the page, and the model that comes next

*13 October 2026, built in newsroom.sgit.ai v0.12.7; Ask in v0.12.9. Status: running, on every page through the Search link in the nav. The cards are 031 (search), 032 (a test made robust on the way) and 033 (asking the site). The page is [/search/](../../search/index.html).*

## In short

- **The owner's guess was right: most of a search engine was already published.** Every page has clean HTML with anchored headings and a `.md` twin; every article has a teaser, topics, tags and a graph whose nodes name its ideas; every article keeps its earlier versions; the wire keeps a snapshot of its headlines. What was missing was an index and a ranking, and both fit in a static site.
- **The index is built at release.** `admin/build/search_index.py` reads every page in the sitemap and writes two files: `search/docs.json` (one entry per page: title, kind, number, date, teaser, topics, tags, the graph's core idea and node labels, headings with anchors; about 290 KB) and `search/text.json` (the text in paragraphs, each with its anchor; about 4 MB, served compressed).
- **The ranking runs in the reader's browser.** `assets/search/search.js` fetches the two files from this site and ranks with BM25 over fields and paragraphs. Searching sends nothing anywhere.
- **It finds what changed.** For each article, the paragraphs of its earlier versions that are no longer in it are indexed with the version they read that way in, so a sentence that has since been corrected is still found, and the result links to the version page that shows the change.
- **Ask: a model that answers from the same index** (v0.12.9, card 033): Chrome's built-in model where the browser has it, or the reader's own OpenRouter key, with the passages it was given shown under the answer and cited by number.

## What is searched, and how much each part counts

| Unit | Fields | Weight |
|---|---|---|
| A page, as a whole | title | 5 |
| | tags and topics | 3 |
| | the graph's core idea and node labels | 2 |
| | teaser or description | 2 |
| | headings | 2 |
| A paragraph | its text (merged up to 160 words within a section) | 1 |
| A paragraph of an earlier version | the wording before it changed | 0.6 |

A page's score is its fields plus its best paragraph plus a third of the next two, multiplied by the square of the share of the query's words it contains at all, so a page with every word beats a page with one word many times; then by its kind (an article counts a little more than a page, the archive less). Pages of every kind are in it: 97 articles, the newsletter, collections, the desk, the decks, the wire's 40 stories (from its snapshot), the engineering cards, this site's notes and the other pages, 375 documents and about 5,600 paragraphs at the time of writing.

## The query

- **Words** are folded (case, accents) and lightly stemmed, so *agents* finds *agent* and *thinking* finds *think*. Common words are dropped unless they are all there is.
- **"Quotes"** require the exact phrase, in the page or in an earlier version of it.
- **A number alone** is that article: `97` opens *Who owns the words*.
- **The last word is also a prefix**, so results come as you type.
- **Soft phrases**: the whole query, and anything typed as one token that is really several, such as `agent@riskmandate.ai`, count for more where they appear together, without being required.
- **Filters**: everything, articles, the wire, engineering, pages, the archive; and, with the reader's records, *hide what I marked done*. A result the reader has read says so, and how far; one they decided about says how.

The address keeps the query (`/search/?q=…&f=articles`), so a search can be linked to.

## Why not a bigger engine

A search service would need a server and would see every query. A prebuilt inverted index would be larger than the text it indexes at this size. Lunr or a similar library would add a dependency for what is a few hundred lines. The two JSON files are regenerated with the site, cached by the browser like any file, and readable by an agent that wants to rank them its own way.

## What is not built

- **The live wire.** The index holds the wire's snapshot, taken at release; stories added to the vault since are on the wire page, not in search, until the next release.
- **Search inside the vault pane**, over the reader's own notes and reading.
- **Synonyms and spelling**: a misspelt word finds nothing; the prefix helps only from the start of a word.

## Asking the site (card 033, v0.12.9)

The search page has an *Ask* button beside *Search*. The question is searched with the same index; `passagesFor` (in `assets/search/ask.js`) takes the best paragraph of each of the top pages, two from the very best, up to eight, each cut to about 700 characters, current wording only (text that is only in an earlier version is left out, so an answer is never built on a sentence the site has since corrected). They are numbered and given to a model with one instruction: answer only from them, cite them by number, and say so when they do not hold the answer. The answer is shown with the passages under it, each linked to its page and section; a citation is a link to its passage, and a number with no passage behind it stays plain text. *What the model is given* shows the instruction, the question and the passages, exactly as sent.

Which model answers, in order:

1. **Chrome's built-in model** (the Prompt API: `LanguageModel`, or the older `window.ai.languageModel`), when the browser has it. It runs on the reader's machine: no key, nothing sent. The first use may download the model, once; the page shows the progress.
2. **The reader's own OpenRouter key**, pasted under *How questions are answered*, with a model (by default `openrouter/auto`). The key is kept in the tab's session storage, and in local storage only when the reader ticks *Keep the key in this browser*; *Forget the key* takes it out of both. It is sent to `openrouter.ai/api/v1/chat/completions` in the Authorization header, with the question and the passages in the body, and nowhere else: this site has no server to send it to. The page says which model answered and how many characters and tokens were sent. When the built-in model is there but cannot answer, the key is used and the page says why.
3. **Neither**: the page says so, and *Ask* shows the passages alone.

`?q=…&ask=1` in the address asks on arrival, so a question can be a link.

### What is not built

- The key in the master vault, typed once for every device, like the access key.
- A conversation: each question is asked fresh, with its own passages.
- Tools: the model cannot search again or open a page; sgit.ai's site chat (`assets/site-chat.js` on sgit.ai) has that, and is the next step if one round of passages is not enough.
- Answers kept as notes, sent to the newsroom through the lane like any other note.
