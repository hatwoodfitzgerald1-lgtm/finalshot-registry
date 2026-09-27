# Financing Bot: design record

Reconstructed 2026-09-26 from the build's finalshot-registry entry and its Build Log run record (financing-bot--20260923--r4xq9), because the original design document lived in the building session's sandbox and was not archived at the time. Every value below is as the run recorded it. The live site is the other half of the record: `vibe-card.jpg`, `shots/`, `copy_fingerprint.json` and `code/` in this folder hold its screens, speech patterns and source.

- Live site: https://financing-bot-site.webflow.io
- Built: 2026-09-23  ·  Repo: financing-bot-site

## Identity

- **domain**: financingbot.com
- **brand type**: net new
- **category**: Mortgage underwriting agent for lenders (B2B software): reads the file, recalculates income, sources deposits, reconciles AUS findings, drafts conditions; a named underwriter signs every decision
- **offering type**: SaaS sold as prepaid file packs (B2B, digital, guest checkout, card or ACH); $0 Pilot Order of 50 funded files as a secondary path through the same checkout
- **offering items**: ["100 File Pack: $2,400.00, 100 files at $24.00, valid 12 months, 5 seats, same business day queue, email support, CSV condition library template, 14 inclusions", "500 File Pack: $11,000.00, 500 files at $22.00, 25 seats, condition library loaded for you, same day phone support, monthly variance report, 15 inclusions", "Enterprise Block: $36,000.00 per block of 2,000 files at $18.00, unlimited seats + SAML, credit policy encoded, model documentation pack, audit log, named implementation lead, priority queue, PO on receipt, 20 inclusions", "Pilot Order: $0.00, 50 already funded files, no card, one per NMLS company ID, variance and defect report in 5 business days, 2 seats"]
- **price range**: $2,400 (100 files at $24) / $11,000 (500 files at $22) / $36,000 per Enterprise Block (2,000 files at $18) / $0 Pilot Order (50 funded files, no card)
- **hero primary cta**: Buy a file pack (lands on the pricing ledger)

## Governing idea and direction

- **governing idea**: The overnight queue: a lender's operations floor after hours where the loan files clear themselves row by row, and every figure that lands does so beside the page that proves it, so the morning underwriter only has to read and sign.
- **archetype**: Swiss or Modular Grid, cast as the Operations Ledger Grid (visible 12 column hairline grid spanning the full viewport, mono row index in the left margin, tables as first class furniture, the signature wall standing in the grid at right)
- **signature move category**: Motion & Scroll
- **signature move id**: MOT-021
- **signature world**: {"object": "the overnight queue wall: a tall graphite ledger wall of sixty loan rows standing on the operations floor, each row a thin slab of mono cells with a queue counter plate at the top right", "verb": "clear", "camera_path": "first person crane straight up the wall face as rows clear beneath the camera, a held stop two thirds up for The Clear (the last twelve rows clearing in a cascade), then a straight dolly back off the wall until the cleared queue sits square in the frame as the product's queue table"}
- **sig object**: the overnight queue wall: a tall graphite ledger wall of sixty loan rows standing on the operations floor, each row a thin slab of mono cells with a queue counter plate at the top right
- **sig verb**: clear
- **sig camera path**: first person crane straight up the wall face as rows clear beneath the camera, a held stop two thirds up for The Clear (the last twelve rows clearing in a cascade), then a straight dolly back off the wall until the cleared queue sits square in the frame as the product's queue table
- **tier**: 1

## Type and color

- **heading font**: Archivo
- **body font**: Archivo (words) with Fragment Mono (figures)
- **typographic set piece**: The Recalculation: the qualifying income figure in Fragment Mono at 160px rolls through the Form 1084 add backs on scroll, cites typing in, and takes verdigris only when it lands (on /product, quoted on Home)
- **palette**: {"field": "dark", "hexes": ["1A1B1D", "232527", "3A3D41", "9A9C98", "E9E5DA", "4FB89A"], "accent_hue_family": "teal (blue green verdigris)", "color_story": "graphite ledger with paper type and one verdigris figure"}
- **palette hexes**: ["1A1B1D", "232527", "3A3D41", "9A9C98", "E9E5DA", "4FB89A"]
- **palette field**: dark
- **accent hue family**: teal (blue green verdigris)
- **color story**: graphite ledger with paper type and one verdigris figure

## Motion and interaction

- **motion signature**: {"easings": ["cubic-bezier(0.8, 0.02, 0.18, 1)", "cubic-bezier(0.34, 0.9, 0.2, 1)"], "durations": {"fast": "0.14s", "base": "0.4s", "slow": "1.0s"}}
- **motion easings**: ["cubic-bezier(0.8, 0.02, 0.18, 1) Carriage Return", "cubic-bezier(0.34, 0.9, 0.2, 1) Ratchet"]
- **motion durations**: {"base": "0.4s", "fast": "0.14s", "slow": "1.0s"}
- **loader transition**: rolling drum counter of real load in Fragment Mono with load stages gaining tally strokes, then the graphite plate splits along its ledger rules (alternate rows slide out left and right) revealing the hero
- **nav style**: ruled cell nav: one ledger header row divided by vertical hairlines, cells fill paper from the bottom rule on hover with the label inverting to ink, mono row index on the active cell, drum count cart cell top right, compresses to 48px on scroll
- **button style**: paper block button: solid paper rectangle, radius 0, ink label with a mono price cell divided by a vertical hairline, label carriage returns 4px and a second rule draws on hover, 1px depress on press; accent never on any button; the Pilot is a text link
- **interactive feature**: drafter: Draft the conditions at /drafter (inputs product, income types, assets, AUS finding, designation, monthly volume; computes a PTD/PTC condition list with page cites; ends on the pack that fits)
- **libraries**: ["Three.js r128", "GSAP 3 ScrollTrigger", "Lenis"]
- **technique ids**: ["MOT-021", "MOT-005", "LAY-003", "TYP-005", "COL-010", "TEX-014", "TEX-008", "TRN-001", "TRN-007", "CUR-007", "CUR-009", "EXP-007"]

