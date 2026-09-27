# SaveBrew (savebrew.com): Art Direction and Technique Stack, THE WEAVE

Prepared 2026-09-24 by the ui-ux-director subagent for finalshot Step 2.5, phase two. Direction chosen by Harlem: Candidate C, THE WEAVE, from `spec/direction_candidates.md`. Built against the final Offering Spec at `spec/offering_spec.md` (read in full): SaveBrew Daily at $7.99 billed monthly (SB101) or $72 billed yearly (SB102); SaveBrew Daily for Two at $11.98 billed monthly (SB201) or $108 billed yearly (SB202); the Weekly Roundup, the Guides and the interactive page are public with no account, no form and no email capture; primary CTA "Add the Daily to my cart" and every other label exactly as the Offering Spec's section 8 sets them; checkout submit "Pay $7.99 now" style with the amount live; guest checkout; two click cancellation from the dashboard.

The two rules of the run still govern: no recognisable pattern shared with Addabill, Financing Bot, Save The Will, Smart Augment, Brainbrook, Hill Wallet or Astroquanta (Hill Wallet re-read, still uncommitted at the offering step), and no negative space at 1280, 1440, 1920 or 2560. No dashes are used anywhere in this document.

---

## 0. THE THREE ACCEPTED CONS, DECIDED AS DESIGN RULES

Harlem chose this direction knowing its three risks. Each becomes a rule the build follows and QA verifies.

### 0.1 Butter must read as restrained, with the warmth in the accents

The decision: butter is the warp, not the wall. The page ground is butter, but the visible surface is mostly white weft blocks laid over it, the way cloth shows only a little of the warp between the weft. Proportions, measured on any desktop screenshot of any page: white weft blocks 62 to 70 percent of the viewport area, butter 24 to 32 percent, indigo solids (buttons, the wordmark block, chart bars, chips) 4 to 8 percent. Butter is structural in exactly five places and nowhere else: the ground between and around the weft blocks (a 20 to 40px reveal), the heading passes (the display H2 bands between rows), the selvedge strips at the two outer gutters, the hero (where the loom sits on butter), and the footer's twill field. Butter is never a wall: no butter block taller than 40 percent of the viewport carries running text, no body prose is ever set on butter, and no two adjacent rows are both butter. Body prose, tables, cards and forms live on white. That is what makes it restrained: the warm tone frames the content rather than flooding it, and the eye reads white pages with a warm edge.

Contrast proof, every text-on-butter and text-on-indigo case (WCAG 2.2 AA needs 4.5:1 for text, 3:1 for large text and UI):

| Case | Foreground | Background | Ratio | Passes |
|---|---|---|---|---|
| Display H1 and H2 on butter | indigo #2B2F8F | butter #F6E7A1 | 8.85:1 | AAA |
| Small labels on butter (edge labels, thread names) | deep indigo #1B1E5C | butter #F6E7A1 | 12.16:1 | AAA |
| Body ink on butter (used only for the hero standfirst) | ink #14163A | butter #F6E7A1 | 13.99:1 | AAA |
| Secondary text on butter (captions on the hero) | muted indigo #4F5280 | butter #F6E7A1 | 5.91:1 | AA |
| Indigo link text on white | indigo #2B2F8F | white #FFFFFF | 11.02:1 | AAA |
| Body ink on white | ink #14163A | white #FFFFFF | 17.42:1 | AAA |
| Secondary text on white | muted indigo #4F5280 | white #FFFFFF | 7.37:1 | AAA |
| Primary button label | butter #F6E7A1 | indigo #2B2F8F | 8.85:1 | AAA |
| Primary button label, pressed | butter #F6E7A1 | deep indigo #1B1E5C | 12.16:1 | AAA |
| White text on indigo solids (chips, chart bars) | white #FFFFFF | indigo #2B2F8F | 11.02:1 | AAA |
| Up move inside the dashboard | green #1F7A4D | white #FFFFFF | 5.32:1 | AA (with an arrow, never colour alone) |
| Down move inside the dashboard | red #B3261E | white #FFFFFF | 6.54:1 | AA (with an arrow) |
| "Slightly behind" chip | amber text #8A5A00 | white #FFFFFF | 5.93:1 | AA |
| Focus ring | indigo #2B2F8F | butter #F6E7A1 | 8.85:1 | passes the 3:1 UI minimum |
| Butter block edge against white | deep butter #EBD77A | white | 1.25:1 (non-text) | every butter-on-white edge carries the stitch or a 1px deep butter rule, so the boundary never depends on contrast |

Lemon, orange, cream and grey text never appear. There are exactly three text colours (ink, indigo, muted indigo) plus the three semantic colours inside the product views, and butter is a text colour only where it sits on indigo.

### 0.2 Five columns at 1280 and on tablets: the collapse rules

The five-thread identity is the archetype, so it stays visible at every width, but the number of true content columns changes. Column width is `(100vw minus 2 gutters minus 4 gaps) / 5` with `--gutter: clamp(16px, 1.25vw, 32px)` and `--gap: clamp(16px, 1.25vw, 32px)`.

