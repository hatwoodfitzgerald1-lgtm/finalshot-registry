# The Sameness Review (added 2026-09-24, ninth amendment): every build is seen against every previous build

## Why this exists, in the user's words

> Make sure that the site is a completely different vibe from Addabill, Financing Bot, Save The Will, Smart Augment, Brainbrook, SaveBrew and Astroquanta (basically every previously made brand). Be creative and make sure the sites have a completely different feel. This is extremely important: the site cannot have a similar vibe, design structure, font choice, speech structure or anything. There should be absolutely no recognizable patterns between them at all.

The seventeen novelty quotas in `build_registry.md` compare named strings: a heading font, an archetype name, a color story. They stay in force, and they are not enough. Ten builds later the Build Log shows what they let through: a loader that Flips or hands off into the hero in six builds, a variable font axis settle as the typographic set piece in three, a small glyph under the active nav link in four, a button that lifts on hover, flattens on press and breathes at idle in five, a round seal with ring text in four, standing tags on a line in two, and "N objects that complete one by one on scroll" (five lights, five shops, five threads, five sheets) in four. Every one of those builds cleared every quota, because the quotas never looked at the mechanism, and nobody opened the old sites.

So this module adds three things that only accumulate: an archive of every build's design files, a review that LOOKS at every previous build before the direction is chosen, and a Pattern Ledger that bans mechanisms, not just names. It relaxes nothing. Every existing quota, window and floor remains exactly as written and is checked exactly as before; the rules here are checked in addition.

## The rule

Everything a visitor reads as the brand's personality is unique across all logged builds and all builds in flight: the vibe, the design structure, the type, the palette, the motion, the objects, the section rhythm, the way the copy speaks. Uniqueness is judged at the level of MECHANISM (how the thing is done), not the label it was given. Two builds that both put "a small glyph beneath the active nav link" share a pattern even if one glyph is a day cell and the other is a lit window.

### The carve out (what is required to be the same, and never counts as a pattern)

1. The conventions floor in `build_registry.md`: logo top left linking home, horizontal primary nav on desktop, cart top right, footer with the address block, links that look like links and buttons that look like buttons, product to cart to checkout to confirmation, forms that submit on Enter, a working back button, normal scrolling, the value proposition and primary action in the first viewport.
2. The compliance set: the verbatim "Join Our SMS List" block, the footer address and contact block, the Terms and Privacy text, the checkout form standard (`checkout_spec.md`, GOV.UK errors), one primary action per screen, guest checkout.
3. The mandates. Every build still ships a loader as overture, a typographic set piece, a brand graphic kit with a seal or medallion, one interactive feature with real inputs and a computed result and a purchase CTA, a named motion signature, a 3D or heavy motion signature moment, video, photography, and the blog. WHAT must exist is fixed by the kit. HOW it is built is what may never repeat. A mandated element built with a mechanism already on the ledger fails.

## The archive: `finalshot-registry/builds/<slug>/`

Written at Step 8 as part of the registry write, through the same logged in browser. The run is not complete until it is pushed. Contents:

| File | What it is | Source |
| --- | --- | --- |
| `vibe-card.html`, `vibe-card.jpg` | The one page card described below, rendered at 1600px wide | `scripts/make_vibe_card.py` |
| `vibe.json` | The card's data: screenshots, palette, type, copy samples, pattern tags, the eight line brief | written by the run |
| `shots/home-1440.jpg`, `shots/home-375.jpg`, `shots/plans-1440.jpg`, `shots/about-1440.jpg`, `shots/post-1440.jpg`, `shots/nav.jpg`, `shots/button.jpg` | First viewport captures (JPEG quality 80, 1440 wide; the phone capture at 375) | the QA screenshot set |
| `design_doc.md` | `<Brand>_Website_Design.md` in full | Step 5 |
| `site_copy.md` | the content engine's finished copy | Step 3 |
| `art_direction_spec.md`, `offering_spec.md` | the ui-ux-director and offering-architect specs | Steps 2 and 2.5 |
| `asset_plan.json` | `ASSET_PLAN.json` | Step 6.5 |
| `brand_kit/README.md` | the palette and logo notes | Step 6.5 |
| `copy_fingerprint.json` | the speech structure fingerprint | `scripts/copy_fingerprint.py` |

