# SaveBrew brand kit

Built 2026-09-24 by the creative asset engine for the finalshot build of savebrew.com. Everything here is drawn as SVG from the graphic kit's signature motif (the knot) and the brand's display face; nothing is a generated raster. One logo per brand: a rebuild reuses this kit and regenerates only what changed.

## Files

logo/
* savebrew-knot.svg: the mark alone on its 24 grid, currentColor, real paths (the 2px warp, the weft loop over, under and pulled tight)
* savebrew-wordmark.svg: the word SaveBrew in Big Shoulders Display 800, glyphs converted to outlines (no webfont needed), currentColor, 24 units cap height
* savebrew-primary.svg and .png (2000 wide, transparent): the horizontal lockup, mark plus wordmark, indigo
* savebrew-primary-currentcolor.svg: the same lockup in currentColor for the site header, footer and app bar
* savebrew-reversed.svg (butter on transparent) and .png (2000 wide, butter on an indigo field): for indigo and other dark grounds
* savebrew-stacked.svg and .png, savebrew-stacked-reversed.svg and .png: the mark above the wordmark, for avatars and square slots
* savebrew-icon.svg and .png (2000 square), savebrew-icon-reversed.svg and .png, savebrew-icon-512.png: the mark only

favicon/
* favicon.svg (the knot in indigo on a butter tile, 7px radius at 32), favicon-16.png, favicon-32.png, favicon-48.png, favicon.ico (16, 32, 48), apple-touch-icon-180.png (butter square, iOS rounds it)

banners/ (built as HTML and screenshotted at the exact pixel size; the .html beside each .png is the source)
* linkedin-cover-1128x191.png, linkedin-logo-400x400.png, x-header-1500x500.png, crunchbase-1200x628.png, og-1200x630.png

## Palette (art_direction_spec.md 3.10)

| Role | Name | Hex |
|---|---|---|
| Ground, the page background and heading passes | butter | #F6E7A1 |
| Edges of butter blocks against white, pressed chips | deep butter | #EBD77A |
| Undyed thread, pale tiles | pale butter | #FBF3CF |
| Weft: every row board, card, table, form | white | #FFFFFF |
| Thread: headings, links, the wordmark, threads, stitches, primary button fill, active nav | indigo | #2B2F8F |
| Pressed states, knots, small labels on butter | deep indigo | #1B1E5C |
| Body text | ink | #14163A |
| Secondary text, captions, freshness stamps | muted indigo | #4F5280 |
| Up move (product views only, always with an arrow) | up | #1F7A4D |
| Down move (product views only, always with an arrow) | down | #B3261E |
| Slightly behind chip (product views only) | amber text | #8A5A00 |

The colour story is butter warp through a white weft, with indigo thread. Butter is a text colour only on indigo. Lemon, orange, cream and grey text never appear.

## Type

* Display: Big Shoulders Display, variable, weight 100 to 900. The wordmark is the word SaveBrew at weight 800, cap height locked to the mark's height, tracking 0, title case. H1 800, H2 700, H3 and cell heads 600.
* Body and UI: Manrope, variable, weight 200 to 800, tabular figures (font-feature-settings "tnum" 1). Labels 13px at 600, figures 700 tabular at text size.
* Both fonts are in ../fonts/ (SIL Open Font License, licence text beside them). No uppercase, no letter-spacing, no monospace anywhere on the marketing site.

## Usage rules

1. The lockup is mark plus wordmark, left aligned, mark first, gap one third of the mark's height. Never centred in an app bar, never mark only in the app bar, never in a sidebar, never watermarked over content.
2. Clear space: one mark height (the knot's 24 grid) on every side. Minimum size: 20px cap height on screen (the phone app bar), 24px on desktop, 8mm in print.
3. Colour: indigo on white or butter; butter (the reversed set) on indigo or deep indigo. Never any other colour, never a gradient, never an outline, never a drop shadow, never rotated.
4. The mark is the knot and only the knot. No coffee cup, no beer glass, no mug: the name collision with brewing is resolved by the weave.
5. The wordmark is never reset in another face or weight and never spaced out. Use the outlined SVG so it renders without the webfont.
6. Product shots carry the lockup in the app's own 56px bar (48px on phone) at 24px (20px on phone), left aligned, with the section tabs inline.
7. Banners carry the lockup on the butter and white weft with the five threads and at most one line of copy. No taglines longer than one line, no dashes.
8. The favicon is the knot on a butter tile so it stays visible on light and dark browser chrome.
9. Nothing here is graded. The brand grade ("morning light on cloth") applies to photography and video only, never to the logo, the kit or the product shots.
