# Smart Augment: design record

Reconstructed 2026-09-26 from the build's finalshot-registry entry and its Build Log run record (smart-augment--20260922--build1), because the original design document lived in the building session's sandbox and was not archived at the time. Every value below is as the run recorded it. The live site is the other half of the record: `vibe-card.jpg`, `shots/`, `copy_fingerprint.json` and `code/` in this folder hold its screens, speech patterns and source.

- Live site: https://smartaugment-site.webflow.io
- Built: 2026-09-22  ·  Repo: smartaugment-site

## Identity

- **domain**: smartaugment.com
- **brand type**: net new
- **offering type**: SaaS research desk, per named user subscription
- **offering items**: ["Research, $0, two gated reports a month, no card", "Desk, $200 per user per month, MOST POPULAR", "Platform, $1,000 per user per month, billed annually at $12,000 per user per year"]
- **price range**: $0 / $200 per user per month / $1,000 per user per month billed annually

## Governing idea and direction

- **governing idea**: Provenance made visible: the committee memo is a stack of paper you can see through, and every figure on the page has a hairline back to the disclosure row that produced it.
- **archetype**: Magazine or Cover Story, cast as a printed research note (Research Note Folio)
- **signature move category**: 3D & WebGL
- **signature move id**: 3DW-007 + 3DW-023
- **signature world**: {"object": "a committee memo as a stack of five translucent paper sheets in depth (memo, comparables, model run, screen definition, disclosure file) joined by hairline provenance leaders", "verb": "collate", "camera_path": "orthographic reading view snaps into a raking perspective as the sheets fan apart in depth, a focus pull walks from the memo to the disclosure sheet at the back and returns, then the sheets collate flat and the camera settles to the reading view"}
- **sig object**: a committee memo as five translucent paper sheets in depth (memo, comparables, model run, screen definition, disclosure file of 9,240 mono rows) joined by hairline Prussian provenance leaders
- **sig verb**: collate
- **sig camera path**: orthographic reading view snaps into a raking perspective as the sheets fan apart, a focus pull walks from the memo to the disclosure sheet at the back and returns, then the sheets collate flat and the camera settles to the reading view
- **signature shader id**: SHD-012
- **tier**: 3 real-time WebGL

## Type and color

- **heading font**: Newsreader
- **body font**: Newsreader (prose) with Spline Sans Mono (figures)
- **typographic set piece**: Footnotes That Walk: mono superscripts on the hero figures lift out of the prose on scroll and travel down drawn hairline leaders into the table beneath, landing as the row index of the figure they cite
- **palette**: {"field": "light", "hexes": ["F6F3ED", "FFFFFF", "EAE5DB", "DCD6CB", "6B665E", "1A1A18", "1B3A5C", "E7ECF2", "7A1F1F"], "accent_hue_family": "prussian blue", "color_story": "paper and ink with one institutional accent"}
- **palette hexes**: ["F6F3ED", "FFFFFF", "EAE5DB", "DCD6CB", "6B665E", "1A1A18", "1B3A5C", "E7ECF2", "7A1F1F"]
- **palette field**: light
- **accent hue family**: prussian blue
- **color story**: paper and ink with one institutional accent

## Motion and interaction

- **motion signature**: {"easings": ["cubic-bezier(0.55, 0.06, 0.18, 1)", "cubic-bezier(0.3, 0.74, 0.08, 1)"], "durations": {"fast": "0.16s", "base": "0.44s", "slow": "1.25s"}}
- **motion easings**: ["cubic-bezier(0.55, 0.06, 0.18, 1) Platen", "cubic-bezier(0.3, 0.74, 0.08, 1) Page Turn"]
- **motion durations**: fast 0.16s / base 0.44s / slow 1.25s
- **loader transition**: The Ruled Sheet: ruling lines draw across blank paper per real load stage, wordmark impresses onto the top rule, rules dissolve into the hero grid
- **nav style**: printed masthead between a top hairline and a bottom double rule, mono small cap horizontal links with rising footnote marks on hover, dateline and folio cart top right, compresses to a single rule on scroll
- **button style**: the stamp: solid Prussian rectangle with an inset paper hairline, serif label plus mono price, hairline steps outward on hover, platen press on click, 4s hairline breathe at idle
- **interactive feature**: calculator (The Payup Calculator at /calculator, fused with a 3D tick ruler)
- **libraries**: ["three@0.185 (module)", "BokehPass", "RawShaderMaterial paper", "GSAP ScrollTrigger", "Newsreader + Spline Sans Mono (Google Fonts, OFL 1.1)"]
- **technique ids**: ["3DW-007", "3DW-023", "SHD-012", "SHD-008", "SHD-005", "LAY-004", "TYP-019", "TYP-003", "TRN-003", "CUR-008", "TEX-006", "TEX-004"]
- **invented techniques**: ["The Collation (five sheet focus pull collate rig)", "Research Note Folio (archetype)"]

## Brand graphic kit and media

- **motif**: the provenance leader: hollow source circle, hairline, terminal tick
- **media manifest**: True

## Voice and copy

- **voice stance**: sceptical analyst who shows the working and names what would break it

## Pages and build

- **routes**: ["/", "/product", "/pricing", "/calculator", "/blog", "/blog/the-six-prints", "/blog/the-two-slabs", "/blog/the-balance-field", "/about", "/contact", "/cart", "/checkout", "/order-confirmed", "/terms-of-service", "/privacy-policy", "/404", "/qa/shaders (noindex)"]
- **framework**: Astro 5.18, output server, @astrojs/cloudflare 12.6, [...slug].astro catch all with prerender false
- **engine profile**: modern-three-0.185

## Measured quality

- **lcp**: 864 ms live on M5 Pro (video poster), fresh load with loader; sandbox software raster was 1.76s
- **cls**: 0.000 live
- **fps**: 60.0 average, 56 minimum over the pinned 1.5 vh Collation scroll, longest frame 17.7 ms, 0 frames over 33 ms (live, ANGLE Metal)
- **js kb**: 92.7 gz initial; 224 gz lazy 3D
- **gates passed**: 15
- **gates total**: 15
- **qa iterations**: 3
