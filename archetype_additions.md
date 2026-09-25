# Archetype additions

## Research Note Folio

**Build:** Smart Augment (smartaugment.com), 2026-09-23. Parent archetype: Magazine or Cover Story, cast as a printed research note. For the registry quota it counts as Magazine or Cover Story; the casting is what is new.

**What it is:** The whole site reads as a periodical research note rather than a landing page. Every page is a folio with the same printed chrome: a masthead between rules (wordmark and horizontal navigation between a top hairline and a bottom double rule, mono small caps links, a dateline and a folio style cart count at right, compressing to a single rule on scroll); a cover spread as the first viewport (headline and standfirst in the left third, the signature world in the right two thirds); two column body spreads with serif prose and a mono for figures, drop caps, pull quotes between hairlines, paper margins; real tables as design (plan columns, comparables, evidence tables as true HTML tables with ruled rows, not cards); footnotes (superscript marks resolving to a footnote block, on that build walking down hairline leaders into the evidence table); a provenance or colophon strip in the footer above the mandatory address, phone, support email, Privacy and Terms.

**Where it fits:** research, analytics, periodical, finance and professional tool brands whose promise is a document a person reads. Light paper field, serif heading.

**Distinguishing it from plain Magazine or Cover Story:** the masthead rules and dateline, tables and footnotes as first class layout elements, and a colophon footer.

## Operations Ledger Grid

**Build:** Financing Bot (financingbot.com), 2026-09-24. Parent archetype: Swiss or Modular Grid, cast as a lender's operations ledger. For the registry quota it counts as Swiss or Modular Grid; the casting is what is new.

**What it is:** The whole site is one ruled ledger. A visible twelve column hairline grid spans the full viewport on every page (no outer margin wider than 48px at any desktop width), with a mono row index in the left margin numbering each section like a ledger line. Tables are first class furniture: the pricing page is a ledger with pack rows, the product page a worksheet and a condition list, all real HTML tables with ruled rows, and the figures sit in a mono while the words sit in a grotesk. The nav is a ruled header row of cells that fill paper on hover; buttons are paper blocks with a mono price cell divided by a hairline. The signature world (a queue wall of sixty loan rows) stands inside the grid at right on Home and docks into the product's queue table. Accent colour is reserved for a single recalculated figure; nothing else on the page is coloured.

**Where it fits:** operations, underwriting, back office, compliance and audit tools, any product whose promise is that the work is already counted and filed. Dark graphite field, grotesk heading, mono figures.

**Distinguishing it from plain Swiss or Modular Grid:** the grid is drawn, not implied; row indices in the margin; tables as the primary layout element rather than cards; one accent colour used only on a figure that changed.

## Meander (the brook spine) (Brainbrook, 2026-09-24)

**Description.** One continuous generative line (a 2D canvas, fixed behind the page, drawn from a seeded noise walk) swings across the full viewport width down the whole page. Every section docks on the bank opposite the line's swing, so both halves of every width are occupied at every desktop width; section labels ride the line as standing tags (`data-tag`); media bands (hero video, scene bands, the Year Rule) run edge to edge where the line straightens. Content sits in two bank grids (`.banks` with 60/40, 40/60 or 35/65 splits) whose inner `.cols` are auto fit content columns: two at 1440, three at 1920, four at 2560. There is never a centered narrow column; prose measure is applied only inside a bank.

**Why it exists.** It was invented to satisfy the FULL PAGE RULE (media and layout must fill the page at every desktop width, no negative space at the edges) while giving the page a single organising object that belongs to the brand (a brook for Brainbrook). The line also carries wayfinding: the tag on the spine names the section, the spine goes quiet (straightens and fades) in the loader, the checkout and the legal pages, and it docks onto the free bank so it never runs under text.

**Fits.** Any brand whose story is one long continuous thing (a river, a road, a tape, a thread, a timeline). Pairs with a light hued field; on a dark field the line becomes a glow path.

**Does not fit.** Dense catalogue pages with many equal items (the alternation reads as arbitrary) or brands that need a hard grid.
