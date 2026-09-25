# Addabill brand kit

Built 2026-09-24 by the creative-asset-engine for addabill.com (Addabill Inc.). Everything here is drawn from the brand graphic kit motif in the design document: the day cell with a standing tag. The mark is SVG, so it scales, recolors and sits on any background without a raster in sight. Never make Addabill a second logo: a rebuild reuses this kit and regenerates only what changed.

## Files

logo/
- addabill-primary.svg, addabill-primary.png (2048 wide, transparent): the mark beside the wordmark, graphite. Use on cream, white, oat and marigold.
- addabill-reversed.svg, addabill-reversed.png: the same lockup in paper white for dark backgrounds.
- addabill-stacked.svg, addabill-stacked.png, addabill-stacked-reversed.svg: the mark above the wordmark, for avatars and square slots.
- addabill-icon.svg, addabill-icon-512.png, addabill-icon-1024.png: the mark alone with the marigold today tick. addabill-icon-reversed.svg for dark, addabill-icon-tile.svg and addabill-icon-tile-512.png (the mark on a cream rounded tile) for directory avatars where the background is not yours to choose.
- addabill-wordmark.svg: the wordmark alone.
- addabill-month-seal.svg, addabill-month-seal.png, addabill-month-seal-reversed.svg: the month seal (kit item 2) for About, the order confirmation and the footer.
- favicon.ico (16, 32, 48), favicon-32.png, favicon-192.png, apple-touch-icon.png (180, on cream).

banners/
- linkedin-cover-1128x191.png, x-header-1500x500.png, crunchbase-1280x720.png, og-card-1200x630.png, each with its source .html.

checks/
- Every lockup rendered on white, black, marigold and cream, plus check-grid.png. The graphite set is for light fields and the paper white set for dark ones; neither is meant to work on both.

## The mark

A day cell: a square with a graphite border, rounded 4 on 64, the date numeral "2" (Fraunces 700) top left, the marigold today tick top right on the icon only. Inside it a paper tag stands on the cell floor: a white slab with a graphite outline and a 2 unit ink stripe along its top edge, over a soft shadow ellipse (graphite at 16 percent). Thursday the 2nd is the water bill in the product master, and the numeral keeps that story.

## Palette

| Role | Name | Hex |
| --- | --- | --- |
| Field | Counter cream | #FAF3E6 |
| Surface | Paper white | #FFFFFF |
| Surface tint | Oat | #EDE2CF |
| Text | Graphite | #2B2622 |
| Secondary text | Shadow | #6B6058 |
| Accent | Marigold | #E9A825 (buttons, heads-up chips, the today tick; never as text on cream) |
| Secondary accent | Moss | #3F6B4B (the paid check and "on time" labels only) |

Contrast: graphite on cream 13.6:1, graphite on marigold 7.2:1, shadow on cream 5.5:1, moss on cream 5.6:1.

## Type

Wordmark: Fraunces, variable axes locked at wght 600, SOFT 100, opsz 144, WONK 0, converted to outlines, so the SVG carries no font. Case is locked: Addabill, one capital, never all caps, never a space. Headings and oversized numerals on the site use the same face; body, UI labels and the product screens use Figtree 400 to 700 with tabular figures.

## Clear space and minimum size

Keep clear space around the lockup equal to the height of the mark on every side. Minimum width for the primary lockup is 120px on screen or 30mm in print; below that use the icon. Never stretch, rotate, add effects or place the graphite set on dark ground (use the reversed set) or the reversed set on light ground.

## Use

Only the favicon set and the OG card are pulled into the site build (site/public/assets). The kit itself stays here at brand-kit/ so 3rd-party-presence and linkedin-company-page-builder read it instead of drawing a new logo.