Budget: about 3 MB per build. Upload in one GitHub web upload batch (under 20 files and 3 MB per batch; split the shots if needed).

A logged build that has no archive folder (the builds shipped before this amendment) gets one at the next run's Step 0: the run captures its shots from the live URL, fingerprints its copy from the live page text, writes its `vibe.json` and pattern tags from the registry entry plus what it sees, and pushes the folder at Step 8. A missing card is never a reason to skip that build in the review.

## The vibe card (one page, 1600px wide)

Rows, top to bottom:

1. Header: brand, domain, ship date, tier, archetype (family and cast), heading and body fonts, palette swatches with hexes, accent hue family, color story, voice stance, signature move category and id.
2. Home first viewport at 1440 beside Home at 375, then Plans at 1440.
3. About at 1440, one blog post at 1440, the nav strip crop, the primary button crop (hover state when available).
4. Speech samples: the H1, three section headlines, every CTA label, the section names in page order, the blog titles, the opening line of About and of one post.
5. The pattern tags (design and copy) and the eight line brief.

`scripts/make_vibe_card.py vibe.json --out builds/<slug>/` writes the HTML and, when Playwright and Chromium are available (they are in the Cowork sandbox), the JPG.

## Step 0: look, then write the Sameness Brief

1. Read `registry.json` (all entries), `claims.json` (builds in flight), `patterns.json` (the ledger) and every `builds/*/vibe.json`. `raw.githubusercontent.com` is reachable from the sandbox, so the JSON and the JPGs can be fetched directly and the cards viewed with the Read tool; the browser is only needed for a live site that has no card yet.
2. Also query the Build Log's `runs` collection for runs whose `run_state` is active and treat their committed direction fields as claims (the claim file can lag a session that is mid step).
3. Open every build's `vibe-card.jpg` and LOOK at it. Then write the Sameness Brief: one block per logged build and per claim, eight lines each:
   - Vibe in one sentence (what a stranger would say the site feels like)
   - Hero composition (what fills the first viewport and how the type sits in it)
   - Type pairing and the set piece mechanism
   - Palette family, field and color story
   - Motion character (the easing feel, the loader mechanism, the signature move's grammar)
   - Speech: H1 grammar, headline grammar, CTA phrasing, section naming device, blog title format
   - Section rhythm (how the page is chunked: bands, chapters, ledger rows, spreads)
   - Pattern tags (from `vibe.json` and `patterns.json`)
4. Close the brief with the consolidated BANNED LIST: every pattern tag on the ledger, every font, every archetype family and cast, every accent family and color story, every voice stance, every H1 and headline grammar, every CTA phrasing, every section naming device, every blog title format, every opening line shape.
5. Hand the brief to ui-ux-director (Step 2.5), the content engine (Step 3), creative-asset-engine (Step 6.5) and direct-qa-loop (Step 7). Record in the Build Log that the review ran and how many builds it covered.

Budget: about 15 seconds and 10k tokens per prior build from the cards; live spot checks limited to the three builds the brief marks closest in category or palette; ten minutes hard cap. A run never skips the review to save time.

## The Pattern Ledger: `patterns.json` and the taxonomy

Every build declares its pattern tags at Step 2.5 (design) and Step 3 (copy). A tag is `<category>.<mechanism>` in lower case with hyphens. A new build may use NO tag that any logged build or claim carries, except tags in the carve out. When the mechanism is new, name it (`nav.two-sided-plates-turning-on-y`) and it joins the ledger at Step 8, banned for every build after it.

Categories and the mechanisms already on the ledger as of 2026-09-24 (from the ten builds in the Build Log; the live file in the registry is authoritative):

- `hero.*` how the first viewport is composed: `hero.rendered-world-under-centered-type` (Addabill), `hero.stack-of-sheets-in-depth` (Smart Augment), `hero.ledger-wall-in-a-visible-grid` (Financing Bot), `hero.split-diptych-print-on-void` (Logifx), `hero.pinned-frame-sequence-with-dealt-cards` (Cash Pass), `hero.continuous-line-across-the-page` (Brainbrook), `hero.house-on-lot-scene` (Save The Will), `hero.columns-edge-to-edge` (SaveBrew), `hero.sidebar-anchored-console` (Astroquanta), `hero.single-object-3d` (BioVirtua).
- `nav.*` the indicator and reveal mechanism, never the placement: `nav.glyph-beneath-active-link` (Addabill, Brainbrook, Save The Will), `nav.footnote-marks-rise-on-hover` (Smart Augment), `nav.ruled-cells-fill-on-hover` (Financing Bot), `nav.two-sided-plates-turning-on-y` (Logifx), `nav.active-at-full-white-rest-dimmed` (Cash Pass), `nav.active-weight-jump-no-mark` (SaveBrew), `nav.condense-on-scroll` (Addabill, Financing Bot, Smart Augment), `nav.hide-on-down-return-on-up` (SaveBrew), `nav.transparent-then-plated-on-scroll` (Logifx).
- `button.*` shape, hover, press and idle: `button.lift-on-hover-flatten-on-press` (Addabill, Brainbrook, Save The Will, Logifx), `button.idle-breathing` (Addabill, Save The Will, Smart Augment, SaveBrew), `button.sliding-duplicate-label` (Addabill), `button.tag-shape-notch-and-hole` (Addabill, Brainbrook), `button.hairline-steps-outward` (Smart Augment), `button.carriage-return-label-second-rule` (Financing Bot), `button.light-band-passes-on-hover` (Cash Pass), `button.tilt-toward-pointer` (Logifx), `button.stitched-border-running` (SaveBrew), `button.mono-price-cell-divided-by-hairline` (Financing Bot, Smart Augment).
- `loader.*` the mechanism and the handoff: `loader.flip-into-hero-element` (Addabill, Brainbrook, Save The Will), `loader.plate-splits-to-reveal` (Financing Bot), `loader.rules-draw-then-dissolve` (Smart Augment), `loader.develop-from-ghost-then-turn` (Logifx), `loader.chapter-index-becomes-sticky-nav` (Cash Pass), `loader.stitch-draws-down-gutter` (SaveBrew), `loader.date-or-count-in-step-with-load` (Addabill, Financing Bot, Brainbrook), `loader.lights-come-on-per-stage` (Save The Will).
- `type.*` the set piece mechanism: `type.variable-axis-settle-on-scroll` (Addabill, Brainbrook, SaveBrew), `type.figure-rolls-through-values` (Financing Bot), `type.superscripts-travel-on-leaders` (Smart Augment), `type.word-turns-on-y-to-reverse` (Logifx), `type.lines-rise-behind-masks-one-per-step` (Save The Will), `type.letter-by-letter-fade-from-black` (Cash Pass).
- `motion.*` idioms: `motion.light-sweep-as-time-of-day` (Addabill), `motion.n-objects-complete-one-by-one` (Save The Will, Cash Pass, SaveBrew, Smart Augment), `motion.camera-pull-back-micro-to-macro` (Addabill), `motion.rail-ride-then-lift-to-birdseye` (Brainbrook, Save The Will), `motion.crane-up-a-wall` (Financing Bot), `motion.focus-pull-through-depth` (Smart Augment), `motion.half-orbit-at-tabletop` (Cash Pass), `motion.turn-to-reverse-side-then-fly-through` (Logifx), `motion.sweep-then-gravity-flip` (SaveBrew), `motion.idle-object-lifts-and-resettles` (Addabill).
- `object.*` the world's grammar: `object.standing-tags-on-a-line` (Addabill, Brainbrook), `object.paper-on-a-counter` (Addabill), `object.stack-of-translucent-sheets` (Smart Augment), `object.wall-of-rows` (Financing Bot), `object.hanging-print` (Logifx), `object.cards-on-glass-under-one-light` (Cash Pass), `object.continuous-tape-or-thread` (Brainbrook, SaveBrew), `object.house-with-windows-lighting` (Save The Will), `object.phone-as-destination-of-the-story` (Addabill, Brainbrook).
- `motif.*` and `seal.*`: `motif.cell-with-tag` (Addabill), `motif.hairline-leader-with-terminal-tick` (Smart Augment), `motif.tally-strokes` (Financing Bot), `motif.ring-bisected-by-seam` (Logifx), `motif.lit-tile-with-reflection` (Cash Pass), `motif.tag-on-tape-line` (Brainbrook), `motif.lit-window-frame` (Save The Will), `motif.knot-over-warp` (SaveBrew), `seal.ring-with-circular-text` (Addabill, Brainbrook, Save The Will, Cash Pass), `seal.square-form-box` (Financing Bot).
- `section.*` rhythm devices: `section.full-bleed-bands-alternating-with-spreads` (Addabill), `section.chapters-with-index` (Cash Pass), `section.ledger-rows-with-row-index` (Financing Bot), `section.docked-on-alternating-banks` (Brainbrook), `section.rows-across-fixed-columns` (SaveBrew), `section.two-sided-panels` (Logifx), `section.folio-pages` (Smart Augment), `section.step-pages-with-progress-strip` (Save The Will).
- `color.*` the story structure: `color.neutral-field-one-accent` (Addabill, Smart Augment, Financing Bot, Save The Will, Cash Pass, Brainbrook, SaveBrew: the dominant structure across the whole registry, now banned in that form), `color.analogous-two-field-one-ring` (Logifx), `color.dark-field-one-warm-accent` (BioVirtua), `color.grey-ladder-one-survivor` (Astroquanta).
- `feature.*` the interaction idiom, not the mandated shape: `feature.inputs-to-live-preview` (Addabill), `feature.drag-sort-with-magnetic-snap` (Brainbrook), `feature.three-question-quiz` (Cash Pass), `feature.form-to-condition-list` (Financing Bot), `feature.flip-cards-fill-a-matrix` (Logifx), `feature.state-lookup` (Save The Will), `feature.toggle-rerank` (SaveBrew), `feature.calculator-with-ruler` (Smart Augment), `feature.simulator` (Astroquanta).
- `voice.*` the stance family: `voice.host` (Addabill), `voice.usher` (Cash Pass), `voice.friend-who-already-did-it` (Brainbrook), `voice.teacher` (Save The Will), `voice.craftsman` (SaveBrew), `voice.night-shift-engineer` (Financing Bot, Logifx), `voice.sceptical-analyst` (Smart Augment), `voice.quantitative-recorder` (Astroquanta).
- `copy.*` speech structure, produced by `scripts/copy_fingerprint.py`: `copy.h1.two-short-sentences` (Addabill, Financing Bot), `copy.h1.category-line-plus-verdict`, `copy.cta.purchase-the-plan` (Addabill, Save The Will, Brainbrook, Logifx), `copy.cta.buy-noun` (Cash Pass, Financing Bot), `copy.device.counting-as-story` (flagged by the user after Financing Bot), `copy.device.numbered-01-02-03` (flagged by the user), `copy.device.every-x-on-one-y` (Addabill), `copy.section.noun-phrase-names`, `copy.section.imperative-names`, `copy.blog.how-to-titles`, `copy.blog.myth-negation-titles` (Logifx), `copy.blog.the-evening-it-gets-done-narrative` (Save The Will, Addabill "in an evening"), `copy.open.scene-in-past-tense`, `copy.open.question`, `copy.open.claim`.

The taxonomy is open. A run that meets a mechanism the taxonomy has no name for names it, in the same shape, and the name goes to the ledger with the build.

## Speech structure: the copy fingerprint

`scripts/copy_fingerprint.py SITE_COPY.md --out copy_fingerprint.json` (or a folder of page text dumps for a live site) extracts: the H1 and its grammar shape; every headline and its shape; the CTA labels; the section names; the blog titles and their format classes; the opening line of About and of each post with its shape; the rhetorical devices found (counting as story, numbered list device, every X on one Y, not X but Y, rule of three, second person conditional, one word sentences); sentence length statistics and contraction rate. `sameness_check.py` fails the copy when its H1 grammar, any headline grammar set, a CTA phrasing, a section naming device, a blog title format, an opening line shape or a device matches any logged build's fingerprint, or when any headline, CTA label or section name is a near duplicate (token overlap 0.6 or higher) of a logged one. The content engine receives the banned list BEFORE writing and is re run on a FAIL.

## Claims: builds in flight see each other

At Step 2.5, the moment `check_novelty.py` and `sameness_check.py` both clear, append the committed direction to `finalshot-registry/claims.json` through the browser: `{ "slug", "brand", "domain", "date", "status": "claimed", "session", every fingerprint field of the registry schema, "patterns": [...] }`. Step 0 of every other run reads claims as logged builds. At Step 8, when the final entry is written, the claim's status becomes `shipped` (the entry is the record; the claim stays for history). A claim older than 14 days with no shipped entry is stale and is reported to the user rather than silently dropped.

## Step 2.5 and Step 3: declare, then check

- ui-ux-director's spec MUST carry a `patterns` list (design tags per category above) and, per named element, the sentence "mechanism: ..., not on the ledger". Run `scripts/sameness_check.py registry.json proposed.json --claims claims.json --patterns patterns.json --builds builds/` after `check_novelty.py`; both must clear before the direction is committed and the claim written.
- The content engine receives the BANNED LIST and the prior fingerprints. After it returns, run `scripts/copy_fingerprint.py` on its copy and `sameness_check.py --copy copy_fingerprint.json`; a FAIL sends the copy back with the exact collisions.

## Step 7: QA Gate 5 becomes a side by side

The QA subagent builds the new build's vibe card FIRST (same script, from its own QA screenshots), then opens it beside every previous card and every claim's card when one exists, and writes one verdict per previous build: `distinct` or the named recognizable pattern(s), in the eight line brief's vocabulary. Any named pattern is a blocking fail that goes back to the build before the human gate, and the fix is re verified the same way. Then `sameness_check.py` is re run against the live build's fields and fingerprint. The verdicts are recorded in the QA report and the Build Log.

## Step 8: archive and ledger

Push `builds/<slug>/` (above), append the build's tags to `patterns.json`, mark the claim shipped, and write the registry entry with the new fields: `patterns`, `hero_composition`, `seal_form`, `feature_shape`, `copy_fingerprint` (path). `technique_additions.md` and `archetype_additions.md` continue exactly as before.

## Fallbacks (never a skip)

- The installed kit lacks `sameness_review.md` or a script: fetch it from `https://raw.githubusercontent.com/hatwoodfitzgerald1-lgtm/finalshot-registry/main/tools/` (the registry repo carries `tools/sameness_review.md`, `tools/sameness_check.py`, `tools/copy_fingerprint.py`, `tools/make_vibe_card.py`) and run it from the scratchpad.
- The browser is unavailable at Step 0: fetch the JSON and JPGs from raw.githubusercontent.com; if that is also unavailable, ask the user for the last builds' cards and say so in the Build Log. The review still runs on whatever is reachable and the gap is reported.
- Playwright is unavailable: write `vibe-card.html` and capture the JPG in the browser instead.
