# Addabill Website Design Document

Finalshot run addabill 20260923 k7m2q. Brand: Addabill (addabill.com). Entity: Addabill Inc. Date: 2026-09-23. Brand type: net new. Build tier: 2 (Authored-Media Editorial). This document is the single source of truth for the build.

## 1. How to build this site

Build the site directly from this document, page by page, exactly as specified. There is no live predecessor to pull cues from: addabill.com has been a parked domain since 2022, so the logo, imagery and identity all come from Section 5 (the Art Direction and Technique Stack spec) and from the brand kit that creative-asset-engine produces before the build. Use the copy in Section 7 word for word, never rewritten or shortened. Compose every media slot around the real file named in ASSET_PLAN.json. Build as an Astro app with a server rendered catch-all for Webflow Cloud, every route below at its own path, and run the direct-qa-loop until every gate passes.

## 2. Brand Snapshot and History Alignment

Addabill is new. The domain was registered in August 2022 and sat parked at GoDaddy until Textla bought it on 21 September 2026; the Wayback Machine holds no capture of it, Ahrefs shows only automated SEO spam pointing at the bare root, and there is no prior company, app, press or social account under the name. There is nothing to revive and nothing to stay consistent with, which also means there is no press to feature and no legacy URL to preserve. The brand starts from the ticket's product brief.

The product is the Addabill app: a household bill organizer. You add every bill the house receives, by typing it or by photographing the paper, and Addabill reads the amount and the due date, sets every bill on one due date calendar, texts you before each is due, and gives you one tap to that biller's own payment page. It never touches the money: no payment processing, no held funds, no bank or card logins, no convenience fees. Revenue is a paid Household plan on top of a Free plan.

The audience is the household's bill keeper: the person juggling 8 to 15 billers across email, paper mail and apps, who has paid at least one late fee this year for a bill they forgot, has tried sticky notes and a spreadsheet, and is wary of autopay because of surprise overdrafts. They want one screen that says what is due and when, without connecting a bank to anything.

Current positioning in one line: every household bill and its due date on one calendar, a text before each one is due, and no fees on your bills.

## 3. Carrier Compliance Mandates (non negotiable, build to these)

- **Real purchasable consumer use case.** The Household plan is bought through a complete guest checkout at $5 a month or $40 a year. Every primary CTA is an explicit purchase action: "Purchase the Household plan", "Buy the annual plan". The Free plan is a subordinate path ("Use the Free plan") that completes through the same checkout at $0 with no card. Never lead capture, never "Sign up" or "Get started" as a primary CTA.
- **Verifiable identity, consistent everywhere.** Addabill Inc., 4201 Spring Valley Rd, Dallas, TX 75244, (888) 338-9070, support@addabill.com, exactly as in the Terms and Privacy Policy. The footer and the Contact page show the physical address (from the Asana Physical Address field). The Terms and Privacy pages carry the registered address; the Asana EIN Address field is empty, so they carry the same Dallas address the ticket's own legal docs use, flagged for Harlem to confirm once the EIN address exists.
- **Privacy Policy and Terms live** at /privacy-policy and /terms-of-service, linked in the footer, in the SMS opt-in block, and from the checkout, carrying the verbatim SMS section (carrier list, "[INSERT SHORT CODE]" twice) and the verbatim no-sharing clause (Section 8).
- **The verbatim "Join Our SMS List" block** on every page (footer, site wide) with both consent checkboxes unchecked by default, ending "Read our Terms and Privacy Policy" (Section 6). Decision 4A (Harlem, 2026-09-23): the site describes finalshot's standard promotional marketing SMS program; the copy's two "never a promotional text" claims were removed so the site never contradicts its own Terms.
- **Brand words and claims.** Never state or imply Addabill pays bills, processes payments, holds money or transmits funds; never describe it with bank, banking, payment processor, money transmitter or advisor; never reference loans, credit, credit scores, bill deferral or debt relief; state plainly that Addabill charges no fees on bills. The copy in Section 7 already obeys this; the build must not add words.
- **No fabricated trust.** No testimonials, ratings, user counts, press logos, partner logos, security badges, founders or team bios anywhere. The brief forbids invented ones and a net new brand has none; finalshot's own no-fabrication rule agrees. Trust is carried by the "What Addabill never does" table, the visible no-fees line, the legal identity card, and the product shown working. "As Seen In" is omitted (no qualifying press exists). Standalone social links are omitted (no brand-owned pages exist yet); add them when they do.
- **No deceptive design.** No scarcity, urgency, confirmshaming, preselected add-ons or hidden costs; the annual and monthly buttons sit at equal weight with neither preselected; cancellation is stated in plain words on the Plans page, in the checkout summary and on the confirmation.
- **No template leftovers,** no lorem, no internal notes, no dead links, indexable (no noindex), desktop and mobile both on brand. The only intentional placeholders are "[INSERT SHORT CODE]" in the legal pages and the app URL on the confirmation page (see Section 7, Confirmation).
- **Guest checkout, full cost before commitment,** one column forms, GOV.UK error standard, correct autocomplete attributes, WebAIM six checked (Section 7, Checkout).

## 4. Product and Service Offering (the consumer use case)

The Offering Spec from offering-architect, embedded verbatim. All prices and limits were approved by Harlem at Gate 1 on 2026-09-23; the build uses them as written.

### Addabill Offering Spec

Finalshot Step 2. All numbers are proposed.

#### OFFERING TYPE
Consumer app subscription. Two plans, Free and Household. Household is bought through a complete guest checkout (contact, billing address, full card fields, no shipping), monthly or annual. Free is a subordinate path with no card. Account creation is offered only on the confirmation page.

#### EVOLUTION
Net new: parked domain since 2022, no prior site. The name is the product: add a bill, see it on one calendar with every other bill, get a text before it is due, tap through to the biller's own page.

#### LINE
Free | $0, no card, no time limit (proposed) | One person, 5 bills, text reminders | Use the Free plan

Household | $5 a month or $40 a year (proposed, $20 less than 12 monthly payments) | Unlimited bills, photo capture, 5 people, yearly summary | Purchase the Household plan (monthly), Buy the annual plan

Why:
* 5 free bills: the handful that cause late fees, so free proves the product; the brief's 8 to 15 billers cross 5 early, so buying is honest.
* $5 a month: a single purpose utility priced like one, under what budgeting apps charge.
* $40 a year: four months at no cost against $60 monthly, a 33 percent saving, about one late fee.

Second paid tier: no. Two plans is the calmer offer and the brief's own line; a multi home tier implies landlords, drifting toward business software and ADAPTABILL, and a third tier would force artificial gating. Five people covers roommate houses.

Companion single purchase: no. The yearly summary is already in Household and needs the household's own bills, so a standalone binder would charge twice or need an account before a guest could buy.

#### INCLUSIONS, complete per plan
Free
1. Up to 5 bills at one time
2. 1 member (you)
3. Add bills by typing
4. One calendar of due dates, month and list views
5. Text reminders before each due date, up to 3 per bill
6. One tap to each biller's own payment page
7. Mark each bill paid
8. No convenience fees, no card on file, no time limit

Household
1. Unlimited bills
2. Up to 5 people (you plus 4), each with their own login
3. Add bills by typing or photo (paper bill or screenshot), unlimited
4. One shared calendar, month and list views, showing who handles each bill
5. Text reminders before each due date, up to 3 per bill, to each person's own number
6. One tap to each biller's own payment page
7. Mark paid, 12 months of history, yearly summary of spending by bill as a PDF
8. No convenience fees, renews at the same price, cancel any time

#### DESCRIPTIONS
Free. Addabill Free is for one person keeping up to 5 bills straight. Type in each bill, see them all on one calendar, get a text before each is due, and tap once to open that biller's own payment page. No card, no fees on your bills. CTA: Use the Free plan.

Household. The Household plan is for the person who keeps the bills for everyone else. Add as many bills as the house gets, photograph the paper ones, and share the calendar with up to 4 other people so the reminder reaches whoever handles a bill. At year end you get a summary of what went to which biller, month by month. CTAs: Purchase the Household plan. Buy the annual plan.

#### DEFAULT PLAN FOR THE HERO
Household, monthly, the lower commitment. The primary button reads "Purchase the Household plan", with "$5 a month or $40 a year. No fees on your bills. Cancel any time." beneath it and a plain link "or use the Free plan, up to 5 bills" as the subordinate path. On the Plans page, monthly and annual are equal purchase buttons, neither preselected.

#### RENEWAL AND CANCELLATION, plain words
Household renews at the same price, $5 on the same date each month or $40 each year. A text and an email go out 7 days before an annual renewal, and a receipt follows every charge. Cancel any time under Plan in the app in two taps, or by emailing support@addabill.com. The plan runs to the end of the period paid for, then the household moves to Free and every bill stays. No cancellation fee. Annual plan: full refund within 14 days. Price changes carry 30 days notice.

#### natureOfServices
Addabill Inc. provides a consumer household bill organizing application that lets users record household bills and due dates, view them on one calendar, receive reminders before each due date, and open a link to each biller's own payment page; Addabill does not process payments, hold funds, connect to any financial account or charge fees on bills, and its paid Household plan is sold as a monthly or annual subscription cancellable at any time.

#### SMS TIE IN
Text reminders are the product's main output. In the app, the Addabill Bill Reminders notifications cover due date reminders, bill added and updated confirmations, login and verification codes, subscription billing and renewal notices and support replies. The website's Join Our SMS List block enrolls visitors in the separate Addabill alerts marketing program described in the Terms (decision 4A, 2026-09-23). At purchase, the required phone field ("for your receipt and your account texts") receives the receipt and renewal notice; the shared calendar texts each member at their own number under their own consent. Consent is a real unchecked checkbox, STOP and HELP work on every message, numbers never sold, rented or shared for marketing.

Samples:
1. Addabill: Water bill, $64.20, due Thu Oct 2. Tap to open your utility's payment page: [link]. Reply HELP for help, STOP to cancel.
2. Addabill: Household plan renews Oct 20, $40 for the year. Change or cancel under Plan in the app. Reply HELP for help, STOP to cancel.

#### VISUAL SPEC (the app UI is the one packaging system)
Form factors: the phone app on an iPhone (primary, portrait, screen legible) and the same app in a 16:10 browser window (secondary), both real HTML from the brand tokens, screenshotted.

One shell: a top header bar carrying the Addabill wordmark at left in every shot, the current month centered and one "Add a bill" button at right; a month grid with bill chips on their due dates and a "Due next" list below; a bottom tab bar (Calendar, Bills, Household, Plan) that becomes a left rail on desktop. Bill rows: biller name as typed, amount, due date, paid check, "Open payment page" arrow. No charts, scores, gauges, payment form look or invoice vocabulary (clear of ADAPTABILL).

Changes per plan: data only. Free shows "4 of 5 bills" and one member; Household shows "14 bills", 5 members' initials, the camera sheet and the yearly summary card.

Never changes: header bar, calendar geometry, tab bar, bill row anatomy, tokens, device frame.

Master image: one phone screenshot of the October Calendar view, 11 bill chips, one bill card expanded (Water bill, $64.20, due Thu Oct 2, reminders Sep 25, Sep 29, Oct 1). Every other shot is the same build in another view. Hero: the phone on a kitchen counter in morning light beside two paper bills. Plan cards: one card system, only values differ.

#### COMPLIANCE SCREEN
Purchasable at a visible price with explicit purchase CTAs, clear of every prohibited vertical.
* Lead capture, ambiguous CTAs: cleared, a priced plan bought through a full guest checkout, purchase labels only.
* Money movement, lending: cleared, no payments processed, funds held or accounts connected, no borrowing or relief topics.
* Hidden costs, hard to cancel: cleared, price, renewal, refund window and no fees on the Plans page at equal weight; two taps or one email to cancel.
* Fabricated trust, deceptive design: cleared, no testimonials, ratings, counts, press, partners, badges, scarcity, urgency, preselection or confirmshaming.
* SMS: cleared, account notifications only, unchecked consent, phone field explained, STOP and HELP.
* Identity, adjacency: cleared, the brief's legal name, address, phone and email on the Plans page, receipt and Terms; never invoicing.

#### FOR THE OWNER TO CONFIRM
1. Free limit: 5 bills.
2. Household: $5 a month, $40 a year ($20 less).
3. Household size: 5 people.
4. Reminders: up to 3 per bill.
5. 14 day annual refund window, 7 day renewal notice, 30 days notice of price changes.
6. Two plans only, no companion product.
7. Hero default: Household monthly.

### Product UI Brief (competitor research, precedes any product imagery)

Method note: the user's Chrome was disconnected during this step and the sandbox cannot reach the competitor domains, so this brief was written from text level research (WebFetch of prismmoney.com which now redirects to wearetrieve.com, chronicleapp.com, monarch.com, rocketmoney.com, cushion.ai, and App Store listings) plus prior knowledge of these products, and it is marked for VISUAL re verification the moment Chrome is back, before the product shots are built. Trade dress rule: take the mechanics, never the composition. A UI that reads as any one of these fails.

What the category's product previews actually show:

| Product | Dominant layout | On screen | Density | Chrome | Default |
| --- | --- | --- | --- | --- | --- |
| Prism (now Trieve) | A vertical list of bills grouped by due date, each row a biller logo, name, amount and "Due in N days", with a month calendar tab | 6 to 9 bills per screen, amounts right aligned, paid ones dimmed | Bottom tab bar (Bills, Calendar, Accounts), a top bar with the month | Light | 
| Chronicle (Mac and iOS) | A sidebar of categories plus a list of bills with "Paid" and "Due" pills, and a compact month calendar with due dots | 8 to 12 rows on desktop, 5 to 7 on phone; logos per biller | Left sidebar on Mac, bottom tabs on iOS, a big "Pay" affordance per row | Light, with a dark mode |
| Rocket Money (Recurring) | A month calendar with amounts on the days, and beneath it a list "Upcoming" with merchant logos and amounts | 5 to 7 upcoming items visible; calendar cells show a small total | Bottom tabs, a top segmented control (Calendar, List) | Light |
| Monarch (Recurring) | A calendar grid of the month with merchant marks on their days, a right column listing what is due this week | 30 day grid plus a 4 to 6 item list | Desktop left nav, phone bottom tabs, filters in the top bar | Light, dark available |
| Mint Bills (legacy, Wayback) | A vertical timeline of bills by due date with "Pay" buttons and account balances beside them | 6 to 8 items | Top bar with the month, bottom tabs | Light |