| Width | Warp columns in a row board | Column width and measure | How the five threads stay visible |
|---|---|---|---|
| 2560 | five | about 473px, body 17.5px, about 52ch (capped by fluid type, never a lone measure) | five columns edge to edge |
| 1920 | five | about 355px, body 17px, about 44ch | five columns edge to edge |
| 1440 (the reference) | five | about 262px, body 16px, about 34ch | five columns edge to edge |
| 1280 to 1439 | five for the row boards (Today's pass, the week strip, the guides row, the FAQ index); four for prose boards (About, guide bodies) | about 230px, body 15px inside the five-column rows, about 31ch, the minimum; prose boards use `columns: 34ch` and get four | five columns hold; headings shorten by design because the display face is condensed; action chips wrap under their line |
| 1024 to 1279 | three plus two: the row wraps into two rows, threads one to three then four to five, the fifth row cell spanning the remaining width | about 300px, body 15.5px, about 38ch | the thread strip (five short vertical threads with their names) sits at the head of every row board, and each cell carries its thread's knot glyph and name, so the order one to five is always legible |
| 768 to 1023 | two plus two plus one: threads one and two, three and four, then five spanning the full width as a selvedge block | about 350px, body 16px, about 42ch | thread strip at the head of each row board; the fifth thread's full-width block keeps the cloth from ending on an odd gap |
| 375 to 767 | one column with a sticky five-thread tab strip under the header | full width minus gutters, body 16px, about 38ch | the tab strip is the five threads: tapping a thread scrolls to that thread's cell in the current row; the strip stays sticky at 44px under the header on every page |

Minimum comfortable measure per column: 31ch at 1280, preferred 34 to 48ch, never above 52ch (fluid type grows the body to 17.5px at 2560 so the wide column stays a readable measure rather than a long line). The build fails QA if any column of running text measures under 30ch or over 55ch at any of the four test widths.

### 0.3 The rhyme with Financing Bot's grid and Addabill's warmth: the differences, as rules

A stranger comparing the three screens must notice these at once, so they are rules, not hopes:

1. No hairline overlay grid. Financing Bot shows a visible twelve-column hairline grid over every section. SaveBrew's columns are the content itself; there is no drawn grid, no column rules, no hairlines between columns. The only lines on the page are threads (the five short vertical threads of the thread strip, the running stitch of the selvedge, the single weft thread of a heading pass), and none of them runs the full height of a section.
2. No row indices, no numbering. Financing Bot numbers rows 0001 to 0010 in the margin; Addabill numbers steps 01 to 04. SaveBrew never numbers anything on the marketing site; the five brief items are marked by their thread's knot glyph and name, and the only numerals are figures inside sentences and tables.
3. No monospace anywhere. Financing Bot sets nav, labels and figures in Fragment Mono; six of the nine logged builds use a mono. SaveBrew uses two proportional faces, Big Shoulders Display and Manrope, and figures are Manrope's tabular numerals.
4. Columns are content, not chrome. Each column is a money thread with a name, an icon and its own items; a column is never an empty track or a layout device. Financing Bot's grid is chrome the content sits on; SaveBrew's columns are the product's own structure.
5. Saturated butter, not cream, and white weft, not cream bands. Butter #F6E7A1 has 83 percent saturation and a hue of 49 degrees; Addabill's cream #FAF3E6 is a near-white at 94 percent lightness and Smart Augment's paper #F6F3ED is greyer still. Butter reads as a colour, cream reads as paper. And the content sits on pure white blocks, where Addabill's bands alternate cream, oat and white.
6. A condensed display face, not a serif, and a question-led heading system. Addabill's H1 is a Fraunces serif in two declarative sentences; SaveBrew's headings are Big Shoulders Display, condensed and vertical in feel, and its H2s are the questions a reader is asking ("What's in today's pass?", "What does it cost?").
7. A woven heading band instead of a sticky condensing bar with a day-cell marker; a stitched Bobbin instead of a paper tag; a selvedge stitch loader instead of a flip calendar; the loom instead of a calendar; cloth at macro instead of a kitchen counter; indigo instead of marigold and verdigris.

QA's screenshot sameness test is run against Financing Bot's hero and Addabill's hero explicitly, and the build fails if a reviewer can point to any of the seven items above being present.

---

## PART 3. THE ART DIRECTION AND TECHNIQUE STACK

### 3.1 GOVERNING IDEA

Five threads run through every working month (savings rates, cashback, coupons, the seasons, the paycheck), and each weekday morning SaveBrew weaves the day's pass and hands you the five knots worth pulling.

### 3.2 EXPERIENCE ARC

Opening beat: the page is painted at once, and a running stitch draws down the left edge as the selvedge is sewn; when it ties off, the loom is already alive under the H1: five taut warp threads run away from the viewer across the whole width, undyed and pale, and a single weft thread passes left to right along the near edge, knotting once on each warp as the H1's letters pull from thin to bold behind it (The Tightening). Build: as the visitor scrolls, the reed sweeps toward the camera through the woven weeks, each pass revealing an earlier day's row of five knots, the threads taking indigo dye as they are woven, while the DOM row of Today's pass rises to meet the near edge. Peak (the wow moment, named THE PASS): today's five knots pull tight on a held beat with an overshoot, the weft snaps taut across the full width, and then gravity turns: the camera lifts as the cloth lays flat, and the flat cloth is the five-column board the page is built on, with the five DOM items docking onto the five warp positions. Resolution: the loom recedes to a thin thread strip that rides at the head of every row, the membership row lands with one stitch, and the page reads as a well-organised briefing from there to the footer's twill and seal. Motion is loud at the stitch tie-off, the pass and the footer; everywhere else it is quick and exact.

### 3.3 ART DIRECTION CONCEPT

A morning on the loom: undyed cloth on butter, indigo thread, condensed display type set like a mill's stencil, everything in rows. Adjectives: woven, dense, exact, warm, unhurried.

### 3.4 LAYOUT ARCHETYPE

WARP COLUMNS (invented; logged for archetype_additions.md as a named, reusable archetype). Five fixed content columns run from edge to edge on every page, one per money thread (Rates, Cashback, Coupons, Seasonal, Paycheck), and every section is a row across all five (a "pass"). Row boards are white weft blocks on the butter ground; rows are introduced by heading passes, display H2s set full width on the butter between rows with a single weft thread drawn beneath them, never a kicker and a left H2 at the top of a band. Column widths are fluid so the matrix grows with the viewport; there is no centred container, no rail, no spine, no visible grid. It differs from all nine logged archetypes: not an object beside an H1, not a sidebar, not a folio, not a full-bleed film with centred type, not Financing Bot's hairline grid (see 0.3), not a rendered world in a reading measure, not a diptych, not stacked cards, not a meander. It differs from Swiss or Modular Grid because the columns are the offering's own categories and nothing is drawn, and from Bento because rows are equal cells across one matrix, not tiles of mixed size.

### 3.5 COMPREHENSION BLOCK

- VALUE PROPOSITION: SaveBrew Daily is five short money moves on your dashboard by 6:30 each weekday morning, pulled from the savings rates, cashback windows, coupon codes, seasonal prices and paycheck habits that someone here checked overnight, for $7.99 a month.
- AUDIENCE: working adults with a paycheck and four minutes; on the page, "written for people with a job and four minutes, not a finance degree".
- PRIMARY ACTION: "Add the Daily to my cart" (the offering's label, verbatim), the indigo Bobbin button, one per view. Desktop: column one of the hero, under the standfirst, first viewport. 375px: directly under the standfirst, above the fold. It adds SB101 (monthly) to the cart; the cart offers the yearly switch. The secondary hero link, "Open this week's free roundup", is a plain indigo text link at clearly lower weight beneath it. The compact nav copy of the button exists per the Offering Spec section 8 and is visually subordinate (smaller, white fill, indigo stitch).
- FIRST-VIEWPORT PLACEMENT: Desktop 1440 x 900: the heading band 84px; the H1 in Big Shoulders Display at 96px in two lines spanning all five columns from x 24px, y 140 to 340px (one line from about 2200px wide); the standfirst in Manrope 19px across columns one and two, y 370 to 450px ("SaveBrew Daily: five short money moves on your dashboard by 6:30 AM Eastern, pulled from the savings rates, cashback windows, coupon codes, seasonal prices and paycheck habits we checked overnight. $7.99 billed monthly, or $72 for the year."), which is where the price lives per the offering; the audience line in column three; the Bobbin button in column one at y 490px with the roundup link under it; the loom filling the viewport behind and below, its five knots labelled Rates, Cashback, Coupons, Seasonal, Paycheck at the bottom of the viewport in columns one to five at y 780 to 860px as the preview of Today's pass. At 1920 and 2560 the same positions scale with the columns and the knot labels gain the item headlines beneath them, so more of the product is in the first viewport, not more space. 375 x 812: heading band 64px, the five-thread tab strip 44px, H1 at 44px in two lines from y 128px, standfirst 17px, Bobbin at about y 430px, roundup link, then the five-thread strip of the mobile hero at y 520 to 700px.
- MOTION CLEARANCE: the heading band, H1, standfirst, audience line, Bobbin and roundup link are plain DOM at first paint with no veil over them; the selvedge stitch runs in the gutter beside them and never covers content; measured target with the loader active: all three readable at 0.8s on broadband, stitch tied off by 1.5s, the loom initialising after 1.6s behind a 1600px WebP poster, LCP under 2.5s. Reduced motion: the stitch appears complete, one 0.3s fade, readable at 0.8s. The Tightening runs only after the standfirst and button are painted and never below weight 500 for longer than 0.6s, so the H1 is readable throughout.
- HEADING STACK (read alone): "Which of the five threads your money runs on moved overnight?" / "What's in today's pass?" / "What does it cost?" / "What did last week's pass look like?" / "What's inside the dashboard?" / "Which threads should you pull first?" / "What's free to read?" / "What do people ask before they join?" / "Join Our SMS List" (the kit's verbatim block heading) / footer. The H1 is a question, open ground no sister uses, and never the two-declarative-sentence formula; read without body copy the stack says what it is, what it costs, that it happens daily, what the product contains, that there is a tool, that some of it is free, and how to ask.
- SCENT MAP: "Roundup" opens /roundup, this week's free Saturday page; "Guides" opens /guides, the free library; "Your moves" opens /your-moves, the ranker; "Membership" opens /membership, the two memberships; "About" opens /about, who checks the threads and where; "Contact" opens /contact, the address, phone and email; "Sign in" opens /today, the member dashboard; the spool glyph opens the cart. No label is a category abstraction, and "Your moves" is the tool's own name, not "Tool".

### 3.6 SIGNATURE MOVE

TEX-008, generative canvas background, Texture & Detail, High (the previous build's category was Typography; Texture & Detail is also an under-used category, so quota 6 is met by the signature itself). What it is: the Loom, a real-time procedural weaving scene that fills the hero edge to edge, generated fresh each load from the date (today's five knots, the last ten weekday rows) and scrubbed by scroll. Why it fits: the offering is five categories read every weekday and handed over as five items, which is literally a warp of five threads with a weft passed once a day; the alignment of product and metaphor is exact, and the cloth laying flat into the five-column board makes the archetype and the signature the same object. How it delivers the wow: THE PASS, the beat where today's knots pull tight with an overshoot and gravity turns so the woven weeks lay flat and become the page. Library: Three.js r128 from cdnjs (baseline engine profile), Line2 fat lines for threads, small TorusGeometry knots with MeshBasicMaterial (unlit, flat dye colours, no HDRI needed), GSAP 3 ScrollTrigger for the scrub, a 2D canvas for the thread alpha map. Benchmarks: https://www.awwwards.com/sites/united-carriers (one colour, one Three.js hero, store-grade weight) and https://tympanus.net/codrops/2026/02/02/building-a-scroll-revealed-webgl-gallery-with-gsap-three-js-astro-and-barba-js/ (the database's TEX-008 example, generative surfaces that respond to scroll).

### 3.7 SIGNATURE 3D EXPERIENCE (the world, in build terms)

- The object: five warp threads, one per money thread, each a Line2 fat line (2.5px at dpr 1, 1.75px on touch) running from the near edge of the frame into depth across the full width at x positions matching the five DOM columns (the world x of each thread is computed from the column centres so DOM and scene agree at every viewport width); a weft thread as a single Line2 that passes left to right along the near edge; knots as small tori (radius 0.045 world units) placed where the weft crosses a warp; behind the near edge, the woven cloth: the last ten weekday rows as rows of five knots joined by faint weft lines, receding. Thread alpha map: a 256 by 16 canvas texture with slight fibre noise so lines read as thread, not vector.
- Materials and colour: threads start undyed (butter-white #FBF3CF at 70 percent) and take indigo #2B2F8F as they are woven; knots are deep indigo #1B1E5C; today's knots flash butter on the pass. The scene background is transparent over the butter ground; no fog, no lighting, so contrast is fixed at 8.85:1 or better between thread and ground. High contrast at load is the first rule and the unlit palette guarantees it.
- Alive on load: the warp threads sag and recover on a 7s cycle (a vertex sine with per-thread phase), the weft creeps across the near edge on an 11s loop knotting each warp with a tiny overshoot, and the cloth behind drifts 1 degree toward the pointer (pointer devices only).
- Scroll choreography (native scroll, GSAP ScrollTrigger scrub with a 0.08 lerp; the canvas is a fixed layer behind the flowing DOM, not a pinned hero): progress 0 to 0.45, cross-section sweep: the reed (a thin butter plane) sweeps from depth toward the camera, and each row it passes snaps from faint to dyed as that day's five knots are revealed, ten rows in all, newest last; 0.45 to 0.6, the held beat: today's weft passes and the five knots pull tight (Knot easing, 1.12 overshoot), the weft snaps taut, a 90ms butter flash on the knots; 0.6 to 0.9, gravity flip: the camera pitches from the weaver's low oblique (12 degrees) to top down (88 degrees) while the cloth's normal rotates to meet it, so the woven rows lay flat as a matrix, and the DOM row of Today's pass docks its five cells onto the five warp positions (each cell's left edge pinned to its thread's projected x via a per-frame projection); 0.9 to 1.0, the loom hands off: the five threads shorten into the thread strip at the head of the row (GSAP Flip onto an SVG twin drawn from the same positions) and the canvas fades. Signature scroll length: 1.3 viewport heights, inside the 1.25 to 1.75 budget, not pinned.
- Environment arc: the dye takes. Threads and cloth move from undyed butter-white to indigo across the scrub while the butter ground stays constant, so the arc is in the material, not the field, and LCP and contrast never move.
- Post chain: none (Tier 1, unlit). Texture: a 4 percent static canvas grain baked into the poster only.
- Streaming plan: first paint ships the DOM, the 1600px WebP poster of the flat cloth at progress 1.0 and the selvedge stitch; fonts subset and preloaded; Three.js r128 (about 150KB gzipped from cdnjs) loads after first paint and idles behind the poster; the alpha map is generated on the client; the canvas cross dissolves over the poster in 0.38s; if init exceeds 3s or fails, the poster stays and the DOM docking runs against a static position table.
- Fallbacks: prefers-reduced-motion serves the flat-cloth poster with the five cells already docked and the thread strip static. Under 900px or coarse pointer, no WebGL: the mobile hero's 2D canvas thread strip with the pull gesture (3.20). Low power (under 30fps after two seconds of sampling) drops to the poster while the DOM docking still runs. Context loss: preventDefault, poster swap, rebuild on restore. One WebGL context per page, dpr capped at 1.5 (1.0 on touch), render paused offscreen and on hidden tabs, disposed on navigation.
- Every other page gets its own bespoke lightweight scene from the kit, never the loom itself: /brief a single weft thread that weaves the day's five knots across the top of the page as the visitor reads; /membership two threads plied into one cord (the Daily for Two) that untwist back into two on hover; /roundup a single thread with three knots that the camera tracks along as the three moves are read; /guides a spool that unwinds a thread down the page as reading progress; /your-moves the visitor's threads lifting out of the cloth in ranked order; /about the Selvedge Seal being woven row by row; /contact a single knot tied at the address line; /cart the knot sliding along a thread into the spool; /checkout a running stitch that advances one section at a time; /confirmation the seal's last stitch tying off; /terms and /privacy a static twill margin; /404 a loose thread that curls. Each is one canvas or one SVG, lazy, paused offscreen.

### 3.8 TECHNIQUE STACK

- Signature: TEX-008 | Generative canvas background | Texture & Detail | the loom is the offering as a procedural surface and it lays flat into the archetype | Three.js r128, Line2, canvas alpha map | High
- Texture and hover: TEX-007 | SVG displacement / turbulence filter | Texture & Detail | the plucked thread: headings on the home page ripple once on hover like a thread plucked and released | SVG feTurbulence and feDisplacementMap, GSAP on the scale attribute | Medium
- Scroll reveal: MOT-018 | Clip-path scroll reveal | Motion & Scroll | every row board wipes in left to right like a weft pass, the site's one reveal language | CSS clip-path with animation-timeline: view(), ScrollTrigger fallback | Medium
- Scroll system: EXP-005 | Scroll-Driven CSS Animations | Emerging & Experimental | the heading passes, thread strips and week strip parallax run off the main thread on native scroll (no Lenis, on purpose) | native animation-timeline, scroll-timeline polyfill for Safari | Medium
- Typography: TYP-003 | Variable font weight/width animation | Typography | The Tightening set piece on the H1 and the weight tightening hover on /brief | CSS @property, GSAP | Medium
- Typography: TYP-014 | Type as layout grid | Typography | the heading passes are structural: display H2s at full width on butter carry the page's rhythm instead of bands and kickers | CSS Grid, Big Shoulders Display | Medium
- Loader: TRN-002 | Preloader progress bar | Page Transitions & Loaders | the selvedge stitch is a real-load progress line drawn as a running stitch down the left gutter | GSAP, imagesLoaded, Three.js LoadingManager | Low
- Microinteraction: CUR-007 | Button hover choreography | Cursor & Microinteractions | the Bobbin's running stitch on hover and tightening on press, label shift, one stitch travelling at idle | CSS stroke-dashoffset, GSAP | Low
- Microinteraction: CUR-009 | Toggle / Switch Animation | Cursor & Microinteractions | the ranker's six toggles and the dashboard's text toggles click with Knot | CSS :checked, role switch | Low
- Forms: CUR-010 | Form Field Focus States | Cursor & Microinteractions | checkout and contact fields whose underline is a stitch that draws on focus, GOV.UK error standard | CSS :focus-within, aria-describedby | Low
- Accessibility: EXP-007 | Accessibility-Forward Motion | Emerging & Experimental | a persistent "reduce motion" control in the footer and the mobile menu, reduced variants everywhere | prefers-reduced-motion, localStorage | Low
- Media: IMG-019 | Aspect-ratio art direction | Imagery & Media | cloth stills served in different crops per breakpoint so the weave stays legible at 375 and 2560 | picture and source media, focal cropping | Low

Twelve techniques, plus two recipes from the award recipe book cast for this brand: Recipe 03 persistent brand-device continuity (the knot travels from the loom to the thread strip to the cart spool to the confirmation seal) and Recipe 08 dot-matrix data visualisation, recast as the knot matrix on the week strip and the roundup's rate summary (each tracked account is a row of daily knots, knot size is the APY, butter where it moved). Cut in the restraint pass: MOT-001 Lenis (content-heavy, native scroll), magnetic and tilt hovers (logged and off-tone), any marquee (constant motion fights reading), TEX-006 paper texture (paper is Smart Augment's), masonry (the matrix is the grid), a numbered steps list, a MOST POPULAR badge, a $0 card, a hero price under the button.

Registry quotas checked (all seventeen pass, script output in Part 4): heading face not in the last eight and pairing never used; archetype not in the last five; signature category (Texture & Detail) differs from Typography; object and camera path never logged; eight fresh technique ids against the last five; Texture & Detail and Emerging & Experimental present; loader differs from the print head; light field after light and unknown; indigo outside every logged accent family; both easings new; ranker not in the last three; nav and button differ in treatment from the tape header and the kept tag; voice not in the last three; colour story not in the last four; Tier 1 after 2 and 1 (not three in a row); no signature shader (Tier 1).

### 3.9 BUILD NOTES

Pulled with `select_techniques.py --ids TEX-008,TEX-007,MOT-018,EXP-005,TYP-003,TYP-014,TRN-002,CUR-007,CUR-009,CUR-010,EXP-007,IMG-019 --full`. Pasted verbatim except that the database's em and en dashes were replaced with commas to honour the no-dash rule; Lenis references in the database notes are overridden by this spec (native scroll). Example links spot-checked on the 2026-09-24 run: the Codrops scroll-revealed gallery article, the Codrops scroll-driven animations article, v-fonts.com and web.dev load; the Awwwards loading round-up and typography collection pages load.

12 of 12 match:

[MOT-018] Clip-Path Scroll Reveal
  id: MOT-018
  technique_name: Clip-Path Scroll Reveal
  industry_term: clip-path wipe / mask reveal on scroll
  category: Motion & Scroll
  subcategory: Reveals
  description: An image or section is revealed by animating a clip-path (inset, polygon, or circle) or an SVG mask from closed to open as it scrolls into view, so content appears to be uncovered rather than faded. Can be directional or shaped.
  aesthetic_effect: Feels tactile and architectural, like a curtain or aperture opening, far more interesting than a plain fade. Shaped/animated masks read as bespoke and high-craft.
  when_to_use: Image reveals, section intros, gallery items, brand statement moments needing a distinctive entrance.
  how_to_implement: Animate `clip-path: inset(0 100% 0 0)` to `inset(0 0 0 0)` with GSAP scrub or CSS view() timeline. For organic shapes use SVG <clipPath> and animate its geometry, or GSAP with MorphSVG. Pair with a slight image scale for depth.
  libraries_tools: GSAP ScrollTrigger, CSS clip-path + animation-timeline, SVG masks, GSAP MorphSVGPlugin
  difficulty: Medium
  performance_a11y_notes: clip-path animation can trigger repaints (less compositor-friendly than transform/opacity); test on mobile. Provide reduced-motion fallback that shows content unclipped. Ensure revealed content isn't hidden from assistive tech.
  example_project: SVG Mask Transitions on Scroll with GSAP and ScrollTrigger (Codrops)
  example_url: https://tympanus.net/codrops/2026/03/11/svg-mask-transitions-on-scroll-with-gsap-and-scrolltrigger/
  example_source: Codrops
  pairs_well_with: Image parallax, text reveal, scroll-zoom
  avoid_when: Performance-constrained pages with many simultaneous clips, or reduced-motion contexts.
  reference_video_match: V4 Everswap (scroll reveal)

[TRN-002] Preloader Progress Bar
  id: TRN-002
  technique_name: Preloader Progress Bar
  industry_term: loading progress bar
  category: Page Transitions & Loaders
  subcategory: Preloaders
  description: A horizontal (or circular) bar fills from 0 to 100% as assets load, then the overlay exits. Simpler and more legible than a counter; communicates determinate progress.
  aesthetic_effect: Calm, reassuring, and minimal; the steady fill telegraphs polish and that loading is under control. Pairs well with type-forward minimalist brands.
  when_to_use: Sites with measurable load (galleries, video), minimalist brands, when you want clear determinate feedback.
  how_to_implement: Bind bar scaleX/width to real load fraction (assets loaded / total) and tween smoothly; on 100% play an exit (wipe up, fade). Use scaleX transform for cheap animation.
  libraries_tools: GSAP, imagesLoaded, Three.js LoadingManager, NProgress (for route loads)
  difficulty: Low
  performance_a11y_notes: Use transform scaleX (compositor-friendly). Expose progress with role=progressbar/aria-valuenow if it gates content. Keep short; reduced-motion can show an instant fill.
  example_project: A Round-up of The Best Loading Animations (Awwwards)
  example_url: https://www.awwwards.com/a-round-up-of-the-best-loading-animations-1.html
  example_source: Awwwards
  pairs_well_with: First-paint reveal, route-based fade, skeleton loaders
  avoid_when: Fast pages where any preloader is pure friction.

[TYP-003] Variable font weight/width animation
  id: TYP-003
  technique_name: Variable font weight/width animation
  industry_term: Variable font axis interpolation (font-variation-settings)
  category: Typography
  subcategory: Variable fonts
  description: A single variable font file carries continuous axes (weight, width, slant, optical size, plus custom axes) that are animated or interpolated at runtime. Hierarchy and motion come from one file instead of many static weights.
  aesthetic_effect: Gives type a living, responsive quality, headlines can breathe, thicken on hover, or morph on scroll, which feels modern, performant and craft-forward.
  when_to_use: Hero headlines, interactive logos, scroll- or hover-reactive type, and to consolidate many weights into one lightweight asset.
  how_to_implement: Declare the font with font-variation-settings: 'wght' 400, 'wdth' 100; then transition or animate those axes (transition: font-variation-settings .3s) or drive them from scroll/pointer JS. Use CSS @property to make custom axis vars animatable.
  libraries_tools: CSS @property; GSAP for axis tweens; variable faces from v-fonts.com / Google Fonts (e.g. Roboto Flex, Recursive, Fraunces); Splitting.js to target per-letter axes.
  difficulty: Medium
  performance_a11y_notes: One file is lighter than many weights but the file itself can be large, subset it. Animating font-variation-settings can be paint-heavy; respect prefers-reduced-motion.
  example_project: Recursive variable font (v-fonts / Google Fonts)
  example_url: https://v-fonts.com/
  example_source: v-fonts (variable font catalog)
  pairs_well_with: Kinetic typography; type-on-scroll; clamp fluid sizing
  avoid_when: Body copy where constant weight shifts hurt readability, or when only one static weight is actually needed.

[TYP-014] Type as layout grid
  id: TYP-014
  technique_name: Type as layout grid
  industry_term: Typographic grid / type-driven layout system
  category: Typography
  subcategory: Type as structure
  description: The page composition is built primarily from typography, scale, weight and spacing define the visual hierarchy and structure, with little to no imagery. Type becomes the interface skeleton rather than decoration over photos.
  aesthetic_effect: Feels editorial, intellectual and content-first; reduces page weight while projecting confidence and a Swiss/International-style discipline.
  when_to_use: Manifesto pages, agency homepages, conference sites, and any brand leaning on language and minimalism over photography.
  how_to_implement: Establish a strict baseline grid and modular type scale, use CSS grid for column structure, and contrast a few weights/sizes to create hierarchy. Lean on whitespace and rule lines rather than images.
  libraries_tools: CSS Grid; modular-scale tooling; faces like GT America, Suisse Int'l, Neue Haas Grotesk; Awwwards 'Typography-Heavy' reference.
  difficulty: Medium
  performance_a11y_notes: Very fast (text-only). Maintain heading hierarchy and contrast; ensure interactive type targets are large enough (WCAG 2.5.8 target size).
  example_project: Typography-Heavy Web Design (Awwwards)
  example_url: https://www.awwwards.com/typography-heavy-design.html
  example_source: Awwwards
  pairs_well_with: Swiss minimalism; mono metadata; hairline borders
  avoid_when: Product/visual brands where imagery is the core proposition.

[TEX-007] SVG displacement / turbulence filter
  id: TEX-007
  technique_name: SVG displacement / turbulence filter
  industry_term: feTurbulence + feDisplacementMap distortion
  category: Texture & Detail
  subcategory: Procedural distortion
  description: Fractal noise from feTurbulence drives feDisplacementMap to warp images, text, or shapes, producing liquid ripples, gooey hover states, heat-haze, and organic edges. The displacement scale and noise frequency control the distortion.
  aesthetic_effect: Adds organic, fluid motion and an artful imperfection; the procedural warping reads as crafted, experimental and tactile.
  when_to_use: Hover/cursor-reactive imagery and type, liquid transitions, and decorative organic edges on creative sites.
  how_to_implement: Define an SVG filter: feTurbulence (baseFrequency, numOctaves) into feDisplacementMap (scale, xChannelSelector); apply via filter: url(#id); animate the turbulence seed or displacement scale for motion.
  libraries_tools: SVG filters (feTurbulence/feDisplacementMap); GSAP/SMIL to animate attributes; Codrops 'SVG Filter Effects' series; Henry Codes 'distort text with SVG'.
  difficulty: Medium
  performance_a11y_notes: Animating SVG filters re-renders the filtered region each frame, keep the area small and FPS modest; disable on reduced-motion. Some filters underperform in certain browsers; test.
  example_project: SVG Filter Effects: Moving Forward (Codrops)
  example_url: https://tympanus.net/codrops/2019/02/26/svg-filter-effects-moving-forward/
  example_source: Codrops
  pairs_well_with: Wavy/warped text; grain overlay; gradient mesh
  avoid_when: Large animated surfaces or performance/motion-sensitive contexts.

[TEX-008] Generative canvas background
  id: TEX-008
  technique_name: Generative canvas background
  industry_term: Generative / particle WebGL-canvas background
  category: Texture & Detail
  subcategory: Generative
  description: An algorithmic, often interactive background drawn in Canvas/WebGL, flow fields, particles, noise fields, fluid sims, or shader gradients, that subtly responds to pointer or scroll. Unique on each load.
  aesthetic_effect: Feels alive, bespoke and high-tech; the responsive generative motion reads as a custom, award-grade centerpiece distinct from any template.
  when_to_use: Hero sections and full-page backdrops for tech/creative brands and portfolios wanting a signature living surface.
  how_to_implement: Render a fragment shader (noise/flow) or particle system on a fullscreen canvas; drive parameters from pointer/scroll and time uniforms; throttle DPR and pause when offscreen.
  libraries_tools: Three.js / OGL / regl shaders; p5.js or vanilla Canvas for 2D particle/flow fields; Codrops WebGL tutorials.
  difficulty: High
  performance_a11y_notes: Can be GPU/CPU heavy and battery-draining, cap DPR/FPS, pause via IntersectionObserver, and offer a static fallback for reduced-motion and low-power devices.
  example_project: Building a Scroll-Revealed WebGL Gallery with GSAP, Three.js, Astro (Codrops)
  example_url: https://tympanus.net/codrops/2026/02/02/building-a-scroll-revealed-webgl-gallery-with-gsap-three-js-astro-and-barba-js/
  example_source: Codrops
  pairs_well_with: Dark mode; bloom; gradient mesh; kinetic type
  avoid_when: Performance budgets, low-end device audiences, or content-first pages.

[IMG-019] Aspect-ratio art direction
  id: IMG-019
  technique_name: Aspect-ratio art direction
  industry_term: <picture> + media-conditioned crops (art direction)
  category: Imagery & Media
  subcategory: Loading & art direction
  description: Different image crops/aspect ratios are served per breakpoint via <picture> + <source media>, e.g., a landscape hero on desktop and a portrait subject-focused crop on mobile.
  aesthetic_effect: Imagery that stays compositionally strong and on-subject at every screen size.
  when_to_use: Hero images and editorial photography that would lose their subject when simply scaled.
  how_to_implement: Use <picture> with multiple <source media='(min-width:...)' srcset='...'> pointing at distinct crops, ending with a fallback <img>; use plain srcset/sizes for resolution-only switching.
  libraries_tools: Native HTML <picture>/srcset/sizes, imgix/Cloudinary focal-point cropping
  difficulty: Low
  performance_a11y_notes: Serves the right bytes per device (perf win) and prevents awkward crops; set width/height to avoid layout shift and always include meaningful alt text.
  example_project: MDN 'Using responsive images in HTML'
  example_url: https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images
  example_source: MDN
  pairs_well_with: Blur-up placeholders, duotone processing, lazy loading
  avoid_when: Decorative images where a single crop works everywhere.

[CUR-007] Button Hover Choreography
  id: CUR-007
  technique_name: Button Hover Choreography
  industry_term: button hover choreography (layered hover states)
  category: Cursor & Microinteractions
  subcategory: Hover interactions
  description: Multi-part, sequenced hover state for buttons: background fill wiping in, label sliding/duplicating, arrow nudging, icon rotating, several coordinated micro-movements rather than a single color change.
  aesthetic_effect: Rich, satisfying, high-craft feedback; the layered motion makes the button feel responsive and premium.
  when_to_use: Primary CTAs, nav links, featured buttons where a moment of delight reinforces the brand.
  how_to_implement: Pseudo-element fill animated with clip-path/transform on :hover; duplicate the label and translateY both copies (text swap); nudge an arrow with translateX; stagger with transition-delay. Keep durations ~150-300ms.
  libraries_tools: CSS transitions/pseudo-elements/clip-path, GSAP, Framer Motion
  difficulty: Low
  performance_a11y_notes: Mirror all hover states on :focus-visible for keyboard users. Animate transform/opacity/clip-path (avoid layout props). Keep it snappy; soften or reduce under prefers-reduced-motion. Maintain text contrast during the fill transition.
  example_project: Magnetic Buttons (Codrops)
  example_url: https://tympanus.net/codrops/2020/08/05/magnetic-buttons/
  example_source: Codrops
  pairs_well_with: Magnetic buttons, link underline animation, custom cursor
  avoid_when: Dense UIs/tables, or when over-animation slows perceived responsiveness.

[CUR-009] Toggle / Switch Animation
  id: CUR-009
  technique_name: Toggle / Switch Animation
  industry_term: animated toggle/switch
  category: Cursor & Microinteractions
  subcategory: Control feedback
  description: On/off switches whose knob slides with the track color crossfading, sometimes with overshoot, an icon morph (sun/moon), or a springy settle, making binary state changes feel physical.
  aesthetic_effect: Satisfying, clear state communication; the motion makes settings feel responsive; a chance for brand delight (e.g. theme toggles).
  when_to_use: Settings, dark-mode toggles, feature flags, filters, opt-ins.
  how_to_implement: Style a checkbox (visually hidden) + label track + knob; on :checked, translateX the knob and transition the track background; add a slight spring via cubic-bezier overshoot; for theme toggles, morph an SVG icon. View Transitions can animate the broader theme swap.
  libraries_tools: CSS :checked + transform, Framer Motion (spring), GSAP, View Transitions API (theme change)
  difficulty: Low
  performance_a11y_notes: Back it with a real checkbox/switch (role=switch, aria-checked) so it's keyboard-operable and announced. State must be conveyed beyond color/position (label). Animate transform; soften under reduced-motion. Min 44px target.
  example_project: Animation and motion (web.dev)
  example_url: https://web.dev/learn/accessibility/motion
  example_source: web.dev
  pairs_well_with: Dark-mode theming, settings panels, view transitions
  avoid_when: When a clearer labeled control (radio/segmented) communicates the choice better.

[CUR-010] Form Field Focus States
  id: CUR-010
  technique_name: Form Field Focus States
  industry_term: form field focus/active states (floating label)
  category: Cursor & Microinteractions
  subcategory: Form feedback
  description: Inputs that respond to focus with animated cues: a floating/shrinking label rising to the top, an underline or border that draws in, and clear focus styling, plus inline validation feedback.
  aesthetic_effect: Guided, modern, reassuring form experience; reduces label clutter; communicates state and errors gracefully.
  when_to_use: Any form, contact, signup, checkout, search, especially where space is tight or a premium feel is wanted.
  how_to_implement: Floating label via :placeholder-shown + :focus state moving the label (transform/translate + scale); animate a border/underline with transform:scaleX; show inline validation with aria-describedby messages; use :focus-visible for the focus ring.
  libraries_tools: CSS :placeholder-shown/:focus-within, :focus-visible, React Hook Form, Framer Motion
  difficulty: Low
  performance_a11y_notes: Never use placeholder as the only label (fails when typing/AT). Keep a strong visible focus indicator (WCAG 2.4.7/2.4.11). Associate errors via aria-describedby/aria-invalid and announce them. Don't animate the focus ring's appearance away.
  example_project: Animation and motion (web.dev)
  example_url: https://web.dev/learn/accessibility/motion
  example_source: web.dev
  pairs_well_with: Inline validation, success micro-feedback, command palette search
  avoid_when: Never skip focus states; avoid over-animating fields in long/critical forms.

[EXP-005] Scroll-Driven CSS Animations
  id: EXP-005
  technique_name: Scroll-Driven CSS Animations
  industry_term: scroll-driven CSS (animation-timeline: scroll()/view())
  category: Emerging & Experimental
  subcategory: Native scroll animation
  description: Native CSS that links animations to scroll position or element visibility with zero JavaScript, using animation-timeline:scroll() (scroll progress) and view() (element-in-viewport progress) plus scroll-timeline/view-timeline.
  aesthetic_effect: Buttery, performant scroll effects, reveals, parallax, progress bars, pinned scaling, without JS jank.
  when_to_use: Progress bars, reveal-on-scroll, parallax, sticky-card scaling, image galleries, wherever scroll position should drive animation.
  how_to_implement: Define @keyframes, then animation:reveal linear; animation-timeline:view(); animation-range:entry 0% cover 40%; for whole-page progress use animation-timeline:scroll(root). Name custom timelines with scroll-timeline-name/view-timeline-name. Add a JS polyfill or fallback for Safari.
  libraries_tools: Native CSS (animation-timeline, scroll-timeline, view-timeline), scroll-timeline polyfill, GSAP ScrollTrigger (fallback)
  difficulty: Medium
  performance_a11y_notes: Runs off the main thread (Chrome 115+), far smoother than scroll listeners. Safari lacks support; the polyfill reintroduces JS cost, so ensure a graceful static fallback. Wrap in prefers-reduced-motion to disable. Keep animated properties compositor-friendly.
  example_project: A Practical Introduction to Scroll-Driven Animations (Codrops)
  example_url: https://tympanus.net/codrops/2024/01/17/a-practical-introduction-to-scroll-driven-animations-with-css-scroll-and-view/
  example_source: Codrops
  pairs_well_with: Sticky stacked cards, reading progress, parallax
  avoid_when: When you need identical behavior across all browsers today without a polyfill, or for complex sequenced timelines (JS may be clearer).

[EXP-007] Accessibility-Forward Motion
  id: EXP-007
  technique_name: Accessibility-Forward Motion
  industry_term: accessibility-forward motion (reduced-motion-first)
  category: Emerging & Experimental
  subcategory: Inclusive motion
  description: Designing animation so it respects vestibular and cognitive needs: honoring prefers-reduced-motion, offering an in-page motion toggle, avoiding large parallax/zoom triggers, and never conveying meaning by motion alone.
  aesthetic_effect: Inclusive polish that still feels crafted; trust and care signaled to all users; award juries increasingly reward it.
  when_to_use: Every animated site, but especially award-targeted, public-sector, and broad-audience products.
  how_to_implement: Wrap non-essential motion in @media (prefers-reduced-motion: no-preference); provide reduced variants (fades/instant) under reduce; add a persistent 'reduce motion' toggle that sets a class/data-attr; avoid large-area panning/scaling that triggers vestibular discomfort; cap durations.
  libraries_tools: CSS prefers-reduced-motion media query, JS matchMedia, motion toggle (localStorage), GSAP/Framer Motion reduced-motion guards
  difficulty: Low
  performance_a11y_notes: This IS the a11y practice: large objects scaling/panning are vestibular triggers; keep essential info in text; let focus rings appear instantly; allow pause/stop; default to reduced when in doubt (web.dev guidance). WCAG 2.3.3 (Animation from Interactions).
  example_project: Animation and motion (web.dev)
  example_url: https://web.dev/learn/accessibility/motion
  example_source: web.dev
  pairs_well_with: Scroll-driven CSS, scrollytelling, immersive intros (all should respect it)
  avoid_when: Never avoid, this is a baseline expectation for any motion-rich build.


Build note additions specific to this spec (not in the database):
- TEX-008 as built here is a Three.js r128 scene, not a fragment-shader plane: Line2 fat lines for the five warp threads and the weft, TorusGeometry knots, MeshBasicMaterial throughout, transparent clear colour over the butter ground, one WebGL context, dpr capped, lazy after first paint. The generative part is the per-load geometry (date-driven knot pattern, per-thread sag phase, fibre noise in the alpha map).
- TEX-007 is pointer-only and headings-only: an SVG filter with feTurbulence baseFrequency 0.012 and feDisplacementMap scale animated 0 to 6 to 0 over 0.38s (Knot easing) on hover, mirrored on :focus-visible as a 2px stitch outline instead (no displacement for keyboard users), never on body text, disabled under reduced motion.
- MOT-018 is the only reveal language on the site: `clip-path: inset(0 100% 0 0)` to `inset(0 0 0 0)` with `animation-timeline: view()` and `animation-range: entry 0% cover 35%`, Shuttle easing, ScrollTrigger fallback on Safari, unclipped under reduced motion.
- TYP-014: the heading passes are true H2s in the document order; Big Shoulders Display at display size on butter with a single weft thread SVG beneath.
- TRN-002: the progress line is a vertical running stitch (SVG stroke-dasharray 6 4) whose stroke-dashoffset is bound to the real load fraction, role progressbar with aria-valuenow, exit is a tie-off knot at the foot of the gutter, no overlay, no counter.

### 3.10 PALETTE AND TYPE

Palette roles and hex:
- Ground: butter #F6E7A1, the page background and the heading passes; deep butter #EBD77A for the 1px edges of butter blocks against white and for pressed chips; pale butter #FBF3CF for undyed thread.
- Weft: white #FFFFFF, every row board, card, table, form and the heading band.
- Thread: indigo #2B2F8F for headings, links, the wordmark, threads, stitches, the primary button fill, active nav; deep indigo #1B1E5C for pressed states, knots and small labels on butter; ink #14163A for body text; muted indigo #4F5280 for secondary text, captions and freshness stamps.
- Semantic, inside the product views only: up #1F7A4D with an up arrow, down #B3261E with a down arrow, unchanged #4F5280, "slightly behind" #8A5A00; meaning always carried by an arrow or a word.
- Contrast: every pair in 0.1 passes AA, most AAA; butter is a text colour only on indigo.

Named colour story: "butter warp through a white weft, with indigo thread". A two-surface textile story (a warm ground showing between white blocks) with one thread colour, which is not a neutral field plus one accent (butter is a full second surface, not a neutral) and is none of the nine logged stories. Accent hue family for the registry: indigo (blue violet), hue 238 degrees at 54 percent saturation, against Smart Augment's prussian, a desaturated navy at hue 211 on paper; a blue violet on saturated yellow reads as a different family at a glance, and no logged build uses violet or blue violet at all. Warmth: the butter ground and the morning light in the cloth photography; restraint: the white weft carries the reading.

Type:
- Heading: Big Shoulders Display, variable, wght 100 to 900, never used in any logged build; condensed, upright, a mill stencil feel that saves width in five columns and reads as "organised" rather than "editorial". H1 at wght 800, H2 heading passes at wght 700, H3 cell heads at wght 600.
- Body and UI: Manrope, variable, wght 200 to 800, `font-feature-settings: "tnum" 1`; body 16px at 1440, labels 13px wght 600, figures wght 700 tabular at text size. Manrope has appeared in no logged build; the pairing is new.
- Scale (fluid to 2560 via `--vwc: min(1vw, 25.6px)`): H1 clamp(44px, 2.4rem + 3.6 * var(--vwc), 118px); H2 heading pass clamp(30px, 1.6rem + 1.8 * var(--vwc), 64px); H3 clamp(19px, 1.05rem + 0.4 * var(--vwc), 26px); body clamp(15px, 0.94rem + 0.14 * var(--vwc), 17.5px); labels 13px fixed.
- Kickers, labels and figures: no uppercase, no letter-spacing, no mono. Row boards have no kicker; the heading pass above them is the title. Cell heads are the thread name in Big Shoulders 600 at 15px with the thread's knot glyph. In-cell labels are Manrope 600 at 13px sentence case. Figures are Manrope 700 tabular at the same size as their sentence; the emphasised figure in a cell gets a 12px indigo thread underline, never a bigger size.

### 3.11 MOTION SIGNATURE

- Shuttle: cubic-bezier(0.36, 0.01, 0.10, 1). The shuttle's pass, fast out of the hand and settling at the far edge. Used for reveals (the weft-pass wipes), the reed sweep, the stitch draw, nav hide and return, hover stitches.
- Knot: cubic-bezier(0.22, 1.12, 0.36, 1). The knot pulling tight with a small overshoot. Used for docking, toggles, presses, chips, the seal, the plucked heading, the pass beat.
- Durations: fast 0.11s (hover stitches, chip presses), base 0.38s (reveals, docking, toggles), slow 1.2s (the stitch tie-off, the gravity flip handoff, the seal). Idle cadence 11s (the travelling stitch on buttons, the weft creep on the loom). Every motion technique, page scene and kit animation uses these two curves and three durations; nothing else is permitted. None of the eighteen logged curves and none of the logged duration triples.

### 3.12 TYPOGRAPHIC SET PIECE

The Tightening. The H1 on the home hero, "Which of the five threads your money runs on moved overnight?", is set in Big Shoulders Display across all five columns, and at first paint every glyph sits at wght 500 (readable, but slack). As the weft passes along the near edge of the loom beneath it, each glyph in turn pulls to wght 800 with the Knot easing, left to right at 18ms per glyph, so the sentence tightens like thread drawn through cloth, finishing exactly as the weft knots the fifth warp. Split by `Intl.Segmenter` into grapheme spans, animated with `font-variation-settings` through a registered `@property`, one file (Big Shoulders Display variable, subset to Latin), paint-heavy so it runs once on load and never on scroll. Reduced motion renders wght 800 immediately. It lives only on the home hero; on interior pages the H1 arrives tight. On /brief a smaller echo runs on the sample issue's date line. Named for the registry, unlike every logged set piece.

### 3.13 MOTION AND ACCESSIBILITY BUDGET

Performance budget in one line: GSAP plus native scroll as the backbone, Three.js r128 as the one deliberate heavy library lazy-loaded after first paint, initial JS under 350KB gzipped excluding the lazy 3D bundle, LCP under 2.5s with the stitch running, CLS under 0.1 (the canvas is fixed and the poster reserves its box), 55fps or better sampled through the 1.3vh signature scroll, one WebGL context per page, dpr capped at 1.5 and 1.0 on touch, render paused offscreen.

Per motion item, the reduced-motion and mobile fallbacks:
- The loom (TEX-008): reduced motion serves the flat-cloth poster with the cells docked; under 900px or coarse pointer, the 2D canvas thread strip with the pull gesture; low power drops to the poster while the DOM docking still runs.
- The selvedge stitch (TRN-002): reduced motion shows the stitch complete and fades once; mobile identical, tied off within 1.5s, hard cap 4s.
- Weft-pass reveals (MOT-018): reduced motion shows content unclipped; mobile uses the same clip at a shorter range; Safari without scroll-timeline support uses ScrollTrigger.
- Heading passes and the week strip parallax (EXP-005): reduced motion static; mobile ranges shortened.
- The Tightening (TYP-003): reduced motion renders the final weight; mobile runs once at half the glyph stagger.
- The plucked heading (TEX-007): pointer only; keyboard gets a stitch outline; reduced motion off.
- Bobbin, toggles and fields (CUR-007, CUR-009, CUR-010): aria-live on state changes, role switch, 44px targets, static states under reduced motion, press stands in for hover on touch.
- The reduce-motion control (EXP-007): in the footer and the mobile menu, persisted in localStorage, sets `data-motion="reduced"` on the root, honoured by every technique above.
- Keyboard: every interactive element reachable, a 2px indigo focus ring with a 2px white offset on white and a 2px butter offset on indigo; the loom is aria-hidden while its five items exist as real DOM.

### 3.14 AMBITION AND RESTRAINT CHECK

One named wow moment, THE PASS, delivered by the one signature move; motion is a material felt across the visit with three loud beats (the tie-off, the pass, the footer seal) and quick, exact weft-pass motion elsewhere; the idea is legible in the look (five threads, rows, knots, cloth) before a word is read; beside the nine logged builds it is unmistakably its own thing; Site of the Day worthy. One signature move, a two-surface palette with one thread colour, twelve techniques inside a stated budget. Considered and cut: Lenis, magnetic and tilt hovers, marquees, paper texture, masonry, numbered lists, badges, a $0 card, a hero price under the button, bloom or any post chain, and a sixth column (the five-thread identity is fixed; density grows inside the columns).

### 3.15 BENCHMARKS

https://www.awwwards.com/sites/united-carriers (one colour, one Three.js hero, store-grade weight) · https://www.awwwards.com/sites/cerebrium (a working tool inside the marketing page, the bar for the ranker) · https://tympanus.net/codrops/2026/02/02/building-a-scroll-revealed-webgl-gallery-with-gsap-three-js-astro-and-barba-js/ (generative surfaces scrubbed by scroll) · https://www.lucas-aufrere.com (reveal choreography and first-paint sequencing).

### 3.16 TIER JUSTIFICATION

Tier 1, procedural concept site, not forced (the last two tiers were 2 and 1, so Tier 1 is not three in a row). One line: SaveBrew's identity is a system, five threads read every morning, and drawing that system in code expresses it better than any photograph of it could; a generative loom, procedural stitches and a computed twill make the identity out of code at store-grade weight with no shader pipeline to stream. The two further generative surfaces beyond the signature scene, as the tier requires: (1) THE SELVEDGE, a procedural running-stitch divider drawn on a 2D canvas per section, each instance generated with its own slight stitch-length and angle jitter and a seed from the section's id, used as the loader line, the row divider and the card edge; (2) THE TWILL, a procedural diagonal weave field (a 2D canvas pattern of over-two-under-two thread crossings at a 45 degree lay, thread width and gap from the palette tokens, generated at build size and tiled) used as the footer field, the membership row's ground and the legal page margins at 6 percent contrast. A third, smaller one, THE THREAD STRIP (five short vertical threads with per-load sag drawn on canvas at the head of every row board), is the continuity device. Media is still sourced and graded per media_engine.md for the cloth photography, and the media manifest ships.

### 3.17 THE FULL-WIDTH LAYOUT RULE (named section, CSS-level)

The owner's second hard rule, made concrete for Warp Columns. No page on this site uses a fixed centred container, and no page leaves an empty outer third at 1280, 1440, 1920 or 2560; every row board runs from the left gutter to the right gutter by construction, because the five warp columns divide the whole width.

- Root tokens: `--gutter: clamp(16px, 1.25vw, 32px); --gap: clamp(16px, 1.25vw, 32px); --vwc: min(1vw, 25.6px); --col: calc((100vw - 2 * var(--gutter) - 4 * var(--gap)) / 5);` The `--vwc` unit caps fluid growth at 2560px so type and spacing stop scaling there while layout keeps filling.
- The pass (a row board): `.pass { width: 100%; max-width: none; padding-inline: var(--gutter); display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); column-gap: var(--gap); }` There is no `.container`, no `max-width: 1200px`, no `margin: 0 auto` wrapper, no `max(1720px, 86vw)`, no `min(100% minus 2 gutters, 1800px)`. A lint rule in QA fails any stylesheet that declares a max-width above 100 percent on a block that holds a section.
- Column counts by breakpoint (the collapse rules of 0.2 in CSS): 1440 and up, five; 1280 to 1439, five for row boards and four for prose boards (`columns: 34ch` yields four); 1024 to 1279, `grid-template-columns: repeat(3, minmax(0, 1fr))` with the fourth and fifth cells on a second row (`grid-column: span 1` and the fifth `span 1`, the remaining track filled by the row's thread strip) so nothing sits empty; 768 to 1023, `repeat(2, minmax(0, 1fr))` with the fifth cell `grid-column: 1 / -1`; below 768, one column with the sticky five-thread tab strip.
- Spanning cells: the membership row spans columns one to two (the Daily), three to four (the Daily for Two) and five ("What's free to read"); the "Look inside the dashboard" row spans one to three (the desktop window) and four to five (the phone view beside it, never overlapping); at 1024 to 1279 both rows wrap to two rows; below 1024 they stack.
- Prose: no lone 65ch column, ever. Long text (guide bodies, About, the legal pages) is set in CSS multicolumn, `columns: 34ch; column-gap: var(--gap);`, which yields two columns at 1280, three at 1440, four at 1920 and five at 2560 (matching the warp count at 2560 by design), or beside a module in a two-track pass (`grid-template-columns: minmax(0, 3fr) minmax(0, 2fr)`), never alone with butter either side. Legal pages set their clauses in two to four columns with the twill margin.
- Media and modules run edge to edge: the loom canvas is `width: 100vw` fixed; the week strip and the cloth photography bands are `width: 100vw` with no inset; the heading passes, the membership row, the SMS row and the footer span the full width with only `--gutter` padding.
- The heading band (header) is full width; the footer's seal, address block, link columns, the reduce-motion control and the SMS reminder sit on the same five-column pass.
- Verification at 1280, 1440, 1920 and 2560: QA screenshots the home page, /brief, /membership, /guides and /your-moves at each width and fails if any row's content box is narrower than the viewport minus twice `--gutter`, if any outer third of a row is empty, or if any butter block runs taller than 40 percent of the viewport with running text on it.

### 3.18 THE LOADER (per preloader_module.md)

Name: the selvedge stitch (a fill gauge in the module's terms, cast as the cloth's finished edge, not the hero motif). Scene zero: the page is painted in full at first paint on its butter ground with the white weft blocks in place; down the left gutter, from the top edge, a dashed indigo running stitch (stroke-dasharray 6 4, 2px, drawn on the Selvedge canvas) draws toward the foot of the viewport with the Shuttle easing, its length bound to the real load fraction (fonts ready, kit SVG ready, poster decoded, Three.js fetched); at ready it ties off with a small knot glyph (Knot easing, 0.38s) and the loom's weft begins its first pass. It masks real load only, never invents delay, never pads, never holds a ready page; nothing counts, nothing flips, and the stitch is a kit divider, not the loom. Skip affordance: "Go straight in", an indigo text link at the bottom centre from 0s, which completes the stitch at once; the stitch also force-completes at the 4s hard cap. Target under 2s of visible stitch on broadband. The hero copy, nav and Bobbin are never covered. Reduced motion: the stitch renders complete and fades in 0.3s. Registry `loader_transition`: "selvedge stitch: a dashed indigo running stitch draws down the left gutter edge in step with real load over the already painted page, ties off at ready, no count, no Flip, skip at the bottom centre" (differs from the previous build's receipt print head and from every logged loader).

### 3.19 BRAND GRAPHIC KIT PLAN (per brand_graphic_kit.md)

All assets bespoke SVG or procedural canvas, derived from the governing idea, animated with Shuttle and Knot, reduced-motion static.

1. The signature motif, drawn: THE KNOT. A vertical warp line (2px indigo) crossed by a weft loop that passes over, under and pulls tight, in a 24 by 24 grid: the loop is a single path with a small overshoot bulge at the crossing. Draw-in: the warp draws top to bottom (Shuttle), the loop draws left to right and tightens (Knot). It marks each brief item, sits beside every cell head, starts the wordmark (SaveBrew's mark is the knot), and is the favicon.
2. The seal: THE SELVEDGE SEAL. A square woven badge, 160px in the footer and 96px on cards: five vertical warp threads crossed by seven weft rows drawn as a real over-under weave, with the letters S and B formed by which crossings are indigo and which are butter (a woven monogram), bounded by a running-stitch border. Used on About, the order confirmation, the membership cards' corner and the footer. Animation: woven row by row top to bottom (Shuttle per row), the border stitches last (Knot).
3. Dividers built from the motif: (a) THE SELVEDGE, the procedural running stitch (generative surface one) as the row divider and card edge, drawn on scroll; (b) THE THREAD STRIP, five short vertical threads with per-load sag at the head of every row board, labelled with the thread names, which is also the continuity device the loom hands off to; (c) THE WEFT PASS, a single horizontal indigo thread under every heading pass with one knot at the left gutter, drawn left to right on reveal. No default horizontal rules anywhere.
4. Icon style and the eleven core icons: 24px grid, 1.75px stroke, square caps (cut thread ends), every icon built from a thread crossing or a knot, indigo by default, deep indigo when active. Rates (a thread rising through a knot), Cashback (a thread looping back on itself), Coupons (a thread with a cut end), Seasonal (four knots on one thread), Paycheck (a thread with a bar knot), Goals (a thread with a filled knot), Texts (a thread ending in a small speech knot), Archive (three stacked weft rows), Your moves (one thread pulled up out of a row), Roundup (a thread with three knots), Membership (two threads plied). No icon fonts, no off-the-shelf sets.
5. Numerals and labels: figures in Manrope 700 tabular at text size with a 12px indigo thread underline for the emphasised figure; nothing is numbered on the marketing site; brief items are marked by their thread's knot and name.
6. Texture: THE TWILL (generative surface two), the procedural diagonal weave field at 6 percent contrast, used only in the footer, the membership row's ground and the legal page margins. No grain in the DOM.

Every page uses the kit: cell heads carry the knot, rows divide with the selvedge or the thread strip, heading passes carry the weft pass, icons come from the eleven, the seal closes the footer. The motif and kit read as nothing like scan lines, trial cells, provenance leaders, day cells, tally marks, lit windows, plates, glass tiles, tags or the receipt line.

### 3.20 THE DESIGNED MOBILE HERO (375px)

Not a poster of the desktop hero. At 375 the loom is replaced by a 2D canvas band, 180px tall, under the standfirst and the Bobbin: five vertical threads across the full width (one per column position, 20 percent each), sagging slightly, each labelled beneath with its thread name and knot glyph. The mobile moment: PULL A THREAD. A one-finger drag down on any thread pulls it (the canvas draws the thread stretching with the finger, Knot easing on release), and past 40px the thread's knot slides out beneath the band as a card carrying today's item for that thread (the real headline and action chip from the sample brief); releasing early lets the thread spring back. A tap without a drag on a thread also opens its card. The five-thread tab strip under the header (44px, sticky) is the same five threads, so the identity is present twice above the fold. The Tightening runs once on the H1 at half stagger. Reduced motion: the band is static, the cards open without animation on tap.

### 3.21 THE INTERACTIVE FEATURE: "Your moves", a ranker (full page brief)

Format: RANKER (registry string "ranker"), the Offering Spec's recommended candidate, recast into the weave; it is not a sorter (a sorter files items into bins, this orders editorial moves for one visitor), not a quiz (no product recommendation, no score), and not a calculator (no arithmetic result). Route /your-moves, in the nav as "Your moves", public, no account, no form, no email field.

- Purpose in one line: dramatise the product promise (someone else does the sifting and hands you the moves worth acting on) by ranking this week's public candidates for the visitor's own situation, using editorial weights rather than arithmetic.
- Heading pass: "Which threads should you pull first?" Standfirst: "Answer six yes or no questions about your money and this week's moves are ranked for you, with the minutes each takes. Members get a ranked list like this each weekday morning."
- Inputs, six toggles (CUR-009, role switch, 44px targets, each a thread that pulls tight when on), in the five-column pass with the sixth centred beneath: has a high yield savings account; money sitting in a big bank account under 1 percent; carries a card with rotating categories; saving toward a dated goal; bought something over $200 in the last month; has not looked at the paycheck split this year.
- Data: this week's candidates, six to eight items authored by the copy step and refreshed each Saturday with the Roundup, held in a JSON file in the repo (`/data/moves.json`): id, thread (one of the five), headline, minutes, one-line why, one-line "skip this if", and a weight vector over the six toggles (integers 0 to 3). No live rates unless the owner supplies a feed; figures are labelled "about".
- Logic, client side and deterministic: score = base editorial rank weight (8 minus its position in the editors' order) plus the sum of toggle weights for toggles that are on; ties broken by fewer minutes; the top four are shown ranked one to four with their minutes, the why line and the skip-if line; the remaining candidates sit beneath, greyed to muted indigo, each with the one-line reason it ranked lower ("ranked lower because you don't carry a rotating category card"). Re-ranking on every toggle change is animated with GSAP Flip (Knot easing, 0.38s) so the threads visibly re-order; the pulled threads lift out of the cloth in the page scene as the rank changes.
- States: empty (no toggles on): the editors' default order with the line "This is the editors' order for this week. Turn on what applies to you and it re-ranks."; in progress: each toggle re-ranks live and the count line reads "4 of 7 shown for you"; result: the ranked four with a "Copy this list" control (clipboard, CUR-011 tick confirmation) and a printable view; error: none possible, the data ships with the page.
- End of the page: the Bobbin "Add the Daily to my cart" with the line beneath it, verbatim from the Offering Spec, "Members get a ranked list like this each weekday morning, built on that morning's brief." Then the educational disclaimer from Offering Spec section 12 at the foot.
- Page scene: the visitor's threads (one per candidate) lie flat in the cloth; when a toggle turns on, the affected threads lift out of the cloth in the new order (the lightweight canvas scene of 3.7), and the ranked four stand highest.
- Works with motion disabled and on a 375px viewport with one thumb: toggles stack in one column, the ranked list stacks beneath, the Bobbin is full width. QA must turn on toggles, watch the re-rank, copy the list and land on /membership from the CTA.

### 3.22 MEDIA DIRECTION (for the creative-asset engine, Higgsfield MCP)

Subject world: material and texture with no people. Woven cloth at macro, denim twill, raw canvas, cotton thread on spools, selvedge edges, a loom's warp under tension, morning light raking across fabric. Never an office, desk, kitchen counter, car, till, threshold or clinic, never hands, never a face, never a coffee cup or a beer glass, no text, no logos, no watermark on anything. The butter and indigo of the palette are found in the world: undyed cotton and indigo-dyed denim under warm early light.

The 12 second hero loop, four independent 3 second clips (16:9, photoreal, no text, no logos, no watermark, hard cuts, seamless from clip four back to clip one). Where it lives: the "What did last week's pass look like?" row, full width behind the week strip at 35 percent, and the About hero. Generation prompts, literal, for generate_video:
1. "Macro shot of undyed cotton warp threads under tension on a wooden loom, dozens of parallel pale threads receding into soft focus, warm early morning window light raking from the left, tiny fibres catching the light, very slow lateral slider move of two centimetres, shallow depth of field, no people, no hands, no text, no logos, no watermark, photoreal, 16:9, 3 seconds."
2. "Extreme close up of indigo denim twill weave, diagonal ridges of blue and white thread filling the frame, slow push in of a few millimetres, warm sunlight sweeping slowly across the cloth from one side, fibres visible, no people, no text, no logos, no watermark, photoreal, 16:9, 3 seconds."
3. "A single indigo cotton thread being drawn across pale undyed cloth on a loom, the thread pulling straight and taut, the shuttle out of frame, macro lens, static tripod, warm morning light, shallow depth of field, no people, no hands visible, no text, no logos, no watermark, photoreal, 16:9, 3 seconds."
4. "Selvedge edge of a bolt of pale cotton canvas with a fine indigo stitched edge, the cloth unrolling slowly toward the camera on a wooden table, soft warm light from a window, shallow depth of field, static camera, no people, no hands, no text, no logos, no watermark, photoreal, 16:9, 3 seconds."

The 6 to 8 second product-in-motion clip: not generated; a built screen capture of the three real HTML dashboard views at 1440 by 900 in the app's own frame (Offering Spec 10.1, no browser chrome). The camera: a single slow left-to-right pan at the speed of a weft pass across Today, the Rate Tracker and Goals laid side by side with a gutter, easing with Shuttle, during which one text toggle clicks on in the Today rail (Knot), the Bank A row's seven day change ticks from 0.00 to +0.05, and the Emergency fund bar fills from 58 to 60 percent; the freshness stamps read 6:00 AM ET throughout; the capture ends on Goals with a 0.4s hold. Ungraded, on the white weft.

Site photography, stills (sourced per media_engine.md from Unsplash, Pexels or Coverr where a match exists, otherwise generated with the prompts below; self-hosted; every asset in MEDIA_MANIFEST.json). Each: prompt, slot, aspect, page.
1. "Overhead flat lay of undyed cotton canvas with a fine indigo selvedge stitch along one edge, warm morning light from the upper left, soft shadows, no objects on the cloth, no people, no text, no logos, no watermark, photoreal." Slot: the About page hero band. Aspect 21:9 desktop, 4:5 phone (IMG-019 crops). Page: /about.
2. "Macro of a wooden spool of indigo cotton thread on pale linen, a single thread trailing off frame to the right, warm side light, shallow depth of field, no people, no text, no logos, no watermark, photoreal." Slot: the membership row's fifth column ("What's free to read") background at 30 percent. Aspect 1:1. Page: home and /membership.
3. "Five parallel indigo threads laid across raw white canvas at even spacing, seen from directly above, one thread with a small knot tied in it, warm daylight, crisp fibres, no people, no text, no logos, no watermark, photoreal." Slot: the "What's in today's pass?" heading pass background at 20 percent on home, and the /brief page header. Aspect 3:1 desktop, 4:3 phone. Page: home and /brief.
4. "Close up of a wooden loom reed and beater with pale warp threads passing through its slots, warm morning light, dust in the air, shallow depth of field, no people, no hands, no text, no logos, no watermark, photoreal." Slot: the "Which threads should you pull first?" row's edge image. Aspect 4:5. Page: home and /your-moves.
5. "Indigo denim twill fabric folded once, the fold catching warm morning light, the weave clearly visible at macro, no people, no text, no logos, no watermark, photoreal." Slot: the /roundup page header band. Aspect 16:9 desktop, 1:1 phone. Page: /roundup.
6. "A stack of folded pale cotton cloths with different weaves, plain, twill and herringbone, edges aligned, soft window light from the left, no people, no text, no logos, no watermark, photoreal." Slot: the /guides index header. Aspect 21:9 desktop, 4:5 phone. Page: /guides.
7. "Macro of a running stitch in indigo thread along the hem of pale linen, the needle out of frame, each stitch slightly irregular, warm light, no people, no hands, no text, no logos, no watermark, photoreal." Slot: the /contact page side image beside the address. Aspect 4:5. Page: /contact.
8. "A loose indigo thread curling on white canvas, out of place, warm light, shallow depth of field, no people, no text, no logos, no watermark, photoreal." Slot: the 404 page. Aspect 1:1. Page: /404.

Blog hero prompts, one per guide post (the four posts of 3.24), 16:9 desktop and 4:5 phone, no text, no logos, no watermark, photoreal, generated with generate_image:
1. For "How to make a rotating cashback category actually pay": "Macro of a single indigo thread looping back on itself once on pale canvas, the loop lit by warm morning light, no people, no text, no logos, no watermark, photoreal."
2. For "The national average savings rate is not a benchmark, it is a warning": "Two threads side by side on raw canvas, one thin pale thread and one thick indigo thread, seen from above in warm light, the difference obvious at a glance, no people, no text, no logos, no watermark, photoreal."
3. For "A 4.00% account against the one you already have: the arithmetic on $10,000": "Macro of a cloth measuring tape's woven edge lying across indigo denim, no numerals legible, warm light, shallow depth of field, no people, no text, no logos, no watermark, photoreal."
4. For "Why patio furniture is cheap in October: the seasonal buying cycle, plainly": "Four small knots tied at even intervals along one indigo thread on pale linen, overhead, warm light, no people, no text, no logos, no watermark, photoreal."

Grade recipe, one grade for every sourced or generated asset, deliberately not the sisters' grayscale, sepia and hue-rotate formula: natural colour retained, then a split tone toward the palette. Base: `filter: contrast(1.05) saturate(0.9) brightness(1.04);` Shadow overlay: indigo #2B2F8F at 8 to 14 percent, `mix-blend-mode: lighten`. Highlight overlay: butter #F6E7A1 at 10 to 16 percent, `mix-blend-mode: multiply`. Strength range: 12 to 24 percent total overlay opacity, tuned per asset so undyed cloth stays pale and denim stays indigo; applied to `video` and `img` alike; never to the product screens. Logged with the design system as "morning light on cloth".

HDRI and texture needs for the loom scene: none for lighting, because the loom uses unlit MeshBasicMaterial with flat dye colours (contrast is guaranteed and there is nothing to stream). Two texture assets only: (1) a 256 by 16 thread alpha map generated on the client (fibre noise, no download); (2) one CC0 fabric texture from Poly Haven (a plain-weave cotton or linen, 1K, colour map only, about 300KB WebP) used solely as the mobile poster's ground and the /404 page's field, listed in the manifest with its CC0 licence. No HDRI, no normal maps, no glTF.

### 3.23 SECTION RHYTHM FOR EVERY PAGE

Rules that apply to all pages: no two adjacent rows share a pattern and a page never uses one pattern twice; every row has its own entrance (the weft-pass wipe is the base language, varied by direction, stagger and what draws); each page has its own text-hover treatment mirrored on :focus-visible; each page has its own lightweight scene (3.7); every page carries the thread strip somewhere; the disclaimer from Offering Spec 12 runs on every content page. Section titles below are the heading passes, set as questions where the reader is asking one.

HOME (/). Text hover: the plucked thread (TEX-007). 1. Hero, the loom (full bleed) with the H1 (The Tightening), standfirst, audience line, Bobbin, roundup link and the five knot labels. 2. "What's in today's pass?": Today's pass, the five-column row of the sample brief (the five items from Offering Spec 10.3, one per thread, each cell with the knot, the thread name, the headline, the two line summary and the action chip); entrance: cells dock onto the warp positions (Knot). 3. "What does it cost?": the membership row, the Daily spanning columns one to two, the Daily for Two spanning three to four, the fifth column "What's free to read" on the twill; both prices always printed, the renewal sentence at the same weight, the inclusion lists in full (eight and eleven), the tax line, the Bobbin per card; entrance: the weft pass draws under the heading then the cards wipe in from the left (Shuttle). 4. "What did last week's pass look like?": the week strip, a full-width horizontal woven strip over the hero loop, five threads by five weekdays as a knot matrix (Recipe 08), hover or tap a knot to read that item; entrance: knots tie in row by row. 5. "What's inside the dashboard?": the desktop window spanning columns one to three and the phone view in four to five, the three views switchable by the thread strip (Today, Rates, Goals), the secondary CTA "Look inside the dashboard" from the hero scrolls here; entrance: each view populates top to bottom at 40ms stagger, one toggle clicks. 6. "Which threads should you pull first?": the ranker embedded (its six toggles and the top four), linking to /your-moves; entrance: threads lift from the cloth. 7. "What's free to read?": this week's Roundup spanning two columns and three guides in the remaining three; entrance: a weft pass per cell, alternating direction. 8. "What do people ask before they join?": the FAQ as an editorial index in five columns (questions as cell heads, answers beneath, knot markers), not an accordion; entrance: knots pop then answers wipe. 9. Join Our SMS List (verbatim block) as a full-width inline row: heading left, consent copy across the middle columns, the phone field and control at the right end, the selvedge stitch as the field underline; entrance: the stitch draws. 10. Footer as a destination on the twill: the Selvedge Seal weaving itself, the line "Tomorrow's pass goes out at 6:30 AM Eastern", link columns on the five-column pass, the reduce-motion control, 660 American Ave, King Of Prussia, PA 19406, (888) 338-8809, support@savebrew.com, Privacy and Terms.

TODAY'S BRIEF SAMPLE (/brief, public). Text hover: weight tightening (wght 400 to 800). Scene: one weft thread weaving five knots across the page head. 1. Header pass: the date line (a Tightening echo), "Published 6:30 AM ET", the disclaimer visible without scrolling. 2. The five items in full, one per column, with summaries and action chips (chips inert on the public page, labelled as members' actions). 3. "What the members' version adds": the rate strip, saved items, the archive, texts, in five cells. 4. "Yesterday's pass" strip (five knots, greyed, hover to read). 5. Membership row (compact: the two cards' names, prices, Bobbins). 6. Footer.

MEMBERSHIP (/membership, the pricing page). Text hover: the running stitch underline. Scene: two threads plied into one cord that untwist on hover. 1. Heading pass "What does it cost?" with the cadence control (Monthly | Yearly, monthly default) as two toggles that ply together. 2. The two cards in the warp (one to two, three to four), the fifth column "What's free to read"; both prices on each card, renewal sentence, full inclusions, tax line, Bobbin. 3. "How do I cancel?": the two click path as two knots on a thread (Membership, then Cancel membership), plus the email path. 4. "What do people ask before they join?" index (the pricing questions). 5. Footer. No badge, no giant numeral, no $0 card, no stepper, no TOTAL line.

THE DASHBOARD (/today, /rates, /goals, /archive, member pages). These are the product's own views built to Offering Spec 10.3 (app bar with the knot mark and wordmark left, tabs inline, date pill, "Texts on" bell, avatar), on white with the thread strip as the tab indicator; the marketing site shows them in "What's inside the dashboard?" and the product clip. Scene: none beyond the thread strip (the app stays fast). Text hover: standard link states only.

ROUNDUP (/roundup, Saturdays, public, RSS). Text hover: the first letter knots (a 1.12 overshoot scale). Scene: one thread with three knots tracked along the page. 1. Header pass "What moved this week?" with the date and the disclaimer. 2. The three moves, each spanning columns (one to two, three, four to five) so the row still fills. 3. "Where the tracked rates ended the week": a knot matrix row of the tracked accounts (illustrative until a data source is confirmed). 4. "Past Saturdays": the archive list, five columns of dated entries with stable URLs. 5. Membership row, compact. 6. Footer.

GUIDES (/guides and /guides/slug). Index text hover: thread underline unspools. Scene: a spool unwinding as reading progress. Index: 1. Header pass "What's free to read?" over still 6. 2. The twelve guides in the warp columns, each guide placed in its thread's column (rates guides under Rates, and so on), a knot and one line each. 3. Roundup cross link row. 4. Footer. Post pages: 1. Hero band with the blog image (IMG-019 crops) and the headline. 2. The body in CSS multicolumn (two to five columns by width) with pull threads (a highlighted sentence set as a weft pass across the columns) instead of pull quotes. 3. The disclaimer. 4. "Read next" as three knots. 5. Membership row, compact. 6. Footer.

YOUR MOVES (/your-moves). As 3.21. Text hover: the word lifts 2px on a thread shadow. 1. Heading pass. 2. The six toggles. 3. The ranked four and the greyed rest. 4. The Bobbin with the members line. 5. Disclaimer. 6. Footer.

ABOUT (/about). Text hover: a butter dye wash behind the word. Scene: the Selvedge Seal woven row by row. 1. Hero band over still 1 with the heading pass "Who checks the threads?". 2. The About copy (350 to 650 words from the content engine) in multicolumn beside the seal. 3. "How items are chosen" (the referral-fee line only if the owner confirms it; otherwise the editorial line only if true; otherwise nothing). 4. "Where we are": the King of Prussia address, phone and email as a row. 5. Membership row, compact. 6. Footer.

CONTACT (/contact). Text hover: stitch dashes under links. Scene: a knot tied at the address line. 1. Heading pass "How do I reach a person?". 2. The address, phone and email in three columns, the support hours, still 7 in the remaining columns. 3. A contact form (name, email, message; CUR-010 stitch underlines; GOV.UK errors; submit "Send my message"), which is support, not capture. 4. Footer.

CART (drawer on any page, and /cart). Text hover: standard. Scene: the knot sliding along a thread into the spool glyph. One membership at a time, quantity fixed at 1; the name, the cadence, today's charge, the renewal amount and date in words, the tax line, the cadence switch (toggle, Knot), "Go to checkout" as the Bobbin; replacing a membership says so in a line; empty state offers the membership link; the drawer opens from the right with a weft-pass wipe.

CHECKOUT (/checkout). The plainest page on the site: one column on white, the selvedge stitch down the left gutter advancing one section at a time (Contact, Billing address, Payment, Order summary), top aligned labels, required and optional marked, autocomplete tokens, no account step, one accepted payment mark near the card fields, the unchecked age and terms box, submit "Pay $7.99 now" (amount live) as the Bobbin, GOV.UK errors, the honest no-live-charge note. Text hover: none beyond focus states. Scene: the advancing stitch.

CONFIRMATION (/confirmation). Order number, what was bought, what was charged, renewal date and amount, support contact; "Your dashboard is ready for [email]" with the optional password and the emailed link; the verbatim SMS block as a separate optional step; "Open my dashboard" as the Bobbin; for Daily for Two, "Invite your second reader" with an email field usable now or later. Scene: the seal's last stitch tying off. Entrance: one weft pass.

TERMS (/terms) and PRIVACY (/privacy). The legal text in two to four columns with the twill margin, the [EIN Address] placeholder until supplied, no dashes; scene: static twill; text hover: underline only. The SMS section of the Terms verbatim from the kit.

404. "This thread isn't on the loom." with the loose thread curling (still 8 or the canvas), a search of the guides, and links to home, the Roundup and Membership.

### 3.24 VOICE STANCE, VOCABULARY AND THE FOUR GUIDE POSTS (for the content engine)

Voice stance: THE OBSESSIVE CRAFTSMAN, from site_content_engine.md's menu. Reasoning: the owner's own words are "a sharp friend who happens to be obsessed with saving money", and the craftsman is the stance that makes obsession a virtue rather than a tic. The craftsman checks twenty published rates before six because that is the job done properly, knows which weeks the clearance cycles turn, counts minutes, and shows the thread and the knot rather than hedging. It matches the governing idea (a weaver at a loom) and it makes density a feature: a craftsman's page is full of exact, useful things. It is used by none of the nine logged builds (their stances: clinical precise humanizing, sober quantitative recorder, sceptical analyst, warm host, night shift handover, patient teacher, plainspoken engineer, the quiet usher, the friend who already filed it), and it is not the kit's default (the quietly annoyed insider), which other pipelines are likeliest to have used. How it sounds: first person plural for the work ("we checked twenty accounts this morning"), second person for the reader's own money, exact figures, short verdict lines after a long one, no hedge stacks, no "you should" (Offering Spec 12: "worth comparing", "the arithmetic on $10,000"), and questions as headings, which the sisters never use. It never sounds like a hobbyist: the craft is money, not cloth, and the weaving words stay in the design, not the copy, except "thread" and "pass", which the site uses as its own vocabulary.

Ten words SaveBrew uses: brief, thread, pass, morning, weekday, tracked, membership, reader, deposit, illustrative. (Plus the product nouns the Offering Spec fixes: the Daily, the Daily for Two, the Roundup, the Guides, "Your moves".)

Ten words SaveBrew refuses, honouring the exclusion brief's list (3.7) and the Offering Spec's section 16: plan, never, every, sample, calendar, month, log, row, figure, page. Also refused on compliance grounds: guaranteed, hack, "you should", "we saved you", subscribe (customer facing), and free member. "Daily" stands as the product name. Where a refused word is unavoidable in legal text, it stays in the legal text only.

The four guide posts (public, /guides/slug, 700 to 1100 words each, one angle apiece, each with the hero prompt in 3.22):
1. /guides/make-a-rotating-category-pay. Headline: "How to make a rotating cashback category actually pay". Angle: the how-to that is actually good. Theme: activation is the easy part; the cap, the timing against the paycheck and the category's real spend are where most people lose the 5 percent, and the craftsman walks the four steps in order with the arithmetic on a $1,500 cap.
2. /guides/the-national-average-is-a-warning. Headline: "The national average savings rate is not a benchmark, it is a warning". Angle: the myth the category believes that is wrong. Theme: 0.37 percent (FDIC, September 2026, dated and attributed) is not the middle of the market, it is the floor most money sits on, and comparing to it flatters a bad account; the honest comparison is to the tracked top, about eleven times higher.
3. /guides/four-percent-against-the-account-you-have. Headline: "A 4.00% account against the one you already have: the arithmetic on $10,000". Angle: the honest comparison the reader is quietly making, with the trade offs named. Theme: the yearly difference in dollars, what a minimum balance and a promotional condition do to it, the time it takes to move, and when it is not worth moving; illustrative figures, dated, no institution named.
4. /guides/why-patio-furniture-is-cheap-in-october. Headline: "Why patio furniture is cheap in October: the seasonal buying cycle, plainly". Angle: the plain language explainer that finally makes a confusing topic clear. Theme: clearance runs on the retailer's floor space, not the shopper's needs; the craftsman lays the year out as the twelve turns of the cycle (denim and outdoor goods in October, big electronics in late November) and says what to wait on.

No two can be swapped without anyone noticing: a procedure, a debunking, a comparison, an explainer.

### 3.25 ALIGNMENT WITH THE FINAL OFFERING SPEC (checklist for the design document and QA)

- Products and prices: SaveBrew Daily $7.99 billed monthly (SB101) and $72 billed yearly (SB102); SaveBrew Daily for Two $11.98 billed monthly (SB201) and $108 billed yearly (SB202); the name "Daily for Two" stays; both prices always printed on each card; the renewal sentence at the same weight as the price; the tax and fees line; the refund line; no badge, no giant numeral, no $0 card, no stepper, no TOTAL line, no rolling numerals.
- Free content: the Weekly Roundup, the Guides and "Your moves" are public pages with no account, no form and no email capture anywhere on the site, including the footer; readers, not free members; RSS and stable URLs on the Roundup and Guides.
- CTA labels, exactly as Offering Spec section 8: home hero "Add the Daily to my cart" with the secondary link "Open this week's free roundup"; membership cards "Add the Daily to my cart", "Add a year of the Daily to my cart", "Add the Daily for Two to my cart", "Add a year of the Daily for Two to my cart", the label changing with the cadence control; product tour "Look inside the dashboard"; end of the ranker "Add the Daily to my cart" with "Members get a ranked list like this each weekday morning, built on that morning's brief."; cart "Go to checkout"; checkout submit "Pay $7.99 now" with the amount live (fallback "Complete my purchase" is not used; the numeral is the full cost statement); confirmation "Open my dashboard"; the desktop nav carries the compact "Add the Daily to my cart" Bobbin and the spool cart control with count; phone widths carry the cart control and a Membership link. The price never sits inside or directly under a marketing button; it sits in the hero standfirst and the card price line.
- Buy flow: /membership → cart drawer → /checkout → /confirmation → /today, guest checkout with no account step, one membership at a time with quantity fixed at 1, the cadence switch in the cart, the empty and replace states designed, the unchecked age and terms box, no SMS consent in checkout, the verbatim SMS block on the confirmation page as a separate optional step, two click cancellation (Membership, then Cancel membership) with the Resume link, renewals as section 9.6.
- Product views: built to Offering Spec 10.1 to 10.5 (the app's own frame, no browser chrome, no device, the knot mark and wordmark left in the 56px bar, tabs inline, date pill, "Texts on" bell, avatar JM, "Published 6:30 AM ET", the corrected Texts card with three rows and the "Ending texts does not cancel your membership." footer, "Monthly deposit", "Adjust the deposit", the footer line "Illustrative figures shown. Live rates move without notice. SaveBrew is a digest, not a bank.", "Twenty accounts and CDs, checked each morning" with seven rows and "13 more").
- Compliance: the disclaimer from section 12 on every content page, visible without scrolling on /brief and above the fold on guides; no testimonials, no press, no ratings, no social icons at launch; the referral-fee line ships only on the owner's confirmation; King of Prussia address, (888) 338-8809 and support@savebrew.com in the footer and on Contact; [EIN Address] on Terms and Privacy until supplied; no dashes anywhere, including inside the product UI.
- Vocabulary: section 16 of the Offering Spec and 3.24 above govern the copy step.

---

## PART 4. NOVELTY CHECK: proposed.json AND THE SCRIPT RESULT

`/home/claude/savebrew/spec/proposed.json` was rewritten for The Weave (every field filled). Checked against `/home/claude/savebrew/research/registry_augmented.json` (registry.json plus the seven Build Log shadow entries, documented in `spec/registry_augmented_notes.md`).

Command run:

```
python3 /root/.claude/skills/synced/52b032fe-0ad2-4fa5-b3f5-e71298887bc0_42f9ac40-a74a-4fbd-93ba-15893646f11d/finalshot/scripts/check_novelty.py /home/claude/savebrew/research/registry_augmented.json /home/claude/savebrew/spec/proposed.json
```

Final output (no FAIL to fix; exit code 0; quota 17 is not printed because a Tier 1 build carries no signature shader, which the script treats as not applicable):

```

=== Novelty check vs 10 logged build(s) ===
  PASS  1a heading font last 8   ('big shoulders display' vs ['newsreader', 'fraunces', 'archivo', 'young serif', 'instrument serif', 'familjen grotesk', 'not yet chosen (placeholder)', 'recursive'])
  PASS  1b pairing never repeated   (('big shoulders display', 'manrope'))
  PASS  2 archetype last 5   ('warp columns (invented: five content columns from edge to edge, one per money thread, every section a row across them, heading passes between rows)' vs ['illustrated scroll world', 'split-screen diptych', 'sticky-stacked cards narrative', 'not yet chosen (placeholder: uncommitted at the offering step)', 'meander (invented, the brook spine)'])
  PASS  3 signature category vs previous   ('texture & detail' vs previous 'typography')
  PASS  4a signature object never repeated   ('the loom: five taut warp threads, one per money thread (rates, cashback, coupons, seasons, paychecks), spanning the full width and receding from the weaver's seat, with the day's weft passing and knotting once on each, and the woven weeks behind')
  PASS  4b camera path never repeated   ('cross-section sweep then gravity flip: the reed sweeps toward the camera through the woven weeks revealing one day's row of knots per pass, today's knots pull tight on a held beat, then the world's up turns as the camera pitches to top down and the cloth lays flat into the five-column board')
  PASS  5 technique freshness (>=2 fresh vs last 5)   (fresh: ['tex-008', 'tex-007', 'mot-018', 'exp-005', 'typ-003', 'typ-014', 'trn-002', 'cur-009', 'cur-010', 'exp-007', 'img-019'])
  PASS  6 under-used category present (EXP/STO/TEX)   (found: ['tex-008', 'tex-007', 'exp-005', 'exp-007'])
  PASS  7 loader vs previous   ('selvedge stitch: a dashed indigo running stitch draws down the left gutter edge in step with real load over the already painted page, ties off at ready, no count, no flip, skip at the bottom centre' vs previous 'receipt print head: a white receipt strip prints the real load stages as line items with dotted leaders, the total line carries the real percentage, the strip tears along a perforation at 100 and flips into the hero tape')
  PASS  8 field not 3 in a row   ('light' after ['not yet chosen (placeholder)', 'light'])
  PASS  9 accent hue family last 5   ('indigo (blue violet)' vs ['rose (dusty pink)', 'carmine (blue-leaning crimson)', 'ice white (cool light as a metallic)', 'not yet chosen (placeholder)', 'copper (rust)'])
  PASS  10 easings never repeated   (repeated: [])
  PASS  11 interactive feature last 3   ('ranker' vs ['quiz', 'pace simulator (placeholder)', 'sorter'])
  PASS  12 nav vs previous   ('the heading band: an opaque white weft band 84px that hides on scroll down and returns on scroll up, big shoulders wordmark with the knot mark top left, four destination links in manrope with the active link at weight 800 and no marker glyph, about, contact and sign in at right, a spool cart glyph with a stitched count and the compact stitched bobbin purchase button per the offering spec' vs previous 'the tape header: a full-width white receipt strip with a perforated bottom edge, recursive wordmark top left, horizontal links with a small copper tag standing under the active link, a folded receipt cart with count top right, thins to 56px')
  PASS  13 button vs previous   ('the bobbin: squat rectangle radius 4 with an inset dashed stitch border, indigo fill and butter label, the stitches run on hover, the fill deepens and the stitch tightens on press, one stitch travels the border every eleven seconds at idle, price never inside the button' vs previous 'the kept tag: tag-shaped button with a notched left end and a punched hole, copper fill, white recursive label with a tabular price, lifts 2px while the hole's string draws out on hover, flat on press, slow shadow breath')
  PASS  14 voice stance last 3   ('the obsessive craftsman' vs ['the quiet usher', 'trail guide (placeholder)', 'the friend who already filed it'])
  PASS  15 color story last 4   ('butter warp through a white weft, with indigo thread' vs ['green baize and silver with one carmine ring', 'oxblood leather with one cool light on', 'not yet chosen (placeholder)', 'brook celadon with white receipts and one copper tag'])
  PASS  16 tier not 3 in a row (unless tier_forced)   ('1' after ['', '1'], forced=False)

VERDICT: ALL QUOTAS CLEAR
```

Note for the orchestrator: quota 8 passes as light after (unknown, light). If Hill Wallet commits a light field before SaveBrew ships, re-run the check; the fallback that keeps this direction intact is an indigo ground with white weft blocks and butter thread (the same three colours inverted: indigo #1B1E5C as the ground, white rows, butter stitches and knots), which changes no archetype, world, type, motion or kit.

## Files

- /home/claude/savebrew/spec/art_direction_spec.md (this file)
- /home/claude/savebrew/spec/proposed.json (The Weave)
- /home/claude/savebrew/spec/direction_candidates.md (phase one: the three candidates; its Part 3 and Part 4 described Candidate A and are superseded by this file)
- /home/claude/savebrew/spec/registry_augmented_notes.md
- /home/claude/savebrew/research/registry_augmented.json
