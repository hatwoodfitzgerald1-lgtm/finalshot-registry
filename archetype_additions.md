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

## Warp Columns (SaveBrew, 2026-09-25)

**What it is.** Five fluid content columns run from edge to edge of the page at every desktop width from 1280 up (three at 1024, two at 768, one on phones), one per money thread (rates, cashback, coupons, the seasons, the paycheck), and every section is a row across them: today's pass puts one item in each column, the membership row gives each plan two columns and the fifth to what is free to read, the FAQ is an editorial index with a question heading each column. Between rows run full width heading passes on the butter ground, a question in Big Shoulders Display over a weft pass rule. The five columns are also the five warp threads of the signature loom, whose 3D threads are solved from the DOM column centres, so the grid and the world are one object.

**Why it exists.** It satisfies the full page rule (content fills every width, no centred narrow column) with a structure that belongs to the brand's governing idea: the page is literally woven, warp columns crossed by weft rows. Media bands (the loom, the week strip over the hero loop, the photo bands) run full bleed across all five.

**Fits.** A brand whose offering divides naturally into a small fixed set of parallel lanes that recur on every page (threads, channels, categories, instruments), and content that is read across as well as down.

**Does not fit.** Long single thread narratives, or catalogues whose item count is not a multiple of the lanes (cells go empty or stretch).


## Altitude Bands

**Build:** Hill Wallet (hillwallet.com), 2026-09-28. Live at https://hillwallet-site.webflow.io.

**Parent archetype:** Maximalist Color-Block. For the quota it counts as Maximalist Color-Block; the casting is what is new.

**What it is:** every section is a full bleed band in the next altitude tint up the hill (meadow, fern, barley, heather, sky, huckleberry), with no neutral field anywhere. Bands meet on hill crest masks cut from the climb profile, never straight lines. There are no max width containers: side padding stops at clamp(16px, 2.5vw, 48px), the grid runs 12 columns at 1440, 16 at 1920 and 20 at 2560, and each section adds columns, media or data at wider widths instead of margin. Verified by gutter_check.mjs (every section spans at least 94 percent of the viewport; no empty rectangle over 18 percent) at 1440, 1920 and 2560.

**Where it fits:** consumer brands whose promise is progress or elevation, and any build where Harlem's no negative space rule is the priority.

**Conventions floor held:** logo top left linking home, horizontal nav on desktop, cart top right, footer with address, phone, email, Privacy and Terms, buttons that look like buttons, product then cart then checkout then confirmation.