## Brand graphic kit and media

- **motif**: the tally (four hairline strokes crossed by a fifth diagonal) plus a square package seal ruled like a form box
- **media subject world**: the underwriting operations floor at night: desks and monitors after hours, a laser printer mid job, a records shelf of binders, a stapled package under a task lamp, cold screen light and one warm task lamp, no window light, no people
- **video concept**: the overnight shift: four 3 second locked off clips (monitors coming on, printer tray filling, queue clearing on a monitor, stapler on the finished package) plus a 6 to 8 second product in motion follow of one file through the built HTML screens
- **shot grammar**: locked off tripod, wide and mid, deep focus, cold screen light against one warm task lamp, 2 second dissolves
- **photography subject**: doorway view down the aisle; three stapled packages; one monitor in a black room; records shelf of binders; task lamp over a closed file; tax schedule page; two bank statement pages; findings report on screen and paper; open policy binder with fan fold log; condition list taped to a bezel; desk phone and support card at reception
- **product shot style**: screenshots of real HTML built for this site: one ink shell with a paper body, three bodies (queue, Form 1084 worksheet, condition list) following LN 2026090412, 1600x1000 at 2x in plain grey window chrome reading app.financingbot.com, ungraded
- **grade recipe**: graphite night, screen verdigris: grayscale(1) sepia(0.2) hue-rotate(120deg) saturate(0.7) contrast(1.18) brightness(0.86) with a 1A1B1D 22 percent lighten and an E9E5DA 10 percent multiply overlay
- **media manifest**: True

## Voice and copy

- **voice stance**: night shift handover
- **copy summary**: About 768 words; blog: form-1084-add-backs (899), large-deposit-letter (881), prior-to-doc-prior-to-close (932), ai-governance-file (966); full page copy for 17 routes with SEO; hero H1 'Read, recalculated and cited. Your underwriter decides.'; voice: plainspoken engineer cast as the night shift handover; 0 dashes, 0 banned words, no testimonials

## Pages and build

- **routes**: ["/", "/pricing", "/product", "/about", "/blog", "/blog/form-1084-add-backs", "/blog/large-deposit-letter", "/blog/prior-to-doc-prior-to-close", "/blog/ai-governance-file", "/drafter", "/contact", "/cart", "/checkout", "/order-confirmation", "/terms-of-service", "/privacy-policy", "/404", "/terms (301)", "/privacy (301)"]
- **framework**: Astro (SSR catch-all) for Webflow Cloud
- **engine profile**: baseline-r128
- **build directive**: Astro output server with [...slug].astro catch all (prerender false), Webflow Cloud adapter, assets under /public/assets, self hosted Archivo + Fragment Mono, Three.js r128 (cdnjs) + GSAP 3 ScrollTrigger + Lenis, client side cart (fb_cart_v1) and checkout with order numbers from 10482, measured budgets LCP < 2.5 s, CLS < 0.1, JS < 350 KB gz, 55 fps signature scroll, full page rule verified at 1440/1920/2560
- **full page rule**: Harlem 2026-09-24: media and layout must fill the full page edge to edge at every desktop width (he marked Astroquanta and Smart Augment's empty outer thirds with red bars); widest empty margin beside media or a section field capped at 48px, verified at 1440, 1920 and 2560 as a QA gate
- **novelty check**: check_novelty.py vs registry + Addabill: ALL QUOTAS CLEAR (16 of 16 applicable; quota 17 n/a at Tier 1)
- **registry comparison**: BioVirtua (Single-Object Hero 3D, dark, coral, Space Grotesk/Inter Tight, 3D&WebGL, tier 3, comparison feature, boot-sequence loader), Astroquanta (Sidebar-Anchored, dark, phosphor green, Schibsted Grotesk/IBM Plex Mono, Storytelling, tier 1, simulator, grid-fill loader, left rail nav), Smart Augment (Magazine/Research Note Folio, light paper, prussian blue, Newsreader, 3D&WebGL, tier 3, calculator, ruled-sheet loader, masthead nav). Quotas for this build: signature category must not be 3D&WebGL; avoid coral/phosphor/prussian accents; avoid comparison/simulator/calculator formats; heading font not Space Grotesk/Schibsted Grotesk/Newsreader; archetype not Single-Object Hero/Sidebar-Anchored/Magazine. Concurrent runs Addabill and Save The Will will be read from this log before the direction is committed (Harlem: none of the three may turn out similar).

## Measured quality

- **lcp**: 256 ms Home (sandbox, software GL)
- **cls**: 0.0061
- **fps**: 23 to 25 under swiftshader (indicative only; re-measure live on a GPU)
- **js kb**: 59.6
- **gates passed**: 7
- **gates total**: 7
- **qa iterations**: 3
- **qa score**: 95/100 (threshold 95) after rounds of 89, 93, 95