Mechanics to take: a real month grid with marks on due days (the category's shared mental model), a "due next" list under the calendar, right aligned tabular amounts, a paid state shown as a dimmed row plus a check, biller names as the user typed them, a due date written with its weekday, a single clear per bill action, a bottom tab bar on phone that becomes a left rail on desktop, and calm information density (6 to 11 bills per screen, never a wall).

Mechanics to refuse (the brief and ADAPTABILL): no account balances beside bills, no "Pay" buttons that imply Addabill moves money (ours reads "Open payment page"), no bank connection prompts, no charts, gauges, scores or totals across the top, no biller logos scraped from third parties (a small initial medallion instead), no invoice vocabulary.

Composition rule for the Addabill screens (the locked visual spec from Section 4): one shell, Figtree UI, cream field with paper white cells, a top header bar carrying the Addabill wordmark at left, the month centered, and one "Add a bill" paper tag button at right; the 7 by 5 month grid with bill tags standing on their due dates; a "Due next" list beneath; a bottom tab bar (Calendar, Bills, Household, Plan) that becomes a left rail at 16:10. Only the data changes between shots.

## 5. Design System (the ui-ux-director Art Direction and Technique Stack spec, verbatim)

Everything in this section is committed and was approved by Harlem at Gate 1 (Tier 2 confirmed): the governing idea, archetype, the signature move and its 3D world, the technique stack with build notes, palette and type, the motion signature, the typographic set piece, the loader, nav and button treatments, the interactive feature, the brand graphic kit, the designed mobile hero, the per page robustness plan, the Media Direction block, the tier (2) with its fit justification, engine profile baseline r128, no signature shader, and the media grade recipe. Novelty: all 17 quotas clear by machine check.

### Addabill: Art Direction and Technique Stack

Finalshot Step 2.5, ui-ux-director. Brand: Addabill (addabill.com), Addabill Inc., a household bill organizing app sold as a Free plan and a Household plan ($5 a month or $40 a year). Registry brief: three logged builds (BioVirtua, Astroquanta, Smart Augment). Every quota below was machine-checked with check_novelty.py: ALL QUOTAS CLEAR.

#### STEP 0: LIVE BENCHMARK (read 2026-09-23, calibration only, never imitation)

- Aardvark Book Club (FUTURE THREE, Awwwards SOTD Aug 30 2026, E-commerce Honors): one physical metaphor, unboxing, carried through a real store; a scroll-driven 3D book reveal is the hero and the checkout still works.
- Noho (Evgeny Morev, SOTD Sep 18 2026): two warm neutrals (F1EEE9, E7E2DA), a preloader intro, WebGL product exploration, an idle screensaver: calm restraint plus one considered idle behavior.
- Warm and Fuzzy (Neutral Studio, SOTD Sep 12 2026): a two-ink palette held with total conviction, idle animations everywhere, page transitions: nothing is ever frozen.
- The First Calendar (older nominee, about 6.1): a flat, colorful, app-style single page with no idea. The cautionary case.
- Today's bar for this build: one domestic metaphor built for real in 3D and carried into the store, two or three inks held without wobble, idle life on every surface, and a first viewport a stranger reads in five seconds.

#### CONCEPTING (the reasoning, kept short)

Truth: every household bill and due date on one calendar, a text before each is due, and it never touches the money. Tension: a money app that refuses to touch money, software about paper, calm about the one thing that makes people panic. Physical world: a kitchen counter at 7:40 on a weekday, the wall calendar with a pencil on a string, the mail on the counter, side window light. Enemy: the forgotten envelope, and the budgeting app that shouts in red charts and asks for a bank login. One feeling: "I know what's due. I can relax."

Three territories: (A) The Month on the Wall: one month you can walk into, bills standing on their days. (B) The Mail Pile, Sorted: envelopes and screenshots flowing onto one line of time (cut: a swarm-like assembly sits too near BioVirtua's motion, paper in depth too near Smart Augment's world). (C) The Heads-Up: a month of texts, the camera riding a ribbon of days (cut: a rail ride is too near Astroquanta's dolly and it reads like a messaging app). A wins: calendar-minded by the brief's own words, domestic, plain about money (tags carry a name and a date, never a total or a chart), ownable, and expressible on every route as a different view of the month.

GOVERNING IDEA: One month on the kitchen wall: every bill stands on its day, the light moves across the counter, and the heads-up arrives before the day does.

EXPERIENCE ARC: Opening beat, a desk flip calendar flips from the 1st to today in step with real load, then the day card lands on the month as today. Build, the camera pulls back from one day cell to the whole standing month while bills slide in from the mail at the left and the phone at the right and land on their dates. Peak, THE HEADS-UP: the morning light reaches Thursday the 2nd, the water bill tag stands, and a marigold heads-up chip lifts off Tuesday the 29th and travels into the phone at the frame edge, which shows the real reminder text; the H1 numeral settles at the same beat. Resolution, the camera settles to an elevated reading angle and the month becomes the quiet ground under the purchase button. Motion is loud at the pull-back and the Heads-Up, breathing everywhere else, and nearly still on Plans and Checkout.

ART DIRECTION CONCEPT: A kitchen counter in morning light, a wall calendar, paper tags, a phone that buzzes once. Adjectives: calm, domestic, warm, plain, dependable.

LAYOUT ARCHETYPE: Full-Bleed Cinematic Hero, cast as the standing month: the rendered world fills the viewport edge to edge under centered type, then the page varies its section furniture from the pattern library. It differs from BioVirtua (one orbited object), Astroquanta (a persistent left rail) and Smart Augment (a printed masthead and memo), and it is not the default left-text, right-product hero. Conventions floor held: logo top left to home, horizontal nav on desktop, cart top right, footer with address, phone, support email, Privacy and Terms, buttons that look like buttons, product to cart to checkout to confirmation.

TIER: Tier 2, Authored-Media Editorial. Fit justification: the brand's essence is a domestic moment, a kitchen counter in morning light, that deserves to be seen, so the graded video and photography the run ships anyway become the design's spine around a procedural month; no logged build has used Tier 2 (last three were 3, 1, 3), and it needs no shader harness or post chain, so it ships faster than the last Tier 3 with nothing weakened. Tier 2 bar: one grade (below) plus three editorial set pieces (the graded hero-loop band under display type on Home, About's alternating spreads with the pull-quote interlude, each blog post's graded hero under a drop-cap spread). Engine profile: baseline r128 (Three.js r128 from cdnjs). No signature shader.

#### COMPREHENSION BLOCK

- VALUE PROPOSITION: Every household bill and its due date on one calendar, with a text before each one is due, and no fees on your bills.
- AUDIENCE: The person who keeps the bills for the house, named on the page as "the household's bill keeper," juggling 8 to 15 billers across email, paper and apps.
- PRIMARY ACTION: "Purchase the Household plan," a marigold paper-tag button centered beneath the subhead, the only dominant call to action in the view. Beneath it, small: "$5 a month or $40 a year. No fees on your bills. Cancel any time." and a text link at clearly lower weight, "or use the Free plan, up to 5 bills."
- FIRST-VIEWPORT PLACEMENT: Desktop 1440 by 900: header row 72px; H1 centered from 18 to 34 percent height; subhead 36 to 42 percent; the button 46 to 52 percent; the standing month fills 55 to 100 percent receding in perspective, the phone at the right edge. At 375 by 667: header 56px; H1 80 to 210px; subhead 226 to 280px; button 300 to 352px; price line to 380px; Free link to 404px; the mobile week strip from 430px to the fold. All three answers sit above the fold on both.
- MOTION CLEARANCE: The header, H1, subhead, button and price line are plain DOM painted at first paint; the loader occupies only the lower 45 percent of the viewport (the panel where the month renders), never covering the copy. With preloaded WOFF2 subsets and font-display swap, all three are readable at about 0.9 s on broadband with the loader active; the 3D scene lazy-inits after the copy paints and the loader resolves on real load (target under 2 s, cap 4 s with a visible Skip). Reduced motion and 375px keep the same 0.9 s.
- HEADING STACK (direction for the content engine, meaning fixed, words final in the warm-host voice): "Every bill on one calendar. A text before each is due." / "Add a bill in the time it takes to open the envelope" / "How Addabill works: Add, See, Heads-up, Tap" / "What Addabill never does" / "Two plans, no fees on your bills" / "The texts you'd get this month" / "Keeping the house on time" / "Join Our SMS List" (verbatim block). Read alone: what it is, how fast, how it works, what it refuses, what it costs, what you get, more to read, how to sign up.
- SCENT MAP: Home, the home page. How it works, the four steps with the app shown. Plans, the store: Free and Household with prices and purchase buttons. Build your month, the builder where you add your own bills and see them on a month. Blog, the articles about keeping household bills on time. About, who Addabill Inc. is and what it never does. Contact, the Dallas address, phone, support email and a form. Cart, top right, the chosen plan. No label is a category abstraction.

#### SIGNATURE MOVE

STO-009 Timeline Storytelling, cast in 3D as THE STANDING MONTH. A visible timeline (the 7 by 5 month) with dated nodes (the day cells), a moving marker (the morning light and its shadows walking across the days) and content revealing per milestone (bills landing, the heads-up firing). Category: Storytelling and Structure, different from the previous build's 3D and WebGL. Why it fits: a due-date organizer's entire product is chronology on one surface, so the site's spine is the month itself, and the wow moment is the product's real output, a text arriving before the day. Library: Three.js r128 for the world, GSAP ScrollTrigger for the scrub, GSAP Flip for the loader handoff. Benchmark: https://www.maglr.com/blog/best-scrollytelling-examples (verified live) and https://aardvarkbookclub.com for a scroll-driven 3D hero inside a working store.

SIGNATURE 3D EXPERIENCE (signature_3d_moment.md): Object: a wall calendar page laid on a kitchen counter, 7 by 5 paper day cells with graphite rules, paper bill tags standing on their due dates (each a thin white slab with a 2px ink stripe along the top edge and a soft contact shadow), and a phone standing at the right edge of the frame. Verb: add and come due. Camera path, two primitives joined at a beat plus an environment arc: (1) micro to macro pull-back, from one day cell (Thursday the 2nd, the water bill) up and back until the whole month stands in view; (2) a time-lapse light sweep, the DirectionalLight travelling from low east to high south so shadows swing and shorten while the "today" cell brightens day by day, bills sliding in from the left (paper) and right (screenshots) to land on their dates until eleven stand, matching the product master; the beat: as the light reaches the 2nd, the heads-up chip lifts from the 29th and flies into the phone (the peak, held with a scroll snap); then the camera settles to an elevated reading angle. Environment arc: cool early light (a slight blue in the shadows) warming to golden mid-morning across the scroll. Scrub: pinned for 1.5 viewport heights (MOT-005), scrub smoothing 0.8, lerp on the light angle. Alive on load: the light drifts slowly, tag shadows creep, the phone screen glows faintly, and one tag lifts and resettles every eight seconds. Contrast: white paper tags with ink stripes and warm graphite shadows on an oat counter behind a paper-white month; fog off; a rim of window light on every tag edge. Lighting: 3DW-020, a downsampled interior HDRI from Poly Haven as scene.environment for the paper's soft ambient plus one shadow-casting DirectionalLight (PCFSoft, 1024 map desktop, 512 touch). Geometry is procedural (InstancedMesh for cells and tags), no asset pipeline. Lazy init after first paint, pixel ratio capped at 1.5 desktop and 1 on touch, render paused offscreen and on hidden tabs, torn down on navigation. Reduced motion: a poster frame of the settled state under the same DOM. Mobile: no WebGL in the hero; see the designed mobile hero below. Differs from every logged world: not a point-cloud body, not a lattice of trial cells, not a stack of paper sheets; not swarm-assembly, not a dolly through gates, not orthographic to raking with a focus pull.

#### TECHNIQUE STACK (12)

- Signature: STO-009 | Timeline Storytelling | Storytelling & Structure | the month is the timeline, the light is the marker | Three.js r128 + GSAP ScrollTrigger | Medium
- 3D support: 3DW-020 | PBR + HDRI environment lighting | 3D & WebGL | paper reads as paper in real morning light | Three.js RGBELoader, PMREMGenerator, MeshStandardMaterial | Medium
- Scroll system: MOT-005 | Sticky Section Pinning | Motion & Scroll | the one held stage for the signature (and the builder's month tilt) | GSAP ScrollTrigger pin and scrub | Medium
- Scroll reveal: MOT-018 | Clip-Path Scroll Reveal | Motion & Scroll | sections open like a day cell, an aperture not a fade | GSAP + CSS clip-path | Medium
- Typography: TYP-003 | Variable font axis interpolation | Typography | the set piece: Fraunces WONK and SOFT settle | CSS @property, GSAP | Medium
- Type scale: TYP-004 | Fluid type with clamp() | Typography | one calm reading rhythm from phone to ultrawide | CSS clamp | Low
- Color: COL-017 | Earthy / organic palette | Color & Visual Style | warm neutrals, cream and graphite, one highlighter | CSS custom properties | Low
- Texture: TEX-013 | Tactile soft shadows | Texture & Detail | everything sits on the counter under window light | layered box-shadow tokens | Low
- Loader: TRN-001 | Preloader Percentage Counter, cast as the flip calendar | Page Transitions & Loaders | real load shown as the day of the month | GSAP timeline + Three.js LoadingManager + Flip | Medium
- Transition: EXP-002 | Cross-Document View Transitions | Emerging & Experimental | the month motif persists between pages of an MPA | View Transitions API | Medium
- Microinteraction: CUR-007 | Button Hover Choreography | Cursor & Microinteractions | the paper-tag button lifts, the label slides | CSS pseudo-elements | Low
- Feedback: CUR-011 | Success / Loading Micro-Feedback | Cursor & Microinteractions | "Added" and "Marked paid" stamps, the order check draws | SVG stroke, aria-live | Medium

Fresh against all logged builds: STO-009, 3DW-020, MOT-018, TYP-004, COL-017, TEX-013, CUR-011 (seven, quota needs two). Under-used categories present: STO, TEX, EXP.

#### BUILD NOTES (mechanics from the database, restated without dashes)

- STO-009: a spine with dated nodes (the month grid, an ordered list in the DOM with real dates for screen readers); reveal each node on enter with IntersectionObserver; drive the progress marker (light angle, today index) from ScrollTrigger progress; reduced motion shows the static list and poster.
- 3DW-020: load the .hdr with RGBELoader, process with PMREMGenerator, assign scene.environment, MeshStandardMaterial on cells and tags (roughness 0.9, metalness 0); downsample the HDRI to 512px (about 300KB), cache it, share it across every page's scene.
- MOT-005: ScrollTrigger.create({ trigger, start: 'top top', end: '+=150%', pin: true, scrub: 0.8, snap at the Heads-Up beat }); set pinSpacing so the next section never overlaps; recalc with matchMedia on resize; shorten on touch; content stays reachable by keyboard.
- MOT-018: animate clip-path inset(0 100% 0 0) to inset(0 0 0 0), or a day-cell rectangle growing from center, with ScrollTrigger scrub or the CSS view() timeline; pair with a 1.03 image scale; reduced motion shows content unclipped; nothing revealed is hidden from assistive tech.
- TYP-003: declare font-variation-settings 'wght' 600, 'SOFT' 100, 'WONK' 1, 'opsz' 144 on the set-piece numerals, register the axes with CSS @property so GSAP can tween them; subset Fraunces; body copy never animates axes.
- TYP-004: font-size: clamp(min, rem + vw, max) across a modular scale built with the Utopia calculator; always keep a rem term so zoom works (WCAG 1.4.4); the same technique drives spacing.
- COL-017: muted warm tokens as custom properties, cream field, contemporary serif headings, body text on the darkest token; AA verified below.
- TEX-013: shadow-1 0 1px 2px rgba(43,38,34,0.06), 0 6px 18px rgba(43,38,34,0.08); shadow-2 (lifted) 0 2px 4px rgba(43,38,34,0.06), 0 14px 32px rgba(43,38,34,0.12); tinted toward graphite, reused as tokens, never the sole carrier of state.
- TRN-001: track real progress with Three.js LoadingManager plus a font and image count; map progress p to displayed day round(1 + p times (today minus 1)); on complete, Flip the day card into the hero's today cell; skippable; no invented delay.
- EXP-002: @view-transition { navigation: auto } in CSS; view-transition-name on the header wordmark and the small month glyph; disabled under prefers-reduced-motion; unsupported browsers navigate normally.
- CUR-007: pseudo-element shadow growth and a duplicated label translated on :hover and :focus-visible, 150 to 300 ms, transform and opacity only, contrast held through the transition.
- CUR-011: on submit disable and show an inline paper-tag spinner, then draw the check with stroke-dashoffset; announce with aria-live; static check under reduced motion.

#### PALETTE AND TYPE

Roles and hex: field, counter cream FAF3E6; surface, paper white FFFFFF (day cells, cards); surface tint, oat EDE2CF (the counter, section bands); text, graphite 2B2622; secondary text, shadow 6B6058; accent, marigold E9A825 (the purchase button, heads-up chips, the today tick, never as text on cream); secondary accent, moss 3F6B4B (the paid check and "on time" labels only). Contrast: graphite on cream 13.6:1, graphite on marigold 7.2:1, shadow on cream 5.5:1, moss on cream 5.6:1, all AA. Marigold on cream is used only for non-text marks (1.9:1). Color story: cream and graphite with one marigold highlighter. Background field: light.

Type: Fraunces (variable: wght, opsz, SOFT, WONK) for headings and every oversized numeral, set soft (SOFT 100) with the WONK axis reserved for the set piece; Figtree for body, UI labels and the product screens, weights 400 to 700; tabular figures for calendar grids and prices. Scale by clamp: body 1rem to 1.125rem, H1 clamp(2.25rem, 1.2rem + 4.2vw, 5.5rem). Rotation checked: Fraunces not in the last eight heading faces; the Fraunces plus Figtree pairing never used.

#### MOTION SIGNATURE

Two curves, unique to this brand: "Heads-up" cubic-bezier(0.24, 0.8, 0.26, 1) for arrivals, landings and reveals (a card laid on a counter, no overshoot); "Page turn" cubic-bezier(0.42, 0, 0.14, 1) for exits, flips and the mobile drawer. Durations: fast 0.2s, base 0.48s, slow 1.4s. Every motion item, the loader, the kit draw-ins and the 3D light lerp use these.

#### TYPOGRAPHIC SET PIECE

The Settled Numeral. In the hero, the oversized due date "2" (Thursday the 2nd, the water bill) stands as DOM Fraunces display type beside its tag over the canvas, starting at WONK 1 and SOFT 100, a date circled by hand on the wall, and settles to WONK 0 with opsz sharpening as the pull-back completes and the tag lands: written on the wall, printed in the app. Every oversized numeral site-wide (the 01 to 04 steps, plan prices, blog indices, the three reminder days) repeats the settle on scroll-in.

#### LOADER AS OVERTURE (preloader_module.md)

Pattern: a rolling counter recast as the desk flip calendar. Three paper cards in Fraunces on the cream panel in the lower 45 percent of the viewport: the month, the day, the weekday. The day card flips (Page turn curve, 0.2s per flip) from the 1st to today's real date in step with real load, landing on today at 100 percent; the month card shows the current month, the weekday card the real weekday. At completion the day card Flips (GSAP Flip) into the hero month as the today marker, the marigold tick. Real load only, target under 2 s, hard cap 4 s with a visible "Skip" text button from the first frame. Header, H1, subhead and CTA sit above the panel as plain DOM from first paint. Reduced motion: the cards show today instantly and the panel fades once, 0.2s. Distinct from the logged boot sequence, grid fill gauge and ruled draw-on.

#### NAV TREATMENT

The calendar header: one cream row, the Fraunces wordmark top left linking home, horizontal Figtree links (Home, How it works, Plans, Build your month, Blog, About, Contact), a hollow day-cell square that slides under the active link and follows hover and focus (Heads-up curve), the cart top right drawn as a paper tag with a count and a marigold today tick beside it. On scroll it condenses to 56px and gains shadow-1. Mobile: a labeled Menu button opens a drawer that turns in like a page (Page turn curve) headed by a 7-day strip. Treatment differs from the previous printed masthead; placement and affordances unchanged.

#### BUTTON TREATMENT

The paper tag: a marigold rounded rectangle (6px radius) with a folded top-right corner drawn by a pseudo-element, graphite label in Figtree 600. Idle: shadow-1 breathing to shadow-2 and back every six seconds. Hover and focus-visible: lifts 2px onto shadow-2 while the label slides up and its duplicate slides in (CUR-007) and a tiny due dot rolls left to right. Press: flattens (shadow collapses, translateY 1px). Secondary: the same tag in paper white with a graphite hairline. Text links: a hairline underline that grows from the left and ends in a marigold dot. Unmistakably a button; differs from the previous stamped rectangle in shape, fill, motion and label type.

#### INTERACTIVE FEATURE: BUILDER, "Build your month" at /builder

Format: builder (quota clear: comparison, simulator, calculator were the last three). The visitor adds three to five of their own bills, each landing on a live month, and the result recommends a plan with the purchase CTA. Inputs per bill: biller name (text, required), amount (optional), due day of the month (1 to 31, required), reminder lead (chips: 1, 3 or 7 days before, default 3), "arrives on paper" (checkbox), "someone else in the house handles it" (checkbox). "Add this bill" stamps "Added" (CUR-011) and the tag slides onto its day on a 2.5D DOM month drawn from the kit (GSAP, no WebGL); the reminder date is drawn in as a hairline heads-up arc landing on a marigold dot. Empty state: an empty month with "Add the first bill your house gets. Electric is a good one." In progress: tags land, arcs draw, and a shelf on the right fills with the texts you would get this month in the real sample format ("Addabill: Water bill, $64.20, due Thu Oct 2. Tap to open your utility's payment page: [link]. Reply HELP for help, STOP to cancel."). Logic: if bills exceed 5, or any bill arrives on paper (photo capture), or any is handled by someone else (shared calendar), recommend Household; otherwise recommend Free with a note on when the house outgrows it. Result state, "Your month, sorted": the finished month tilts from standing to flat (the page's scroll scene), the count of bills and reminders, one plan card, and one dominant CTA: "Purchase the Household plan" to /checkout?plan=household-monthly (with "or buy the annual plan, $40 a year" and "or use the Free plan" as lower-weight links), or, for a Free result, "Use the Free plan" dominant with Household beneath. Real inputs, a real computed result, a purchase CTA, verified by use in QA. Nothing is stored server side.

#### BRAND GRAPHIC KIT (brand_graphic_kit.md)

1. Motif, "the day cell with a standing tag": an SVG square with a 1px graphite border and a small date numeral top left, a paper tag standing inside it (a rectangle with a 2px ink stripe along its top edge) over a soft shadow ellipse. Draw-in: the border draws (stroke-dashoffset, 0.48s, Heads-up), the tag rises 8px to 0, the shadow fades in. Companion mark, "the heads-up arc": a hairline arc from the reminder day to the due day ending in a marigold dot, drawn left to right.
2. Seal, "the month seal": a circular medallion, double hairline ring, a 7 by 5 dot grid inside with one marigold dot, "ADDABILL" above and "EVERY BILL ON ITS DAY" below in Fraunces caps. Settle animation: rotates 6 degrees and lands as the dots stamp in. Anchors About, the order confirmation and the footer.
3. Dividers: (a) the week rule, a hairline with seven ticks, today's tick thicker in marigold; (b) the perforation, a dashed tear line like a bill's stub, drawing in; (c) the reminder row, three hairline arcs landing on one dot.
4. Icon style: 1.5px graphite strokes on a 24px grid, rounded joins, 2px corners, line only, a marigold dot where a date matters. Core icons (10): Add a bill (tag with a plus), Calendar month (7 by 5 grid), Heads-up text (bubble with a date tick), Tap to the payment page (tag with an arrow leaving), Paper bill (rectangle with a window), Photo capture (camera outline with a tag inside), Household (two overlapping tags with initials), Mark paid (tag with a moss check), No fees (tag with a zero), Cancel any time (tag with an open stub).
5. Numeral treatment: the Settled Numeral (above); steps and blog indices as two-digit numerals inside a hairline day-cell frame; prices in Fraunces tabular figures with the currency symbol at 60 percent, raised.
6. Texture: none beyond the two shadow tokens; the palette carries the warmth.
Every asset derives from the month; none would look right on another brand.

#### DESIGNED MOBILE HERO

"The week in hand": at 375px the copy and button come first, then a 7-day week strip built in DOM with CSS 3D transforms (no WebGL): a horizontal scroll-snap list of the month's weeks, day cells standing slightly, tags landing as the visitor scrolls the first 60 percent of a viewport, and when the week holding the 2nd is centered the heads-up chip lifts into a small phone frame showing the sample text. Draggable by thumb, native scroll-snap, no library. Reduced motion: the strip renders settled.

#### PER-PAGE ROBUSTNESS PLAN (design_robustness.md: one scene, one text-hover treatment, distinct entrances per section; one canvas per page, lazy init, capped ratio, paused offscreen)

1. Home. Scene: The Standing Month (flagship). Hover: the pencil circle, a hand-drawn SVG ellipse draws around the hovered word (mirrored on focus, drawn on press for touch). Sections and entrances: hero (signature); "Add a bill in the time it takes to open the envelope," a full-bleed graded hero-loop band with an inset card, opening as a day-cell clip-path from center (MOT-018); How it works as an oversized numeral index whose numerals settle and whose connecting hairline draws; What Addabill never does as a spec table as design, rows stamping in at 90 ms intervals with moss checks and graphite "no"; the two plan cards rising from the counter as their shadows shorten; the texts shelf, a horizontal scroll-snap row of sample messages popping in staggered from the right; the blog teaser as a masonry grid whose cards unmask upward like envelopes opening; the verbatim SMS block fading up; the mega footer as destination, the whole year as 12 small months flipping in staggered, this month marked in marigold, the seal, the address block.
2. Plans (the store). Scene: two small standing months side by side, one person with 5 tags and five people with 14 tags and initials; the camera slides laterally from Free to Household as the second fills, then both tilt flat as the price cards dock. Hover: the highlighter, a skewed marigold stroke wipes behind the word. Sections: plan cards two up with equal monthly and annual purchase buttons for Household (prices settling); "Everything in each plan" as a split sticky spec sheet, rows drawing from a hairline; renewal, cancellation and refund window as an FAQ index with motif markers stamping in; the legal identity card fading in.
3. Checkout. Scene, lightweight: today's single day cell standing at the top with the plan tag on it; its shadow shortens as the form is completed. Hover: the dated underline (hairline growing to a marigold dot). Sections: sticky order summary with full cost, renewal cadence and no fees, sliding in from the right; one column of fieldsets, each rising 8px on enter with focus lifting the field onto shadow-2; one recognized payment mark; the SMS phone reason beside the phone field; the paper-tag place-order button. Motion is quietest here.
4. Confirmation. Scene: the month with the new plan tag landing on today and the first heads-up chip lifting into the phone; camera held elevated. Hover: the settle (words settle from WONK 1 to 0). Sections: the order check drawing (CUR-011) under the seal settling; what happens next as a timeline that draws (receipt, renewal text, first reminder); the account offer, only here, fading in; the app CTA.
5. How it works. Scene: the week walk, seven paper day cells; the camera tracks Monday to Sunday as the four steps happen on the days, then rises to look down at Thursday. Hover: the tap (the word depresses 1px, shadow tightens). Sections: a sticky media rail with the phone pinned right while the four steps scroll past, each step's tag sliding in; "By typing or by photo" as a tabbed panorama (chips: Type, Snap, Share) whose screen crossfades; "Reminders, exactly when" as a timeline that draws the three reminders before a due date; the text message as component callouts with leader lines drawing to biller, amount, date, link, HELP and STOP; the CTA band.
6. About. Scene: the wall calendar hanging on a pin with a slow sway; the camera tilts down from the calendar to the counter and the sorted mail below. Hover: the pull-quote lift (2px rise onto shadow-2). Sections: alternating editorial spreads with graded photographs unmasking from the left and text lines masking up; a pull-quote interlude on the seal; the belief and the never-does list as a perforation-divided column; the legal identity card; the store CTA.
7. Blog index. Scene: the year, 12 small months lying on the counter; the camera slides across them like reading a wall planner and each post docks to its month. Hover: the date stamp (the post's date stamps in marigold beside the title). Sections: masonry editorial grid of four posts flipping in like the loader cards; topic chips drifting (floating chips cloud); the builder CTA.
8. Post A, the how-to (putting every bill on one calendar in an evening). Scene: a month that fills tag by tag as the reader scrolls. Hover: the check (a moss check draws beside the link). Sections: drop-cap spread over the graded hero; oversized numeral steps settling; the kit month diagram assembling; a pull quote; CTA to the builder.
9. Post B, the myth (autopay is not a plan). Scene: a month where one day cell dips where the draft lands before payday, its tag crooked; as the reader scrolls a heads-up moves the tag to a chosen day and the cell levels. Hover: the strike that redraws as an underline. Sections: pull-quote interlude; a checkerboard of what autopay does against what a reminder does; the heads-up arc drawing; CTA to Plans.
10. Post C, the honest comparison (sticky notes, spreadsheets, reminder apps). Scene: three objects on the counter, a sticky note, a cell grid, a phone; the camera pans across and each lifts as its section is read. Hover: the sticky lift (a marigold note background peels at a corner). Sections: alternating spreads; a spec table as design of what each catches and misses; a perforation divider; CTA to the builder.
11. Post D, the explainer (what a late fee costs and the three days that prevent it). Scene: three standing reminder markers before a due date on a week strip; the camera walks the three days. Hover: the count (hovered numerals count up). Sections: oversized numeral index of the three days; a timeline that draws; the reminder-row divider; a pull quote; CTA to Plans.
12. Contact. Scene: a small month held by a marigold magnet on a fridge-door plane that tilts toward the pointer (touch: tilts with scroll). Hover: the magnet (links snap 2px toward the pointer). Sections: the one-column form rising; the printed address, phone and email card stamping in; a stylized Dallas map band drawn from kit lines (no third-party map), lines drawing.
13. Terms and 14. Privacy. Scene, lightweight: a dimmed month in the page header with today marked and a very slow light. Hover: the dated underline. Sections: a sticky contents column whose items stagger in; each legal section fading up on enter; the verbatim SMS clauses untouched.
15. Builder (Build your month). Scene: the interactive month itself, tilting from standing to flat as the result arrives (GSAP 2.5D, pinned briefly). Hover: the Added stamp preview on chips. Sections: intro with the motif drawing; the builder (inputs left, month right; stacked on mobile with the month sticky above); the texts shelf filling; the result and CTA rising.

#### MEDIA DIRECTION (inherited by creative-asset-engine)

SUBJECT WORLD: the moment of use (consumer app). A kitchen counter at 7:40 on a weekday: the phone face up beside two paper bills and a mug, the wall calendar with a pencil on a string, the edge of the fridge door, the mail on the counter, side window light. People only as hands, never a face, never a stock smile. Never a desk, a bank, a spreadsheet or invoice vocabulary.

VIDEO CONCEPT, 12 second silent hero loop as four 3 second clips: (1) morning light crossing the counter, the dark phone waking to the Addabill calendar (built product screen composited); (2) a hand sets a paper bill beside the phone, the envelope window catching light; (3) the wall calendar close, the pencil swinging once on its string beside a circled date; (4) the phone buzzes as the sample reminder arrives, coffee steam drifting. Shot grammar: static tripod or a 2 cm slide, 35 mm equivalent, shallow depth of field, side window light, warm white balance, hard cuts, hands only. Clean wrap, no watermark, 1080p target.

PRODUCT IN MOTION, 6 to 8 seconds, image to video off the product master (the October calendar phone screenshot): a slow push in on the phone on the counter as the water bill card expands and its three reminder dates appear, morning light drifting across the glass.

PHOTOGRAPHY, 11 shots, one per page and per post, none repeating a video frame: (1) Home, the fridge door with a small paper month under one magnet; (2) Plans, two mugs on a counter with one paper bill between them; (3) Confirmation, the phone face down beside the keys in evening light; (4) How it works, a hand photographing a paper bill with the phone (screen composited); (5) About, the mail sorted into three small stacks on the counter; (6) Blog index, the wall calendar seen from across the kitchen, the room soft; (7) Post A, an evening table, a closed laptop, bills fanned, a mug; (8) Post B, a pile of envelopes with one window envelope on top in hard side light; (9) Post C, curling sticky notes on a fridge, close; (10) Post D, a wall calendar with three pencil ticks before a circled date, macro; (11) Contact, a hand holding the phone with the sample text (screen composited). Checkout carries only the kit.

GRADE RECIPE, "morning counter," one grade for the brand, derived from the palette: filter: grayscale(0.3) sepia(0.32) hue-rotate(-6deg) saturate(1.2) contrast(1.05) brightness(1.04), plus a cream FAF3E6 overlay at 8 percent multiply and a graphite 2B2622 overlay at 10 percent lighten, both pointer-events none, applied to video elements too. Strength range: full as written for the hero video and atmosphere stills; light for site photography (grayscale(0.15) sepia(0.16) hue-rotate(-3deg) saturate(1.1) contrast(1.02) brightness(1.02), overlays at half opacity); none for product imagery and the brand kit. HDRI: one Poly Haven interior, downsampled to 512px.

#### MOTION AND ACCESSIBILITY BUDGET

Budget in one line: GSAP (core, ScrollTrigger, Flip) plus Three.js r128 lazy-loaded after first paint, one canvas per page, native scroll (no Lenis), initial JS under 350KB gzipped excluding the lazy 3D bundle, hero loop under 3MB desktop and 1.2MB mobile with a poster, HDRI about 300KB cached, pixel ratio 1.5 desktop and 1 touch, LCP on the plain-DOM H1 under 1.2s, CLS under 0.1, 55fps or better through a 1.5 viewport-height signature scroll. Fallbacks: the signature scene, poster frame under reduced motion, the DOM week strip on mobile; the loader, instant today plus one fade; pinning, no pin and static content under reduced motion, shortened on touch; clip-path reveals, content unclipped; the numeral settle, static crisp numeral; button choreography, color and shadow change only; view transitions, off under reduced motion and absent in unsupported browsers; micro-feedback, a static check with aria-live; kit draw-ins, drawn state; per-page scenes, poster or settled DOM. Every hover is mirrored on :focus-visible with a press equivalent on touch; nothing essential lives in hover or motion; AA contrast holds during transitions.

#### AMBITION AND RESTRAINT CHECK

One named wow moment, The Heads-Up, delivered by the one signature move, The Standing Month; motion is a material across the visit with a rhythm of loud (the pull-back, the Heads-Up) and quiet (Plans, Checkout); the idea is legible without a word; beside the three logged builds it is unmistakably its own thing; Site of the Day worthy. Palette of five roles plus two tints, AA throughout. Two easings, three durations. Anti-patterns checked: only two pinned moments site-wide, no autoplay sound, the loader masks real load with a Skip, no carousel carries primary content, no custom cursor, parallax limited to the scene, no deceptive design, no testimonials, ratings, counts, press or badges anywhere. Considered and cut: Lenis (calm brief, blog reading, native scroll keeps the kitchen plain); a pencil custom cursor (desktop-only decoration); MOT-009 multi-layer parallax (the scene already supplies depth); TEX-015 sticker aesthetic (cute over calm); the mail-pile swarm opening (too near BioVirtua's motion); a Tier 3 raymarched world (alien to a kitchen and the runtime pain point).

Novelty quotas checked and clear: archetype, heading face and pairing, signature category, signature world (object and camera path), loader, technique freshness, under-used category, field, accent hue family, easings, interactive feature format, nav, button, voice stance (warm host), color story, tier, shader (none).

Registry technique_additions to log at Step 8: "The Standing Month" (an InstancedMesh month of paper day cells and standing tags whose scroll-scrubbed DirectionalLight angle encodes the time of day, with tags landing per scroll milestone; Three.js r128 plus GSAP ScrollTrigger) and "the flip calendar loader" (real load progress mapped to a day-of-month flip that Flips into the hero as today; GSAP Flip plus LoadingManager). Example links spot-checked live: Maxima Therapy, Maglr, Codrops SVG mask transitions; none found dead.

#### BENCHMARKS

https://www.maglr.com/blog/best-scrollytelling-examples (timeline storytelling); https://maximatherapy.com (pinned stage feel); https://tympanus.net/codrops/2026/03/11/svg-mask-transitions-on-scroll-with-gsap-and-scrolltrigger/ (shaped reveals); https://aardvarkbookclub.com (a scroll-driven 3D hero inside a working store); https://noho.ink (calm neutrals with a preloader intro and idle life).

## 6. Global Elements

### Header (sticky, every page)
The calendar header from Section 5. One cream row, 72px, condensing to 56px with shadow-1 after 40px of scroll. Left: the Addabill wordmark (brand kit primary lockup, Fraunces) linking to `/`. Center: horizontal Figtree links, in this order: **Home** `/`, **How it works** `/how-it-works`, **Plans** `/plans`, **Build your month** `/builder`, **Blog** `/blog`, **About** `/about`, **Contact** `/contact`. A hollow day-cell square slides under the active link and follows hover and focus (Heads-up curve, 0.48s). Right: the primary purchase button **Purchase the Household plan** (paper tag, marigold) which adds the Household monthly plan to the cart and routes to `/checkout?plan=household-monthly`; and the **cart** drawn as a paper tag with the item count, a marigold today tick beside it, opening the cart drawer (label "Cart, N items" for screen readers). Mobile (under 900px): wordmark left, cart right, a labeled **Menu** button that opens a full height drawer turning in like a page (Page turn curve), headed by a 7 day strip of the current week, then the links stacked, then the purchase button. Skip link "Skip to content" as the first focusable element. View Transitions: `view-transition-name` on the wordmark and the small month glyph so both persist between pages.

### Footer (every page, the destination footer from Section 5)
Top band: "The year at a glance", 12 small kit-drawn months flipping in staggered on scroll, the current month marked with the marigold tick (pure decoration, `aria-hidden`). Then four columns on desktop, stacked on mobile:
1. Wordmark, the month seal (kit), and the tagline **For whoever keeps the bills at your place.**
2. **Pages:** Home, How it works, Plans, Build your month, Blog, About, Contact.
3. **Plans:** Free (`/plans#free`), Household (`/plans#household`), **Purchase the Household plan** (`/checkout?plan=household-monthly`), Cart (`/cart`).
4. **Addabill Inc.** on its own line, then the physical address **4201 Spring Valley Rd, Dallas, TX 75244**, phone **(888) 338-9070** (as a `tel:` link), **support@addabill.com** (as a `mailto:` link), then **Terms of Service** (`/terms-of-service`) and **Privacy Policy** (`/privacy-policy`).
Beneath the columns: the verbatim "Join Our SMS List" block (below). Last line: "© 2026 Addabill Inc. All rights reserved." No social icons (no brand-owned pages exist yet; add them here when they do). No "As Seen In" (no qualifying press).

### The "Join Our SMS List" block (verbatim, footer, every page)
Reproduce exactly. Only the brand name, phone, support email and the two link targets are substituted.

**Heading:** Join Our SMS List
**Phone field placeholder:** Your Phone Number
**Consent checkbox 1 (unchecked by default):** I agree to the Terms & Privacy Policy
("Terms" links to `/terms-of-service`; "Privacy Policy" links to `/privacy-policy`.)
**Consent checkbox 2 (unchecked by default):** I agree to receive SMS marketing notifications from Addabill. Reply HELP for help or call/email (888) 338-9070 / support@addabill.com STOP to cancel. Msg & data rates may apply. Msg frequency varies. Information gathered in the SMS campaign will not be shared with third parties or affiliates for marketing purposes. Read our Terms and Privacy Policy.
(The trailing "Terms" links to `/terms-of-service`; "Privacy Policy" links to `/privacy-policy`.)
**Button:** Submit

Behavior: the phone field has a visible top aligned label ("Phone number", the placeholder stays "Your Phone Number"), `type="tel"`, `autocomplete="tel"`, required. Submit validates: phone present and 10 digits (error: "Enter a 10 digit US phone number, like 214 555 0100."), both boxes checked (error: "Tick the box to agree to the Terms & Privacy Policy." / "Tick the box to agree to receive texts from Addabill."). Errors appear beneath their control and in a summary above the button, never by color alone, never while typing. Success state replaces the form with a paper tag stamping in (CUR-011) reading "You're on the list. Reply HELP for help, STOP to cancel." announced by `aria-live`. No real send is made; the success state is the confirmation. Both boxes are never prechecked, never bundled, never required for any purchase.

### Cart drawer and `/cart`
The cart holds at most one plan line (Free, Household monthly, Household annual); choosing a different plan replaces it and the drawer says so ("Swapped to Household, annual."). The drawer slides in from the right (Page turn curve) with: the plan name, the price line, the renewal line in plain words, "Fees on your bills: None", a monthly/annual toggle for Household, **Remove**, and a dominant **Checkout** paper tag button to `/checkout`. The `/cart` page shows the same content full width with the small standing month scene from Plans dimmed behind. Cart state persists in `localStorage` with an in memory fallback. Empty state: "Your cart is empty. The plans are one tap away." with **See the plans** to `/plans`. Checkout with an empty cart redirects to `/plans` with the same line shown. Removing the last item shows the empty state without leaving the drawer.

### 404 page (real 404 status)
The day-cell motif drawn large with no tag in it, then **This page isn't on the calendar.** and **Nothing's due here. Head home, or have a look at the plans.** Buttons: **Home** (`/`, secondary paper tag) and **Purchase the Household plan** (`/checkout?plan=household-monthly`, primary). Header and footer as everywhere.

### Head hygiene (every route)
Unique `<title>` and meta description per page (given in Section 7), `<html lang="en">`, canonical URL, Open Graph title, description and image (`/assets/og-card.png`, the brand kit OG card, 1200 by 630), Twitter card summary_large_image, favicon set from the brand kit (favicon.ico, apple-touch-icon.png), theme-color FAF3E6, no `noindex` anywhere, a `robots.txt` allowing all and a `sitemap.xml` listing every route in Section 7.

### Motion, accessibility and performance (every page)
The named motion signature (Heads-up and Page turn curves; 0.2s, 0.48s, 1.4s) drives every animation. Every page ships its own scroll driven scene, its own text hover treatment, and a distinct scroll in animation per section, exactly as the per page plan in Section 5 lists; every button, word and clickable element moves on hover, focus and press; every hover is mirrored on `:focus-visible` with a press equivalent on touch. `prefers-reduced-motion` swaps every scene for its poster or settled DOM, shows the loader's today card instantly, and disables view transitions. Budgets (measured, not eyeballed): LCP under 2.5s (target under 1.2s on the plain DOM H1), CLS under 0.1, initial JS under 350KB gzipped excluding the lazy Three.js bundle, 55fps or better through the 1.5 viewport height signature scroll, signature scroll measured at 1.25 to 1.75 viewport heights, hero loop under 3MB desktop and 1.2MB mobile with a poster, HDRI about 300KB. WebAIM six checked on every page: contrast (graphite on cream 13.6:1, graphite on marigold 7.2:1, shadow on cream 5.5:1; marigold never carries text on cream), alt text on every image, a visible label on every form control, no empty links or buttons, `lang` set.

## 7. Page by page specification

The finished copy for every page is in Section 7a (SITE_COPY, embedded verbatim). Each page below names its sections top to bottom, every CTA as label → destination → action, every form, its asset slots (ids match ASSET_PLAN.json), its head tags, and its mobile notes. Its scroll scene, text hover treatment and per section entrances are the ones the per page robustness plan in Section 5 assigns to that page; build them as written there.

### Sitemap
`/` Home · `/how-it-works` · `/plans` (the store) · `/builder` (Build your month) · `/blog` · `/blog/every-bill-on-one-calendar-in-an-evening` · `/blog/autopay-is-not-a-plan` · `/blog/sticky-notes-spreadsheet-reminder-app` · `/blog/what-a-late-fee-costs` · `/about` · `/contact` · `/cart` · `/checkout` · `/confirmation` · `/terms-of-service` · `/privacy-policy` · `/404`. Plus `/robots.txt` and `/sitemap.xml`.

### 7.1 Home `/`
Title: "Addabill: every household bill and due date on one calendar". Description: "Add every bill your house gets, see them on one calendar, and get a text before each is due. No fees on your bills. Free plan, or Household for $5 a month."
Purpose: a stranger understands what Addabill is, who it is for and how to buy it inside the first viewport, then is shown the product working.
Sections, top to bottom:
1. **Loader** (the flip calendar, lower 45 percent of the viewport only; Skip visible from the first frame) resolving into:
2. **Hero, The Standing Month** (signature scene, pinned 1.5 viewport heights): centered H1 **Every bill on one calendar. A text before each is due.**, subhead **For the household's bill keeper, and every bill that arrives by email, by app or on paper.**, primary **Purchase the Household plan** → `/checkout?plan=household-monthly` (adds Household monthly to the cart), price line **$5 a month or $40 a year. No fees on your bills. Cancel any time.**, text link **or use the Free plan, up to 5 bills** → `/checkout?plan=free`. The Settled Numeral "2" stands beside the water bill tag in the scene. The phone at the frame edge shows the real reminder text (Text 1). Mobile: "The week in hand" strip (Section 5) replaces the WebGL scene beneath the copy and button.
3. **Add a bill in the time it takes to open the envelope**: full bleed graded hero loop `hero-loop` (poster `hero-loop-poster`, `muted playsinline loop preload="metadata"`, reduced motion shows the poster) with an inset paper card carrying the heading and copy. No CTA here (the primary already sits above).
4. **How Addabill works: Add, See, Heads-up, Tap**: oversized numeral index 01 to 04 with the one sentence each, the connecting hairline drawing; a text link **See every step** → `/how-it-works`.
5. **What Addabill never does**: the six row table as design (statement | why), rows stamping in.
6. **Two plans, no fees on your bills**: two plan cards. Free card line, **Use the Free plan** → `/checkout?plan=free`. Household card line, price line, **Purchase the Household plan** → `/checkout?plan=household-monthly`. Beneath: text link **Compare everything in each plan** → `/plans`.
7. **The texts you'd get this month**: horizontal scroll snap shelf of the five sample texts as phone bubbles, each with the day tick; drag on touch, arrow keys and visible buttons on desktop.
8. **Keeping the house on time** (blog teaser): heading, the line, four post cards (title, standfirst, the post photo `photo-post-a` to `-d` as thumbnails) each → its route; **Read the blog** → `/blog`.
9. **Build your month** band: one line "Add three of your own bills and see the texts you'd get" (from the builder standfirst, shortened is not allowed, so use: **Add three to five of the bills your house actually gets. Watch them land on a month, see the texts you'd receive, and find out which plan fits.**), **Build your month** → `/builder` (secondary paper tag; the primary purchase button lives in the header on this band).
10. Footer with the verbatim SMS block.
Assets: `hero-loop`, `hero-loop-poster`, `photo-home-fridge` (used in section 8 as the blog index card image or beside the never-does table on desktop), `svg-month-seal`, `hdri-interior-512`, `tex-paper`, `tex-counter`.
Mobile: sections stack; the shelf and the 12 month footer band scroll horizontally with snap; the table becomes stacked rows with the statement bold and the why beneath.

### 7.2 How it works `/how-it-works`
Title: "How Addabill works: add, see, heads-up, tap". Description: "Four steps, in detail: how bills get added by typing or by photo, what the calendar shows, when the texts arrive, and how one tap opens your biller's own payment page."
Sections: H1 **Four steps. That's the whole app.** with the standfirst; **sticky media rail** (the phone pinned right, desktop) with the `product-motion` clip (poster `product-motion-poster`) while the four expanded steps scroll past on the left, each step's tag sliding in, step screens `prod-add`, `prod-calendar`, `prod-bills` swapping in the phone frame; **By typing or by photo** tabbed panorama (chips Type, Snap, Share; the phone screen crossfades between `prod-add`, `prod-photo`, `prod-add`); **Reminders, exactly when** timeline that draws the 7, 3 and 1 day markers before a due date; **anatomy of a text** with leader lines drawing from the sample bubble to the six labels; photo `photo-hiw-capture` in the Snap tab; atmosphere still `atmos-hiw-cta` behind the closing band **Put the first bill on its day tonight. The first text comes before you'd have thought of it.** with **Purchase the Household plan** → `/checkout?plan=household-monthly`. Footer.
Mobile: the rail unpins and the phone sits above each step; tabs become a segmented control.

### 7.3 Plans `/plans` (the store)
Title: "Addabill plans: Free, or Household for $5 a month". Description: "Free keeps one person on time with up to 5 bills. Household keeps the whole house on time: unlimited bills, photo capture, up to 5 people, $5 a month or $40 a year, cancel any time."
Sections: H1 and standfirst; the **two plan cards** side by side (stacked on mobile), each with name, price line, description, EVERY inclusion as its own line with a kit icon, and CTAs: Free **Use the Free plan** → `/checkout?plan=free`; Household **Purchase the Household plan** → `/checkout?plan=household-monthly` and **Buy the annual plan** → `/checkout?plan=household-annual`, equal weight, neither preselected, with the note **Same plan either way. The year costs $20 less than twelve months.**; the small standing months scene (Free 5 tags, Household 14 tags with initials) above the cards; **Everything in each plan** as a real HTML table (11 rows from the copy) with a sticky first column; product shots `prod-household` and `prod-summary` beside the Household column on desktop; photo `photo-plans-mugs` as the section image beside the FAQ heading; **FAQ** as an accordion of six (each question a `<button>` with `aria-expanded`, answers from the copy, kit motif markers); `atmos-plans-faq` as a very light band behind the FAQ; **The company behind the plan** legal identity card; footer.
Every cost is visible here before checkout begins: price, renewal cadence and price, "No convenience fees", the 14 day annual refund, cancel any time. Nothing new appears inside the checkout.

### 7.4 Build your month `/builder` (the interactive feature)
Title: "Build your month: see your bills on one calendar". Description: "Add three to five of your own bills, watch them land on a month with their reminder days, see the texts you'd get, and find out whether Free or Household fits your house."
Sections: H1 **Build your month** and standfirst; the **builder**: inputs left, live 2.5D month right (stacked on mobile with the month sticky above the form). Fields exactly as the copy lists (Biller required; Amount optional; Due day required 1 to 31; Text me before it's due chips 1, 3, 7 with 3 default; This one arrives on paper; Someone else in the house handles it), top aligned labels, required and optional both marked, **Add this bill** button. On add: "Added" stamp (CUR-011), the tag slides onto its day, the heads-up arc draws to the reminder day (due day minus lead, wrapping into the previous month visually as a dimmed leading cell), the **texts shelf** on the right gains the message in the exact product format ("Addabill: {Biller}, {amount or blank}, due {weekday} Oct {day}. Tap to open your biller's payment page: [link]. Reply HELP for help, STOP to cancel."), screen reader announcement "{biller} added, due on the {day}." Empty state line **Add the first bill your house gets. Electric is a good one.** Bills can be removed (a small "Remove" text button per tag). Logic: Household when bills exceed 5, or any arrives on paper, or any is handled by someone else; else Free. Result state **Your month, sorted** with the summary line template filled, the month tilting flat (the page's scroll scene), then the recommendation block (Household: subheading, reason clause by first match, paragraph, dominant **Purchase the Household plan** → `/checkout?plan=household-monthly`, lower links **or buy the annual plan, $40 a year** → `/checkout?plan=household-annual` and **or use the Free plan** → `/checkout?plan=free`; Free: subheading, paragraph, dominant **Use the Free plan** → `/checkout?plan=free`, lower link **or purchase the Household plan, $5 a month** → `/checkout?plan=household-monthly`). Nothing is stored server side; state lives in memory only. Footer.
QA verifies by adding 3 bills (Free result) and 6 bills including one on paper (Household result), with keyboard only, and at 375px.

### 7.5 Blog index `/blog`
Title: "Keeping the house on time: the Addabill blog". Description: "Short pieces about what's due, when, and how not to find out from the fee."
Sections: H1 and standfirst; photo `photo-blog-wall` as the editorial lead image; the four post cards in a masonry grid (photo, headline, standfirst, "Read" link → route) flipping in like the loader cards; topic chips (Getting organized, Autopay, Systems, Late fees) as plain filters that show and hide cards (no page reload, `aria-pressed`); a **Build your month** band → `/builder`; footer.

### 7.6 Blog posts (four, each its own route)
Common template: title tag "{headline} | Addabill"; description = the standfirst; the post photo as the graded hero (`photo-post-a` to `-d`) under the headline and standfirst; a drop cap spread; the kit SVG graphic for the post (`svg-post-a` to `-d`, assembling on scroll); the body verbatim from Section 7a with its subheads; a pull quote where the copy marks one; the closing internal CTA from the copy (Post A and C **Build your month** → `/builder`; Post B and D **See the plans** → `/plans`); "More from the blog" with the other three cards; footer. Scenes and hover treatments per post are in Section 5 (Posts A to D).
Routes and headlines: `/blog/every-bill-on-one-calendar-in-an-evening`, `/blog/autopay-is-not-a-plan`, `/blog/sticky-notes-spreadsheet-reminder-app`, `/blog/what-a-late-fee-costs` (headlines and standfirsts in Section 7a).

### 7.7 About `/about`
Title: "About Addabill: one calendar for every household bill". Description: "Why Addabill exists, what it does, and what it never does: no payments, no account connections, no fees on your bills."
Sections: H1 **About Addabill** (the copy's opening line becomes the standfirst), the full About copy in alternating editorial spreads with `photo-about-mail` unmasking from the left and a second image slot using `atmos-about-quote` behind the pull quote interlude on the month seal; the "never does" list as a perforation divided column; **The company behind the plan** identity card; the closing purchase CTA from the copy **Purchase the Household plan** → `/checkout?plan=household-monthly`; footer. No founders, no team.

### 7.8 Contact `/contact`
Title: "Contact Addabill". Description: "Write to support about a bill on your calendar, your plan, or a text you received. Addabill Inc., Dallas, TX. (888) 338-9070."
Sections: H1 **Talk to us** and standfirst; one column **form**: Your name (required, `autocomplete="name"`), Email (required, `email`, format validated), Phone, if you'd like (optional, `tel`, with the stated reason), Message (required, textarea), helper text as written, **Send** button. Validation on blur with delay; errors beneath the field and summarized above the button ("Enter your name." "Enter an email address in the correct format, like name@example.com." "Enter your message."). Success: the form is replaced by a stamping paper tag "Sent. Support answers within one business day." (no real send; the state is the confirmation). Right column (below on mobile): the address card (Addabill Inc., 4201 Spring Valley Rd, Dallas, TX 75244, (888) 338-9070 as `tel:`, support@addabill.com as `mailto:`), the hours line, and `photo-contact-hand`; beneath, the stylized Dallas map band drawn from kit lines (no third party map). Footer.

### 7.9 Cart `/cart` and the cart drawer
As specified in Section 6. Title: "Your cart | Addabill".

### 7.10 Checkout `/checkout` (complete, guest, digital: no shipping)
Title: "Checkout | Addabill". `noindex` is NOT set (the page is indexable but excluded from the sitemap). Query `plan=free | household-monthly | household-annual` preselects the line; with no plan and an empty cart the page redirects to `/plans`.
Layout: sticky **order summary** right (top on mobile, collapsible): Plan, Price, Renews, Fees on your bills: None, then Total with the same figure, then the line **No account needed. Pay for the plan, get your receipt, and we'll offer you a login afterward if you want one.** and a monthly/annual switch for Household. Left: one column of numbered fieldsets:
1. **Contact**: First name (required, `given-name`), Last name (required, `family-name`), Email address (required, `email`), Phone number (required, `tel`) with the helper **for your receipt and your account texts**.
2. **Billing address** (Household only; hidden for Free): Address line 1 (required, `address-line1`), Address line 2 (optional, `address-line2`), City (required, `address-level2`), State (required, select of US states, `address-level1`), ZIP code (required, `postal-code`, 5 digits), Country (required, select, default United States, `country`).
3. **Payment** (Household only; hidden for Free, which shows "No card. Free is $0, no card on file, no time limit." in its place): one row of accepted card marks (Visa, Mastercard, Amex, Discover) as the single trust mark; Name on card (required, `cc-name`), Card number (required, `cc-number`, grouped in fours, Luhn and length), Expiry month (required, select, `cc-exp-month`) and Expiry year (required, select, `cc-exp-year`) side by side with CVV (required, 3 to 4 digits, `cc-csc`, a "What's this?" disclosure explaining where it is). Beneath: **Place order** (paper tag, full width) and, in small type, "No charge is made on this preview site." plus links to Terms and Privacy.
Rules: labels top aligned and always visible; required AND optional both marked; validation on blur with a short delay, never while typing; messages per the GOV.UK set in the copy, beside the field and repeated in a summary above the button linked to the fields; values are never cleared on failure; Enter submits. On valid submit: the button shows the paper tag spinner then routes to `/confirmation?plan=...&term=...` with the order held in `sessionStorage`. Free path: fieldset 1 only, then the same **Place order** button, because the Free plan is a $0 order placed through the same flow; the summary reads Plan: Free, Price: $0, Renews: Never, Fees on your bills: None. Never an account step anywhere in this page.

### 7.11 Confirmation `/confirmation`
Title: "Sorted | Addabill". Not in the sitemap.
Sections: the month seal settling and the order check drawing; H1 **Sorted. Your Household plan starts now.** (for Free: **Sorted. Your Free plan starts now.**); the order card (plan, term, price, renewal line, the contact email and phone from the order); the confirmation paragraph (for Free, the same paragraph with "buying the Household plan" read as "choosing the Free plan" and the renewal sentence omitted); **What happens next** timeline (three items, the annual and Free variants as the copy notes); the **account offer** (optional, only here): a disclosure "Set up a login" opening Email (prefilled) and a Password field with **Create login** as a plain secondary button that shows a "Login saved for {email}" stamp (no real account is made on this preview); app CTA: the copy's **Open Addabill** button links to the app URL placeholder `https://app.addabill.com` ONLY once that URL is live; until then the build shows **See how to add your first bill** → `/how-it-works` in its place and this substitution is listed in the handoff for Harlem. The Free order confirmation photo slot `photo-confirm-phone`. Footer.

### 7.12 Terms of Service `/terms-of-service` and Privacy Policy `/privacy-policy`
Titles "Terms of Service | Addabill" and "Privacy Policy | Addabill". Rendered from the complete legal text in Section 8, headings as `<h2>`, a sticky contents column, the dimmed month in the page header, "Last updated: September 23, 2026". `[INSERT SHORT CODE]` stays verbatim. Reachable from every page (footer, SMS block, checkout).

### 7.13 404
As specified in Section 6, served with a real 404 status.

### Asset slot contract (input to creative-asset-engine, ids are final)
Video: `hero-loop` (16:9, 12s, 4 clips, silent, loop; Home section 3), `hero-loop-poster`, `hero-loop-mobile` (smaller encode), `product-motion` (9:16 phone or 16:9 framed phone, 6 to 8s; How it works rail), `product-motion-poster`.
Product shots (built in HTML, screenshotted, phone at 1170 by 2532 and one 16:10 desktop family shot): `prod-calendar` (the master: October month view, 11 tags, water bill card open), `prod-bills`, `prod-add`, `prod-photo`, `prod-household`, `prod-summary`, `prod-desktop-family`.
Photography (11, 3:2 unless noted, light grade): `photo-home-fridge`, `photo-plans-mugs`, `photo-confirm-phone`, `photo-hiw-capture` (screen composited from `prod-photo`), `photo-about-mail`, `photo-blog-wall`, `photo-post-a`, `photo-post-b`, `photo-post-c`, `photo-post-d`, `photo-contact-hand` (screen composited from a text bubble).
Atmosphere stills (full grade): `atmos-hiw-cta` (21:9), `atmos-about-quote` (21:9), `atmos-plans-faq` (21:9).
Blog kit graphics (SVG, built from the kit): `svg-post-a` (a month filling), `svg-post-b` (a dipped day cell leveling), `svg-post-c` (sticky note, grid, phone), `svg-post-d` (three ticks before a circled date).
Brand kit: `logo-primary`, `logo-reversed`, `logo-stacked`, `logo-icon`, `favicon`, `apple-touch-icon`, `banner-linkedin`, `banner-x`, `banner-crunchbase`, `og-card`.
3D: `hdri-interior-512` (Poly Haven interior, 512px), `tex-paper`, `tex-counter`.
Alt text for every photo and product shot is in Section 7a (Alt text), corrected against the real image after generation.

### 7a. The finished copy (SITE_COPY, verbatim; build word for word)

#### Addabill site copy (Step 3, site content engine)

Brand: Addabill (addabill.com), Addabill Inc. Voice stance: the warm host. Every heading, sentence and label below is final and meant to be used word for word. Subheads inside the blog posts are marked with four hashes. Placeholders in curly braces are the only text the build fills in.

Note on the list of things Addabill never does: the About brief named the account login item and the lending item using two nouns that sit on the brand's refused list. Both ideas are stated here without those nouns ("connect an account or hand over a login to wherever your money lives"; "never lends you anything, and it never grades the way you pay"). The meaning is intact and the refused list is clean across the whole file.

* * *

##### ABOUT

H1: About Addabill

Somewhere in your house there's a dentist statement. It came on paper, in a window envelope, and it's the only bill you get that way, so it lives nowhere. Not in your email. Not in an app. Not on the calendar with the electric and the rent. It's on the counter under two catalogs, and it's due on the 9th.

Addabill started with that envelope. Not with a mission, with a question: why does one bill get to hide just because it arrived through a different door? Every house has one. For you it might be the orthodontist, or the HOA, or the county sending a paper notice once a year. The bill keeper knows about it, in the way you know where you left your keys. Right up until the late fee.

Here is the one thing we believe about bills, and it's why the app looks the way it does. The problem was never the money. The problem is time. A bill costs one amount on the day it's due and more on the day after, and the whole job of keeping a house on time is knowing which day is which, for a dozen billers at once, across email, paper and apps that each think they're the only one you have. So Addabill is a calendar first. One month, every bill standing on its day, and a text to your phone before each one is due.

That belief is also why there's a list of things Addabill will never do. It never pays a bill for you; you tap through to your biller's own page and pay there, same as before. It never asks you to connect an account or hand over a login to wherever your money lives, because a calendar doesn't need to see a balance. It never adds a fee to anything. Household is $5 a month or $40 a year, and that price is the whole of what you'd ever pay us. It never lends you anything, and it never grades the way you pay. It's a calendar with a text. That's the whole idea, and we intend to keep it that small.

We built it for a specific person, and you probably know who that is at your place. The one who put the phone plan on autopay, watched it draft two days before payday, and got an overdraft fee for being on time. The one whose fridge has a sticky note that says WATER 2ND, which worked well until it slid behind the toaster. The one with eight to fifteen billers and a very good memory that still slipped once this year. That person doesn't need a lecture or a chart. They need to know what's due, and to hear about it first.

Addabill Inc. is new. The company is in Dallas, at 4201 Spring Valley Rd, the app is the first thing we've made, and there's no founding story worth telling beyond the envelope on the counter. We'd rather say that plainly than dress it up. What we can offer is the calendar, the texts, and the short list of things we'll never do, and we'd like you to hold us to all three.

If you keep the bills for your house, the Household plan is where to start: every bill the house gets, the paper ones by photo, up to five people on one calendar, and a summary of the year when December comes.

CTA: Purchase the Household plan

Pull quote for the seal interlude (lifted from the body, not new text): "The problem was never the money. The problem is time."

* * *

##### BLOG

###### Post A (how to)

Route slug: /blog/every-bill-on-one-calendar-in-an-evening

Headline: Your bills live in three places. One evening moves them to one.

Angle: The practical guide that is actually good: the order of operations for gathering every household bill in a single sitting, with the reason behind each step.

Theme: The bill keeper hasn't failed at discipline. Bills arrive through three different doors (email, the mailbox, and apps that only speak up when they want money) and nobody has ever walked all three in one go. An evening with the inbox search, the mail pile and the phone gets every regular bill onto one month, a second pass catches the quarterly and yearly ones, and one house rule keeps the calendar true from then on.

Standfirst: A kitchen table, a laptop, the mail pile and about ninety minutes. Here's the order that gets every regular bill onto one month, and the reason for each step.

Body:

Nobody forgets the rent. The bills that go late are the ones that come through a door you weren't watching: the propane company that only sends paper, the streaming plan quietly billing a card you don't look at, the trash service that wants money four times a year on its own schedule. A house has three doors for bills. Email, the mailbox, and the apps that only speak up when they want something. Nobody has ever walked all three in one sitting, which is why the month never feels complete.

So don't try to remember harder. Spend one evening walking the three doors, put everything on one month, then set a single house rule so nothing gets past the counter again. Ninety minutes, roughly. Here's the order, and the order is most of the trick.

####### Start with the inbox, because it's the widest door

Open your email and search the last 60 days for "due", "amount due", "statement is ready" and "autopay". Every biller that emails you will surface, including the ones whose messages you've been swiping past since spring. Don't add anything yet. Write a plain list: the biller, the rough amount, the day of the month it's due. Electric, 14th. Internet, 20th. Phone plan, 6th.

The list comes first for a reason. You want to see the shape of the month before you commit it anywhere. A house that discovers it has six bills due between the 1st and the 5th learns something useful right there, and it's easier to see on one sheet of paper than one bill at a time.

####### Then walk the house for paper

Now stand up. The counter pile, the fridge door, the drawer by the phone charger, the glovebox, the basket by the front door where the mail lands when nobody's ready for it. You're after window envelopes and anything with a stub along the bottom. These are the billers that never went digital, or that you never got around to switching: the propane company, the pest service, the county for the trash. Add them to the same list, with a mark that says paper.

Why paper second and not first? Because the inbox search is mechanical and warms you up. Paper needs you to actually look, and by now you know what you're looking for.

####### Open the apps that bill you without asking

The third door is the quietest. The phone plan, the gym, the streaming plans, the cloud storage you forgot you pay for. Each one lives in its own app or its own website, each one thinks it's the only bill you have, and none of them will ever appear in your inbox unless something goes wrong. Open each one, find the billing date, and add it to the list. Ten minutes. This is usually where the surprises are, and they're rarely large, which is exactly why they hide.

####### Put the list on one month

Now the app. Take the list top to bottom and add each bill: the biller's name the way you say it at home, the due day, the amount if you have it. On the Household plan the paper ones can go in by photo, which is faster than typing and catches the amount and the due date off the page. When each one lands you'll see it standing on its day, and by the end of the list the month has a shape. Clusters near the 1st. A quiet stretch in the middle. The 20th to the 25th busier than you thought.

Give each bill its reminders as you go. Three days before is the default and a good one. If a bill needs money moved first, say from savings, take seven days as well. And if someone else in the house handles a bill, mark it, so it shows under their name on the shared calendar and the heads-up goes to their number.

Before you close the app, go back through the year in your head for the ones that don't come monthly. Renters insurance, once a year. Car registration, once a year, from the county. The trash service, quarterly. Propane, whenever they fill the tank, which is not a schedule but is still a bill. Add each with its next due date and let the calendar carry it forward. These are the bills late fees are made of, because no monthly rhythm reminds you they exist.

####### The one rule that keeps the month true

The evening gets you to complete. Staying complete takes one rule, and it's a house rule, not an app feature: a bill goes onto the calendar before it goes onto the counter. Envelope arrives, add it, then open it properly or don't. Email arrives, add it, then archive it. New subscription, add it the day you sign up, while you still remember it exists. It takes less time than the sorting you'd otherwise do later, and the calendar stays something you can trust, which is the entire point of having one.

The first evening is the only hard one. After that, the house has one month, and the month is right.

If you want to see the shape of your month before you give it the full evening, put three of your bills into Build your month and watch where they land. (Link: /builder, label "Build your month")

Pull quote (lifted from the body): "A bill goes onto the calendar before it goes onto the counter."

###### Post B (the myth)

Route slug: /blog/autopay-is-not-a-plan

Headline: Autopay is not a plan

Angle: The myth the category believes, that automating the payment is the same as being organized about it, and why a heads-up plus a pay day you chose beats a draft you can't see.

Theme: Autopay solves forgetting by removing you from the exact moment the money leaves, which is the one moment the bill keeper most needs to be present: the draft that runs at 6 a.m. on a payday that posts at noon, the promotional rate that ended without a word, the summer electric that doubled and drafted anyway. A text before the due date, with the amount and the link, keeps the part of autopay that works and hands back the choosing. Autopay still belongs on the bills that never change and never move.

Standfirst: Set it and forget it works right up until the morning the draft runs before the paycheck posts. There's a calmer arrangement: hear about the bill, then pay it on a day you picked.

Body:

Autopay was invented to solve forgetting, and it does. It just solves it by taking you out of the room. The bill arrives, the amount is decided, the money leaves, and you find out afterward, if you find out at all. That's not a plan. A plan is something you can look at on Tuesday and act on by Thursday. Autopay is a decision you made one afternoon three years ago and haven't looked at since.

None of this is an argument against paying on time. It's an argument about who's in the room when it happens.

####### The draft that runs before the paycheck posts

Here's the morning that sours people on autopay. Rent is due on the 1st. Payday is also the 1st. The draft runs at 6 a.m., the paycheck posts at noon, and for six hours the account is short, which is all it takes. The rent goes through, an overdraft fee lands on top of it, and you've paid extra for the privilege of being on time. Nobody did anything wrong. The lease says the 1st, payroll says the 1st, and the two never met.

A heads-up a few days before changes the shape of that morning. You know rent is due Thursday. You know the paycheck lands Thursday too. So you pay that afternoon, after the money is in, and rent is still on time. Same bill, same day, different hour, no fee. Or the text simply reminds you on Wednesday to move money over so the account is ready at 6 a.m. Either way, you were in the room.

####### The amount that changed and nobody said so

An electric bill moves with the weather. A house that pays, say, $95 in April can pay $210 in August with the air conditioning running, and autopay will pay $210 without a word, because that's its whole design: the amount is whatever the biller says it is. You find out when you look at the account, which is to say later.

A text with the amount in it is a different experience. "Electric bill, $210, due Thu Oct 16" arrives a week out and you have a week to decide what to do with that information. Maybe nothing. Maybe you move some money. Maybe you finally call about the thermostat. The point isn't the deciding. It's that the number reached you before the money left.

####### The promotional rate that quietly ended

Internet plans love a first year price. Twelve months at one rate, then the regular rate, disclosed somewhere in the paperwork you signed on a tablet at the door. With autopay, month thirteen looks exactly like month twelve until you happen to check, and that could be months later. A heads-up that carries the amount catches month thirteen on the day it happens, because the number is different and you're looking at it. Any bill that resets on an anniversary behaves the same way, and every house has a couple of those.

This isn't a complaint about any company. Prices change and companies say so, somewhere. It's a complaint about an arrangement where nobody on your side of the transaction is watching.

####### A heads-up and a day you chose

So here's the calmer arrangement, and it isn't complicated. Each bill gets a text before it's due, on the lead you pick, and each text carries the biller, the amount and a link to that biller's own payment page. You pick the day you pay: after payday, on the Sunday when you do the household chores, the moment the text arrives, whenever suits the house. Then you tap the link and pay on the page you'd have used anyway.

A house can end up with one paying day a week this way. The week's texts sit in the thread, Saturday morning arrives with coffee, and four bills get paid in the time the kettle takes. Nothing early by accident, nothing late, and no draft you had to brace for.

You keep the good part of autopay, which is never being ambushed by a due date. You get back the part it took, which is seeing the amount and choosing the moment. And you lose the 6 a.m. draft entirely, because nothing moves until you move it.

####### Where autopay still belongs

Some bills never change and never move. A monthly parking spot, the storage unit, the water softener rental. If the amount is fixed, the date sits well clear of payday and the biller is one you'd never need to question, autopay is fine, and the bill can still live on the calendar so the month shows it. The heads-up then just tells you the draft is coming, which is its own kind of calm.

The rule of thumb is short. Autopay the bills that are boring. Get a heads-up on the ones that aren't. Keep all of them on one month, so you can tell which is which.

The Household plan puts every bill, drafted or not, on one calendar with a text before each is due, for $5 a month or $40 a year. Have a look at both plans. (Link: /plans, label "See the plans")

Pull quote (lifted from the body): "It's an argument about who's in the room when it happens."

###### Post C (the honest comparison)

Route slug: /blog/sticky-notes-spreadsheet-reminder-app

Headline: The sticky note, the spreadsheet and the reminder app: what each one catches, and what slips past

Angle: The honest comparison the reader is already making in their head, with the tradeoffs of each method named plainly, including the one Addabill sells.

Theme: Every system the bill keeper has tried is good at the part of the problem it was built for. The sticky note is visible, the spreadsheet knows totals, the reminder app knows the time. None of them knows the bill itself (the amount, the due date, where to pay it and who in the house handles it), and none of them travels to the person who needs it. Addabill knows the bill and travels as a text, but it will not pay anything for you and it only knows what you add. The right pick depends on which thing slips through in your house.

Standfirst: Four ways to keep bills straight, laid side by side, with the failure of each one named plainly. Ours included.

Body:

Every bill keeper has a system, and every system is a good answer to part of the question. That's why they're so hard to give up. The sticky note isn't silly. The spreadsheet isn't overkill. The reminder app isn't lazy. Each one catches something real, each one lets something else through, and the something is usually the bill that went late. Here's what each one actually does, including the one we make.

####### The sticky note: visible right up until it isn't

A note on the fridge is the most honest system there is. You see it every time you get the milk. It costs nothing and it needs no login. For one or two bills with hard dates, it's close to perfect.

What it catches: the bill you'd otherwise forget exists. A note that says CAR INS does its job by being in your eyeline.

What slips past: everything about the bill except its name. CAR INS, but not how much, not which day, not where to pay it, and not whose turn it is. The note also has a lifespan. It curls at the corners in about a month, the adhesive gives up, and it ends up face down under the fridge with the magnets that fell. And it can't leave the kitchen. If you're at work when the due date arrives, the note is still at home, doing nothing.

####### The spreadsheet: brilliant with totals, useless on a Tuesday

A spreadsheet knows everything the sticky note doesn't. Every biller in a column, every amount, a total at the bottom that tells you what the house costs to run. If you've ever built one, you know the quiet satisfaction of the sum.

What it catches: the whole picture. Which bills went up this year. What a month really costs. Where the money goes.

What slips past: time. A spreadsheet doesn't know what day it is. It sits in a folder until you open it, and nobody opens a spreadsheet on a random Tuesday to see what's due Thursday. It's also work to keep true. The column you filled in faithfully through February goes blank in March, and from then on the totals are fiction. A spreadsheet is a fine record and a poor alarm.

####### The reminder app: knows the time, not the bill

Phone reminders fix the spreadsheet's problem. They know what day it is and they interrupt you. A reminder that says "Pay electric" at 9 a.m. on the 14th will fire whether you remember or not.

What it catches: the date. If the only thing between you and on time is being told, a reminder app tells you.

What slips past: the bill. "Pay electric" sits between "buy milk" and "call Mom" and looks exactly like them, so it gets swiped like them. It doesn't carry the amount, so you can't tell whether this month is normal. It doesn't carry the link, so you go hunting for the login. It doesn't know that your partner handles the electric now. And when you've paid, nothing happens; the reminder just stops, and there's no record that it was paid or what it cost.

####### What Addabill catches, and what it doesn't

Addabill was built to know the bill. Each one goes in with its biller, its amount and its due day, by typing or by photographing the paper, and stands on one month with every other bill the house has. Before it's due, a text arrives with the biller, the amount, the date and a link to that biller's own payment page. On the Household plan the calendar is shared, so the text about the electric reaches the person who handles the electric, at their number. Mark it paid and it stays paid, with 12 months of history behind it on Household. That's the sticky note's visibility, the spreadsheet's record and the reminder app's timing in one place, and it travels to wherever your phone is.

Now the part most comparison pages leave out.

Addabill doesn't pay anything for you. Ever. The text arrives, you tap the link, you pay on the biller's page the way you did before. If you read the text and set the phone down, the bill is exactly as unpaid as it was. We think that's the right design, since a calendar has no place near your money, but it means the last step is always yours.

It only knows what you add. A bill you never typed or photographed isn't late in Addabill; it's invisible, same as it would be on a sticky note you never wrote. The first evening of adding everything is real work, and nothing we do removes it.

And the Free plan holds five bills at a time. That's enough for the five that cause the trouble, and it's honest about being a limit. The house with fourteen billers needs the Household plan, at $5 a month, or it needs to choose which five matter.

####### Pick by what slips through in your house

If your bills go late because you forget they exist, the spreadsheet won't save you; you need the alarm, and any alarm helps. If they go late because you were at work when the date came, the alarm needs to be on your phone and carry the link. If they go late because the person who was supposed to pay didn't know it was their turn, the calendar needs to be shared. And if you want to know what the year cost, you need a record that fills itself in as you mark things paid.

None of these is a character flaw. They're different holes, and the right system is the one shaped like yours.

If you'd like to see how your own bills sit on a month before choosing anything, Build your month takes three of them and shows you. (Link: /builder, label "Build your month")

Pull quote (lifted from the body): "A spreadsheet is a fine record and a poor alarm."

###### Post D (the explainer)

Route slug: /blog/what-a-late-fee-costs

Headline: What a late fee actually costs, and the three days that stop it

Angle: The plain language explainer: what paying a day late really costs once you count everything the fee drags with it, and why the seventh, third and first days before a due date each have one specific job.

Theme: A late fee is the visible part of a larger cost. Behind the flat charge sit the reconnection charge, the lapsed policy, the lease clause and the hour on the phone putting it right. None of that is fixed by more willpower on the due date. It's fixed by three specific days before the due date, each with one small job: look, pay, check. Every dollar figure in this piece is an example, not a measurement.

Standfirst: A late fee looks like ten dollars. Count what comes with it and it looks different. Here's the real cost, and the three days before the due date that keep it from arriving.

Body:

Ask what a late fee costs and the honest answer starts with the fee. Ten dollars on the electric. A percent and a half on the water. Fifty on the rent after the fifth. Those numbers are real enough (they're examples, and yours will differ), and they're also the smallest part of the cost. The fee is what shows up on the statement. The rest shows up in your week.

####### The fee is the small part

Take an invented but ordinary month. The electric bill is $130 and the late fee is a flat $10. That's about 8 percent of the bill for being a day late, which is already a poor rate for one day. Suppose it goes further. A utility can suspend service after enough notices, and turning it back on usually means a reconnection charge; call it $30 as an example, plus a morning at home waiting for it. Now the ten dollar fee is a forty dollar problem with a morning attached.

Car insurance is the sharper case. Miss the payment and there may be no late fee at all, which sounds generous until you learn why. After a grace period, the policy can lapse. The cost isn't a fee. It's the days you drove without coverage, the phone call to reinstate, and a rate that may not be the one you had. No number on a statement captures that.

Rent is a clause. Say the lease reads "$50 after the 5th," as an example. The fee is fixed, and so is the awkward conversation, and neither one is worth a Thursday you could have known about.

The phone plan is the quiet one. Pay late enough and the line stops working, and the day it stops is never a convenient day. Add the charge to restore it, as an example $20, and the hour on hold.

Add up the ordinary month. Fee, reconnection, the lapse, the hour on the phone. The late fee was the headline. The story ran longer.

####### Why the due date is the wrong day to remember

Here's the thing about willpower on the due date: it's the worst day to use it. The due date is when a payment must have arrived, and some billers take a day or two to post one, which means paying on the due date can still be late by their clock. It's also a day you didn't choose. It falls on a Thursday when you're at work or a Sunday when the office is closed. Being reminded on the day is being reminded too late to do anything but hurry.

So the fix isn't more remembering. It's three earlier days, each with one small job.

####### Seven days before: look

A week out, the text arrives with the biller and the amount. The job is to read it. That's all. Is the number what you expected? Will the money be in the right place on the day? Is this the month to move the due date, or to call about the amount? A week is enough time for any of those, and it costs you fifteen seconds to check. Most weeks the answer is "yes, fine," and the text is filed. That's the point. You've looked, and now Thursday holds no surprise.

####### Three days before: pay

Three days out is the paying day, and it's the one to keep if you keep only one. It's close enough that the money is where it needs to be and far enough that a payment has time to post before the due date, even with the billers that take a day or two. The text carries the link to the biller's own page. Tap, pay on that page, come back, mark it paid. The whole thing runs shorter than reading this section. And because you've paid three days early, the due date becomes a day like any other.

####### One day before: check

The last text is a check, not a nag. If the bill is marked paid, you're done, and the text is a small confirmation that the month is holding. If it isn't marked paid, something happened: the tap got interrupted, the page timed out, the amount stopped you. The day before is the last moment to fix that without a fee. It's the day the late fee, and everything that rides with it, is still entirely avoidable.

So what does this cost you instead? Three texts a bill. Fifteen seconds on the first, a minute on the second, a glance on the third. Against an ordinary month's late fee with its passengers, it isn't close. The math isn't the persuasive part, though. The persuasive part is what the due date feels like when you've already looked, paid and checked: an ordinary Thursday.

The Free plan sends those three texts for up to five bills at no cost. Household does it for every bill the house gets and everyone in it, for $5 a month or $40 a year. Have a look at both plans. (Link: /plans, label "See the plans")

Pull quote (lifted from the body): "The late fee was the headline. The story ran longer."

* * *

##### COPY

###### Home

Hero H1: Every bill on one calendar. A text before each is due.

Hero subhead: For the household's bill keeper, and every bill that arrives by email, by app or on paper.

Primary CTA (fixed): Purchase the Household plan

Price line (fixed): $5 a month or $40 a year. No fees on your bills. Cancel any time.

Secondary link (fixed): or use the Free plan, up to 5 bills

Value props (three):

1. Heading: The paper bills stop hiding
   Copy: The dentist's statement, the lawn service, the county's yearly notice. Photograph the paper and it stands on the same month as the electric, so nothing is off the calendar just because it came through the mailbox.

2. Heading: The heads-up reaches whoever pays it
   Copy: On Household the calendar is shared with up to four other people and shows who handles each bill, and each person's texts go to their own phone. You stop being the house's reminder.

3. Heading: Pay it where you always have
   Copy: The link in each text opens that biller's own payment page. Same login you already use, same card you already pay from, and not a cent added by us.

Section under the hero loop:

Heading: Add a bill in the time it takes to open the envelope
Copy: Type the biller, the due day and the amount if you know it, or point the camera at the paper. Addabill reads the amount and the due date, sets the bill on its day, and stamps it Added. It's quicker than finding the envelope was.

How it works (home):

Heading: How Addabill works: Add, See, Heads-up, Tap

01 Add: Type the biller and its due day, or photograph the paper bill, and it's on the calendar.
02 See: Every bill stands on its day on one month, with the week ahead in a list underneath.
03 Heads-up: A text reaches your phone before each due date, with the amount and a link.
04 Tap: One tap opens that biller's own payment page. Nothing about how you pay changes.

What Addabill never does (table, five rows: statement | why):

Row 1. Never pays a bill for you | so money moves only when you move it, from the page you already use.
Row 2. Never asks to connect an account | because the calendar works from the due date, not the balance.
Row 3. Never adds a fee to a bill | the only charge from Addabill is the plan, and Free is $0.
Row 4. Never lends money or grades how you pay | it's a calendar with a text, not a verdict on you.
Row 5. Never sells, rents or shares your number for marketing | the texts are the product, and they stay between you and us.

Two plans (home):

Heading: Two plans, no fees on your bills

Free card line: One person, up to 5 bills, a text before each is due. No card, ever.
Free CTA: Use the Free plan

Household card line: Every bill the house gets, paper ones by photo, up to 5 people, and the year on one page.
Household CTA: Purchase the Household plan
Household price line: $5 a month or $40 a year

The texts you'd get this month:

Heading: The texts you'd get this month

Text 1 (water): Addabill: Water bill, $64.20, due Thu Oct 2. Tap to open your utility's payment page: [link]. Reply HELP for help, STOP to cancel.
Text 2 (electric): Addabill: Electric, $142.37, due Wed Oct 15. Tap to open your power company's payment page: [link]. Reply HELP for help, STOP to cancel.
Text 3 (rent): Addabill: Rent, $1,450.00, due Wed Oct 1. Tap to open your landlord's payment page: [link]. Reply HELP for help, STOP to cancel.
Text 4 (car insurance): Addabill: Car insurance, $148.60, due Tue Oct 21. Tap to open your insurer's payment page: [link]. Reply HELP for help, STOP to cancel.
Text 5 (phone plan): Addabill: Phone plan, $85.00, due Fri Oct 10. Tap to open your phone company's payment page: [link]. Reply HELP for help, STOP to cancel.

(All five follow the design's October, in which the 2nd is a Thursday, matching the product master. Each is under 140 characters with the [link] placeholder, leaving room for a real short link.)

Blog teaser:

Heading: Keeping the house on time
Line: Four pieces so far: gathering the bills in one evening, the trouble with autopay, the systems you've already tried, and what a late fee really costs.

Footer tagline: For whoever keeps the bills at your place.

###### Plans page

H1: Free keeps you on time. Household keeps the whole house on time.

Standfirst: Pick by how many bills the house gets and how many people pay them. The prices below are the whole price.

Free card:
Name: Free
Price line: $0. No card, no time limit.
Description: For one person who wants the handful of bills that keep catching them to stop doing that.
Inclusions (each its own line):
Up to 5 bills at one time
1 member (you)
Add bills by typing
One calendar of due dates, month and list views
Text reminders before each due date, up to 3 per bill
One tap to each biller's own payment page
Mark each bill paid
No convenience fees, no card on file, no time limit
CTA: Use the Free plan

Household card:
Name: Household
Price line: $5 a month or $40 a year
Description: For the person who keeps the bills for a whole house and would like the phone to buzz in the right pocket.
Inclusions (each its own line):
Unlimited bills
Up to 5 people (you plus 4), each with their own login
Add bills by typing or photo (paper bill or screenshot), unlimited
One shared calendar, month and list views, showing who handles each bill
Text reminders before each due date, up to 3 per bill, to each person's own number
One tap to each biller's own payment page
Mark paid, 12 months of history, yearly summary of spending by bill as a PDF
No convenience fees, renews at the same price, cancel any time
CTA (monthly): Purchase the Household plan
CTA (annual): Buy the annual plan
Note beneath the two buttons: Same plan either way. The year costs $20 less than twelve months.

"Everything in each plan" table (row | Free | Household):

Bills at one time | Up to 5 | Unlimited
People | 1 (you) | Up to 5 (you plus 4), each with their own login
Adding a bill | By typing | By typing or photo (paper bill or screenshot), unlimited
Calendar | One calendar, month and list views | One shared calendar, month and list views, showing who handles each bill
Text reminders | Up to 3 per bill, before each due date | Up to 3 per bill, to each person's own number
Link to each biller's own payment page | One tap | One tap
Marking bills paid | Yes | Yes, with 12 months of history
Yearly summary of spending by bill | No | Yes, as a PDF
Fees on your bills | None | None
Card on file | None | Only for the plan itself
Price and term | $0, no time limit | $5 a month or $40 a year, renews at the same price, cancel any time

FAQ (six):

Q1. When does Household renew, and how will I know?
A1. Monthly renews on the same date each month at $5, and annual renews once a year at $40, always at the same price you signed up at. Before an annual renewal you get a text and an email 7 days ahead, and a receipt follows every charge. If the price ever changes, you'll have 30 days notice first.

Q2. How do I cancel, and what happens to our bills?
A2. Cancel under Plan in the app in two taps, or email support@addabill.com and we'll do it. There's no cancellation fee, and the plan runs to the end of the period you've paid for. After that the household moves to the Free plan and every bill you added stays where it is; nothing is deleted. Free holds up to 5 bills at one time for one person, so the Household extras (photo capture, the shared calendar, the yearly summary) are the parts that stop.

Q3. Can I get a refund on the annual plan?
A3. Yes. If you buy the annual plan and change your mind within 14 days, email support@addabill.com and you'll get a full refund. After 14 days the plan runs its year, and you can still cancel at any point so it doesn't renew.

Q4. How does photo capture work?
A4. On Household, point the camera at a paper bill or pick a screenshot of one, and Addabill reads the amount and the due date off it. You see what it read before the bill lands, and you can change anything it got wrong. There's no limit on how many bills you add this way.

Q5. Who else can see the calendar, and who gets the texts?
A5. On Household you can add up to four other people, each with their own login, and the calendar shows who handles each bill. Each person gets their reminder texts at their own number, after agreeing to texts themselves. Everyone sees the same month, so nobody has to ask what's due.

Q6. What does "no fees on your bills" actually mean?
A6. It means the plan price is the only money you ever pay Addabill, and on Free that's nothing. When you tap through to a biller's own payment page, you're dealing with them directly; we're not part of that transaction and add nothing to it. If a biller charges its own fee for paying by card, that's between you and them, exactly as it was before.

Legal identity card:
Heading: The company behind the plan
Text: Addabill Inc., 4201 Spring Valley Rd, Dallas, TX 75244. (888) 338-9070. support@addabill.com. The same name and address appear on your receipt and in the Terms.

###### How it works page

H1: Four steps. That's the whole app.

Standfirst: Each step in more detail than the home page had room for, plus exactly what the texts say and when they arrive.

Steps expanded:

01 Add
Give the bill the name you use at home, the day of the month it's due, and the amount if you know it. That's the whole form. On the Household plan you can skip the typing and photograph the paper bill or a screenshot instead, and Addabill reads the amount and the due date off it. Either way an Added stamp appears, a short text confirms it, and the bill is on the calendar.

02 See
The month view shows every bill standing on its due day, with a Due next list underneath for the week ahead. Switch to the list view when you'd rather read down the month than across it. On Household, each bill shows who in the house handles it, so nobody has to ask. There are no charts, no scores and no totals shouting at you, just what's due and when.

03 Heads-up
Before each bill is due, a text arrives at your phone with the biller, the amount, the due date and a link to that biller's own payment page. You choose how far ahead: 7 days, 3 days and 1 day before, any or all of them. On Household, every person gets their texts at their own number, after saying yes to texts themselves. Every message ends with HELP and STOP.

04 Tap
The link in the text opens that biller's own payment page in your browser, where you sign in and pay exactly as you did last month. Addabill isn't part of that transaction and never sees the card you use there. Come back and mark the bill paid, and it gets a check on the calendar. Household keeps 12 months of that history and turns it into a yearly summary of spending by bill, as a PDF.

By typing or by photo (tabs):

Type: Name the biller the way you say it at home, add the due day, and the amount if you have it. That's the entire form, and it's the same on both plans.

Snap: On Household, point the camera at a paper bill and Addabill reads the amount and the due date off the page. Check what it read, fix anything the envelope crumpled, and it's added.

Share: Bills that never touch paper come in as screenshots. Take one in your email or the biller's app, send it to Addabill, and it reads the amount and the due date like any photo.

Reminders, exactly when:

Heading: Reminders, exactly when
Copy: Each bill gets up to three texts before it's due, and you decide which of the three days you want. Keep all of them for the bills that need managing, or just one for the bills that don't. They come as texts to your phone, not as notifications you'd swipe away, and each one carries the amount and the link. On Household, each person's texts go to their own number.

7 days before: The first text, far enough out to plan around.
3 days before: The middle text, and the default if you only want one.
1 day before: The last text, in case the bill is still open.

Anatomy of a text (labels and one line each):

Biller: The name exactly as you typed it, so "Water bill" means the one you meant.
Amount: What's due, as you entered it or as read from the paper. Nothing added to it.
Due date: The day with its weekday, because "Thu Oct 2" lands differently than "10/2".
Link: Opens that biller's own payment page. Their page, your usual login, and we're not in between.
HELP: Reply HELP and you get the support number and email straight back.
STOP: Reply STOP and the texts end on the spot. Your calendar keeps working.

Closing CTA band line: Put the first bill on its day tonight. The first text comes before you'd have thought of it.
Band CTA: Purchase the Household plan

###### Builder page (/builder)

H1: Build your month

Standfirst: Add three to five of the bills your house actually gets. Watch them land on a month, see the texts you'd receive, and find out which plan fits. Nothing you type here is kept.

Empty state line (fixed): Add the first bill your house gets. Electric is a good one.

Fields:

Biller (required). Label: Biller. Helper: As you'd say it at home. Electric, Rent, the dentist.
Amount (optional). Label: Amount, if you know it. Helper: Leave it blank and the bill still lands on its day.
Due day (required). Label: Due day of the month. Helper: The day it's due each month, 1 to 31.
Reminder lead (chips, default 3). Label: Text me before it's due. Chips: 1 day, 3 days, 7 days. Helper: 3 days is the default. In the app you can have all three.
Arrives on paper (checkbox). Label: This one arrives on paper. Helper: Paper bills go in by photo on the Household plan.
Someone else handles it (checkbox). Label: Someone else in the house handles it. Helper: On Household their heads-up goes to their phone, not yours.
Button: Add this bill

"Added" stamp text: Added
Screen reader announcement: {biller} added, due on the {day}.

Result heading (both outcomes): Your month, sorted
Summary line template: {bills} bills on the month, {reminders} texts before they're due.
Optional extension when it applies: {paper} arriving on paper, {shared} handled by someone else.

Household recommendation:
Subheading: Household fits this house
Paragraph: {reason_clause} Unlimited bills, photo capture for the paper ones and a shared calendar for the people who handle their own are the three things Free doesn't do, and your month needs at least one of them. It's $5 a month or $40 a year, and every bill you just added comes with you.
Reason clauses (the build picks the one that applies, first match wins):
More than 5 bills: You've added {bills} bills, and Free holds five at a time.
Any on paper: At least one of these arrives on paper, and photographing it needs Household.
Any shared: Someone else handles at least one of these, and their text has to reach their phone.
Dominant CTA: Purchase the Household plan (to /checkout?plan=household-monthly)
Lower weight links: or buy the annual plan, $40 a year | or use the Free plan

Free recommendation:
Subheading: Free fits, for now
Paragraph: {bills} bills, all typed, all handled by you, is exactly what Free is for, and it stays free with no card and no time limit. The day the house passes five bills, or a paper one turns up, or someone else takes over the car insurance, Household picks up where Free leaves off and every bill comes along.
Dominant CTA: Use the Free plan
Lower weight link: or purchase the Household plan, $5 a month

###### Contact page

H1: Talk to us

Standfirst: A question about a bill on your calendar, your plan, or a text you got from us. Write it below and support will answer.

Form:
Name. Label: Your name. Helper: What should we call you?
Email. Label: Email. Helper: We'll reply here.
Phone (optional). Label: Phone, if you'd like. Helper: Only if you'd rather we reply by text, or your question is about a text you received. We use it for nothing else.
Message. Label: Message. Helper: Tell us what's going on. A bill, a plan, a text, anything.
Button: Send

Address card:
Addabill Inc.
4201 Spring Valley Rd
Dallas, TX 75244
(888) 338-9070
support@addabill.com

Hours line: Support answers within one business day, by email, or by text if you gave us a number and asked for that.

###### Checkout

H1: Your Household plan

Sticky summary labels:
Plan: Household, monthly (or: Household, annual)
Price: $5 a month (or: $40 a year)
Renews: On this date each month, same price (or: In a year, same price, with a text and an email 7 days before)
Fees on your bills: None

Fieldset headings: Contact | Billing address | Payment

Phone field reason (fixed): for your receipt and your account texts

Place order button: Place order

Guest checkout line: No account needed. Pay for the plan, get your receipt, and we'll offer you a login afterward if you want one.

Error messages (GOV.UK pattern, one plain sentence each):
Required field empty: Enter your {field name}. (Examples: Enter your full name. Enter your email address. Enter your phone number. Enter your street address. Enter your city. Enter your state. Enter your ZIP code. Enter the name on the card. Enter the card number. Enter the card's expiry date. Enter the card's security code.)
Invalid email: Enter an email address in the correct format, like name@example.com.
Invalid card number: Enter the card number as it appears on your card, digits only.
Expired card: The card's expiry date must be in the future.
Invalid postal code: Enter a ZIP code in the correct format, like 75244.

###### Confirmation

H1: Sorted. Your Household plan starts now.

Paragraph: Thanks for buying the Household plan. Your receipt is on its way by email and by text to the number on your order, and the plan is attached to that email from this minute. Open the Addabill app, add the first bill the house gets, and its heads-up is on the calendar before you've set the phone down.

What happens next (three timeline items):
1. Now: your receipt. By email, and by text to the number on your order.
2. As soon as you add a bill: the first heads-up. Seven days before it's due, or whichever lead you chose.
3. Next month: the renewal. $5 on this date, same price, cancel any time. (Annual variant: In a year: the renewal. $40, same price, with a text and an email 7 days before.)

Account offer (only here, optional): If you'd like a login for this site as well as the app, set one up now with the email from your order. It's optional, and the plan is yours either way.

App CTA: Open Addabill

###### Blog index

H1: Keeping the house on time

Standfirst: Short pieces about the unglamorous part of running a house: what's due, when, and how not to find out from the fee. Written for whoever keeps the bills, whether or not they wanted the job.

###### Terms and Privacy

Terms page H1: Terms of Service
Privacy page H1: Privacy Policy

###### 404 page

H1: This page isn't on the calendar.
Line: Nothing's due here. Head home, or have a look at the plans.

###### Alt text

Photography (11):
1. Home: A small paper calendar page for October held to a fridge door by one round magnet, in soft morning light.
2. Plans: Two coffee mugs on a kitchen counter with a single paper bill lying between them.
3. Confirmation: A phone lying face down on a counter beside a set of house keys in low evening light.
4. How it works: A hand holding a phone above a paper bill on the counter, the Addabill photo capture screen framing the bill.
5. About: Household mail sorted into three small stacks on a kitchen counter beside a window.
6. Blog index: A wall calendar hanging in a kitchen, seen from across the room, with a pencil on a string beside it.
7. Post A: A kitchen table in the evening with a closed laptop, a fan of paper bills and a mug.
8. Post B: A pile of envelopes on a counter with one window envelope on top, lit by hard light from the side.
9. Post C: Several sticky notes on a fridge door with their corners curling, photographed up close.
10. Post D: A close view of a wall calendar with three pencil ticks on the days before a circled date.
11. Contact: A hand holding a phone that shows a text reminder from Addabill about a water bill due Thursday.

Product shots (6):
1. Calendar month view: The Addabill October calendar on a phone, bill tags standing on their due dates and the water bill card open showing $64.20 due Thursday October 2.
2. Bills list: The Addabill Bills list on a phone, each row showing a biller, its amount, its due date, a paid check and an arrow to open the payment page.
3. Add a bill sheet: The Add a bill sheet in the Addabill app, with fields for the biller, the amount, the due day and the reminder days.
4. Photo capture: The Addabill photo capture screen framing a paper bill, with the amount and due date it read shown for checking.
5. Household members: The Household screen in the Addabill app listing five members by their initials, with the bills each one handles.
6. Yearly summary card: The Addabill yearly summary card showing twelve months of spending by biller, with a button to save it as a PDF.

* * *

##### SELF EDIT CHECKLIST

Confirmed against site_content_engine.md after the machine scan:

1. Zero dashes used as punctuation. Scanned for the long dash character, the short dash character, the spaced double hyphen and the spaced single hyphen: every count is zero. The only hyphens in the file sit inside the brand term "heads-up", the route slugs, the phone number and the query string household-monthly.
2. No banned words or phrases. Scanned against the full kill list in site_content_engine.md and the avoid list in humanized_writing.md, including the mirror constructions and the stacked transitions: zero hits. Scanned against the brand's refused list from the research brief and the orchestrator's instruction, including the two nouns that describe the account login item and the lending item: zero hits in copy.
3. Sentence length varies hard. Every piece mixes long sentences with two, three and four word ones ("Ever.", "That's all.", "Ten minutes.", "Not in an app.") and a few deliberate fragments.
4. Every article has a point of view and a real takeaway. Body word counts excluding subheads: Post A 853, Post B 827, Post C 937, Post D 815. Subheads: five in each post. Each post ends with one internal CTA (A and C to /builder, B and D to /plans).
5. The About reads as this brand only: the dentist statement on paper, the phone plan drafted two days before payday, WATER 2ND behind the toaster, a company that says it is new. 575 words, fully written, no founders named.
6. Every claim is supported by the research brief and the Offering Spec. Prices ($5 a month, $40 a year, $20 less than twelve months, Free up to 5 bills), inclusions (copied line for line), renewal (same price, text and email 7 days before annual), cancellation (two taps under Plan or email support, runs to period end, moves to Free, bills stay, no fee), the 14 day annual refund and 30 days notice of price changes all match. Dollar figures in Post D are labeled as examples. No customers, testimonials, counts, ratings, press, partners, certifications or team members appear anywhere.
7. Read aloud. Nothing in it should make a careful reader think a machine wrote it, and the single narrator (the warm host) holds from the hero to the 404.
8. Brief rules held: Addabill is never said or implied to pay bills, process payments, hold money or move funds; the no fees statement appears plainly; no lending or scoring topics; the legal identity (Addabill Inc., 4201 Spring Valley Rd, Dallas, TX 75244, (888) 338-9070, support@addabill.com) matches the brief exactly; no vocabulary that could be read as ADAPTABILL's.
9. No redundancy across pages: the hero states what it is; the value props state three outcomes the hero did not; the envelope section is about speed of adding; How it works on the home page is four captions and the How it works page adds the form, the views, the timings and the anatomy of a text; About carries the belief and the moment; Plans carries who each plan is for and the terms; each blog post owns its examples (A: propane, the trash service, renters insurance, the inbox search; B: rent on payday, summer electric, the promotional rate; C: CAR INS, the spreadsheet column, "Pay electric" between "buy milk" and "call Mom"; D: the $10 fee on $130, the lapse, the lease clause, the reconnection charge). No value proposition sentence is reused between pages.

## 8. Full Legal Page Content

The complete text of both generated documents (Addabill_TOS.docx and Addabill_Privacy_Policy.docx), rendered at /terms-of-service and /privacy-policy. "[INSERT SHORT CODE]" stays as is.

### 8.1 Terms of Service

**Terms of Service**

Addabill Inc.

*Welcome to Addabill. These Terms of Service (\"Terms\") govern your
access to and use of the addabill.com website and the resources and
services made available through it (collectively, the \"Services\"),
operated by Addabill Inc. (\"Addabill,\" \"we,\" \"us,\" or \"our\"). By
accessing or using the Services, you acknowledge that you have read,
understood, and agree to be bound by these Terms. If you do not agree,
please discontinue use of the Services.*

1\. Company Information

**Company:** Addabill Inc.

**Mailing Address:** 4201 Spring Valley Rd, Dallas, TX 75244

**Phone:** (888) 338-9070

**Email:** support@addabill.com

2\. Nature of Services

Addabill Inc. provides a consumer household bill organizing application,
available at addabill.com and as the Addabill app, that lets users
record the household bills they receive and their due dates, view every
bill on one due date calendar, receive reminders before each due date,
and open a link to each biller\'s own payment page or contact
information when it is time to pay. Addabill does not process payments,
hold or transmit funds, connect to any bank, card or other financial
account, or charge fees on any bill. Payments are made directly between
the user and the biller under that biller\'s own terms.

The Service is offered as a Free plan (one member, up to 5 bills at one
time, typed entry, the due date calendar and text reminders) and a paid
Household plan sold as a subscription at \$5 a month or \$40 a year
(unlimited bills, photo capture of paper bills, shared access for up to
5 people, 12 months of history and a yearly summary of spending by
bill). The Household plan renews automatically at the same price until
canceled; it can be canceled at any time from the app or by emailing
support@addabill.com, the plan then runs to the end of the period
already paid for, and annual plans are refundable in full within 14 days
of purchase. The Services also include customer support and an optional
SMS program for account notifications such as due date reminders, bill
added and updated confirmations, verification codes and subscription
billing notices.

3\. Reminders, Due Dates and Plan Information Disclaimer

Addabill is an organizing tool. Reminders and the due date calendar are
based on the bill information you enter or that we read from an image
you upload, and they can be delayed, missed or inaccurate because of
carrier outages, device settings or errors in that information. You
remain solely responsible for paying your bills on time and in the
correct amount, and Addabill is not liable for late fees, service
interruptions, collection activity or any other consequence of a missed
or incorrect payment. Nothing in the Services is financial, legal or tax
advice.

We make every effort to describe the Free plan, the Household plan,
their inclusions and their prices accurately, but we do not warrant that
plan descriptions or pricing are error free. In the event of a pricing
or description error we reserve the right to correct it and to cancel
any affected order, and we will give at least 30 days notice before any
change to the price of a plan you already hold.

4\. Eligibility and Acceptable Use

You must be at least 18 years of age, or the age of majority in your
jurisdiction, to use the Services. By using the Services, you represent
that you meet this requirement and that any information you provide is
accurate and current.

You agree to use the Services only for lawful purposes and in a manner
that does not infringe the rights of, or restrict or inhibit the use of,
the Services by any third party. You agree not to attempt to gain
unauthorized access to any portion of the Services, disrupt their
operation, or use them to transmit harmful or unlawful content.

5\. Intellectual Property

All content on the Services, including text, graphics, logos, icons,
images, and the compilation thereof, is the property of Addabill Inc. or
its content suppliers and is protected by applicable intellectual
property laws. The Addabill name and logo are marks of the Company. You
may not reproduce, distribute, modify, or create derivative works from
any content without our prior written permission.

6\. Third-Party Content and Links

The Services may reference, summarize, or link to third-party content,
products, and websites for convenience and informational purposes. Such
references do not constitute endorsement, and we are not responsible for
the accuracy, availability, or content of third-party materials. Your
interactions with any third party are solely between you and that party.

7\. SMS Messaging: Promotional Marketing Only

Addabill Inc. operates an SMS messaging program strictly for promotional
marketing purposes. By enrolling in this program, you acknowledge and
agree to the following terms:

-   **Program Description:** By opting in, you consent to receive
    recurring automated promotional marketing text messages from
    Addabill at the mobile number you provide. Consent to receive
    marketing text messages is not a condition of any purchase.

-   **Message Frequency:** Message frequency varies.

-   **Message and Data Rates:** Message and data rates may apply.

-   **Opting Out and Help:** You may opt out of the SMS program at any
    time by texting the keyword STOP to \[INSERT SHORT CODE\]. After you
    send STOP, we will send a one-time message confirming that you have
    been unsubscribed, and no further messages will be sent. For
    assistance, text the keyword HELP to \[INSERT SHORT CODE\], or
    contact us at support@addabill.com or (888) 338-9070.

-   **Supported Carriers:** Supported carriers include AT&T, T-Mobile,
    Metro PCS, Verizon Wireless, US Cellular, Google Voice, Cellular
    One, Cellcom, Cellular South, Interop, and Clearsky. Carriers are
    not liable for delayed or undelivered messages.

-   **Privacy:** No mobile information will be shared with third parties
    or affiliates for marketing or promotional purposes. Information
    sharing with subcontractors in support services, such as customer
    service, is permitted. All other use case categories exclude text
    messaging originator opt-in data and consent; this information will
    not be shared with any third parties.

8\. Disclaimer of Warranties

The Services are provided on an \"as is\" and \"as available\" basis
without warranties of any kind, whether express or implied, including
but not limited to implied warranties of merchantability, fitness for a
particular purpose, and non-infringement. We do not warrant that the
Services will be uninterrupted, error-free, or free of harmful
components, or that any information provided is complete, accurate, or
current.

9\. Limitation of Liability

To the fullest extent permitted by law, Addabill Inc. and its officers,
directors, employees, and agents shall not be liable for any indirect,
incidental, special, consequential, or punitive damages, or any loss
arising from your access to, use of, or inability to use the Services,
or reliance on any information provided through them, even if advised of
the possibility of such damages.

10\. Indemnification

You agree to indemnify and hold harmless Addabill Inc. and its
affiliates from and against any claims, liabilities, damages, losses,
and expenses, including reasonable legal fees, arising out of or in any
way connected with your use of the Services or your violation of these
Terms.

11\. Governing Law

These Terms are governed by and construed in accordance with the laws of
the State of Texas, without regard to its conflict of law provisions.
Any disputes arising under these Terms shall be subject to the exclusive
jurisdiction of the courts located in Texas.

12\. Changes to These Terms

We may update these Terms from time to time to reflect changes in our
Services or applicable law. The current version will always be posted on
this page, and your continued use of the Services after any update
constitutes acceptance of the revised Terms.

13\. Contact Information

If you have questions about these Terms, please contact us:

**Company:** Addabill Inc.

**Phone:** (888) 338-9070

**Email:** support@addabill.com

**Address:** 4201 Spring Valley Rd, Dallas, TX 75244

### 8.2 Privacy Policy

**Privacy Policy**

Addabill Inc.

*Addabill Inc. (\"Addabill,\" \"we,\" \"us,\" or \"our\") respects your
privacy and is committed to protecting the personal information you
share with us. This Privacy Policy explains what information we collect
through addabill.com (the \"Services\"), how we use and protect it, and
the choices available to you.*

Company Information

**Company:** Addabill Inc.

**Address:** 4201 Spring Valley Rd, Dallas, TX 75244

**Phone:** (888) 338-9070

**Email:** support@addabill.com

1\. Information We Collect

We collect information you provide directly to us, such as your name,
email address, and mobile phone number when you contact us, submit a
form, or opt in to our SMS program. We also automatically collect
limited technical information, such as device type, browser, and usage
data, when you interact with the Services.

2\. How We Use Your Information

We use the information we collect to operate and improve the Services,
respond to your inquiries, deliver the updates and SMS messages you
request, maintain the security and integrity of the Services, and comply
with legal obligations.

3\. How We Share Your Information

We do not sell your personal information. We may share information with
trusted service providers who perform functions on our behalf (such as
hosting, analytics, and customer support), and only to the extent
necessary for them to provide those services. We may also disclose
information when required by law or to protect our rights and the safety
of others.

4\. SMS Messaging and Mobile Data

When you opt in to our SMS program, we collect your mobile phone number
and your consent records in order to deliver the text messages you have
requested. The categories of information collected through the SMS
program are used solely to operate the program and send the messages you
signed up to receive.

No mobile information will be shared with third parties or affiliates
for marketing or promotional purposes. Information sharing with
subcontractors in support services, such as customer service, is
permitted. All other use case categories exclude text messaging
originator opt-in data and consent; this information will not be shared
with any third parties.

You may cancel SMS messages at any time by replying STOP, and you may
request help by replying HELP. Message frequency varies, and message and
data rates may apply.

5\. Cookies and Tracking Technologies

The Services may use cookies and similar technologies to remember your
preferences, understand how the Services are used, and improve your
experience. You can control cookies through your browser settings,
although disabling them may affect certain features.

6\. Data Security

We implement reasonable administrative, technical, and physical
safeguards designed to protect your information. However, no method of
transmission or storage is completely secure, and we cannot guarantee
absolute security.

7\. Data Retention

We retain personal information only for as long as necessary to fulfill
the purposes described in this Policy, to comply with our legal
obligations, resolve disputes, and enforce our agreements.

8\. Your Privacy Rights and Choices

Depending on your jurisdiction, you may have the right to access,
correct, or delete your personal information, or to object to or
restrict certain processing. To exercise these rights, contact us using
the details below. You may also opt out of SMS messages at any time by
replying STOP.

9\. Children\'s Privacy

The Services are intended for individuals who are at least 18 years of
age. We do not knowingly collect personal information from children. If
you believe a child has provided us with personal information, please
contact us so we can take appropriate action.

10\. Third-Party Links

The Services may contain links to third-party websites. We are not
responsible for the privacy practices or content of those sites, and we
encourage you to review their privacy policies.

11\. Changes to This Privacy Policy

We may update this Privacy Policy from time to time. The most current
version will always be available on this page, and your continued use of
the Services indicates your acceptance of any changes.

12\. Contact Us

If you have questions or requests regarding this Privacy Policy or your
personal information, please contact us:

**Company:** Addabill Inc.

**Phone:** (888) 338-9070

**Email:** support@addabill.com

**Address:** 4201 Spring Valley Rd, Dallas, TX 75244

## 9. SMS Program and Sample Messages

Program name: Addabill alerts (the web opt-in list, a promotional marketing program per the Terms Section 7, decision 4A on 2026-09-23). Messages may include plan news and offers alongside account notices such as due date reminders for bills the person added, bill added and updated confirmations, verification codes and subscription billing notices. Message frequency varies. Message and data rates may apply. Consent is a real unchecked checkbox, never bundled, never a condition of purchase or account. STOP stops every message; HELP returns real contact information. Mobile information is never shared with or sold to third parties or affiliates for marketing.

- **Opt-in confirmation:** Addabill: You're subscribed to Addabill alerts. Msg frequency varies. Msg&data rates may apply. Reply HELP for help, STOP to cancel.
- **HELP:** Addabill alerts: for help, call (888) 338-9070 or email support@addabill.com. Msg&data rates may apply. Reply STOP to cancel.
- **STOP:** You've been unsubscribed from Addabill and will receive no further messages. Reply START to rejoin.
- **Sample 1 (due date reminder):** Addabill: Water bill, $64.20, due Thu Oct 2. Tap to open your utility's payment page: [link]. Reply HELP for help, STOP to cancel.
- **Sample 2 (plan offer):** Addabill: The annual Household plan is $40 for the year, $20 less than monthly. Switch under Plan in the app: [link]. Reply HELP for help, STOP to cancel.
- **Sample 3 (plan renewal notice):** Addabill: Household plan renews Oct 20, $40 for the year. Change or cancel under Plan in the app. Reply HELP for help, STOP to cancel.

## 10. Pre-Launch Compliance QA Checklist

- [ ] The purchase path works end to end with explicit CTAs: Purchase the Household plan → checkout → Place order → confirmation, monthly and annual, with no account created; the Free path completes at $0 with no card fields shown.
- [ ] Every cost is visible before checkout begins (price, renewal cadence and price, no fees, the 14 day annual refund, cancel any time) and nothing appears for the first time inside the checkout.
- [ ] Footer and Contact show Addabill Inc., 4201 Spring Valley Rd, Dallas, TX 75244, (888) 338-9070, support@addabill.com on every page; the name, address, phone and email match the Terms and Privacy exactly.
- [ ] Terms of Service and Privacy Policy are live at their routes, linked from the footer, the SMS block and the checkout, with the verbatim SMS section (carrier list, "[INSERT SHORT CODE]" twice) and the verbatim no-sharing clause; a reminder to fill "[INSERT SHORT CODE]" before vetting is in the handoff.
- [ ] The verbatim "Join Our SMS List" block is on every page with only brand, phone, email and links swapped, both checkboxes unchecked by default, consent text ending "Read our Terms and Privacy Policy".
- [ ] No testimonials, ratings, user counts, press logos, partner logos, security badges, founders or team bios anywhere; "As Seen In" and social links omitted because none exist.
- [ ] No refused words (bank, banking, payment processor, money transmitter, advisor, pay through us, instant payments, financial freedom, never worry again, bank-grade, guaranteed, crushing debt) and no references to loans, credit, credit scores, deferral or debt relief anywhere in rendered copy, alt text, titles or metadata; "no fees on your bills" stated plainly.
- [ ] No template leftovers, lorem, internal notes, demo text, cut off or overflowing text, broken links or dropdowns; the site is indexable; desktop and 375px both on brand.
- [ ] No dashes used as punctuation anywhere in rendered copy (the verbatim legal and SMS blocks excepted).
- [ ] The product imagery is one shell across every shot, built in HTML from the brand tokens, the Addabill wordmark in the app's own header bar, text legible, no charts or scores or invoice vocabulary; every media slot in ASSET_PLAN.json is a real file, no placeholder or gray box or hotlink; the hero loop wraps cleanly with no watermark; four to six photographs minimum, at least one per page and per post, none repeating a video frame, each reverse image searched.
- [ ] Every blog post opens a real, fully written page at its own route (750+ words), no card 404s.
- [ ] The interactive builder works: 3 typed bills give a Free result, 6 bills or one on paper or one shared give a Household result, keyboard only and at 375px, ending in a purchase CTA.
- [ ] Distinct identity: The Standing Month archetype and signature, Fraunces plus Figtree, cream and graphite with one marigold, the flip calendar loader, the paper tag button, the calendar header; all 17 novelty quotas re-checked at Gate 5 against the registry; nothing reads as BioVirtua, Astroquanta or Smart Augment.
- [ ] Total motion: every page has its own scroll scene, text hover treatment and per section entrances per Section 5; every button, word and clickable moves; the named motion signature drives everything; the Settled Numeral set piece is built; the mobile hero is the designed week strip; reduced motion paths work.
- [ ] Measured budgets pass: LCP under 2.5s, CLS under 0.1, initial JS under 350KB gzipped excluding the lazy Three.js bundle, 55fps or better through the signature scroll, signature scroll 1.25 to 1.75 viewport heights, asset weight within budget.
- [ ] WebAIM six pass on every page; WCAG AA contrast; keyboard and focus visible everywhere; forms submit on Enter; the back button works; scrolling is never hijacked.
- [ ] Comprehension: a person answers "what is this, who is it for, what do I do next" from the first viewport alone on desktop and at 375px (Step 7.5 human gate), and completes a purchase unaided.
- [ ] Three or more rounds of post build QA run to 100 percent, then the live click through on the webflow.io URL is 100 percent green, then the registry entry and hero screenshot are written.
