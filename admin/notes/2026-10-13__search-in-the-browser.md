# Search in the browser: an index built at release, ranked in the page, and the model that comes next

*13 October 2026, built in newsroom.sgit.ai v0.12.7. Status: running, on every page through the Search link in the nav. The cards are 031 (search), 032 (a test made robust on the way) and 033 (asking the site, next). The page is [/search/](../../search/index.html).*

## In short

- **The owner's guess was right: most of a search engine was already published.** Every page has clean HTML with anchored headings and a `.md` twin; every article has a teaser, topics, tags and a graph whose nodes name its ideas; every article keeps its earlier versions; the wire keeps a snapshot of its headlines. What was missing was an index and a ranking, and both fit in a static site.
- **The index is built at release.** `admin/build/search_index.py` reads every page in the sitemap and writes two files: `search/docs.json` (one entry per page: title, kind, number, date, teaser, topics, tags, the graph's core idea and node labels, headings with anchors; about 290 KB) and `search/text.json` (the text in paragraphs, each with its anchor; about 4 MB, served compressed).
- **The ranking runs in the reader's browser.** `assets/search/search.js` fetches the two files from this site and ranks with BM25 over fields and paragraphs. Nothing typed leaves the page.
- **It finds what changed.** For each article, the paragraphs of its earlier versions that are no longer in it are indexed with the version they read that way in, so a sentence that has since been corrected is still found, and the result links to the version page that shows the change.
- **Next is a model that answers from the same index**: Chrome's built-in model where the browser has it, or the reader's own OpenRouter key, with the passages it was given shown beside the answer. That is card 033.

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

- **Asking the site** (033): a model that answers from the passages the search finds, below.
- **The live wire.** The index holds the wire's snapshot, taken at release; stories added to the vault since are on the wire page, not in search, until the next release.
- **Search inside the vault pane**, over the reader's own notes and reading.
- **Synonyms and spelling**: a misspelt word finds nothing; the prefix helps only from the start of a word.

## Next: asking the site (card 033)

The search page gains an *Ask* mode. The question is searched as above; the top passages (about eight paragraphs, with their pages and anchors) are given to a model with an instruction to answer only from them and to cite them by number; the answer is shown with the passages beside it, so every claim can be checked against the page it came from.

- **Chrome's built-in model** (the Prompt API, `LanguageModel`), when the browser has it: on the reader's machine, no key, nothing sent. The page says plainly when it is not there.
- **The reader's own OpenRouter key**, when they choose to use one: kept in the tab's session storage unless they ask to keep it, sent to openrouter.ai and nowhere else, with the model named. sgit.ai's site chat (`assets/site-chat.js` on sgit.ai) is the earlier proof of concept of this tier, with tools over its own index.
- **Later**, the key could live in the reader's master vault like the access key, so it is typed once for every device.
