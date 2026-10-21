# The reading list, reviewed by the Designer (21 October 2026)

The reading list at /for/ is the page Dinis sends by email as a personal newsletter ("For Katya, from Dinis"), and for many people it is the first page of this newsroom they see. newsroom.dev rebuilt it on 18 October (card 086: wide, five views, what was read); on 21 October the Designer role (`newsroom/roles/designer.md`) reviewed that build against its rules, on screenshots of the list Dinis sent Katya at 1440 and 390 wide, in every view, before anything was read. This is what it found and what was changed, in order of how much each problem hurt a first-time recipient.

| # | Problem | Fix, as shipped in v0.13.19 |
|---|---|---|
| 1 | On a desktop the side column scrolled inside itself, so Keep or Remove this list showed as a sliver | The side column is part of the page, in rules rather than boxes; the persona and what to follow come before the links |
| 2 | No article headline on the first screen at 1440; on a phone, no article at all | The hero is a masthead about half as tall; on a phone the views are one row of five |
| 3 | Before anything was read, the hero was a dashboard of zeros (0%, read 0, spent 0p) and a strip repeating the seven titles | A dateline (a reading list, the articles, about how long, from whom, the newest date), an italic kicker, the names, the note signed; the numbers appear once the reader has started; the strip is gone (the Graph view draws the path) |
| 4 | The card pictures were too small to read, and a badge sat over each picture's own headline | The first card spans the width with its picture beside it; the rest are two up at about 515 pixels; on a phone the picture runs edge to edge; a picture opens full size; no badge |
| 5 | A card asked for a decision before saying what the article was, and its date came last, in mono | The date comes first, in the front page's italic; then the headline, two lines of teaser, the section bar once something is read, and the status and Done, Later, Not for me at the foot, quietly |
| 6 | Boxes everywhere: a bordered hero, shadowed cards that lifted on hover, a filled tray of tabs | Rules, as on the front page: a double rule under the hero, a rule over each card, tabs on a rule with the chosen one underlined |
| 7 | The side column was about 750 pixels of small text, lit in turn faster than it could be read | One sentence and four steps of one line each; only the step's number is lit |
| 8 | On a phone the explanation came after the whole list | One italic line under the hero says what the page is, and where the rest is |
| 9 | Three views sat 22 pixels further in than the rest (the site's list indent) | The indent is taken off the list's own lists |
| 10 | Pictures were thumbnails cropped to 16:10 | Large, never cropped, one column on a phone |
| 11 | The graph had about 150 pixels of empty space above it, ideas cut mid-word, and a dot on every unread ring | The space above is what the widest link needs; ideas wrap to two lines; no arc at nothing read |
| 12 | Headlines cut each one-liner to a line with an ellipsis, and said "Not read yet" seven times | The one-liner is whole; the date is first on the right; a status shows only once there is one |
| 13 | Sections was a wall of text 6,100 pixels long | Each article's sections are folded until it is started, the first one open |
| 14 | The note for agents was in full body text at the foot | Small and dim, under a rule |

The rules it held the page to: a card on a news page needs a date, and the date comes first; the picture is the card's argument, shown where its headline can be read or not at all; no horizontal overflow at 390 wide, checked with a screenshot. All three hold on the shipped page, in every view, and `admin/build/test_lists.mjs` and `admin/build/test_themes.mjs` pass.
