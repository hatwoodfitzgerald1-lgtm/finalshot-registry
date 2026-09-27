# SaveBrew Website Design Document

SaveBrew (savebrew.com). Legal entity SaveBrew Inc. Finance vertical. Finalshot Step 5, the design document, assembled Thursday, September 24, 2026 from the run's research, offering, art direction, copy, legal and asset outputs. This file is the single source of truth the build agent codes from. Nothing in it is a summary of an input: the Offering Spec's products, the whole Art Direction and Technique Stack spec, the copy, the four guides, the Roundup, the brief items, the ranker data and the two legal documents are embedded verbatim.

## Run facts

| Fact | Value |
|---|---|
| Brand, display name | SaveBrew (one word, capital S and B; not "Save Brew", not "SaveOnBrew") |
| Legal entity | SaveBrew Inc. |
| Vertical | Finance: a paid daily savings digest with a member dashboard |
| Domain | savebrew.com. Parked at Afternic (GoDaddy aftermarket) at the time of the run. The custom domain is NOT attached at deploy; the site ships to a webflow.io staging URL and the domain is attached later, deliberately, after review. |
| Brand history | Net new. No readable prior site, no press, no profiles, no continuity claim to the April 2022 Wayback capture. No founding year is stated anywhere on the site. |
| Public physical address (footer and Contact) | 660 American Ave, King Of Prussia, PA 19406. This is the real Physical Address from the Brand Tracker, so no [Physical Address] placeholder is used on this site. |
| Phone | (888) 338-8809 in the NAP record, the verbatim SMS block and the legal pages. Written (888) 338 8809 with spaces in all other customer facing copy (the copy step's convention, matching the dashboard's "(555) 010 0123" pattern). href tel:+18883388809 everywhere. |
| Support email | support@savebrew.com |
| EIN / registered address | Unknown at the time of the run. The Terms of Service and the Privacy Policy carry the literal placeholder [EIN Address] until the owner supplies it. It appears on /terms and /privacy only, and nowhere else. |
| Short code | [INSERT SHORT CODE], kept literally in the Terms until the code is leased. |
| Press | None qualifying (research brief section 4). The "As Seen In" section is omitted because nothing qualifying exists, per the guardrails. No outlet logos anywhere. |
| Social links | None brand owned (research brief section 5). Social icons and links are omitted because nothing qualifying exists. No dead handles. |
| Testimonials and ratings | None exist. Omitted because nothing qualifying exists; no candour substitute either (see the anti sameness rule). |
| Owner decisions | The finalshot standard verbatim "Join Our SMS List" block is used as the kit gives it (the brief's account notifications purpose shapes the surrounding copy, the dashboard's Texts card and the Terms' nature of services, but the block itself is the kit's verbatim text). Free content ships as public pages with no account and no email capture. SaveBrew Daily for Two ships as the second product. Build Tier 1. Higgsfield MCP is the generator for the video and photography slots. |
| Two run rules | THE ANTI SAMENESS RULE (section 3.2) and THE FULL WIDTH RULE (section 3.3). Both are named, testable requirements and both are cited in the QA checklist (section 10). |
| Engine profile | Baseline Three.js r128 from cdnjs, one WebGL context per page, no shader pipeline (Tier 1). |
| Deploy target | Astro with `output: 'server'` and the Webflow Cloud adapter, a server rendered catch all, assets under /public/assets, pushed to a fresh GitHub repo `savebrew-site` (suffix `-v2` on collision) and built by Webflow Cloud in Harlem's Workspace to a webflow.io URL. |

## The ten sections

1. How to build this site
2. Brand Snapshot and History Alignment
3. Carrier Compliance Mandates (with THE ANTI SAMENESS RULE at 3.2 and THE FULL WIDTH RULE at 3.3)
4. Product and Service Offering (the consumer use case)
5. Design System (the Art Direction and Technique Stack spec verbatim, the asset slots, the Media Direction reference)
6. Global Elements
7. Page by Page Specification (twenty three routes)
8. Full Legal Page Content
9. SMS Program and Sample Messages
10. Pre Launch Compliance QA Checklist

Embedded verbatim material (the Offering Spec sections, the Art Direction spec, the copy files, the legal text) keeps its own headings and is fenced with [[VERBATIM BEGIN]] and [[VERBATIM END]] markers or introduced by a subsection title naming its source, so a heading inside a fence belongs to the embedded document, not to this outline.

## Inputs embedded in this document

| Input | Path | Where it lands here |
|---|---|---|
| Research brief | /home/claude/savebrew/research/research_brief.md | Sections 2 and 3 |
| Offering Spec | /home/claude/savebrew/spec/offering_spec.md | Section 4 (products, inclusions, descriptions, CTAs, buy flow, product visual spec), section 3 (compliance screen), section 9 (SMS tie in) |
| Art Direction and Technique Stack spec | /home/claude/savebrew/spec/art_direction_spec.md | Section 5, the whole file verbatim |
| Marketing copy and site strings | /home/claude/savebrew/spec/copy/copy.md | Sections 6, 7, 9; strings quoted by id |
| About copy | /home/claude/savebrew/spec/copy/about.md | Section 7, /about |
| The Weekly Roundup | /home/claude/savebrew/spec/copy/roundup.md | Section 7, /roundup |
| Brief items (today, yesterday, last week, this week so far) | /home/claude/savebrew/spec/copy/brief_items.md | Section 7, /, /brief, /today, /archive |
| Ranker candidates | /home/claude/savebrew/spec/copy/moves.json | Section 7, /your-moves |
| The four guides | /home/claude/savebrew/spec/copy/guides/*.md | Section 7, /guides/slug |
| Asset plan | /home/claude/savebrew/assets/ASSET_PLAN.json | Section 5.2 |
| Product UI brief | /home/claude/savebrew/research/product_ui_brief.md | Section 4.11 (Parts B and C) |
| Terms of Service and Privacy Policy | /home/claude/savebrew/legal/SaveBrew_TOS.docx, SaveBrew_Privacy_Policy.docx | Section 8, complete text |
| Exclusion brief | /home/claude/savebrew/exclusion/exclusion_brief.md | Section 3.2 (sections 3 and 4) and section 10 |

## Conventions in this document

- No em dash, no en dash and no hyphen used as punctuation appears anywhere in this document, except inside the verbatim legal text (section 8), the verbatim SMS block, URL slugs, file paths, CSS custom properties, autocomplete tokens, technique ids and cubic bezier values, which are code, not prose.
- Copy strings are quoted by their copy.md id in backticks followed by the string itself, so the builder pastes the string, not the id. A string marked `add.` is microcopy this document adds because copy.md has no string for that state; it is written in the same voice and obeys the same vocabulary rules.
- Where the Offering Spec and copy.md differ in wording for the same customer facing line (the copy manifest documents each departure: item 6 of the inclusions, item 11, the Thursday date, "the list reranks", the question form of the /brief members' heading, the spaced phone number), copy.md is the shipped string and the Offering Spec is the record of what is sold.
- The refused vocabulary of Offering Spec section 16 and Art Direction 3.24 governs shipped, customer facing text. This document's own build instructions use ordinary words such as row, page and route in their technical sense; those instructions are not shipped text. Anything the builder renders comes from a quoted string, a verbatim file, or an `add.` string, all of which are checked.
- Today, for each dated string, is Thursday, September 24, 2026. The brief shown was published 6:30 AM ET. This week's Roundup is dated Saturday, September 19, 2026. Last week's pass ran Monday, September 14 to Friday, September 18. The illustrative member is Jordan, initials JM, "Member since 2026".

## 1. How to build this site

Build the site directly from this document as the single source of truth, following the contract in /home/claude/savebrew/spec/BUILD_DIRECTIVE.md. There is no live site to pull anything from: savebrew.com is a parking page, so the logo, the wordmark, the graphic kit and all imagery come from the run's own assets (/home/claude/savebrew/assets/brand-kit, /home/claude/savebrew/assets/kit-svg, /home/claude/savebrew/assets/product-ui and the slots in ASSET_PLAN.json), not from the parked domain and not from saveonbrew.com. Build the pages exactly as section 7 specifies them, with the copy pasted word for word, the Design System of section 5 implemented as real tokens, the signature loom and the twelve techniques built with the named libraries, the complete guest checkout, the demo dashboard behind the demo sign in, the two legal pages from section 8, and the verbatim SMS block from section 6. Preview it, then run the QA loop of section 10 until each item passes.

## 2. Brand Snapshot and History Alignment

SaveBrew has no past to align with, and the site says so rather than inventing one. The research (research brief, section 3) found that savebrew.com was registered on October 22, 2022 by the current registrant, sat in an aftermarket portfolio, and still redirects to a GoDaddy for sale page. The one Wayback capture (April 3, 2022) predates that registration and belongs to someone else. Ahrefs shows a Domain Rating of 0, no organic traffic in any year, and about 800 referring domains that are all link farm spam accumulated against a parked domain since July 2024. There is no press, no Crunchbase profile, no social handle in the brand's name, and no legacy URL to preserve. The only public "SaveBrew" footprint belongs to a different company, SaveOnBrew of Houston, a beer price search engine turned homebrewing affiliate site, whose search results will outrank the brand until it builds its own.

What SaveBrew is now is therefore the whole story. SaveBrew Inc., at 660 American Ave in King of Prussia, Pennsylvania, publishes SaveBrew Daily: five short money moves on a member dashboard by 6:30 AM Eastern each weekday, pulled from the savings rates, cashback windows, coupon codes, seasonal prices and paycheck habits the editors checked overnight. The brew is money, not coffee or beer, and the hero and the meta description say so in the first line because of the name collision. The paid product is a membership at $7.99 billed monthly or $72 billed yearly (proposed), with a two reader version at $11.98 or $108. The Weekly Roundup, the Guides and the "Your moves" ranker are free to read with no account and no email form. The market context that shapes the copy is dated and attributed: the FOMC raised its target range to 3.75 to 4.00 percent on September 16, 2026; the FDIC national average savings rate is 0.37 percent for September 2026; competitive high yield accounts cluster between 3.80 and 4.21 percent as of September 23 and 24, 2026.

The through line is the name itself: what is brewing in savings rates, cashback cycles and seasonal prices each morning, poured into one short brief. The About page states plainly that SaveBrew is a new publication with no heritage to tell. The positioning that shapes the offer is the answer to the number one complaint about finance newsletters found in the research (recycled content, affiliate bias, generic advice, overload): a short brief someone actually checked, cut to five items, with the arithmetic done on an illustrative balance. The "no referral fees" line ships only if the owner confirms it is true.

Current positioning in one line: SaveBrew Daily is five short money moves on your dashboard by 6:30 each weekday morning, pulled from the savings rates, cashback windows, coupon codes, seasonal prices and paycheck habits that someone here checked overnight, for $7.99 a month.

## 3. Carrier Compliance Mandates (non negotiable, build to these)

The site is a vetting artifact for a leased SMS short code (compliance.md). Each line below is pass or fail.

- **A real purchasable consumer use case with explicit purchase CTAs and a working guest checkout.** The visitor buys a SaveBrew Daily membership on the site at a visible price. The primary CTA on the hero, on both membership cards, in the nav and at the end of the ranker is "Add the Daily to my cart" (or its cadence and product variants from Offering Spec section 8). Cart, checkout and confirmation work end to end with no account step. Not lead capture; no "Get in Touch", "Learn More", "Get Started" or "Sign Up" as a primary action anywhere; no free signup form anywhere, not even in the footer.
- **Verifiable business identity.** SaveBrew Inc. is the entity named on the site and it matches the entity being vetted. The footer and the Contact page carry the public physical address 660 American Ave, King Of Prussia, PA 19406, the phone (888) 338 8809 and support@savebrew.com. The name and phone are identical site wide. The EIN / registered address appears only on /terms and /privacy as [EIN Address] until supplied; it is not in the footer and the footer address is not blank.
- **Privacy Policy and Terms live and linked** in the footer, from the SMS opt in block and from the checkout's age and terms box, at /terms and /privacy, rendered from the complete text in section 8, including the SMS section with [INSERT SHORT CODE] and the verbatim no sharing clauses.
- **The verbatim "Join Our SMS List" block** (section 6.3) present on the site: on Home as its own row, on the order confirmation as a separate optional step, and inside the dashboard's Texts card when texts are off. Only the brand name, phone, support email and the two links are substituted. Both consent checkboxes unchecked by default. The consent text ends "Read our Terms and Privacy Policy". One opt in maps to one program; the checkout carries no SMS consent.
- **No recycled template content, no off category content, desktop and mobile both on brand.** No lorem, no placeholder text other than [EIN Address] and [INSERT SHORT CODE], no internal notes, no leftover parking page material, nothing from saveonbrew.com.
- **Trust elements real or absent.** No testimonials (none exist), no press (none exists), no ratings, no social icons, no stock avatars. No candour device substituting for them. The "no referral fees" line ships only on the owner's confirmation.
- **Educational only, finance vertical care.** The disclaimer below runs on each content page (the brief, the Roundup, each guide, the Rate Tracker, the Goals view, the archive, the ranker), visible without scrolling on /brief and above the fold on the guides. No advice, no lending, no investment management, no product sales, no "we move your money" feature anywhere.
- **No deceptive design** (compliance.md, prohibited section): no fabricated scarcity or urgency, no countdown, no confirmshaming, no hidden cost, no preselected option, no retention wall on cancellation, no trick wording on any consent control. Cancellation is two clicks from the dashboard and is honoured by email.
- **THE ANTI SAMENESS RULE** (3.2) and **THE FULL WIDTH RULE** (3.3) are build mandates of this run, verified by screenshot.

The disclaimer, verbatim (copy.md `disclaimer.text`):

> SaveBrew is an educational digest, not financial advice. We are not a bank, a lender, a broker or a registered investment adviser, and we do not hold, move or manage money. Rates and offers come from public sources on the date shown and change without notice, so confirm them with the institution before you act. What you save depends on your own choices.

### 3.1 The Offering Spec's compliance screen, verbatim

## 12. COMPLIANCE SCREEN

The quick screen: (1) a visitor can buy on the site right now at a visible price, yes; (2) the primary action is a purchase, yes ("Add the Daily to my cart" on the hero, every card, the nav and the interactive page); (3) clear of prohibited verticals, yes: no lending, no gambling, no investments, no lead generation, no "get matched", no affiliate marketplace.

Finance vertical care, applied:
- Educational only. SaveBrew publishes information about published rates and public offers and frameworks. It does not recommend that any individual open, close or move an account. Copy avoids "you should" in the second person about money moves and prefers "worth comparing", "the maths on a $10,000 balance".
- No APY or savings guarantees. Any APY on the marketing site is dated and attributed or clearly illustrative. Dashboard figures derived from the member's own inputs are labelled "about" and framed as arithmetic on published rates, never as money SaveBrew earned or saved for the member. The phrases "estimated extra earned", "we saved you", "guaranteed", "you will save" do not appear.
- No income claims. No "members save $X a year" statistic unless the owner has real, dated data behind it and a source line.
- Not a bank. The dashboard footer and the Rate Tracker say SaveBrew tracks published rates and does not hold deposits; the Goals view says it does not hold or move money. The offering adds no feature that moves money, links bank accounts or originates anything (research brief, open question 9).
- Referral fees. The line "SaveBrew does not take referral fees or commissions from the banks, cards or retailers it writes about" is the single strongest positioning statement available (it answers the number one complaint in the research). It is a PROPOSAL and ships only if the owner confirms it is true. Until then the site says how items are chosen ("chosen by the editors on what a reader can act on, not on who pays") only if that too is true, otherwise nothing.
- The disclaimer, run on every content page (the brief, the Roundup, each guide, the Rate Tracker, the Goals view, the archive), visible without scrolling on the brief and above the fold on guides:

  "SaveBrew is an educational digest, not financial advice. We are not a bank, a lender, a broker or a registered investment adviser, and we do not hold, move or manage money. Rates and offers come from public sources on the date shown and change without notice, so confirm them with the institution before you act. What you save depends on your own choices."

- Deceptive design, none: no fabricated scarcity, no countdowns, no "founding member price ends tonight", no confirmshaming, no hidden costs, no preselected options, no retention wall on cancellation, no trick wording on any consent control. If the owner wants a launch price, it must be dated, honoured and stated as such.
- Trust elements: no testimonials, no press, no ratings at launch (research found none; the presence and press steps create them later and validate them then). No social icons until the handles are claimed.
- Identity: SaveBrew Inc. on the site matches the entity being vetted; footer and Contact carry the King of Prussia physical address, (888) 338-8809 and support@savebrew.com; Terms and Privacy carry the [EIN Address] placeholder until supplied.

COMPLIANCE NOTE, one line: purchasable on the site at visible prices with explicit "Add ... to my cart" CTAs and a guest checkout; a finance content subscription with no advice, lending, investment management, product sales or lead generation; educational only disclaimer on every content page; SMS limited to account notifications by separate, unchecked opt in.


### 3.2 THE ANTI SAMENESS RULE (named, testable)

**The rule.** SaveBrew shares no recognisable pattern with the seven Textla sister sites: Addabill, Financing Bot, Save The Will, Smart Augment, Brainbrook (the brief's "brainbook"), Hill Wallet and Astroquanta. Not the vibe, not the structure, not the fonts, not the speech pattern, not the motion, not the loader, not the section order. The exclusion brief (/home/claude/savebrew/exclusion/exclusion_brief.md) is the record of what those sites are; its section 3 is the consolidated DO NOT list and its section 4 is the shared template DNA. Both are carried below and both are cited, by section, in the QA checklist (section 10, block E).

**The test.** QA opens the four live sister sites (addabill-site.webflow.io, financing-bot-site.webflow.io, smartaugment-site.webflow.io, astroquanta-site.webflow.io) beside the SaveBrew build at 1440 and at 375, and reads the direction records of the three unbuilt sites (Save The Will, Brainbrook, Hill Wallet) from the exclusion brief's fingerprint table. For each of the twelve DNA items and each of the eight DO NOT sections, QA states pass or fail with what was observed. A stranger shown the SaveBrew hero beside any sister hero must not be able to point to a shared pattern. One fail is a build fail. The Art Direction spec's own seven differences from Financing Bot and Addabill (section 5, part 0.3) are run as a second explicit screenshot test.

**The twelve items of shared DNA (exclusion brief section 4), each an explicit fail, with the SaveBrew pass condition beside it.**

1. FAIL: a sticky bar or rail with the wordmark and a small icon top left, six or seven text links with a marker glyph on the active one, and a cart with count plus a purchase button at the right, in the sisters' treatment. PASS: the heading band (Art Direction 3.5, proposed.json `nav_style`): an opaque white weft band 84px that hides on scroll down and returns on scroll up, four destination links in Manrope with the active link at weight 800 and no marker glyph, About, Contact and Sign in at right, a spool cart glyph with a stitched count, the compact stitched Bobbin. Logo top left, horizontal nav and cart top right are the conventions floor and stay; the treatment is what differs (no marker glyph, no condensing bar, no uppercase mono, no perforation, no rule, no dateline).
2. FAIL: a hero pinned for about 1.5 viewports in which a bespoke Three.js object is scrubbed by scroll while a plain H1 sits beside or over it (ScrollTrigger `pin: true` or `position: sticky` on the hero). PASS: the loom is a fixed canvas layer behind flowing DOM, not a pinned hero; the signature scroll is 1.3 viewport heights of native scroll; the object lays flat into the page's own five column board so the archetype and the signature are one object (Art Direction 3.6, 3.7).
3. FAIL: a loader that counts real load stages in the hero motif and Flips into the hero object; a percentage, a "0% loaded" line, a counter, a Skip control top right. PASS: the selvedge stitch (Art Direction 3.18): a running stitch draws down the left gutter over the already painted page, no count, no Flip, ties off with a knot, "Go straight in" at the bottom centre.
4. FAIL: the sisters' section procession in their order: hero, a what it does band, a numbered 3 to 5 item list with big mono numerals, HTML product screens in a neutral shell, a candour section, pricing with a MOST POPULAR card and a giant numeral, an interactive tool teaser, a blog or about teaser, the SMS block, the footer. PASS: the home order of Art Direction 3.23 (hero, today's pass, cost, last week's pass, the dashboard, the ranker, free to read, questions, SMS, footer) with no numbered list, no candour section, no MOST POPULAR badge, no giant numeral, no $0 card, and the SMS block set as a full width inline row rather than a boxed centred form.
5. FAIL: one display face paired with one monospace used for uppercase letter spaced kickers, section indices and figures. PASS: Big Shoulders Display and Manrope, both proportional, figures in Manrope tabular numerals, no mono anywhere, no uppercase, no letter spacing, no kickers (Art Direction 3.10).
6. FAIL: a 65 to 68ch measure with the H2 left aligned at the top of each band. PASS: five warp columns edge to edge with a 31 to 52ch measure per column, heading passes set full width on butter between rows with a weft thread beneath, no kicker and no left H2 at the top of a band (Art Direction 3.4, 3.17, part 0.2).
7. FAIL: a neutral field (cream paper, celadon, graphite, near black, plum) plus exactly one sparing accent. PASS: butter #F6E7A1 as a saturated second surface showing between white weft blocks, with indigo #2B2F8F thread; the colour story "butter warp through a white weft, with indigo thread" (Art Direction 3.10).
8. FAIL: photography graded toward the accent (grayscale plus sepia plus hue rotate) and staged as a subject world of hands and objects without faces. PASS: material and texture with no people and no hands (cloth, thread, loom, selvedge), natural colour retained with the "morning light on cloth" split tone (Art Direction 3.22); no kitchen counter, ops floor, desk, threshold, car, till or clinic, and no coffee cup.
9. FAIL: the plainspoken hedged register: second person, present tense, exact numbers, declarative full sentence headlines with full stops, hedge sentences, "never" lists. PASS: the obsessive craftsman stance (Art Direction 3.24): first person plural for the work, questions as headings (the H1 is a question), short verdict lines after long ones, no hedge stacks, no "never" list.
10. FAIL: a candour device ("What X never does", "What would break it", a QA target hedge, a pull quote from a paper) standing in for testimonials. PASS: no testimonials and no substitute; the trust work is done by the dated, attributed figures, the disclaimer, the address and the two click cancellation.
11. FAIL: "Purchase the [plan]" (or Purchase a Plan, Buy a file pack, Purchase Plus) as the CTA with the price printed inside or directly beneath it, and "See how it works" as the secondary link. PASS: "Add the Daily to my cart" and its variants, first person singular, the price in the standfirst and the card's price line and nowhere near a button, and "Open this week's free roundup" as the secondary link (Offering Spec section 8).
12. FAIL: the sisters' motion: any of the eighteen claimed easing curves, fade up reveals, hover lift with press depress and idle breathing, Lenis smooth scroll, a Flip from the loader. PASS: Shuttle cubic-bezier(0.36, 0.01, 0.10, 1) and Knot cubic-bezier(0.22, 1.12, 0.36, 1) at 0.11s, 0.38s and 1.2s (Art Direction 3.11), the weft pass clip path wipe as the one reveal language, the Bobbin's running stitch and tightening press, native scroll with no Lenis. GSAP ScrollTrigger, Flip and Three.js r128 are the kit's libraries and stay; the curves, the reveal language and the choreography are what must differ.

**The DO NOT list (exclusion brief section 3), carried verbatim. Each item is a fail if present in the build.**

### 3.1 Fonts never to use (heading or body, any weight or axis)
Fraunces, Figtree, Archivo, Fragment Mono, Schibsted Grotesk, IBM Plex Mono, Newsreader, Spline Sans Mono, Young Serif, Hanken Grotesk, Recursive (including Recursive Mono Linear and the casual axis), Source Serif 4. Also excluded by the registry and the in-flight builds: Space Grotesk, Inter Tight, Instrument Serif, Instrument Sans, Martian Mono, Familjen Grotesk. Do not repeat any logged pairing, and avoid the formula itself: one display serif or grotesque plus one monospace for figures, kickers and labels (every site does this). Do not set nav links or kickers in uppercase letter-spaced mono. Do not use a giant display numeral as the hero's first read ("48 / 48", "$7,500", "$0").

### 3.2 Archetypes and hero compositions never to use
- Full-Bleed Cinematic Hero with a centred H1 + subhead + one button + price line stacked over a rendered scene (Addabill).
- Swiss or Modular Grid with a visible hairline grid, mono row indices and a left text column beside a right 3D wall (Financing Bot).
- Sidebar-Anchored: any persistent left rail carrying nav, status, a clock or a purchase button (Astroquanta).
- Magazine or Cover Story and its Research Note Folio casting: masthead between rules, dateline, left-third copy and right-two-thirds object, footnotes, colophon (Smart Augment).
- Illustrated Scroll World with a rendered house or lot filling the viewport and type docked in a reading measure (Save The Will).
- Meander: a continuous spine line with sections docking on alternating banks (Brainbrook).
- From the registry and the other in-flight builds: Single-Object Hero (3D), Split-Screen Diptych, Sticky-Stacked Cards Narrative.
- The shared hero mechanics regardless of archetype: a hero pinned for about 1.5 viewport heights whose 3D object is scrubbed by scroll while a plain DOM H1 sits over or beside it; the "left text, right product cluster" 40/60 split; a hero whose object is a calendar, a ledger wall, a cube lattice, a stack of sheets, a house, a tape or ribbon, cards on a counter, a photographic print or a point cloud; a hero subhead that begins "For [audience]..."; a price sentence directly under the hero button.

### 3.3 Palette fields, accent hues and colour stories never to use
- Fields: cream paper (#FAF3E6, #F6F3ED, #EDE2CF, #EAE5DB), pale celadon (#DCE8DF), dark graphite (#1A1B1D, #232527), near-black green (#0A0C0B), dusk plum (#2A2035, #1E1727), oxblood (#2E0B0C), green baize (#17392C), navy (#070B1A, #0E1B3A). Avoid any "warm off-white paper" or "graphite console" field reading.
- Accents: marigold #E9A825, verdigris teal #4FB89A, phosphor yellow-green #9BE15D, Prussian blue #1B3A5C, dusty rose #E39BBA, copper #A04219, carmine #E2265F, coral #FF6A4D, ice white as a metallic, and the green family generally (moss #3F6B4B, verdigris, phosphor, baize) which three builds lean on.
- Colour stories: "neutral field plus one sparing accent" in any form; "paper and ink with one institutional accent"; "cream and graphite with one marigold highlighter"; "graphite ledger with paper type and one verdigris figure"; "grey ladder with one surviving phosphor"; "dark field with one warm accent"; "dusk plum, lamplit linen and one rose"; "brook celadon, white receipts and one copper tag"; "oxblood leather with one cool light on"; "green baize and silver with one carmine ring". Also avoid graded photography tinted toward the accent (every build ships a named grade recipe of grayscale + sepia + hue-rotate + a tint overlay).

### 3.4 Nav and button treatments never to use
Nav: a sticky 56 to 72px bar that condenses on scroll; wordmark plus a small icon top left; six or seven text links in a row with an active-link marker beneath or around the link (day-cell box, lit window glyph, copper tag, ">" prompt, footnote mark, cell fill); uppercase letter-spaced mono links; a dateline; a cart tag with a count and a primary purchase button living in the bar; a left status rail; ruled cells divided by vertical hairlines; a masthead between rules; a receipt strip with a perforated edge; a translucent bar over the hero. (Logo top left, horizontal desktop nav and cart top right are conventions the kit keeps; vary the treatment, never the placement.)

Buttons: paper tag with a folded corner; paper block rectangle with a mono price cell divided by a hairline; square hairline console button with a prompt glyph; stamped rectangle with an inset hairline and a platen press; lit-window rounded rectangle with a glow; tag with a notch and a punched hole; glass tile with a light band; extruded silver plate; magnetic button with layered hover. Do not put the price inside the button ("from $2,400", "$200 a user a month"). Do not use the "lift on hover, depress on press, breathe at idle" choreography. Do not label the primary CTA "Purchase the [X] plan", "Purchase a Plan", "Buy a file pack" or "Purchase Plus", and do not pair it with a secondary "See how it works" text link.

### 3.5 Loaders never to use
Any loader that counts real load stages and then Flips into the hero object: percentage counter, "0% loaded" status text, flip calendar cards, rolling drum counter with tally strokes, trial grid fill gauge (48 cells outlining), ruled sheet draw-on, porch light five lights, receipt print head tearing at a perforation, five shops chapter index, latent image develop, boot sequence to swarm assembly; a "Skip" control top right; a loader that reuses the hero motif as its progress metaphor.

### 3.6 Section orders and recurring section types never to repeat in that order
The shared order across the seven: hero with the signature object → one "what it does" band or table (Add a bill / Sixty files / What lands on the desk / Four gates) → a numbered list of 3 to 5 props, steps or gates with big mono numerals (01 to 05, Step 1 to 4, Gate 01 to 04) → a product-screen showcase (HTML-built screens in a neutral shell, often tabbed) → a candour section ("What X never does", "What would break it", "what it never decides") → pricing with a MOST POPULAR card, a giant numeral and a per-plan purchase button → an interactive-tool teaser (builder, drafter, sweep, calculator, finder, sorter) → a blog or about teaser ("Founded in 2026", "Keeping the house on time", a pull quote) → the "Join Our SMS List" block → a footer with entity, address, phone, support email, Terms, Privacy and a copyright line. Do not reproduce this rhythm. Specific section types to avoid: numbered lists with oversized mono numerals; "How X works: A, B, C, D" step rows; an SMS sample shelf with arrow buttons; a "Founded in 2026" card; a pull quote from a paper; an FAQ accordion titled "Seats, billing and cancellation" style; tables as sections; a year-at-a-glance strip; a log-line footer; a colophon or run stamp. The SMS opt-in block is verbatim and mandatory, so its placement and framing (a boxed form centred in a narrow column, or set left in the grid) is where it must differ.

### 3.7 Headline formulas, CTA verbs, recurring words and sentence rhythms never to use
- H1 formulas: two declarative sentences with full stops ("Every bill on one calendar. A text before each is due." / "Forty eight specifications ran overnight. Six are still standing."); a participle triad plus a verdict ("Read, recalculated and cited. Your underwriter decides."); "[Noun], [past participle]." ("Bond research, automated."); a number-led narrative headline; a one-object metaphor stated as fact ("Every receipt you ever paid is one long tape").
- H2 formulas: "[Number] [plans / things / gates / frames / packs], [candour clause]" ("Two plans, no fees on your bills", "Three plans, prices on the page", "Three prepaid packs, one rate each, nothing that renews on its own", "Four gates. A specification clears all of them..."); "What X never does" / "What would break it" / "what it never decides"; "How X works: A, B, C"; "The X, the Y, the Z: three screens"; "[Noun phrase], [participial clause]"; imperative triads ("Run a sweep of your own. Choose N. Watch what dies."); H3s beginning "The [noun] [verb phrase]".
- Subheads that open with "For [audience]..." as the audience signal.
- CTA verbs and labels: Purchase, Buy, Use, Subscribe, Order, Run, Start, Empty, Check, Compare, "See how it works", "See the plans", "Read the blog", "Submit". Price inside or directly under the CTA ("$5 a month or $40 a year. No fees on your bills. Cancel any time.", "from $2,400").
- Recurring words to avoid as brand vocabulary: plan, file, page, desk, month, day, kept / keep, killed, log, row, figure, cite, never, nothing, every, sample, memo, queue, calendar, tape, receipt, gate, climb, base camp, switchback, route.
- Sentence rhythm to avoid: present-tense medium declaratives with a comma-spliced qualifying clause followed by a short verdict sentence; the hedge sentence ("not a result we promise", "Counts illustrate one month and are not a guarantee", "Prices in USD and proposed"); the "never" list; the "no card, ever" / "no fees" / "nothing behind a form" candour tic; lowercase mono log fragments; footnote superscripts on figures; uppercase mono kickers naming the section ("SECTION 02 · THE CYCLE IN ONE TABLE", "ADDING A BILL", "RESEARCH NOTE. SEPTEMBER 2026"); mono disclaimers under the hero; second person "you" plus a hedging "we"; no questions, no exclamation, no first person singular (so a question headline, a first person voice or an address to a named reader is open ground, subject to the kit's trust rules).
- Prices: do not present a Free / paid pair as two cards with a giant "$0"; do not use a MOST POPULAR badge; do not use seat steppers with a TOTAL line; do not use rolling drum numerals for prices.
- Testimonials and press: every site ships none and substitutes a candour device (a never list, a QA-target hedge, a pull quote from a paper, a sample photograph caption). Do not copy those substitutes.

### 3.8 Image styles and motion signatures never to use
- Image: graded photography of a "subject world" with hands only and no faces (kitchen counter, ops floor at night, research desk at dawn, home threshold at dusk, parked car after the appointment, body shop bay, night till); HTML-built product screens in a neutral phone frame or grey browser chrome; 3D hero objects (calendar, ledger wall, cube lattice, translucent paper sheets, raymarched house, receipt ribbon, cards on leather, photographic print, point-cloud body); paper, receipt, tag, tally, cell and window motifs; thermal grain, halftone and film grain passes; black and white or single-tint photography. A coffee cup already appears in Smart Augment's desk photography, so a brew world must not be staged as "a desk with a cup".
- Camera paths already used: pull back from one cell to the whole then a light sweep; first-person crane up a wall then dolly back; single-axis dolly through gate planes then a quarter turn; orthographic snap to raking perspective with a focus pull; eye-height dolly then a pendulum arc to birdseye then descent; low rail ride then a straight lift to birdseye then descent; slow half orbit at tabletop height; frontal hold then a turnover to the reverse side; swarm assembly then orbit and rise then explode to data.
- Motion: pinned scroll-scrubbed hero of about 1.5 viewport heights; a Flip handoff from the loader into the hero; fade-up reveals on scroll; rolling numerals and drum counters; hairline leaders that draw themselves; "walking" footnotes; breathing idle states; magnetic buttons; tilt toward the pointer; cursor blink in steps(1,end); light that walks across a surface; five things lighting one by one; a property line or rule drawing itself closed. Easing curves already claimed (SaveBrew must own its own two): cubic-bezier(0.24,0.8,0.26,1), cubic-bezier(0.42,0,0.14,1), cubic-bezier(0.8,0.02,0.18,1), cubic-bezier(0.34,0.9,0.2,1), cubic-bezier(0.7,0,0.1,1), cubic-bezier(0.12,0.7,0.16,1), cubic-bezier(0.55,0.06,0.18,1), cubic-bezier(0.3,0.74,0.08,1), cubic-bezier(0.2,0.62,0.12,1), cubic-bezier(0.58,0.04,0.2,1), cubic-bezier(0.1,0.82,0.26,1), cubic-bezier(0.76,0,0.12,1), cubic-bezier(0.68,0,0.08,1), cubic-bezier(0.16,0.66,0.04,1), cubic-bezier(0.46,0.03,0.24,1), cubic-bezier(0.05,0.7,0.3,1), cubic-bezier(0.16,0.84,0.24,1), cubic-bezier(0.65,0.02,0.32,1).
- Layout: no narrow centred column with wide empty side margins (Astroquanta's 1200px cap and Smart Augment's 1360px cap were Harlem's red-bar complaints); no alternating full-width colour bands each opened by a kicker and a left H2; no two-column copy-plus-aside grids at a 65 to 68ch measure with the rest of the width left as field; no pages of 10,700 to 12,400px built from 600 to 2,100px tall sections.


Notes on the DO NOT list for this build: "Daily" stands as the owner's product name although "day" is on the vocabulary list; "12 month CD" stays as the Rate Tracker's product label; "this month" in the fixed Seasonal item is the Offering Spec's own sentence (the owner may change it to "in October"). The route /your-moves and "Your moves" are the tool's own name, not the excluded "route" vocabulary. "Submit" appears only as the verbatim SMS block's button, which cannot change.

### 3.3 THE FULL WIDTH RULE (named, testable)

**The rule.** No negative space. Content fills the whole viewport at 1280, 1440, 1920 and 2560. No page uses a fixed centred container, no page leaves an empty outer third, and no long text sits alone in a single reading measure with field either side: prose is set in CSS multicolumn or beside a module in a two track pass. The five warp columns divide the whole width by construction.

**The test.** QA screenshots /, /brief, /membership, /guides, /your-moves, /about, one guide post, /roundup, /checkout and /terms at 1280, 1440, 1920 and 2560 wide and fails the build if any row's content box is narrower than the viewport minus twice `--gutter`, if any outer third of any row is empty, if any stylesheet declares a max-width above 100 percent on a block that holds a section (the lint rule), if any running text column measures under 30ch or over 55ch, or if any butter block runs taller than 40 percent of the viewport with running text on it. The screenshots are attached to the QA record.

**The CSS level rules, carried verbatim from Art Direction 3.17 (also present in section 5).**

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


The collapse rules for widths below 1280 are Art Direction part 0.2 (five columns at 1280 and up; three plus two at 1024 to 1279; two plus two plus one at 768 to 1023; one column with the sticky five thread tab strip at 375 to 767), also in section 5.

## 4. Product and Service Offering (the consumer use case)

What the customer buys, in one line: a SaveBrew Daily membership, a paid savings digest inside a member dashboard on savebrew.com, added to the cart with "Add the Daily to my cart", paid through a guest checkout, confirmed on /confirmation, opened at /today. Two products (one reader, two readers), each at two cadences (monthly, yearly), four SKUs, all prices proposed. No add ons, no free tier, no trial. The free content (the Weekly Roundup, the Guides, "Your moves") is public and needs no account.

The Offering Spec (Step 2) is the record of what is sold. Its sections 1, 3, 4, 5, 6, 7, 8, 9, 10 and 13 follow verbatim. Section 11 (the SMS tie in) is in section 9 of this document; section 12 (the compliance screen) is in section 3.1; section 15 (nature of services) is the legal text's section 2; section 16 (vocabulary) is in section 7's preamble; section 17 (open questions for the owner) is in section 10.

The one build rule that sits over these sections: where a customer facing line in the Offering Spec was rewritten by the copy step for vocabulary or date reasons, the copy.md string ships (the copy manifest lists each departure). The prices, SKUs, inclusions, CTA labels, buy flow and the product visual spec are not among those departures and are built exactly as written here.

### 4.1 Offering type and purchase mechanism (Offering Spec section 1)

## 1. OFFERING TYPE

SaaS or app subscription, delivered as a paid digest inside a member dashboard (a web app), with a public content layer that costs nothing and needs no account.

Purchase mechanism, in one line: the visitor adds a membership to the cart on the site, pays through a guest checkout with no account step, and lands on an order confirmation that opens the dashboard for the email used at checkout.

This is a hybrid in the sense of offering_types.md: the primary purchasable thing is software access (the dashboard with the Rate Tracker, the goals and the archive), and the editorial brief is the content that lives inside it. One offering stays clearly primary: the SaveBrew Daily membership.


### 4.2 Free content (Offering Spec section 3)

## 3. HOW THE FREE TIER IS HANDLED

Agreed with the recommended shape, with one refinement below.

The owner's brief describes "free members" with a "limited weekly digest". On this site there are no free members and no free account. The free content is simply public:

- The Weekly Roundup: published on savebrew.com each Saturday morning as a normal public article, readable by anyone. Three of the week's moves plus a short summary of where the tracked savings rates ended the week. Full text, not a teaser.
- The Guides library: evergreen explainers (proposed twelve at launch) on how high yield savings accounts work, when rotating cashback categories are worth the bother, the 50/30/20 split and its variants, the seasonal buying cycle, and similar. Full text, public.
- The one interactive page (section 14): public, working, no form.

Why this is the right shape:
1. A free signup form is a lead capture in a vetting reviewer's eyes and it competes with the purchase CTA for the primary position. With public content there is no form anywhere on the free path, so the only account SaveBrew has is the paid one.
2. It makes the brief's non negotiable ("free content genuinely useful, not a bait shell") verifiable by anyone who opens the URL. A reviewer can read the Saturday Roundup without giving anything.
3. Three sister sites (Addabill, Brainbrook, Hill Wallet) present a Free $0 card beside a paid card. Removing the $0 card removes that fingerprint and satisfies exclusion 3.7 without effort.
4. Free readers give no phone number, so SMS stays a members only account notification channel, which is the cleanest story for the short code.

The refinement: the roundup and guides carry an RSS feed and stable URLs so readers can follow them without an email list. No email capture form ships at launch, not even in the footer. If the owner later wants an email list, it must be a separate optional form that is not the primary action on any page; that is a post approval decision, not a launch item.

Where this departs from the owner's words: "free members" becomes "readers", and the paid product is the only "membership". The marketing copy should say so plainly ("The Weekly Roundup and the Guides are free to read. No account needed.").


### 4.3 Pricing rationale (Offering Spec section 4)

## 4. PRICING RATIONALE

### 4.1 The anchor stays at $7.99 billed monthly

Comparables from the research brief, section 11: free ad and affiliate funded roundups (NerdWallet, Bankrate, Morning Brew, The Penny Hoarder) at $0; YNAB at $109 a year; Motley Fool Stock Advisor at $99 intro and $199 normal per year; NYT Your Money at $3.75 a week, about $195 a year; MaxMyInterest at 0.16 percent a year with a $20 quarterly minimum, so at least $80 a year and aimed at large balances.

$7.99 billed monthly is $95.88 over a year, which sits below YNAB and Motley Fool's intro price and well below NYT, and above the free roundups. That is the right band for a product that is more than a roundup (a daily cadence, a tracker, goal tools, an archive, account texts) and less than a budgeting app that connects to bank accounts. It is also distinct from the sister sites' $4, $5 and $6 monthly points. No better anchor emerged from the research, so it stays.

### 4.2 The yearly price: $72, which is $6 a month

Monthly for twelve months costs $95.88. The yearly membership is $72 paid once, which is $6.00 a month and a saving of $23.88 (24.9 percent). Nine months at the monthly price is $71.91, so the plain English version is "pay for about nine months, read for twelve". Both figures ($72 and $95.88) print on the card so the arithmetic can be checked by the buyer.

Rejected: $79 (twelve months for the price of ten; the per month equivalent of $6.58 does not read cleanly) and $84 ($7 a month, a saving too small to move anyone).

### 4.3 A second paid product: SaveBrew Daily for Two

Included. The audience is working adults who share savings goals with a partner more often than not, and the Savings Goal view is a shared goal feature waiting to exist. A two reader membership gives the pricing section a real ladder with unit counts (one reader, two readers), it is cheaper per reader than two single memberships, and it adds value without withholding anything from the base membership.

Price: $11.98 billed monthly (two singles would be $15.98, so $5.99 per reader, a saving of $4.00 a month) and $108 billed yearly (two yearly singles would be $144; $9.00 a month for the pair, $4.50 per reader per month). Yearly for Two against monthly for Two: $143.76 versus $108, a saving of $35.76 (24.9 percent), the same ratio as the single yearly so the two yearly prices tell one story. Nine months at $11.98 is $107.82, so "pay for about nine months, read for twelve" holds for both yearly prices.

Justification against the comparables: budgeting tools (YNAB, Monarch) include household sharing in one price; digests (NYT, Motley Fool) sell single seats only. SaveBrew sits between them, so a priced two reader option is defensible and no comparable undercuts it. It is a proposal; if the owner declines it, the ladder is the Daily at two cadences and nothing else changes.

Naming note: Save The Will (a sister site) sells "Will for two". "Daily for Two" echoes that naming, not a banned formula from 3.6 or 3.7. If Harlem wants zero echo, the alternative name is "Daily Duo" with the CTA "Add the Daily Duo to my cart".

### 4.4 Rejected: a paid rate alert add on

Rejected on compliance grounds. Alerts on the member's own tracked rates are account notifications and belong inside the membership. Selling texts as an add on would make the SMS program look like the product being sold, which muddies the consumer use case for vetting, and any add on invites the preselection pattern that compliance.md prohibits. No add ons exist on this site.

### 4.5 Rejected: a third tier

There is no honest feature to withhold from the base membership that would not turn it into a stub. Gating the Rate Tracker or the archive behind a higher tier breaks the pricing_and_descriptions.md rule that the cheapest paid tier must be genuinely useful. Two products, two cadences, done.

### 4.6 No free trial

A trial signup is not a purchase and it adds a second account path. The public Roundup, the Guides and the interactive page are the try before you buy.


### 4.4 The line: products, SKUs, prices, cadences, CTA labels (Offering Spec section 5)

## 5. THE LINE

Format: Name | price (proposed) | one line what it is | purchase CTA label.

| SKU | Name | Price (proposed) | Billing | What it is | CTA label |
|---|---|---|---|---|---|
| SB101 | SaveBrew Daily | $7.99 | billed monthly, renews monthly | One reader: the weekday morning brief, the Rate Tracker, goals, saved items, playbooks and worksheets, the archive, account texts by opt in | Add the Daily to my cart |
| SB102 | SaveBrew Daily, yearly | $72 ($6.00 a month) | billed once, renews yearly | The same membership for twelve months, paid once, with a renewal notice 30 days ahead | Add a year of the Daily to my cart |
| SB201 | SaveBrew Daily for Two | $11.98 ($5.99 per reader) | billed monthly, renews monthly | Two readers on one bill: two sign ins, shared goals, separate alert settings | Add the Daily for Two to my cart |
| SB202 | SaveBrew Daily for Two, yearly | $108 ($4.50 per reader per month) | billed once, renews yearly | The two reader membership for twelve months, paid once | Add a year of the Daily for Two to my cart |

Public, no SKU, no CTA, no form: the Weekly Roundup (Saturdays), the Guides library, the interactive page. Secondary link from the hero: "Open this week's free roundup".

Unit counts: one reader (SB101, SB102), two readers (SB201, SB202). Quantity is fixed at 1 per membership; the cart holds one membership at a time (section 8).

Renewal terms, stated on the card at the same weight as the price: monthly memberships renew at the same price each month until cancelled; yearly memberships renew at the same price each year, with an email (and a text, if opted in) 30 days before the renewal date. Cancellation is two clicks from the dashboard and access runs to the end of the period already paid for.

Tax and fees: the price shown is the price charged; it includes any applicable sales tax, and there is no setup fee, no cancellation fee and no charge to invite the second reader. (Owner to confirm the tax inclusive stance with their payment processor; see section 17.)

Refunds (proposed): a yearly membership is refundable in full within 14 days of purchase on request to support@savebrew.com; monthly memberships are not refunded but can be cancelled at any point, with access running to the end of the paid month.


### 4.5 Inclusions, in full, with descriptions (Offering Spec section 6)

## 6. INCLUSIONS, IN FULL

Every membership card lists all of these, each with its one line description, nothing truncated, no "and more".

### 6.1 SaveBrew Daily (one reader)

1. The morning brief. Five items, about four minutes to read, on the dashboard by 6:30 AM Eastern each weekday: savings rate movements, cashback and coupon opportunities, seasonal spending strategy, budgeting frameworks and money management techniques. Each item ends with one small action.
2. The Rate Tracker. Published rates for the high yield savings accounts, money market accounts and CDs on SaveBrew's checked list (twenty at launch, proposed), checked each morning, with a 30 day history per account, a slot to type in your own account's rate for comparison, and alert thresholds you set yourself.
3. Goals. Up to six savings goals, each with a target, a date, a monthly deposit, an on track status, a deposit streak and milestone marks at 25, 50, 75 and 100 percent. SaveBrew records what you type; it does not hold or move money.
4. Saved items. The codes, category activations and deadlines you save from the brief, in one list with their expiry dates, with reminders on the dashboard and by email.
5. Playbooks and worksheets. The monthly seasonal playbook (what to buy now and what to wait on) and fillable worksheets for the frameworks the brief covers, starting with the 50/30/20 tune up and the paycheck split.
6. The archive. Every past brief since your membership began and since launch, searchable by topic and by date.
7. Account texts, if you opt in. Alerts you set on tracked rates and goals, billing and renewal notices, sign in codes, confirmations when you change settings, and replies from support. Nothing promotional. Reply STOP to end texts at any time.
8. Two click cancellation. Membership, then Cancel, from your dashboard. Access continues to the end of the period you paid for and a Resume link stays there until it does.

### 6.2 SaveBrew Daily for Two (two readers)

Everything in 6.1, for two people, plus:

9. Two sign ins on one bill. Each reader has their own dashboard, their own morning brief view, their own saved items and their own text settings and opt in.
10. Shared goals. Any goal can be marked shared; both readers can record deposits and both see one progress bar. Private goals stay private to the reader who made them.
11. The invite. The second reader is invited by email from the dashboard after the order is placed. Nothing about them is asked at checkout.


### 4.6 Descriptions (Offering Spec section 7)

## 7. DESCRIPTIONS

Two to three sentences each, human voice, no dashes, no two from the same template. Each ends with its CTA label.

SaveBrew Daily, billed monthly ($7.99). Five things worth doing about your money, written up and waiting on your dashboard by 6:30 each weekday morning, with the rates we checked overnight sitting right above them. The same membership carries the Rate Tracker, your goals, the archive and the text alerts you choose. $7.99 billed monthly, and it stops whenever you say so. CTA: Add the Daily to my cart.

SaveBrew Daily, billed yearly ($72). The same Daily, paid once for twelve months at $72, which works out to $6 a month against $95.88 if you paid monthly all year. We email you thirty days before it renews. Cancelling takes two clicks from your dashboard at any point in the year. CTA: Add a year of the Daily to my cart.

SaveBrew Daily for Two, billed monthly ($11.98). One bill, two readers. You each get your own sign in, your own morning brief and your own alert settings, and the goals you mark as shared show both of your deposits on one bar. $11.98 billed monthly, which is $5.99 a reader. CTA: Add the Daily for Two to my cart.

SaveBrew Daily for Two, billed yearly ($108). Two readers for a year at $108, or $4.50 per reader per month. Invite the second reader by email from your dashboard the moment your order is placed; nothing about them is needed at checkout. CTA: Add a year of the Daily for Two to my cart.

The Weekly Roundup (free, public). Each Saturday morning, three of the week's moves and a short account of where the tracked savings rates ended the week, published on savebrew.com for anyone to read. No account, no form, no email address. Link: Open this week's free roundup.

The Guides (free, public). Evergreen explainers on how high yield savings accounts work, when rotating categories are worth the bother, the 50/30/20 split and its variants, and the seasonal buying cycle. Read them in any order, as often as you like. Link: Open the guides.


### 4.7 CTA label system (Offering Spec section 8)

## 8. CTA LABEL SYSTEM

The seven sister sites use "Purchase the [X] plan", "Purchase a Plan", "Purchase Plus", "Buy a file pack", "Start Free", "Subscribe to Research" and "See how it works", with the price inside or directly under the button. Exclusion 3.7 also lists Purchase, Buy, Use, Subscribe, Order, Run, Start, Empty, Check, Compare and Read as CTA verbs to avoid. SaveBrew's labels are built on "Add ... to my cart", which is an unambiguous purchase action (it adds the membership to the cart, and the cart leads only to payment) and is the compliance document's own first example of an explicit purchase CTA.

| Position | Label | Notes |
|---|---|---|
| Home hero, primary | Add the Daily to my cart | Adds SB101 (monthly) by default; the cart shows the cadence and lets the buyer switch to yearly before checkout |
| Home hero, secondary link | Open this week's free roundup | Leads to the public Saturday page; not "See how it works" |
| Membership card, Daily, monthly selected | Add the Daily to my cart | Button label changes with the cadence radio |
| Membership card, Daily, yearly selected | Add a year of the Daily to my cart | |
| Membership card, Daily for Two, monthly selected | Add the Daily for Two to my cart | |
| Membership card, Daily for Two, yearly selected | Add a year of the Daily for Two to my cart | |
| Product tour section | Look inside the dashboard | Secondary; scrolls to the three product shots |
| End of the interactive page | Add the Daily to my cart | With the line "Members get a ranked list like this each weekday morning." |
| Cart | Go to checkout | |
| Checkout submit | Pay $7.99 now | Amount bound to the cart total; the checkout spec names "Pay $X" as an accepted submit. The price in the button here is the full cost statement compliance requires, not the sister sites' marketing price line. If the design step wants no numeral in the button, the fallback is "Complete my purchase". |
| Order confirmation | Open my dashboard | The dashboard is keyed to the checkout email; a password is optional (section 8.4) |
| Nav, desktop | Add the Daily to my cart (compact button) plus a cart control with count | On phone widths the nav carries the cart control and a Membership link; the hero button is always in view within one scroll |

Rules: the price is never printed inside a marketing button or directly beneath it. It sits in the hero standfirst sentence and in the card's price line. No "Cancel any time" line under a button; cancellation is inclusion 8 in the list. Every CTA above is first person singular ("my cart"), which exclusion 3.7 identifies as open ground.

Compliance over novelty: "Take the Daily", the newspaper idiom, was considered for the hero and rejected as the button label because a reviewer could read it as "take a look". It may appear as headline language in the copy step; the button says what the button does.


### 4.8 The buy flow (Offering Spec section 9)

## 9. THE BUY FLOW

### 9.1 Pages and states

/membership (the pricing page) → cart drawer (any page) → /checkout → /confirmation → /today (the dashboard). Also /roundup (the public Weekly Roundup), /guides, and the interactive page.

The membership page: a short cadence control (Monthly | Yearly) above two cards, monthly selected by default because it is the cheaper commitment. Both prices are always printed on each card whichever cadence is selected. Each card: name, one line of who it is for, the price line with the renewal sentence at the same weight, the full inclusion list from section 6, the tax and fees line, then the CTA button at the bottom. No badge, no giant numeral, no $0 card, no seat stepper, no TOTAL line, no rolling numerals.

### 9.2 Cart

The cart holds one membership at a time with quantity fixed at 1. Adding a different membership replaces the current one and says so ("Your cart now holds SaveBrew Daily for Two, yearly. The Daily, monthly, was removed."). The cart shows: the membership name, the cadence, today's charge, the renewal amount and date in plain words, the tax and fees line, and a cadence switch so the buyer can change monthly to yearly here without going back. No upsell prompt, no add on, no preselected anything. Cart persists across pages (localStorage with an in memory fallback). Empty cart, remove last item and checkout with an empty cart all have designed states; the empty state offers the membership page link.

### 9.3 Checkout (guest, per checkout_spec.md)

No account step anywhere between cart and confirmation. Sections, one column, top aligned labels, required and optional marked, autocomplete tokens on every field:

1. Contact: first name, last name, email (this becomes the dashboard sign in), phone with the helper "Used for support and to confirm it is you if you ever lose access. Texts are sent only if you opt in on your dashboard."
2. Shipping: omitted (digital).
3. Billing address: full address with country and postal code.
4. Payment: accepted card badges, name on card, card number, expiry month and year, CVV with help text.
5. Order summary: the membership, the cadence, today's charge, the renewal sentence, the tax and fees line, total. One unchecked required box: "I am 18 or older and accept the Terms of Service and Privacy Policy." No SMS consent box here; SMS consent lives in its own verbatim block and is never bundled with the purchase.
6. Submit: "Pay $7.99 now" (amount live). Validation follows the GOV.UK error standard in the checkout spec. A small honest note that no live charge is made during the vetting build is acceptable; the form is complete regardless.

### 9.4 Order confirmation and delivery

The confirmation page shows the order number, what was bought, what was charged, the renewal date and amount, and the support contact. Then: "Your dashboard is ready for [email]. Set a password to open it now, or use the sign in link we just emailed you." Setting a password is optional; the emailed link signs the member in. Beneath that, the verbatim SMS opt in block (unchecked, one program) as an optional step, clearly separate from the order, which is already complete. Then the button "Open my dashboard". For Daily for Two, the confirmation also carries "Invite your second reader" with an email field that can be used now or later from the dashboard.

### 9.5 Cancellation (two clicks, self service)

From the dashboard app bar: Membership (click one) → Cancel membership (click two). The cancellation is immediate; the screen shows the date access ends and a Resume membership link that stays available until that date. No retention offer, no survey gate, no "are you sure" modal. Replying STOP to a text ends texts only; the dashboard and the Terms say so. Cancellation is also honoured by email to support@savebrew.com. The pricing page states the two click path in the inclusion list.

### 9.6 Renewals

Yearly members get an email 30 days before renewal (and a text if opted in) naming the amount and the date. Monthly members get a receipt each month. A failed payment produces one notice and a seven day grace period before access pauses; no fee.


### 4.9 Product Visual Spec: the locked visual spec (Offering Spec section 10, verbatim)

SaveBrew is a SaaS subscription, so the "product photograph" of the kit's physical product rule becomes the product UI: three real HTML dashboard views built to the spec below, screenshotted in the app's own frame, with the membership cards drawn from the same system. There is no packaging, no container and no label; the one master image rule becomes the one app bar, one palette, one type system and one card radius across all six product shots and both cards (10.5). The views are built as real interactive pages at /today, /rates and /goals (section 7) and the shots are captured from those pages, so the marketing site and the product are literally the same code.

## 10. LOCKED VISUAL SPEC

Type: SaaS or app subscription, so two visual jobs (offer_visual_spec.md): the membership cards and the product UI. The product is SaveBrew's own dashboard, built later as real HTML views and screenshotted, never generated as imagery.

### 10.1 Form factors

Two, and only two.

A. Desktop window at 16:10. Canvas 1440 by 900, exported at 2x. The window IS the app: the SaveBrew app bar is the top edge of the frame. No browser strip, no three dots, no address bar, no grey chrome. Corner radius 12px, a 1px hairline outline in the brand ink at low opacity, a soft 2px edge shadow at most, sitting on a field of the brand's own paper colour from the design step. Never a black backdrop.

B. Phone view at 375 by 812 (the checkout QA viewport), exported at 3x. A frameless screen crop: no bezel, no notch, no simulated status bar, no hand, no tilt. Corner radius 20px. The same app bar with the mark and wordmark left; the section tabs become a horizontally scrolling row directly under the bar (never a bottom tab bar, never a hamburger only). Single column.

Pairing: a desktop shot and its phone shot may stand side by side with a clear gutter, never overlapping (Monarch's phone over the window corner is excluded).

This overrides one line of the product UI brief (Part D, "a rounded desktop app window with a slim, neutral browser style top strip showing app.savebrew.com/today and three window dots"): grey browser chrome and neutral phone frames are on the exclusion brief's never use list (3.8), so the frame is the app's own header, as above.

### 10.2 The logo rule

Every shot carries the SaveBrew mark plus wordmark, left aligned in the app's own 56px header bar (48px on phone), at 24px height on desktop and 20px on phone, using the brand's wordmark from the design step. Never centered, never mark only, never in a sidebar, never watermarked over the content, and never a coffee cup or a beer glass as the mark (name collision guidance, research section 9). The rest of the desktop bar, left to right: the section tabs inline (Today, Rates, Goals, Archive), then at the right end a date pill ("Wed, Sep 24"), a bell with the small label "Texts on", and a circular avatar with the member's initials ("JM"). Sample member across all shots: Jordan, initials JM, badge "Member since 2026".

### 10.3 The three screens

Light theme. One UI sans family from the design step with tabular numerals for all figures; a small caps tag style for section labels; body copy at 16px in the brief. Density medium: five brief items, seven visible rate rows, three goals. Whitespace between modules 24px or more. Every data module carries a freshness stamp ("Rates checked 6:00 AM ET"). Every shot carries the footer line inside the app frame: "Illustrative figures shown. Live rates move without notice. SaveBrew is a digest, not a bank." No em or en dashes anywhere in UI copy. Institution names are placeholders ("Bank A (illustrative)"); all APYs are round sample values; no real bank names or live rates in any shot.

Screen 1, Today (the homepage hero shot). Two columns on desktop (main about 62 percent, right rail about 38 percent).
- Main column, top: caps eyebrow "TODAY'S BRIEF", heading "Good morning, Jordan.", sub line "Wednesday, September 24 · 5 items · 4 minute read", status chip "Published 6:30 AM ET". The greeting stands on its own line with no quip after it.
- Rate strip, four tiles: "Top tracked APY" 4.00% (no change); "Average of tracked" 3.60% (up 0.05 this week); "Your account" 3.50% (Bank F, illustrative); "Gap to top" 0.50 pts (about $50 a year on $10,000). Under the strip: "Rates checked 6:00 AM ET. Illustrative figures."
- Five numbered items, each with a caps tag, a bold one line headline, a two line summary and one small action chip:
  1. RATES. "Top online savings rates held at 4.00% this week." Summary: "Three of the twenty accounts we track nudged up by 0.05 points and none cut. If your account is under 3.75%, today is a good morning to compare." Chip: "Open tracker".
  2. CASHBACK. "The rotating 5% category switches to grocery stores through September 30." Summary: "Activate it once and the cap covers about $1,500 of spend. A reminder lands on your Today view on the last morning." Chip: "Remind me".
  3. COUPON. "A stackable 20% code on winter tires ends Friday." Summary: "It works with the retailer's rebate on the same order, which brings a $600 set to about $430 after both." Chip: "Save code".
  4. SEASONAL. "October playbook: buy patio furniture and jeans now, wait on TVs and toys." Summary: "Clearance cycles favour outdoor goods and denim this month; big electronics drop again in late November." Chip: "Open playbook".
  5. FRAMEWORK. "The 50/30/20 tune up: a ten minute look at your paycheck split." Summary: "Three questions to ask before the next pay run, with a worksheet you can fill in on the Goals tab." Chip: "Open worksheet".
- Under the list: a quiet link row "Yesterday's brief" and "Browse the archive".
- Right rail (stacked cards, 16px radius, hairline border, no drop shadows): (1) "Goal snapshot": Emergency fund, $6,000 of $10,000, a 60 percent bar, "On track for Mar 2027", link "Add $250 this month". (2) "Texts": rows "Rate moves over 0.25 pts on tracked accounts" toggle on, "Goal check ins and milestones" toggle on, "Billing, renewal and sign in codes" toggle on; footer "Sending to (555) 010 0123. Reply STOP to end texts. Ending texts does not cancel your membership." (3) "This week so far": "Rate changes tracked: 3", "Codes saved: 2", "Gap to top rate on your balance: about $50 a year".
- Phone version: the brief header, the four tiles as a 2 by 2 grid, the five items, then the three rail cards stacked below.

Screen 2, Rate Tracker.
- Header: "Rate Tracker", sub line "Twenty accounts and CDs, checked each morning", freshness pill "Updated Sep 24, 6:00 AM ET", primary button "Set an alert".
- Controls: filter chips (All, Savings, CDs, Money market), a "Balance" input prefilled "$10,000", a sort control "APY, high to low".
- Summary strip: "Top tracked" 4.00%, "Average tracked" 3.60%, "Moved up this week" 3, "Moved down this week" 1.
- Table (about 70 percent width) on one white surface with hairline dividers, no per row cards, no per row buttons, no bank logos (two letter monogram tiles). Columns: Institution, Product, APY, 7 day change, Minimum, At this APY $10,000 would earn about, Alert. Rows: Bank A (illustrative), High yield savings, 4.00%, +0.05, $0, $400, alert on; Bank B, High yield savings, 3.90%, 0.00, $100, $390, off; Bank C, Money market, 3.80%, +0.10, $1,000, $380, off; Bank D, 12 month CD, 3.75%, 0.00, $500, $375, off; Bank E, High yield savings, 3.70%, down 0.05, $0, $370, off; Bank F, High yield savings, 3.50%, 0.00, $0, $350, tagged "Your account"; Bank G, 6 month CD, 3.40%, +0.05, $500, $340, off. Footer link "13 more". APY at about 20px, the largest text in the row and no larger. Up moves green with an up arrow, down moves red with a down arrow, no change grey.
- Right detail panel (about 30 percent) for Bank A: "Bank A, High yield savings", "4.00% APY", a 30 day line stepping from 3.95 to 4.00 mid month with ticks at 3.75, 4.00, 4.25, a History list ("Sep 12: 3.95 to 4.00", "Aug 3: 3.90 to 3.95"), and an input "Alert me if this drops below" showing "3.90%".
- Under the table: "APY figures are illustrative, not live rates. SaveBrew tracks published rates and does not hold deposits."
- Phone version: summary strip as 2 by 2, the table as stacked rows (institution and product on line one, APY and change on line two), the detail panel opens as a sheet.

Screen 3, Goals.
- Header: "Goals", sub line "Three goals, $8,500 of $16,700", primary button "Add a goal".
- Featured goal card: "Emergency fund", $6,000 with "of $10,000" beside it, a wide 60 percent bar with four small tick marks at 25, 50, 75 and 100, stat cells "Target: Mar 2027", "Monthly deposit: $250", "Status: On track" (green chip), a six bar deposit chart labelled Apr to Sep at $250 each with the caption "6 month streak", and the footnote "At 4.00% APY, $6,000 would earn about $20 a month. Illustrative."
- Two smaller cards side by side: "Holiday spending", $1,000 of $1,500, 67 percent, "Target: Dec 2026", "Monthly deposit: $250", "On track"; "New laptop", $1,500 of $5,200, 29 percent, "Target: Jun 2027", "Monthly deposit: $400", "Slightly behind" (amber chip) with the link "Adjust the deposit".
- Right rail: "From today's brief": "Moving to the top tracked rate: about $50 a year on your balance" and "This month's 5% grocery category: about $30 on $600 of groceries", each with the link "Apply to a goal". "Check ins by text": "Weekly goal check in" toggle off, "Milestone alerts at 25, 50, 75 and 100 percent" toggle on, "Next check in: Monday 8:00 AM".
- Footer: "Illustrative figures shown. Goals are planning tools; SaveBrew does not hold or move money."
- Treatment: flat bars with a rounded end, text chips for status, no photo thumbnails, no ring charts, no hexagon badges, no piggy bank.
- Phone version: featured card, then the two cards stacked, then the rail cards.

### 10.4 The membership cards

One card system for both products. Same shape, same order of parts: name, the one line audience, the price line with both cadence prices and the renewal sentence, the full inclusion list (eight items on the Daily, eleven on Daily for Two, every one with its description line), the tax and fees line, the CTA button. Only the name, the reader count, the prices and the three extra inclusions change between the two cards. The price sits at a normal heading size in the card's upper third, well away from the button. No "MOST POPULAR", no $0 card, no seat steppers, no TOTAL line, no drum numerals, no price under the button. The cards use the same corner radius, hairline border and type as the dashboard cards so the store and the product read as one system.

### 10.5 The consistency rule

Across the site the product appears as one thing: the same app bar, the same logo placement, the same palette, the same type, the same card radius and hairlines in all six product shots and both membership cards. The only things that change between shots are the screen's content. Before launch, view every product shot and both cards side by side and rebuild anything that drifts, shows a dash, shows a real bank name or live rate, or shows a device frame. Trade dress to avoid is listed in the product UI brief, Part C; QA fails any shot that reads as Morning Brew, Raisin, Monarch, Rocket Money or NerdWallet.


### 4.10 Where the Offering Spec corrects the Product UI Brief (Offering Spec section 13)

## 13. WHERE THIS SPEC CORRECTS THE PRODUCT UI BRIEF

For the build and QA steps, the product UI brief (Part D) stands except for these lines, which change for compliance or exclusion reasons:
1. Frame: no browser style strip, no three dots, no URL (section 10.1).
2. Today status chip: "Published 6:30 AM ET" replaces "Delivered 6:30 AM, also sent by text". The brief is not texted.
3. Item 2 summary: "A reminder lands on your Today view on the last morning" replaces "We will text a reminder on the last day". Chip "Remind me" replaces "Set reminder".
4. Texts card: the "Cashback deadlines" toggle is removed; rows are the three in section 10.3; the footer adds "Ending texts does not cancel your membership."
5. "This week so far": "Gap to top rate on your balance: about $50 a year" replaces "Estimated extra earned: $4".
6. Goals: "Monthly deposit" replaces "Monthly plan"; "Adjust the deposit" replaces "Adjust plan".
7. Footer lines: "Illustrative figures shown. Live rates move without notice. SaveBrew is a digest, not a bank." replaces "Sample data for illustration. Rates change daily. SaveBrew is a digest, not a bank." (the word "sample" is on the exclusion vocabulary list).
8. Tracker sub line: "Twenty accounts and CDs, checked each morning" with seven rows visible and a "13 more" link.


### 4.11 The Product UI Brief, Parts B and C (research, verbatim)

The research step recorded what the category's product previews actually show (Morning Brew, Raisin, Monarch, Rocket Money, NerdWallet, The Daily Upside) so the SaveBrew shots read as a credible product in this category while sharing no competitor's trade dress. Part B lists the mechanics to take; Part C lists the compositions QA fails a shot for. Part D of that brief (the content plan) is superseded by Offering Spec sections 10.1 to 10.5 and 13 above, which carry its corrected content in full; Part E (its QA checklist) is folded into section 10, block N, with the corrected footer wording ("Illustrative figures shown." rather than "Sample data for illustration."). The reference screenshots under /home/claude/savebrew/research/screenshots/ are for comparison only and are not shipped.

## Part B. Category mechanics to take

These are the things a buyer in this category expects to see. Take the mechanic, not the competitor's rendering of it.

- A rate table with, per row: institution name, product type, APY as the dominant numeral, minimum balance or deposit note, an FDIC or NCUA line, and one action. Sortable columns and a product-type filter (Savings, CDs, Money market).
- A deposit-amount input that recalculates an "estimated annual earnings" column (Raisin) and a national average versus top rate comparison (NerdWallet).
- A visible freshness stamp on every data module: "Updated Sep 24, 6:00 AM", "as of ...", "Last updated".
- One big headline number with a delta since a date or period (NerdWallet, Monarch, Rocket Money), with a small trend chart and a range control.
- A "today" reading view that opens with a greeting and the date, then a small number of items (three to five), each with a caps section tag, a bold one-line headline, and a short summary; bold lead-in phrases inside body copy (Morning Brew, The Daily Upside).
- A compact data strip inside the brief (The Daily Upside's markets tiles); for SaveBrew this becomes rate tiles.
- Goal rows or cards showing name, current amount, target amount, target date and a progress bar; an "on track" status; a monthly contribution figure (Monarch, Rocket Money).
- A streak or milestone mechanic for deposits (Rocket Money) in generic form only: a count of consecutive weeks or months contributed, no hexagons.
- An archive list of past editions with date, title, and one-line subline, plus a date filter (The Daily Upside).
- Account or alert freshness and control rows ("Sync now", "Text alerts on"); for SaveBrew the SMS notification settings and the "sent" state.
- Small print disclaimers inside the UI: "Sample data for illustration", "Rates change daily", "SaveBrew is not a bank" (NerdWallet, Raisin).
- Persistent navigation: top tabs or a sidebar with a short list of sections (Today, Rates, Goals, Archive, Settings).
- Filter chips and time-range pills (All, Savings, CDs; 1M, 3M, 6M).
- Tabular numerals everywhere numbers stack.
- Light default theme; dark is optional and none of the five uses dark as the marketing default except the NerdWallet net worth screen.

---

## Part C. Compositions to avoid (trade dress)

QA should check the SaveBrew shots against each item and fail the shot if it reads as the named competitor.

Morning Brew:
- A white phone tilted about 30 degrees over a hard white/royal-blue split background.
- A full-width blue masthead bar with a centered white logo at the top of the reading view.
- "Good morning." in bold followed by a quip on the same line as the opening of the brief.
- A single lead story with a wide photo directly under a caps tag as the first module.

Raisin:
- A black phone held in a real hand over a blurred home interior.
- A donut chart with a "Your Wealth" style total in the center and a four-item legend as the first module.
- Rate rows rendered as separate white shadowed cards with a giant light-blue APY and a solid blue "Save now" button per row.
- A "UP TO $1,000 CASH BONUS" style promo badge floating beside the device.

Monarch:
- Cream page background with orange accent and serif display headlines paired with orange caps eyebrow labels.
- Floating UI cards with no device frame, offset and overlapping each other, including an avatar chip card.
- Goal rows with square photo thumbnails on the left and a green progress bar spanning the row.
- A left sidebar with an icon-only logo at the top and a user name at the bottom; a Sankey cash flow diagram; a four-tile KPI row in green and red.
- A rounded app window on a black backdrop with a phone overlapping its bottom-right corner.

Rocket Money:
- A red to crimson gradient header with a centered white logo and a white card overlapping the header edge.
- "Current spend this month" with a dashed BUDGET line over a blue line chart; a "Payday in N days" row.
- Hexagon milestone badges (25, 50, 75, party), a streak card with a piggy bank, and a ring chart with a palm tree icon.
- An upright black iPhone on a light grey rounded panel with a QR "Scan to download" card.

NerdWallet:
- Green on green hero with a tilted phone and decorative starburst shapes.
- A dark green app screen with the logo icon centered between a hamburger and a bell, a pill chip row, and a green area chart.
- A lime "expert tip" callout with a two-bar national average versus top rate comparison.
- The rate table treatment with large bank logos, star ratings with "Best for" descriptors, and green "LEARN MORE" buttons with "at Bank, Member FDIC" beneath.

The Daily Upside (supplementary):
- A centered masthead with an asterisk, dark green date blocks in the archive list, and a three-tile "MARKETS" strip labelled in green caps.

General rule: SaveBrew's shots must not pair a centered logo with symmetric utility icons in the app bar (Rocket Money, NerdWallet), must not use an icon-only sidebar (Monarch), and must not use a phone-in-hand or tilted-phone hero (Raisin, Morning Brew, NerdWallet).

---

## 5. Design System

The design system is the Art Direction and Technique Stack spec from Step 2.5 (ui-ux-director, direction "THE WEAVE", chosen by Harlem from three candidates), embedded in full in 5.1. It is not trimmed. The registry record the design doc spec asks for:

| Field | Value |
|---|---|
| Art direction | A morning on the loom: undyed cloth on butter, indigo thread, condensed display type set like a mill's stencil, everything in rows. Woven, dense, exact, warm, unhurried. |
| Layout archetype | WARP COLUMNS (invented; logged in archetype_additions.md): five fixed content columns edge to edge, one per money thread, each section a row across all five, heading passes between rows, no centred container. |
| Governing idea | Five threads run through each working month (savings rates, cashback, coupons, the seasons, the paycheck), and each weekday morning SaveBrew weaves the day's pass and hands you the five knots worth pulling. |
| Signature move | TEX-008, generative canvas background: the Loom, a real time procedural weaving scene in Three.js r128, scrubbed by scroll, whose wow moment is THE PASS. |
| Palette | Butter #F6E7A1 (ground), deep butter #EBD77A, pale butter #FBF3CF, white #FFFFFF (weft), indigo #2B2F8F (thread), deep indigo #1B1E5C, ink #14163A, muted indigo #4F5280; semantic up #1F7A4D, down #B3261E, behind #8A5A00 inside the product views only. Colour story: butter warp through a white weft, with indigo thread. Accent hue family: indigo (blue violet). |
| Type | Big Shoulders Display (variable, headings) and Manrope (variable, body and UI, tabular numerals). No mono. |
| Motion signature | Shuttle cubic-bezier(0.36, 0.01, 0.10, 1) and Knot cubic-bezier(0.22, 1.12, 0.36, 1); durations fast 0.11s, base 0.38s, slow 1.2s; idle cadence 11s. |
| Typographic set piece | The Tightening (the home H1 pulls from weight 500 to 800 glyph by glyph as the weft passes). |
| Loader | The selvedge stitch (a fill gauge cast as the cloth's finished edge). |
| Brand graphic kit | The Knot (motif and favicon), the Selvedge Seal, three dividers (the Selvedge, the Thread Strip, the Weft Pass), eleven icons, the numeral treatment, the Twill texture. |
| Interactive feature | "Your moves", a ranker, at /your-moves. |
| Voice stance | The obsessive craftsman. |
| Build tier | Tier 1, procedural concept site. Fit line: SaveBrew's identity is a system, five threads read every morning, and drawing that system in code expresses it better than any photograph of it could. Two further generative surfaces beyond the signature scene: THE SELVEDGE and THE TWILL (plus THE THREAD STRIP as the continuity device). Not forced. |
| Engine profile | Baseline: Three.js r128 from cdnjs. No modern importmap profile, no post chain, no signature shader recipe (none used; the registry field is empty). |
| Media grade | "morning light on cloth": `filter: contrast(1.05) saturate(0.9) brightness(1.04);` plus an indigo #2B2F8F shadow overlay at 8 to 14 percent (`mix-blend-mode: lighten`) and a butter #F6E7A1 highlight overlay at 10 to 16 percent (`mix-blend-mode: multiply`), 12 to 24 percent total, on video and img alike, not on the product screens or the kit. Media is sourced or generated per media_engine.md and logged in MEDIA_MANIFEST.json even though the tier is 1. |
| Novelty check | All quotas clear (check_novelty.py output in Part 4 of the embedded spec). |

### 5.1 The Art Direction and Technique Stack spec, verbatim in full

[[VERBATIM BEGIN: /home/claude/savebrew/spec/art_direction_spec.md]]

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


[[VERBATIM END: /home/claude/savebrew/spec/art_direction_spec.md]]

### 5.2 Asset slots (from /home/claude/savebrew/assets/ASSET_PLAN.json)

The build composes around these slot ids. Each slot resolves to a real, self hosted file under /public/assets (served at /assets/...) or to the kit and product UI folders under /home/claude/savebrew/assets that the builder imports. No slot ships as a placeholder box, no asset is hotlinked, and each shipped asset has a MEDIA_MANIFEST.json entry (filename, source URL or generator and prompt id, licence, usage location, alt text). The creative asset engine (Step 6.5) fills the slots before a line of the site is built; a slot it could not fill is reported, not faked.

| Slot id | Page(s) | Role | Aspect | File path(s) | Generator |
|---|---|---|---|---|---|
| `video.hero-loop` | / (What did last week's pass look like? row, behind the week strip at 35 percent); /about (hero band) | 12 second silent hero loop, four 3 second clips hard cut, clean wrap | 16:9 | desktop: `/assets/video/hero-loop.mp4`; mobile: `/assets/video/hero-loop-720.mp4`; poster: `/assets/video/hero-loop-poster.webp` | higgsfield seedance_2_5 |
| `video.product-pan` | / (What's inside the dashboard? row); /membership | 6 to 8 second product in motion clip: one slow left to right pan across the three real dashboard views (Today, Rate Tracker, Goals) with one toggle click, one row ticking and one bar filling | 16:9 | desktop: `/assets/video/product-pan.mp4`; poster: `/assets/video/product-pan-poster.webp` | built: Playwright capture of the HTML views |
| `photo.about-hero` | /about | About page hero band | desktop 21:9, phone 4:5 | src: `/assets/photo/about-hero.webp` | higgsfield image |
| `photo.membership-free-column` | /; /membership | membership row fifth column background at 30 percent | 1:1 | src: `/assets/photo/membership-free-column.webp` | higgsfield image |
| `photo.todays-pass-heading` | /; /brief | What's in today's pass? heading pass background at 20 percent and the /brief header | desktop 3:1, phone 4:3 | src: `/assets/photo/todays-pass-heading.webp` | higgsfield image |
| `photo.ranker-edge` | /; /your-moves | Which threads should you pull first? row edge image | 4:5 | src: `/assets/photo/ranker-edge.webp` | higgsfield image |
| `photo.roundup-header` | /roundup | /roundup header band | desktop 16:9, phone 1:1 | src: `/assets/photo/roundup-header.webp` | higgsfield image |
| `photo.guides-header` | /guides | /guides index header | desktop 21:9, phone 4:5 | src: `/assets/photo/guides-header.webp` | higgsfield image |
| `photo.contact-side` | /contact | /contact side image beside the address | 4:5 | src: `/assets/photo/contact-side.webp` | higgsfield image |
| `photo.404` | /404 | 404 page image, a loose thread | 1:1 | src: `/assets/photo/404-loose-thread.webp` | higgsfield image |
| `photo.guide-hero.make-a-rotating-category-pay` | /guides/make-a-rotating-category-pay; /guides | guide hero | desktop 16:9, phone 4:5 | src: `/assets/photo/guide-rotating-category.webp` | higgsfield image |
| `photo.guide-hero.the-national-average-is-a-warning` | /guides/the-national-average-is-a-warning; /guides | guide hero | desktop 16:9, phone 4:5 | src: `/assets/photo/guide-national-average.webp` | higgsfield image |
| `photo.guide-hero.four-percent-against-the-account-you-have` | /guides/four-percent-against-the-account-you-have; /guides | guide hero | desktop 16:9, phone 4:5 | src: `/assets/photo/guide-four-percent.webp` | higgsfield image |
| `photo.guide-hero.why-patio-furniture-is-cheap-in-october` | /guides/why-patio-furniture-is-cheap-in-october; /guides | guide hero | desktop 16:9, phone 4:5 | src: `/assets/photo/guide-patio-october.webp` | higgsfield image |
| `product.today-desktop` | / (What's inside the dashboard?); /membership; /brief | Today view, desktop window 1440x900 at 2x, app's own bar, knot mark and wordmark left | 16:10 | src: `/assets/product/today-desktop.webp`; html: `/home/claude/savebrew/assets/product-ui/today.html` | built in HTML, screenshotted |
| `product.rates-desktop` | /; /membership | Rate Tracker view, desktop window | 16:10 | src: `/assets/product/rates-desktop.webp`; html: `/home/claude/savebrew/assets/product-ui/rates.html` | built in HTML, screenshotted |
| `product.goals-desktop` | /; /membership | Goals view, desktop window | 16:10 | src: `/assets/product/goals-desktop.webp`; html: `/home/claude/savebrew/assets/product-ui/goals.html` | built in HTML, screenshotted |
| `product.today-phone` | /; /membership | Today view, phone 375x812 at 3x, frameless | 375:812 | src: `/assets/product/today-phone.webp` | built in HTML, screenshotted |
| `product.rates-phone` | / | Rate Tracker view, phone | 375:812 | src: `/assets/product/rates-phone.webp` | built in HTML, screenshotted |
| `product.goals-phone` | / | Goals view, phone | 375:812 | src: `/assets/product/goals-phone.webp` | built in HTML, screenshotted |
| `kit.logo` | header; footer; app bar; /brand-kit/ | primary, reversed, stacked and icon only lockups of the knot mark and the SaveBrew wordmark, SVG and PNG, checked on white, on indigo and on butter |  | dir: `/home/claude/savebrew/assets/brand-kit/` | drawn |
| `kit.favicon` | (global) | favicon set: svg, 32 png, 180 apple touch, ico |  | dir: `/home/claude/savebrew/assets/brand-kit/favicon/` | drawn |
| `kit.banners` | (global) | LinkedIn cover 1128x191 and logo 400x400, X header 1500x500, Crunchbase 1200x628, OG 1200x630 |  | dir: `/home/claude/savebrew/assets/brand-kit/banners/` | built in HTML, screenshotted |
| `kit.svg` | (global) | the graphic kit: the Knot motif, the Selvedge Seal, the thread strip, the weft pass divider, the eleven icons, four guide graphics (one per post), the 404 loose thread |  | dir: `/home/claude/savebrew/assets/kit-svg/` | drawn |
| `texture.fabric` | (global) | one CC0 plain weave cotton or linen colour map, 1K, WebP, for the mobile poster ground and the 404 field |  | src: `/assets/texture/fabric-1k.webp` | Poly Haven CC0 (fallback: procedural canvas weave rendered to WebP) |


Weight budget from the asset plan, checked as a QA gate: total 9,000 KB; hero loop desktop 2,600 KB, mobile 1,200 KB; product pan 1,500 KB; each still at most 180 KB at 1600 wide; each product shot at most 260 KB; each kit SVG at most 24 KB; the fabric texture at most 320 KB. Each photograph ships as WebP with a responsive srcset and the IMG-019 crops per breakpoint; everything below the fold is lazy loaded; the video is muted, loops, plays inline, carries its poster, and pauses when offscreen.

Alt text rules: the loom canvas and the kit dividers are decorative and aria hidden (the five items exist as real text); the video carries `aria-hidden="true"` with the row's heading as the accessible name; each photograph carries a short factual alt in the copy voice (for example "Undyed cotton warp threads under tension on a loom, morning light from the left"); the product shots carry alts naming the view ("The Today view of the SaveBrew dashboard for the illustrative member Jordan"); the seal carries `footer.seal.alt`.

### 5.3 Media Direction reference

The Media Direction block is section 3.22 of the embedded spec above (subject world, the four hero loop clips with their generation prompts, the built product pan, the eight site photographs with prompt, slot, aspect and page, the four guide heroes, the grade recipe, and the two texture assets). The creative asset engine generates through the Higgsfield MCP (owner decision) using those prompts literally, sources the fabric texture from Poly Haven under CC0, and records everything in /home/claude/savebrew/assets/ASSET_PLAN.json and MEDIA_MANIFEST.json. The usage fences of media_engine.md hold: stock and generated media play environment, texture and mood only; nothing plays the product (the product is the built dashboard); no people, no hands, no faces, no third party logos, no text in any image, no coffee cup, no beer glass.

## 6. Global Elements

Each element here is built once and included on each route, so the nav, the purchase CTA, the cart, the address, the legal links and the SMS block are identical site wide. Strings are copy.md ids with the string beside them.

### 6.1 Header: the heading band

- Treatment (Art Direction 3.5 and proposed.json `nav_style`): an opaque white weft band, 84px tall at 1440 (64px at 375), full width with `--gutter` padding, sitting on the butter ground with a deep butter 1px lower edge. It hides on scroll down and returns on scroll up (translateY, Shuttle, base 0.38s). No condensing, no rule, no dateline, no perforation, no marker glyph on the active link. Skip link first in the DOM: `global.skip` "Skip to the content".
- Left: the knot mark and the Big Shoulders Display wordmark from /home/claude/savebrew/assets/brand-kit (primary lockup on white), 24px tall, alt `global.wordmark.alt` "SaveBrew" → `/`.
- Centre left, the four destination links in Manrope 600 at 15px, the active link at weight 800 and indigo, hover the page's own text hover treatment: `nav.roundup` "Roundup" → `/roundup`; `nav.guides` "Guides" → `/guides`; `nav.moves` "Your moves" → `/your-moves`; `nav.membership` "Membership" → `/membership`.
- Right: `nav.about` "About" → `/about`; `nav.contact` "Contact" → `/contact`; `nav.signin` "Sign in" → `/sign-in` (or `/today` when a demo session exists); the spool cart glyph (kit icon) with a stitched count, label `nav.cart.label` "Cart", aria `nav.cart.aria.pattern` "Cart, {count} membership" or `nav.cart.aria.empty` "Cart, empty" → opens the cart drawer (6.5); the compact Bobbin `nav.cta.compact` "Add the Daily to my cart" → adds SB101 (monthly) to the cart and opens the drawer, visually subordinate to the hero Bobbin (smaller, white fill, indigo stitch, indigo label).
- Phone widths (375 to 767): the band carries the wordmark, the cart control with count, a `nav.membership` "Membership" link and the `nav.menu.open` "Menu" control. The menu opens as a full height white sheet with a weft pass wipe from the right (Shuttle): the seven links in order, `nav.signin`, the reduce motion control (6.7), the address line, and `nav.menu.close` "Close the menu". Focus is trapped in the sheet while open; Escape closes it.
- Directly under the band on phone widths, on each route: the five thread tab strip, 44px, sticky, aria `tabstrip.aria` "The five threads", hint `tabstrip.hint` "Tap a thread to jump to its item" (announced once). The five tabs are `thread.rates` "Rates", `thread.cashback` "Cashback", `thread.coupons` "Coupons", `thread.seasonal` "Seasonal", `thread.paycheck` "Paycheck"; tapping one scrolls to that thread's cell in the current row (Art Direction part 0.2).
- Motion: the Bobbin idle stitch travels the border once per 11s idle cycle; link hover per page; `:focus-visible` 2px indigo ring with a 2px white offset. Reduced motion: the band shows and hides without transition.

### 6.2 Footer: a destination on the twill

The footer is a full width pass on THE TWILL (generative surface two, 6 percent contrast), five columns, three rows, no default horizontal rule. Entrance: the Selvedge Seal weaves itself row by row (Shuttle per row), the border stitches last (Knot), then the link columns wipe in as one weft pass. Reduced motion: static.

Row one, the five link columns (Manrope 600 13px headings in Big Shoulders 600 15px, links Manrope 15px indigo, hover the page's treatment):

- Column one, `footer.col.1.heading` "The brief": `footer.col.1.link.brief` "Today's brief" → `/brief`; `footer.col.1.link.moves` "Your moves" → `/your-moves`; `footer.col.1.link.signin` "Sign in" → `/sign-in`.
- Column two, `footer.col.2.heading` "Free to read": `footer.col.2.link.roundup` "The Roundup" → `/roundup`; `footer.col.2.link.guides` "The Guides" → `/guides`; `footer.col.2.link.rss` "Follow the Roundup by RSS" → `/roundup/feed.xml`.
- Column three, `footer.col.3.heading` "Membership": `footer.col.3.link.daily` "The Daily" → `/membership#daily`; `footer.col.3.link.two` "The Daily for Two" → `/membership#daily-for-two`; `footer.col.3.link.cart` "Your cart" → `/cart`.
- Column four, `footer.col.4.heading` "SaveBrew": `footer.col.4.link.about` "About" → `/about`; `footer.col.4.link.contact` "Contact" → `/contact`; the reduce motion control (6.7); the SMS reminder link, the block heading string `sms.block.heading` "Join Our SMS List" → `/#sms` (the home row; the block itself is not repeated in the footer).
- Column five, `footer.col.5.heading` "Legal": `footer.col.5.link.terms` "Terms of Service" → `/terms`; `footer.col.5.link.privacy` "Privacy Policy" → `/privacy`.

Row two, the identity pass:

- Columns one to two: the Selvedge Seal at 160px (kit.svg, alt `footer.seal.alt` "The Selvedge Seal, SaveBrew's woven monogram") with `footer.seal.line` "Tomorrow's pass goes out at 6:30 AM Eastern." beneath it, replaced from 6:30 AM Eastern on Friday until 6:30 AM Eastern on Monday by `footer.seal.line.weekend` "Monday's pass goes out at 6:30 AM Eastern." (computed on the client from the Eastern clock so the line is true on the day it is read), then `footer.brand` "The five threads, checked before six each weekday."
- Column three, the address block as an `address` element: `footer.address.entity` "SaveBrew Inc.", `footer.address.street` "660 American Ave", `footer.address.city` "King Of Prussia, PA 19406". This is the public physical address; it is not the EIN address and it is not blank.
- Column four: `footer.phone` "(888) 338 8809" → `footer.phone.href` tel:+18883388809; `footer.email` "support@savebrew.com" → mailto:support@savebrew.com.
- Column five: `footer.copyright` "© 2026 SaveBrew Inc."

Row three, across all five columns: `footer.disclaimer` (the string of `disclaimer.text`, section 3), Manrope 13px muted indigo.

Phone widths: the columns stack in one column in the order above; the seal sits at 96px beside the seal line.

### 6.3 The SMS opt in block, verbatim (Join Our SMS List)

Reproduced from the finalshot kit's sms_optin_block.md with exactly four substitutions: the brand name (SaveBrew), the phone ((888) 338-8809 as the kit formats it), the support email (support@savebrew.com) and the two links ("Terms" → `/terms`, "Privacy Policy" → `/privacy`, in both checkbox labels). Nothing else is reworded, reordered, shortened or added. Both checkboxes are unchecked by default. The consent text ends "Read our Terms and Privacy Policy". One opt in, one program (SaveBrew account notifications, section 9); the checkout carries no SMS consent and the phone field at checkout is not consent.

[[VERBATIM BLOCK BEGIN]]

- Heading (`sms.block.heading`): Join Our SMS List
- Phone field placeholder (`sms.block.phone.placeholder`): Your Phone Number
- Consent checkbox 1, unchecked by default (`sms.block.consent.1`): I agree to the Terms & Privacy Policy
  ("Terms" links to `/terms`; "Privacy Policy" links to `/privacy`.)
- Consent checkbox 2, unchecked by default (`sms.block.consent.2`): I agree to receive SMS marketing notifications from SaveBrew. Reply HELP for help or call/email (888) 338-8809 / support@savebrew.com STOP to cancel. Msg & data rates may apply. Msg frequency varies. Information gathered in the SMS campaign will not be shared with third parties or affiliates for marketing purposes. Read our Terms and Privacy Policy.
  (The trailing "Terms" links to `/terms`; "Privacy Policy" links to `/privacy`.)
- Button (`sms.block.button`): Submit

[[VERBATIM BLOCK END]]

Where it renders: on Home as row nine, a full width inline band (heading left in Big Shoulders 700, the two consent lines across the middle columns in Manrope 15px with real checkboxes at 24px and 44px targets, the phone field and the Submit control at the right end, the selvedge stitch as the field's underline that draws on focus); on /confirmation as its own optional step after the dashboard section (section 7); inside the dashboard's Texts card when texts are off (section 7, /today). The field has a visible label for assistive tech ("Your Phone Number", visually the placeholder text is also the label above the field so the placeholder is not the only label), `type="tel"`, `autocomplete="tel"`, `inputmode="tel"`.

States (microcopy added here; copy.md has no strings for these, and none of it touches the block's wording):

- Sending: `add.sms.sending` "Sending your number" replaces the button label while the request is in flight; the button is disabled for the duration only.
- Success (replaces the form with a confirmation line, aria live polite): `add.sms.success` "Thanks. A confirmation text is on its way to {phone}. Reply STOP to any text to end them; ending texts does not cancel a membership." Example: "Thanks. A confirmation text is on its way to (555) 010 0123. Reply STOP to any text to end them; ending texts does not cancel a membership."
- Validation, GOV.UK standard (beside the field or box, repeated in a summary above the button titled `add.sms.error.summary` "There is a problem", the number typed preserved): phone empty `add.sms.error.phone.empty` "Enter your phone number"; phone format `add.sms.error.phone.format` "Enter a phone number with 10 digits, like (555) 010 0123"; first box unticked `add.sms.error.consent.1` "Check the first box to agree to the Terms & Privacy Policy"; second box unticked `add.sms.error.consent.2` "Check the second box to agree to receive SMS notifications from SaveBrew". Validate on blur with a short delay, not while typing; the error carries text and a knot glyph beside the red, not colour alone.
- System failure: `add.sms.error.system` "Sorry, that didn't go through. Try again in a minute, or email support@savebrew.com and we'll add your number by hand."
- The preview build stores nothing and sends nothing; the success state still renders so the flow is complete.

### 6.4 As Seen In and social links: omitted

- As Seen In / Featured In: omitted, because no qualifying press exists (research brief section 4: no press about this brand; every "SaveBrew" result belongs to SaveOnBrew). No outlet logos, no placeholder row. If validated press appears after the press release step, it is added then with clickable links to the live articles.
- Social links: omitted, because no brand owned page exists (research brief section 5: the @savebrew handles are unclaimed or absent on YouTube, Instagram, LinkedIn, X, Facebook and TikTok; the only hits belong to SaveOnBrew). No icons, no dead links. Added when the presence step claims the handles.
- Testimonials and ratings: omitted, none exist. No substitute device.

### 6.5 The cart drawer (on any route) and /cart

Opens from the right with a weft pass wipe (Shuttle, base) when a Bobbin adds a membership or the spool glyph is pressed; scene: the knot slides along a thread into the spool glyph (Knot). Focus moves to the drawer heading; Escape and `cart.close` "Close" return focus to the trigger. Contents, top to bottom:

- `cart.heading` "Your cart".
- The line item: `cart.line.pattern` "{membership}, billed {cadence}" (example `cart.line.example` "SaveBrew Daily, billed monthly"), with `cart.quantity.note` "One membership per order." Quantity is fixed at 1; adding a different membership replaces the current one and announces `cart.replace.pattern` "Your cart now holds {new membership}, {new cadence}. {old membership}, {old cadence}, was removed." (example "Your cart now holds SaveBrew Daily for Two, yearly. The Daily, monthly, was removed."). Adding announces `cart.added.pattern` "Added. {membership}, billed {cadence}, is in your cart." (aria live polite).
- `cart.charge.label` "Today's charge" with the amount ($7.99, $72, $11.98 or $108).
- The renewal sentence: `cart.renewal.monthly.pattern` "Renews on {date in words} for {amount}, then monthly at the same price until you cancel." (example "Renews on October 24, 2026 for $7.99, then monthly at the same price until you cancel.") or `cart.renewal.yearly.pattern` "Renews on {date in words} for {amount}, then yearly at the same price until you cancel. We email you 30 days before." (example "Renews on September 24, 2027 for $72, then yearly at the same price until you cancel. We email you 30 days before."). Dates are computed from today's date.
- `cart.tax` "Sales tax is included where it applies. There are no other fees."
- The cadence switch, a two option toggle (CUR-009, role radiogroup, aria `cart.cadence.aria` "Billing cadence") with `cart.cadence.monthly` "Monthly" and `cart.cadence.yearly` "Yearly"; switching re-renders the charge, the renewal sentence and the note `cart.cadence.note.yearly.pattern` "Yearly makes today's charge {amount} and moves the next renewal to {date in words}." (example "Yearly makes today's charge $72 and moves the next renewal to September 24, 2027.") or `cart.cadence.note.monthly.pattern` "Monthly makes today's charge {amount} and moves the next renewal to {date in words}." (example "Monthly makes today's charge $7.99 and moves the next renewal to October 24, 2026."). Switching cadence swaps the SKU (SB101 to SB102, SB201 to SB202 and back).
- `cart.remove` "Remove" → empties the cart and announces `cart.removed` "Removed. Your cart is empty."
- The Bobbin `cart.checkout` "Go to checkout" → `/checkout`.
- Empty state (no membership): `cart.empty.line` "Your cart is empty." and the link `cart.empty.link` "Choose a membership" → `/membership`.
- Persistence: localStorage key `savebrew.cart` holding `{sku, cadence, addedAt}`, an in memory fallback when storage throws; the count in the heading band updates on each change; the cart survives navigation between routes (QA adds a membership, opens two other routes, returns).
- /cart renders the same contents as a full page (head title `head.cart.title`, meta `head.cart.meta`, noindex) for visitors who open the footer link or land without JavaScript.

### 6.6 The loader: the selvedge stitch

Per Art Direction 3.18 and preloader_module.md. The page paints in full at first paint; a dashed indigo running stitch (stroke-dasharray 6 4, 2px, on the Selvedge canvas, role progressbar with aria-valuenow, label `loader.aria` "Loading SaveBrew") draws down the left gutter with its length bound to the real load fraction (fonts ready, kit SVG ready, poster decoded, Three.js fetched); at ready it ties off with a knot (Knot, 0.38s). Skip: `loader.skip` "Go straight in", an indigo text link at the bottom centre from 0s, completes the stitch at once; the stitch force completes at the 4s hard cap; target under 2s on broadband. The hero copy, nav and Bobbin are plain DOM beneath it and not covered. Reduced motion (or `?qa=rm`): the stitch renders complete and fades in 0.3s. No count, no Flip, no overlay.

### 6.7 The reduce motion control

In footer column four and in the mobile menu: a switch (CUR-009, role switch, 44px target) labelled `motion.label` "Reduce motion" with states `motion.state.on` "On" and `motion.state.off` "Off"; announces `motion.announce.on` "Motion is reduced across the site." or `motion.announce.off` "Motion is back on." (aria live polite). Persisted in localStorage as `savebrew.motion`; sets `data-motion="reduced"` on the root; honoured by each technique (Art Direction 3.13). `prefers-reduced-motion: reduce` and the `?qa=rm` hook set the same attribute.

### 6.8 Kit elements on each route

- The thread strip (kit divider b) at the head of each row board; the selvedge (kit divider a) as the row divider and card edge; the weft pass (kit divider c) under each heading pass; the knot beside each cell head and as the favicon; the eleven icons for Rates, Cashback, Coupons, Seasonal, Paycheck, Goals, Texts, Archive, Your moves, Roundup and Membership; the Selvedge Seal in the footer and on About, the confirmation and the membership cards' corner. Imported from /home/claude/savebrew/assets/kit-svg, not redrawn per page.
- The compact membership strip on interior routes (/brief, /roundup, /guides, each guide, /about): two cards on the twill, each with the name, the price line and the Bobbin, plus that route's own one line and the link: `compact.daily.name` "SaveBrew Daily", `compact.daily.price` "$7.99 billed monthly, or $72 billed yearly", Bobbin `compact.daily.cta` "Add the Daily to my cart" → adds SB101 and opens the drawer; `compact.two.name` "SaveBrew Daily for Two", `compact.two.price` "$11.98 billed monthly, or $108 billed yearly", Bobbin `compact.two.cta` "Add the Daily for Two to my cart" → adds SB201 and opens the drawer; `compact.link` "What each membership includes" → `/membership`. The strip does not repeat the home cards' copy.
- The disclaimer (`disclaimer.text`) on each content route in the position section 7 gives.
- Head hygiene on each route: `lang="en"`; a unique title and meta description (section 7, from copy.md `head.*`); canonical URL; the favicon set from /home/claude/savebrew/assets/brand-kit/favicon (svg, 32px png, 180px apple touch, ico); the Open Graph image from kit.banners (the 1200 by 630 OG banner built from the kit) on each route; `noindex` on /today, /rates, /goals, /archive, /sign-in, /cart, /checkout and /confirmation; the public routes indexed; RSS feeds at /roundup/feed.xml and /guides/feed.xml linked with `rel="alternate"`.
- QA hooks, inert for visitors: `?qa=rm` forces the reduced motion path; `?qa=arc` logs THE PASS timeline's start and end scroll positions to the console on Home.

## 7. Page by Page Specification

Twenty three routes, each specified below in the same order: purpose; sections top to bottom with the copy pasted in; each button, link and CTA as label → destination → action; forms with fields, required or optional, validation and the GOV.UK error strings; the route's own scroll scene, text hover treatment and per section entrance; the asset slots it uses; mobile notes; the head title and meta description. The routes: `/`, `/brief`, `/membership`, `/roundup`, `/guides`, `/guides/make-a-rotating-category-pay`, `/guides/the-national-average-is-a-warning`, `/guides/four-percent-against-the-account-you-have`, `/guides/why-patio-furniture-is-cheap-in-october`, `/your-moves`, `/about`, `/contact`, `/cart`, `/checkout`, `/confirmation`, `/today`, `/rates`, `/goals`, `/archive`, `/sign-in`, `/terms`, `/privacy` and the 404. Aliases served as 301 redirects by the catch all: `/terms-of-service` → `/terms`, `/privacy-policy` → `/privacy`, `/roundup/2026-09-19` → the current Roundup (a stable address, served with a 200 rather than a redirect, so the issue keeps its own URL once a second issue exists).

Rules that apply to all routes (Art Direction 3.23): no two adjacent rows share a pattern and a page never uses one pattern twice; each row has its own entrance, with the weft pass wipe (MOT-018, `clip-path: inset(0 100% 0 0)` to `inset(0 0 0 0)`, Shuttle, `animation-timeline: view()`, `animation-range: entry 0% cover 35%`, ScrollTrigger fallback on Safari) as the base language, varied by direction, stagger and what draws; each route has its own text hover treatment mirrored on `:focus-visible` (keyboard users get a 2px stitch outline where the pointer treatment would displace text); each route has its own lightweight scene from 3.7 (one canvas or one SVG, lazy after first paint, paused offscreen, disposed on navigation, static under reduced motion); each route carries the thread strip somewhere; the disclaimer runs on each content route; each button, link, heading, card, chip, toggle and field has idle, hover or focus, and press movement using Shuttle and Knot only; each route has at least one interactive moment beyond its hero; each route's emblems, dividers and icons come from the kit. Section titles are the heading passes, set as questions where the reader is asking one.

Vocabulary for any microcopy the builder must add (Offering Spec section 16, verbatim; Art Direction 3.24 adds the ten words used and the ten refused):

## 16. VOCABULARY AND VOICE NOTES FOR THE COPY STEP

- The paid product is "the Daily" or "SaveBrew Daily"; the word "membership" is the customer facing noun; "subscription" appears in legal text only. The owner's flagship name "SaveBrew Daily Digest" may be used in full on the About and legal pages.
- Free content is "free to read" and its readers are "readers", not "free members".
- Exclusion 3.7 lists plan, file, page, desk, month, day, kept, keep, killed, log, row, figure, cite, never, nothing, every, sample, memo, queue, calendar, tape, receipt, gate, climb, base camp, switchback and route as sister site vocabulary. Customer facing copy in this spec avoids them ("billed monthly" not "a month", "each weekday" not "every day", "illustrative" not "sample", "monthly deposit" not "monthly plan", "seasonal buying cycle" not "calendar"). "Daily" is the owner's product name and stands.
- The excluded CTA verbs (Purchase, Buy, Use, Subscribe, Order, Run, Start, Empty, Check, Compare, Read, See, Submit) do not appear on any button. In app buttons use Set, Open, Add, Save, Remind, Adjust, Apply, Invite, Resume, Cancel, Pay.
- The money meaning of "brew" must land in the first line of the hero and the meta description (the SaveOnBrew collision). No coffee cup, no beer glass.
- No dashes of any kind in any customer facing text, including inside the product UI.
- Open ground that no sister site uses: a question headline, a first person voice, an address to a named reader.


### 7.1 Home (/)

**Purpose.** Make the money meaning of "brew" land in the first line, show the product (today's pass) as the page's own structure, and sell the Daily: one primary action per view, "Add the Daily to my cart".

**Head.** Title `head.home.title` "SaveBrew Daily: five money moves each weekday morning". Meta `head.home.meta` "What's brewing in savings rates, cashback windows, coupon codes and seasonal prices, checked overnight and on your dashboard by 6:30 AM Eastern.". Indexed.

**Scene.** The Loom, TEX-008, the signature scene of Art Direction 3.6 and 3.7: five Line2 warp threads at the DOM column centres, the weft passing and knotting once per warp, ten woven weekday rows behind, the reed sweep (progress 0 to 0.45), the held beat THE PASS (0.45 to 0.6, Knot overshoot, 90ms butter flash), the gravity flip (0.6 to 0.9, camera 12 to 88 degrees, the five DOM cells docking onto the five warp positions), the handoff to the thread strip (0.9 to 1.0, GSAP Flip onto the SVG twin). Signature scroll length 1.3 viewport heights, native scroll, the canvas a fixed layer, not pinned. Alive on load (7s sag cycle, 11s weft creep, 1 degree pointer drift). Poster: a 1600px WebP of the flat cloth at progress 1.0 with 4 percent grain baked in. `?qa=arc` logs the timeline's start and end scroll positions. Fallbacks per 3.7 and 3.13.

**Text hover.** The plucked thread (TEX-007): headings ripple once on hover through an SVG feTurbulence (baseFrequency 0.012) and feDisplacementMap whose scale animates 0 to 6 to 0 over 0.38s (Knot); `:focus-visible` gets the 2px stitch outline instead; pointer only, headings only, off under reduced motion. Links: the running stitch underline draws left to right (Shuttle, 0.11s).

**Asset slots.** `video.hero-loop` (row 4, behind the week strip at 35 percent, graded), `photo.todays-pass-heading` (row 2 heading pass background at 20 percent), `photo.membership-free-column` (row 3, column five, at 30 percent), `video.product-pan` and `product.today-desktop`, `product.rates-desktop`, `product.goals-desktop`, `product.today-phone`, `product.rates-phone`, `product.goals-phone` (row 5), `photo.ranker-edge` (row 6, the row's edge image), `kit.svg` throughout, `texture.fabric` (the mobile poster ground).

**Sections, top to bottom.**

1. **Hero: the loom.** Full bleed on butter. The heading band above it (6.1). Plain DOM at first paint, in this order: the H1 `home.hero.h1` "Which of the five threads your money runs on moved overnight?" in Big Shoulders Display across all five columns (two lines at 1440, one from about 2200px), running The Tightening once on load (each glyph pulls from wght 500 to 800 left to right at 18ms per glyph, Knot, finishing as the weft knots the fifth warp; wght 800 at once under reduced motion); the standfirst `home.hero.standfirst` "SaveBrew Daily: five short money moves on your dashboard by 6:30 AM Eastern, pulled from the savings rates, cashback windows, coupon codes, seasonal prices and paycheck habits we checked overnight. $7.99 billed monthly, or $72 for the year." in Manrope 19px across columns one and two (this is where the price lives; it is not inside or under a button); the audience line `home.hero.audience` "written for people with a job and four minutes, not a finance degree" in column three, muted indigo; the Bobbin `home.hero.cta` "Add the Daily to my cart" in column one at about y 490px; beneath it the plain indigo text link `home.hero.link` "Open this week's free roundup" at clearly lower weight. At the bottom of the viewport, in columns one to five, the five knot labels `home.hero.knot.rates` "Rates", `home.hero.knot.cashback` "Cashback", `home.hero.knot.coupons` "Coupons", `home.hero.knot.seasonal` "Seasonal", `home.hero.knot.paycheck` "Paycheck" (group aria `home.hero.knots.aria` "Today's pass: Rates, Cashback, Coupons, Seasonal, Paycheck"), which at 1920 and 2560 also carry the item headlines beneath them. The loom canvas is aria hidden (`home.hero.poster.alt` is empty). Buttons and links: **Add the Daily to my cart** → adds SB101 (SaveBrew Daily, monthly) to the cart and opens the cart drawer, where the yearly switch is offered; **Open this week's free roundup** → `/roundup`. Entrance: the opening beat of Art Direction 3.2: the selvedge stitch draws down the left gutter and ties off, the loom is already alive beneath the H1, the weft passes and The Tightening runs. First viewport placement and motion clearance exactly as the Comprehension Block (3.5): all three answers readable at 0.8s with the loader active.

2. **What's in today's pass?** Heading pass `home.pass.heading` "What's in today's pass?" set full width on butter with `photo.todays-pass-heading` behind at 20 percent and the weft pass thread beneath. Intro line `home.pass.intro` "Thursday, September 24, published 6:30 AM ET: one item on each of the five threads, as a member read them this morning. Four minutes, start to finish.". Then the row board: five cells, one per thread, each with the knot glyph, the thread name (`home.pass.thread.rates` "Rates" and the four others), the headline in Big Shoulders 600, the two line summary in Manrope, and the action chip. The five items are the fixed TODAY items of brief_items.md (pasted below this route's spec), item five relabelled Paycheck on the marketing site. Chips: `home.pass.chip.rates` "Open tracker", `home.pass.chip.cashback` "Remind me", `home.pass.chip.coupons` "Save code", `home.pass.chip.seasonal` "Open playbook", `home.pass.chip.paycheck` "Open worksheet"; on the public site they are inert (a button with `aria-disabled`, press feedback still plays) and carry the tooltip `home.pass.chip.tip.pattern` "A member's action. On the dashboard, {chip} does exactly that." (example "A member's action. On the dashboard, Save code does exactly that."). Link row beneath the cells: **Open today's brief in full** (`home.pass.link.brief`) → `/brief`; **Look inside the dashboard** (`home.hero.link.dashboard`, the Offering Spec's product tour control) → scrolls to row 5 (`#dashboard`). Entrance: the five cells dock onto the warp positions as the loom lays flat (Knot, 0.38s, 40ms stagger left to right), the thread strip landing at the head of the row.

3. **What does it cost?** Heading pass `home.cost.heading` "What does it cost?". The membership row: the Daily card spanning columns one to two, the Daily for Two spanning three to four, the fifth column on the twill with `photo.membership-free-column` at 30 percent. One card system (Offering Spec 10.4): name, the one line audience, the price line with both prices and the renewal sentence at the same weight, the arithmetic line, the inclusion list in full (each item marked by the knot, not a numeral), the tax line, the refund line, the Bobbin. A cadence control above the two cards (Monthly | Yearly, two toggles that ply together, monthly selected by default, aria `membership.cadence.aria` "Billing cadence") changes only the button label; both prices stay printed. The Selvedge Seal at 96px in each card's corner. No badge, no giant numeral, no $0 card, no stepper, no TOTAL line, no rolling numerals, no price inside or under a button.

   The Daily card (id `daily`): `home.cost.daily.name` "SaveBrew Daily"; `home.cost.daily.audience` "One reader: the brief, the tracker, the goals and the archive on one dashboard."; `home.cost.daily.price` "$7.99 billed monthly, or $72 billed yearly."; `home.cost.daily.arithmetic` "Twelve monthly payments come to $95.88. The year costs $72, which is $6 monthly."; `home.cost.daily.renewal` "Monthly renews at $7.99 until you cancel. Yearly renews at $72, with an email 30 days before (and a text, if you've opted in)."; `home.cost.daily.inclusions.label` "Included, in full:"; then the eight inclusions, name in Manrope 700 and description beside it:
   - `home.cost.daily.inc.1.name` "The morning brief." `home.cost.daily.inc.1.desc` "Five items, about four minutes to read, on the dashboard by 6:30 AM Eastern each weekday: savings rate movements, cashback and coupon opportunities, seasonal spending strategy, budgeting frameworks and money management techniques. Each item ends with one small action."
   - `home.cost.daily.inc.2.name` "The Rate Tracker." `home.cost.daily.inc.2.desc` "Published rates for the high yield savings accounts, money market accounts and CDs on SaveBrew's checked list (twenty at launch), checked each morning, with a 30 day history per account, a slot to type in your own account's rate for comparison, and alert thresholds you set yourself."
   - `home.cost.daily.inc.3.name` "Goals." `home.cost.daily.inc.3.desc` "Up to six savings goals, each with a target, a date, a monthly deposit, an on track status, a deposit streak and milestone marks at 25, 50, 75 and 100 percent. SaveBrew records what you type; it does not hold or move money."
   - `home.cost.daily.inc.4.name` "Saved items." `home.cost.daily.inc.4.desc` "The codes, category activations and deadlines you save from the brief, in one list with their expiry dates, with reminders on the dashboard and by email."
   - `home.cost.daily.inc.5.name` "Playbooks and worksheets." `home.cost.daily.inc.5.desc` "The monthly seasonal playbook (what to buy now and what to wait on) and fillable worksheets for the frameworks the brief covers, starting with the 50/30/20 tune up and the paycheck split."
   - `home.cost.daily.inc.6.name` "The archive." `home.cost.daily.inc.6.desc` "Each brief published since launch, including the ones before you joined, searchable by topic and by date."
   - `home.cost.daily.inc.7.name` "Account texts, if you opt in." `home.cost.daily.inc.7.desc` "Alerts you set on tracked rates and goals, billing and renewal notices, sign in codes, confirmations when you change settings, and replies from support. None of it promotional. Reply STOP to end texts at any time."
   - `home.cost.daily.inc.8.name` "Two click cancellation." `home.cost.daily.inc.8.desc` "Membership, then Cancel membership, from your dashboard. Access continues to the end of the period you paid for and a Resume link stays there until it does."

   Then `home.cost.daily.tax` "The price shown is the price charged, sales tax included where it applies. No fee is added for setup, for cancelling or for inviting a second reader."; `home.cost.daily.refund` "A yearly membership is refundable in full within 14 days of the order date, on request to support@savebrew.com. Monthly memberships aren't refunded; cancelling stops the next charge and access runs to the end of the paid period."; the Bobbin: with Monthly selected **Add the Daily to my cart** (`home.cost.daily.cta.monthly`) → adds SB101 and opens the drawer; with Yearly selected **Add a year of the Daily to my cart** (`home.cost.daily.cta.yearly`) → adds SB102 and opens the drawer.

   The Daily for Two card (id `daily-for-two`): `home.cost.two.name` "SaveBrew Daily for Two"; `home.cost.two.audience` "Two readers who share savings goals: two sign ins, one bill."; `home.cost.two.price` "$11.98 billed monthly, or $108 billed yearly."; `home.cost.two.arithmetic` "That's $5.99 a reader monthly. Twelve monthly payments come to $143.76; the year costs $108, which is $4.50 a reader monthly."; `home.cost.two.renewal` "Monthly renews at $11.98 until you cancel. Yearly renews at $108, with an email 30 days before (and a text, if you've opted in)."; `home.cost.two.inclusions.label` "Included, in full, for both readers:"; inclusions one to eight duplicated verbatim from the Daily card in the same order (`home.cost.two.inc.1.to.8`), then:
   - `home.cost.two.inc.9.name` "Two sign ins on one bill." `home.cost.two.inc.9.desc` "Each reader has their own dashboard, their own morning brief view, their own saved items and their own text settings and opt in."
   - `home.cost.two.inc.10.name` "Shared goals." `home.cost.two.inc.10.desc` "Any goal can be marked shared; both readers can record deposits and both see one progress bar. Private goals stay private to the reader who made them."
   - `home.cost.two.inc.11.name` "The invite." `home.cost.two.inc.11.desc` "The second reader is invited by email from the dashboard after the order is placed. No detail about them is asked for at checkout."

   Then the tax line and the refund line (`home.cost.two.tax` and `home.cost.two.refund`, the same strings as the Daily's); the Bobbin: Monthly **Add the Daily for Two to my cart** (`home.cost.two.cta.monthly`) → adds SB201 and opens the drawer; Yearly **Add a year of the Daily for Two to my cart** (`home.cost.two.cta.yearly`) → adds SB202 and opens the drawer.

   The fifth column: `home.cost.free.heading` "What's free to read" (an H3, not a heading pass); `home.cost.free.line` "The Roundup each Saturday, the Guides and Your moves are public: full text, no account. Open them as often as you like."; links **Open this week's free roundup** (`home.cost.free.link.roundup`) → `/roundup`; **Open the guides** (`home.cost.free.link.guides`) → `/guides`; **Open Your moves** (`home.cost.free.link.moves`) → `/your-moves`. Entrance: the weft pass draws under the heading, then the two cards wipe in from the left (Shuttle, base) one after the other, the fifth column last; the cadence toggles click once (Knot).

4. **What did last week's pass look like?** Heading pass `home.week.heading` "What did last week's pass look like?". Framing line `home.week.framing` "Monday, September 14 to Friday, September 18. Five threads, five mornings, twenty five items, and each morning's five read in about four minutes." and the hint `home.week.hover` "Hover or tap a knot to read that morning's item.". The week strip: a full width horizontal woven band (`width: 100vw`, no inset) with `video.hero-loop` behind it at 35 percent under the grade, and on it the knot matrix (Recipe 08): five threads (rows, labelled with the thread names) by five weekdays (columns, labelled `home.week.column.monday` "Monday 14", `home.week.column.tuesday` "Tuesday 15", `home.week.column.wednesday` "Wednesday 16", `home.week.column.thursday` "Thursday 17", `home.week.column.friday` "Friday 18"), twenty five knots. Each knot is a button (44px target, aria `home.week.knot.aria.pattern` "{weekday}, {date}, {thread}: {headline}", example "Tuesday, September 15, Cashback: October to December categories published: warehouse clubs, and online retail."); hover or tap or focus opens that morning's item beneath the strip (headline and summary from the LAST WEEK'S PASS data of brief_items.md, pasted below), the open item replacing the previous one with a weft pass. Entrance: the knots tie in row by row, Monday to Friday (Knot, 40ms stagger), the video fading up under them. Interactive moment: the twenty five knots.

5. **What's inside the dashboard?** (`id="dashboard"`.) Heading pass `home.dashboard.heading` "What's inside the dashboard?". Framing `home.dashboard.framing` "Three views, built the way the product is built, not drawn: pick a thread to switch between them. The accounts and rates shown are illustrative; a member's own view carries the rates we checked that morning.". The desktop window (Offering Spec 10.1 form factor A, the app's own bar as the frame, radius 12px, hairline outline, on butter) spans columns one to three; the phone view (form factor B, frameless, radius 20px) spans four to five with a clear gutter, not overlapping. On entering the viewport the desktop window plays `video.product-pan` once (muted, inline, poster first, ungraded) and then rests on the still of the selected view. The view switch is a thread strip of three (radiogroup, aria `home.dashboard.switch.aria` "Dashboard view"): `home.dashboard.view.today.name` "Today" with caption `home.dashboard.view.today.caption` "The five items, the rate strip above them, and your goal snapshot and text switches beside them." (stills `product.today-desktop` and `product.today-phone`); `home.dashboard.view.rates.name` "Rates" with `home.dashboard.view.rates.caption` "Twenty accounts and CDs checked each morning, a 30 day line for each, and the alert you set." (`product.rates-desktop`, `product.rates-phone`); `home.dashboard.view.goals.name` "Goals" with `home.dashboard.view.goals.caption` "Up to six goals, each with a target, a date and a monthly deposit, and the deposit streak beneath." (`product.goals-desktop`, `product.goals-phone`). Beneath the phone: `home.dashboard.phone.caption` "The same views at phone width: one column, the tabs in a strip under the bar.". The row's control `home.dashboard.control` "Look inside the dashboard" is the switch's visible label and the scroll target of the row 2 link. Each still links to `/sign-in` (title "Open the demo dashboard"). Entrance: each view populates top to bottom at 40ms stagger (the modules wipe in one after another), and one Texts toggle clicks on in the Today rail (Knot). Interactive moment: the switch.

6. **Which threads should you pull first?** Heading pass `home.ranker.heading` "Which threads should you pull first?". Intro `home.ranker.intro` "Turn on what's true of your money and this week's public moves change order. The four at the top are the ones worth your minutes; the rest say why they ranked lower.". The ranker embedded: the six toggles and the ranked top four, the same component, strings, data and logic as `/your-moves` (7.10), with `photo.ranker-edge` as the row's edge image in column five at 4:5. Link beneath: **Open Your moves for the full list, the minutes each takes and a copy you can print.** (`home.ranker.link`) → `/your-moves`. Entrance: the candidate threads lift out of the cloth in the editors' order (Knot, 60ms stagger). Interactive moment: the toggles re-rank live with GSAP Flip.

7. **What's free to read?** Heading pass `home.free.heading` "What's free to read?". This week's Roundup spans columns one to two: `home.free.roundup.label` "The Weekly Roundup", `home.free.roundup.framing` "Saturday, September 19: three of last week's moves and where the twenty tracked rates ended, in full, for anyone. The next one goes out Saturday morning.", the three move headlines from roundup.md as a list, and the link **Open this week's free roundup** (`home.free.roundup.link`) → `/roundup`. The Guides fill columns three to five: `home.free.guides.label` "The Guides", `home.free.guides.framing` "Evergreen explainers, each under the thread it belongs to. Three of them here; the rest are a click away.", three guides one per column, each with its thread's knot, its title and its dek → its route: "The national average savings rate is not a benchmark, it is a warning" → `/guides/the-national-average-is-a-warning`; "How to make a rotating cashback category actually pay" → `/guides/make-a-rotating-category-pay`; "Why patio furniture is cheap in October: the seasonal buying cycle, plainly" → `/guides/why-patio-furniture-is-cheap-in-october`; then the link **Open the guides** (`home.free.guides.link`) → `/guides`. Entrance: a weft pass per cell, alternating direction (left to right, then right to left).

8. **What do people ask before they join?** Heading pass `home.faq.heading` "What do people ask before they join?". An editorial index in five columns, two rows of five: the question as the cell head in Big Shoulders 600 with the knot, the answer beneath in Manrope. Not an accordion; everything is visible. The ten pairs, verbatim:
   - `home.faq.q1` "What arrives, and when?" `home.faq.a1` "Five items on your dashboard by 6:30 AM Eastern each weekday, one per thread: a rate movement, a cashback window, a coupon code, a seasonal buy or wait, and a paycheck framework, each ending with one small action. Reading takes about four minutes. Saturday brings the free Roundup; Sunday brings no brief at all. The brief is not emailed or texted; it waits on the dashboard."
   - `home.faq.q2` "What can I read without paying?" `home.faq.a2` "The Weekly Roundup, each Saturday: three of the week's moves and where the tracked savings rates ended, full text. The Guides: evergreen explainers on high yield accounts, rotating categories, the 50/30/20 split and the seasonal buying cycle. Your moves, which ranks this week's moves for your situation. None of it asks for an account or an email address, and the Roundup and the Guides carry an RSS feed."
   - `home.faq.q3` "Is this financial advice?" `home.faq.a3` "No. SaveBrew is an educational digest. We report published rates and public offers on the date shown, lay out the arithmetic on an illustrative balance, and say what the editors are watching. We don't recommend that you open, close or move any account, and we don't hold, move or manage money. Rates change without notice, so confirm any of them with the institution before you act."
   - `home.faq.q4` "How do I cancel?" `home.faq.a4` "From your dashboard: Membership, then Cancel membership. Two clicks, and it's done at once. The screen shows the date your access ends and a Resume membership link that stays there until that date, in case you change your mind. Your dashboard stays open to the end of the period you've paid for. Emailing support@savebrew.com from the address you joined with works too."
   - `home.faq.q5` "Can I get a refund?" `home.faq.a5` "A yearly membership is refunded in full if you ask within 14 days of the order date: email support@savebrew.com with your order number and the $72 or $108 goes back to the card you paid with. Monthly memberships aren't refunded. Cancelling stops the next charge, and you read to the end of the period you've already paid for."
   - `home.faq.q6` "What are the texts, and what aren't they?" `home.faq.a6` "Texts are account notifications you turn on yourself: alerts on the rates and goals you track, billing and renewal notices, sign in codes, confirmations when you change a setting, and replies from support. They aren't the brief, a code, a category, an offer or a nudge to upgrade. The opt in is a separate, unticked box, and replying STOP ends texts without touching your membership."
   - `home.faq.q7` "What is the Daily for Two?" `home.faq.a7` "One bill, two readers. Each of you gets your own sign in, your own morning brief view, your own saved items and your own text settings, and any goal marked shared shows both your deposits on one bar. You invite the second reader by email from your dashboard once the order is placed. $11.98 billed monthly, or $108 billed yearly."
   - `home.faq.q8` "How does the yearly price work out?" `home.faq.a8` "Twelve monthly payments of $7.99 come to $95.88. The year, paid once, is $72, which is $6 monthly and $23.88 less. Nine monthly payments would be $71.91, so the year costs about nine and reads for twelve. It renews at $72 a year later, and we email you 30 days before that date so the renewal is not a surprise."
   - `home.faq.q9` "What is the Rate Tracker, and what isn't it?" `home.faq.a9` "A list of published rates for twenty high yield savings accounts, money market accounts and CDs, checked each weekday morning, with a 30 day history for each, a slot for your own account's rate and an alert threshold you set. It records published numbers. It isn't an account, it holds no deposit, and it can't move money anywhere; that stays with you and your bank."
   - `home.faq.q10` "Who is behind SaveBrew?" `home.faq.a10` "SaveBrew Inc., at 660 American Ave in King of Prussia, Pennsylvania. The editors who write the brief check the twenty tracked accounts and the week's cashback, coupon and clearance windows before six each weekday morning, then cut what they found to five items. Who they are is on About; a person answers support@savebrew.com and (888) 338 8809."

   The email address and phone in a9 and a10 are live links (mailto and tel). Entrance: the ten knots pop in (Knot, 30ms stagger), then the answers wipe in.

9. **Join Our SMS List** (`id="sms"`). The verbatim block of 6.3, as a full width inline band: heading left, the consent copy across the middle columns, the phone field and the Submit control at the right end, the selvedge stitch as the field underline. No framing line above or below it on Home (`home.sms.block`). Entrance: the stitch draws under the field (Shuttle, slow 1.2s).

10. **Footer** (6.2) on the twill.

**Mobile (375).** The designed mobile hero of Art Direction 3.20, PULL A THREAD: the loom is replaced by a 180px 2D canvas band under the standfirst and the Bobbin with five vertical threads labelled with their names and knots; a one finger drag down on a thread past 40px slides that thread's knot out beneath the band as a card carrying the real headline and chip for that thread (from the TODAY items), releasing early springs it back (Knot); a tap opens the card too; the hint `home.hero.mobile.hint` "Pull a thread to read today's item on it." sits under the band; the card's close control is `home.hero.mobile.card.close` "Close". The Tightening runs once at half stagger. Reduced motion: static band, cards open without animation. Rows collapse per part 0.2: one column with the sticky tab strip; the membership cards stack (Daily, Daily for Two, the free column); the week strip scrolls horizontally with the five weekday columns at 80vw each and the knots at 44px; the dashboard row stacks the phone view first with the desktop window beneath at full width; the ranker toggles stack; the FAQ stacks; the SMS band stacks heading, copy, field, button. The hero Bobbin is in view within one scroll at all times.

**The data behind rows 2 and 4 (and /brief, /today and /archive): brief_items.md, verbatim.**

[[VERBATIM BEGIN: /home/claude/savebrew/spec/copy/brief_items.md]]

# Brief items: today's pass, yesterday's pass, last week's pass and this week so far

All items are illustrative and dated. No institution is real; banks are Bank A to Bank H (illustrative), cards are "the two rotating category cards we track", retailers are "the retailers we track". Each item is one thread's knot: thread name, headline, one line summary, and (for today) the member action chip. The five threads run in the fixed order Rates, Cashback, Coupons, Seasonal, Paycheck.

## TODAY, Thursday, September 24, 2026 (published 6:30 AM ET)

The five items fixed by offering_spec.md section 10.3, copied verbatim. Item five's thread is relabelled Paycheck; its text is unchanged. Chips are inert on the public /brief and live on the member dashboard.

Thread: Rates
Headline: Top online savings rates held at 4.00% this week.
Summary: Three of the twenty accounts we track nudged up by 0.05 points and none cut. If your account is under 3.75%, today is a good morning to compare.
Chip: Open tracker

Thread: Cashback
Headline: The rotating 5% category switches to grocery stores through September 30.
Summary: Activate it once and the cap covers about $1,500 of spend. A reminder lands on your Today view on the last morning.
Chip: Remind me

Thread: Coupons
Headline: A stackable 20% code on winter tires ends Friday.
Summary: It works with the retailer's rebate on the same order, which brings a $600 set to about $430 after both.
Chip: Save code

Thread: Seasonal
Headline: October playbook: buy patio furniture and jeans now, wait on TVs and toys.
Summary: Clearance cycles favour outdoor goods and denim this month; big electronics drop again in late November.
Chip: Open playbook

Thread: Paycheck
Headline: The 50/30/20 tune up: a ten minute look at your paycheck split.
Summary: Three questions to ask before the next pay run, with a worksheet you can fill in on the Goals tab.
Chip: Open worksheet

## YESTERDAY'S PASS, Wednesday, September 23, 2026 (published 6:30 AM ET)

Shown greyed on the /brief strip and as the Wednesday column of "This week so far". Headlines at most 14 words.

Thread: Rates
Headline: A second tracked account moved up 0.05 this week, and none has cut.
Summary: Bank H (illustrative), further down the tracked list, is 3.65% this morning; the top tracked rate stays 4.00%.

Thread: Cashback
Headline: Activation for the October categories opened on one of the two tracked cards.
Summary: Turning it on today costs nothing and the 5% starts October 1; the grocery category keeps paying through September 30.

Thread: Coupons
Headline: A 15% code on running shoes stacks with a $20 rebate through Sunday.
Summary: On a $140 pair the two together bring the price to about $99.

Thread: Seasonal
Headline: Denim clearance spread to three of the four chains we track, at 40% off.
Summary: A $90 pair is about $54 this week; the fourth chain's published prices had not moved by six.

Thread: Paycheck
Headline: October holds three paydays if your alternate Friday paycheck lands on October 2.
Summary: The third paycheck has no bills assigned to it, and the split worksheet shows where it could go before it arrives.

## LAST WEEK'S PASS, Monday, September 14 to Friday, September 18, 2026 (the five by five knot matrix)

Twenty five knots for the week strip. Headlines at most 12 words, summaries at most 20 words. The week's news: the FOMC raised its target range on Wednesday, September 16; four tracked accounts moved; both tracked cards named their October categories on Tuesday; the patio clearance turned. The Saturday, September 19 Roundup summarises this week.

### Monday, September 14

Thread: Rates
Headline: The top tracked rate holds at 4.00% into the Fed's meeting week.
Summary: All twenty tracked accounts and CDs are unchanged since Friday; Bank A (illustrative) still leads at 4.00%.

Thread: Cashback
Headline: The grocery category runs sixteen more days, and unused cap doesn't carry.
Summary: Spend under the $1,500 cap counts through September 30; whatever is left of it that night is gone.

Thread: Coupons
Headline: A 25% code on kids' winter coats runs through Thursday night.
Summary: It applies to sale items as well; an $80 coat comes to about $60 with it.

Thread: Seasonal
Headline: TVs sit near August prices; their cut comes in late November.
Summary: The tracked 65 inch sets sit within $30 of August prices; the deep cuts follow Thanksgiving.

Thread: Paycheck
Headline: The 50/30/20 split starts with net pay, not the offer letter.
Summary: Take one pay stub, find the deposit amount and split that; the taxes already left.

### Tuesday, September 15

Thread: Rates
Headline: A tracked savings account moved up 0.05 to 3.90% before the Fed.
Summary: Bank B (illustrative) repriced overnight, the first tracked move of the Fed's week.

Thread: Cashback
Headline: October to December categories published: warehouse clubs, and online retail.
Summary: Both tracked rotating cards named their fourth quarter categories; activation windows open before October 1.

Thread: Coupons
Headline: Two grocery delivery codes stack this week: $15 off and free delivery.
Summary: On a $120 order the pair brings it to about $105 with no delivery fee.

Thread: Seasonal
Headline: Outdoor furniture clearance began at two of the three tracked home retailers.
Summary: An $899 four piece set is listed at $599 this morning; the third retailer had not moved.

Thread: Paycheck
Headline: The date sets the deposit: $4,000 in a year, $154 a payday.
Summary: Divide what's left of a goal by the alternate Friday paydays before its date, then round up.

### Wednesday, September 16

Thread: Rates
Headline: Fed decision at 2 PM today; no tracked account moved overnight.
Summary: No tracked account moved overnight; the average of the twenty sits at 3.54%.

Thread: Cashback
Headline: Activating next quarter early costs nothing where the card allows it.
Summary: One tracked card opens activation on September 23, the other on October 1; both run through December 31.

Thread: Coupons
Headline: At the tire retailer, 10% off beats $20 off past $200.
Summary: Two codes, one order; on $500 the percentage code wins by $30.

Thread: Seasonal
Headline: Halloween costumes hold their price through October; the candy doesn't.
Summary: Costumes are full price until the week of the 31st; candy is cut in the last three days.

Thread: Paycheck
Headline: Fixed costs first: what share of net pay is already spoken for?
Summary: Add rent, insurance, minimum payments and utilities, then divide by net pay; past 60% the 20% has no room.

### Thursday, September 17

Thread: Rates
Headline: The Fed raised a quarter point; a tracked CD moved 0.10 overnight.
Summary: Bank D (illustrative) is 3.75% on its one year CD this morning; the twenty savings accounts held.

Thread: Cashback
Headline: Past the $1,500 cap the grocery category pays 1%, not 5%.
Summary: Beyond the cap a flat 3% grocery card wins; the cap line is in the card's app.

Thread: Coupons
Headline: The 25% coats code ends tonight, and no rebate stacks with it.
Summary: Orders placed by 11:59 PM ET keep the code; the rebate form is separate and doesn't combine.

Thread: Seasonal
Headline: The third tracked home retailer joined the patio clearance at 35% off.
Summary: All three now list the same four piece set between $549 and $599.

Thread: Paycheck
Headline: Where the 20% sits matters: 0.37% against 4.00% on $200 a payday.
Summary: Over a year of alternate Friday deposits the difference is about $100 in interest.

### Friday, September 18

Thread: Rates
Headline: A money market up 0.10, a savings account down 0.05, overnight.
Summary: Bank C (illustrative) is 3.80%; Bank E cut to 3.70%, the week's only cut since the Fed's move.

Thread: Cashback
Headline: The grocery category has twelve days left: how much cap remains?
Summary: The card's app shows spend toward the $1,500 cap; anything left after September 30 is gone.

Thread: Coupons
Headline: A 20% winter tire code opened today and runs through next Friday.
Summary: Eight days to use it; the rebate form on the same order is separate and still applies.

Thread: Seasonal
Headline: Grills joined the clearance: a $399 gas grill is listed at $279.
Summary: The outdoor aisle is being emptied for holiday stock, and the grills go with the patio sets.

Thread: Paycheck
Headline: The deposit that's automatic on payday is the one that happens.
Summary: A standing transfer set for the morning after payday removes the decision; the amount can be $25.

## THIS WEEK SO FAR, Monday, September 21 to Wednesday, September 23, 2026

One headline per thread per morning, with a one line summary. Wednesday reuses yesterday's pass above.

### Monday, September 21

Thread: Rates
Headline: Tracked rates open the week where they closed it: the top at 4.00%.
Summary: No overnight moves; four accounts moved last week, three of them up.

Thread: Cashback
Headline: Activation for October opens Wednesday on one of the tracked cards.
Summary: The other card opens on October 1; the grocery category runs nine more days.

Thread: Coupons
Headline: The winter tire code stacks with a $50 rebate through Friday.
Summary: On a $600 set the code takes it to $480 and the rebate to $430.

Thread: Seasonal
Headline: Denim clearance began: 40% off at two of the four chains we track.
Summary: A $90 pair is about $54 at the two; the other two had not moved by six.

Thread: Paycheck
Headline: Where did the 30% go in September? The card statement knows.
Summary: The wants line is the one that drifts; three statements show the drift before the split worksheet does.

### Tuesday, September 22

Thread: Rates
Headline: A tracked CD moved up 0.05 to 3.40% overnight.
Summary: Bank G (illustrative), the shortest CD on the list, is the first tracked account to move this week.

Thread: Cashback
Headline: The last September grocery trips decide whether the $1,500 cap is met.
Summary: Under the cap, groceries earn 5% on the category card; over it, the flat 3% card wins.

Thread: Coupons
Headline: A $10 off $50 pharmacy code covers the aisle, not the prescription.
Summary: Household goods and over the counter items count; the prescription line is excluded by the code's terms.

Thread: Seasonal
Headline: The grill markdown held through the weekend: $399 listed at $279.
Summary: The tracked home retailers cut grills with the patio sets on Friday, and the price held.

Thread: Paycheck
Headline: A raise resets the split: the new net pay, the same three shares.
Summary: The 20% grows with the paycheck only if the deposit is redone; a fixed $200 shrinks as a share.

### Wednesday, September 23

Reuse YESTERDAY'S PASS above, unchanged.


[[VERBATIM END: /home/claude/savebrew/spec/copy/brief_items.md]]

### 7.2 Today's brief (/brief, public)

**Purpose.** Show today's five items in full, exactly as a member read them at 6:30 this morning, so a reviewer or a reader can see the product without an account, then say what the members' version adds.

**Head.** Title `head.brief.title` "Today's brief, Thursday, September 24 · SaveBrew". Meta `head.brief.meta` "Today's five items in full, as members read them at 6:30 AM ET: a rate move, a cashback window, a coupon code, a seasonal call and a paycheck framework.". Indexed.

**Scene.** One weft thread (a single SVG path on a lazy canvas across the page head, under the heading band) that weaves the day's five knots left to right as the visitor reads: each knot ties as its item's cell enters the viewport; the thread creeps on the 11s idle cadence; static and fully knotted under reduced motion.

**Text hover.** Weight tightening: hovered headings and links animate `font-variation-settings` wght from 400 to 800 (Knot, 0.38s) and back on leave; `:focus-visible` shows the same weight at once plus the stitch outline. A smaller Tightening echo runs once on the date line at load.

**Asset slots.** `photo.todays-pass-heading` (the header pass background, 3:1 desktop, 4:3 phone), `product.today-desktop` (a 96px wide thumbnail in the "The rate strip" cell as a link to the dashboard row on Home), `kit.svg`.

**Sections.**

1. **Header pass.** The date line `brief.header.date` "Thursday, September 24, 2026" in Big Shoulders 700 (the Tightening echo), `brief.header.published` "Published 6:30 AM ET" as a chip, and the disclaimer `disclaimer.text` set directly under the header pass so it is on screen before any scrolling at 1440 by 900 and at 375 by 812 (`brief.header.disclaimer`). Entrance: the date line tightens, the chip pops (Knot).
2. **The five items in full.** Framing `brief.items.framing` "Today's five, exactly as a member read them at 6:30 this morning, one per thread, with the member's action chip under each. Four minutes.". Five cells in the warp, one per thread, in the fixed order Rates, Cashback, Coupons, Seasonal, Paycheck, each with the knot, the thread name, the headline, the summary and the chip, from the TODAY items of brief_items.md (7.1) and the chips `home.pass.chip.rates` "Open tracker", `home.pass.chip.cashback` "Remind me", `home.pass.chip.coupons` "Save code", `home.pass.chip.seasonal` "Open playbook", `home.pass.chip.paycheck` "Open worksheet". The chips are inert on this public route (aria-disabled, press feedback plays) and the note beneath the row reads `brief.items.chip.note` "Members' actions. On the dashboard these chips save the code, set the reminder, and open the tracker, the playbook or the worksheet. Here they show you where each one sits.". Entrance: the five knots on the scene thread tie in turn and each cell wipes in beneath its knot (Shuttle, 60ms stagger).
3. **What does the members' version add?** Heading pass `brief.members.heading` "What does the members' version add?". Five cells: `brief.members.rates.name` "The rate strip" with `brief.members.rates.text` "Four tiles above the five items: the top tracked APY, the average of the twenty, your own account's rate as you typed it, and the gap between them in points and in dollars a year on your balance. Checked at 6:00 AM ET each weekday."; `brief.members.saved.name` "Saved items" with `brief.members.saved.text` "The Save code and Remind me chips put a code, a category activation or a deadline into one list with its expiry date. The reminder lands on your Today view and by email on the last morning, so the code you meant to use gets used."; `brief.members.archive.name` "The archive" with `brief.members.archive.text` "Each brief since launch, including the ones before you joined, searchable by topic and by date. Type coupon and you get each coupon item we've run; pick a date and you get that morning's whole pass, chips and all."; `brief.members.texts.name` "Texts" with `brief.members.texts.text` "Three switches, all yours to set: rate moves over 0.25 points on accounts you track, goal check ins and milestones, and billing, renewal and sign in codes. The brief itself is not texted, and neither is any code or offer. Reply STOP and the texts end; the membership doesn't."; `brief.members.goals.name` "Goals" with `brief.members.goals.text` "Up to six goals, each with a target, a date and a monthly deposit. SaveBrew records what you type and shows the streak, the milestones at 25, 50, 75 and 100 percent, and about how much the balance would earn at the top tracked rate.". Each cell head carries its kit icon (Rates, Archive, Texts, Goals; the saved items cell uses the Coupons icon). Entrance: the cell heads' icons draw themselves (stroke draw, Shuttle), then the text fades up inside the clip.
4. **Yesterday's pass strip.** Label `brief.yesterday.label` "Yesterday's pass, Wednesday, September 23" and the hint `brief.yesterday.hover` "Hover or tap a knot to read what it said.". Five knots, greyed to muted indigo, one per thread, aria `brief.yesterday.knot.aria.pattern` "Wednesday, September 23, {thread}: {headline}"; hover, tap or focus reveals that item's headline and summary from the YESTERDAY'S PASS data of brief_items.md beneath the strip. Entrance: the five knots slide in along the thread from the right (Shuttle, 40ms stagger). Interactive moment: the knots.
5. **Compact membership strip** (6.8) with the line `brief.compact.line` "Everything above, each weekday morning, with the tracker, the goals and the archive behind it." and the two cards and link (`brief.compact.cards`). Entrance: a single weft pass across the strip.
6. **Footer** (6.2).

**Buttons and links.** The five chips (inert). **Add the Daily to my cart** → adds SB101, opens the drawer. **Add the Daily for Two to my cart** → adds SB201, opens the drawer. **What each membership includes** → `/membership`.

**Mobile.** One column; the disclaimer stays above the fold under the header pass; the five items stack in thread order with the tab strip jumping between them; the yesterday strip scrolls horizontally; the compact strip stacks its two cards.

### 7.3 Membership (/membership, the pricing page)

**Purpose.** The storefront: the two memberships at two cadences with both prices printed, the full inclusion lists, the renewal sentence, the tax line, the two click cancellation, the pricing questions, and one explicit purchase button per card.

**Head.** Title `head.membership.title` "Membership: the Daily and the Daily for Two · SaveBrew". Meta `head.membership.meta` "SaveBrew Daily is $7.99 billed monthly or $72 billed yearly; the Daily for Two is $11.98 or $108. Both prices printed, cancellation in two clicks.". Indexed.

**Scene.** Two threads plied into one cord (a lazy 2D canvas band under the heading pass): the two threads twist together on load (the Daily for Two) and untwist back into two on hover or focus over the Daily for Two card, re-plying on leave (Knot); static plied under reduced motion.

**Text hover.** The running stitch underline: a dashed indigo underline (stroke-dasharray 6 4) draws under the hovered heading or link and the dashes travel once (Shuttle, 0.38s); `:focus-visible` shows the drawn underline at once.

**Asset slots.** `photo.membership-free-column` (column five at 30 percent), `video.product-pan` with `product.today-desktop`, `product.rates-desktop`, `product.goals-desktop` and `product.today-phone` (row 3), `kit.svg`.

**Sections.**

1. **Heading pass with the cadence control.** `membership.heading` "What does it cost?" full width on butter; beneath it the cadence control, two toggles that ply together (CUR-009, role radiogroup, aria `membership.cadence.aria` "Billing cadence"): `membership.cadence.monthly` "Monthly" (selected by default, the cheaper commitment) and `membership.cadence.yearly` "Yearly"; the note `membership.cadence.note` "Both prices stay printed on each card whichever you pick; only the button changes.". Entrance: the weft pass draws under the heading, the two toggles ply (Knot).
2. **The two cards and the fifth column.** The Daily in columns one to two (id `daily`) and the Daily for Two in columns three to four (id `daily-for-two`), built from `home.cost.daily.*` and `home.cost.two.*` in full (name, audience, price, arithmetic, renewal, inclusions label, all eight or eleven inclusions with descriptions, tax, refund, the cadence bound Bobbin), exactly as pasted in 7.1 row 3 (`membership.cards`), and the fifth column from `home.cost.free.*` on the twill with the still behind it. Buttons: **Add the Daily to my cart** / **Add a year of the Daily to my cart** → adds SB101 / SB102 and opens the drawer; **Add the Daily for Two to my cart** / **Add a year of the Daily for Two to my cart** → adds SB201 / SB202 and opens the drawer; **Open this week's free roundup** → `/roundup`; **Open the guides** → `/guides`; **Open Your moves** → `/your-moves`. Entrance: the cards wipe in from the left one after the other (Shuttle), the seals in their corners weaving last.
3. **What's inside the dashboard?** The home row 5 component in compact form (heading `home.dashboard.heading`, framing `home.dashboard.framing`, the desktop window playing `video.product-pan` once then resting on the selected still, the phone beside it, the three view switch with its captions), so the buyer sees the product on the page that sells it. Entrance: the desktop window's modules populate top to bottom, then the phone slides in from the right (Shuttle). (The Art Direction's section list for this route names four rows; this row is added so the asset plan's placement of the product shots on /membership is honoured and so the buyer not has to leave the storefront to see the product.)
4. **How do I cancel?** Heading pass `membership.cancel.heading` "How do I cancel?". The two click path as two knots on one thread across columns one to three: knot one labelled `membership.cancel.knot.1` "Membership", knot two labelled `membership.cancel.knot.2` "Cancel membership"; beneath, `membership.cancel.path` "From your dashboard's app bar: Membership, then Cancel membership. That's the whole path, and it takes effect at once." and `membership.cancel.after` "The screen shows the date your access ends and a Resume membership link that stays there until that date."; columns four to five carry the email path `membership.cancel.email` "Or email support@savebrew.com from the address you joined with, and we cancel it for you within one working day." with support@savebrew.com as a mailto link ("within one working day" is proposed and needs the owner's confirmation). Entrance: the thread draws left to right and the two knots tie in turn (Shuttle then Knot).
5. **What do people ask before they join?** Heading pass `membership.faq.heading` "What do people ask before they join?". The five pricing questions as an editorial index in five columns, question as cell head with the knot, answer beneath:
   - `membership.faq.q1` "Can I switch from monthly to yearly later?" `membership.faq.a1` "Yes, from Membership on your dashboard. Pick yearly and the change takes effect on your next monthly renewal date: that day you're charged $72 instead of $7.99, and from then on the membership renews yearly. Switching back works the same way in reverse. No day is charged twice, and none is lost."
   - `membership.faq.q2` "What happens if a payment fails?" `membership.faq.a2` "You get one notice by email (and by text, if you've opted in), then seven days to update the card from Membership on your dashboard. Access pauses after that until a payment goes through, and that's all that happens: no fee, no penalty, and your goals, saved items and archive wait exactly as you left them."
   - `membership.faq.q3` "Is sales tax included in the price?" `membership.faq.a3` "Yes. The price on the card is the amount that appears on your statement, $7.99, $72, $11.98 or $108, with sales tax included where it applies. No amount appears for the first time at checkout. There is no setup fee, and neither cancelling nor inviting a second reader carries a charge."
   - `membership.faq.q4` "Can I move from the Daily to the Daily for Two?" `membership.faq.a4` "Yes, from Membership on your dashboard, at any point. Your dashboard, goals, saved items and archive stay as they are, and the second reader gets their invite by email the moment you confirm. The new price applies from your next renewal date at whichever cadence you're on: $11.98 monthly or $108 yearly."
   - `membership.faq.q5` "What does the second reader pay, and what do they need?" `membership.faq.a5` "They pay no part of the bill and need only an email address. The invite gives them their own sign in, their own morning brief view, their own saved items and their own text settings, and any opt in to texts is theirs to make from their own dashboard. If the membership is cancelled, both dashboards stay open to the end of the paid period."
   Entrance: the answers wipe in from the right, one column at a time (Shuttle, 50ms stagger), the knots popping first.
6. **Footer** (6.2).

**Mobile.** The cadence control is full width under the heading; the cards stack in the order Daily, Daily for Two, the free column; the dashboard row stacks phone first; the cancel path's two knots sit one above the other; the five questions stack.

### 7.4 The Weekly Roundup (/roundup, Saturdays, public, RSS)

**Purpose.** The free Saturday page: three of the week's moves and where the tracked rates ended the week, full text, no account, no form, so anyone can read what the product does before paying.

**Head.** Title `head.roundup.title` "The Weekly Roundup, Saturday, September 19 · SaveBrew". Meta `head.roundup.meta` "Three of the week's money moves and where the tracked savings rates ended the week, free to read each Saturday. No account needed.". Indexed. RSS at `/roundup/feed.xml` with the description from roundup.md. The issue's stable address `/roundup/2026-09-19` serves the same page with a 200.

**Scene.** One thread with three knots (a lazy canvas ribbon along the left gutter): the camera, in 2D, tracks along the thread as the three moves are read, each knot tightening as its move enters the viewport; static and knotted under reduced motion.

**Text hover.** The first letter knots: the first letter of a hovered heading or link scales to 1.12 and settles (Knot, 0.38s); `:focus-visible` shows the stitch outline.

**Asset slots.** `photo.roundup-header` (the header band, 16:9 desktop, 1:1 phone), `kit.svg` (the Roundup icon, the knot matrix).

**Sections.**

1. **Header pass.** `roundup.heading` "What moved this week?" over `photo.roundup-header` graded; `roundup.date` "Saturday, September 19, 2026"; the covers line from roundup.md ("Covers: Monday, September 14 to Friday, September 18, from the 6:00 AM ET checks."); `roundup.intro` "Three of the week's moves and where the twenty tracked rates ended the week, in full, for anyone. Published each Saturday morning; the next goes out Saturday, September 26."; the disclaimer `disclaimer.text` beside the date (`roundup.disclaimer`). Entrance: the header band's clip opens from the left, the date pops.
2. **The three moves.** Move one spans columns one to two, move two spans column three, move three spans columns four to five, so the row fills at each width; each with its thread's knot and name, the headline in Big Shoulders 600, the body in Manrope, the arithmetic paragraph and the "Worth doing" paragraph as pasted below. Entrance: each move's knot ties on the scene thread and its cell wipes in (Shuttle), left to right.
3. **Where did the tracked rates end the week?** Heading pass `roundup.rates.heading` "Where did the tracked rates end the week?". Columns one to three: the six row table from roundup.md (the build draws the rule lines; Manrope tabular numerals; up moves green with an up arrow, down moves red with a down arrow, unchanged grey); columns four to five: the knot matrix (Recipe 08) of the same six accounts, each account a row of five daily knots Monday to Friday, knot size following the APY, butter where the rate moved that morning, with the note `roundup.rates.note` "Illustrative accounts and rates. Butter knots mark the mornings a rate moved; knot size follows the APY."; beneath both, the line from roundup.md ("The average of the twenty tracked accounts and CDs ended the week at 3.55 percent, up 0.01 on the Friday before. Illustrative until the owner confirms the rate data source."). Entrance: the table's rows wipe in top to bottom, then the matrix knots tie column by column.
4. **Past Saturdays.** Heading pass `roundup.past.heading` "Past Saturdays". Five columns of dated entries, each `roundup.past.entry.pattern` "Saturday, {date}" (example "Saturday, September 12, 2026") with the issue's one line; at launch one entry exists: "Saturday, September 19, 2026: A quarter point from the Fed, the October categories, and the patio clearance." → `/roundup/2026-09-19`; the remaining columns carry the line from roundup.md ("New roundups are added here each Saturday morning, each at its own stable address.") spread as one sentence across the pass, and the RSS link `roundup.rss.label` "Follow the Roundup by RSS" → `/roundup/feed.xml`. Entrance: the entries slide in along the thread (Shuttle).
5. **Compact membership strip** (6.8) with `roundup.compact.line` "Members read five moves each weekday morning, not three on Saturday." (`roundup.compact.cards`). Entrance: one weft pass.
6. **Footer** (6.2).

**Buttons and links.** **Follow the Roundup by RSS** → `/roundup/feed.xml`. **Add the Daily to my cart** → adds SB101, opens the drawer. **Add the Daily for Two to my cart** → adds SB201, opens the drawer. **What each membership includes** → `/membership`.

**Mobile.** The header still crops to 1:1; the three moves stack; the table becomes stacked rows (account and product on line one, APY and change on line two) with the matrix beneath; Past Saturdays stacks.

**The Roundup copy, verbatim.**

[[VERBATIM BEGIN: /home/claude/savebrew/spec/copy/roundup.md]]

# The Weekly Roundup (/roundup, public, Saturdays)

Stable address for this issue: /roundup/2026-09-19

RSS description: Three of the week's money moves and where the twenty tracked savings rates ended the week, published on savebrew.com each Saturday morning, free to read, with no account and no form.

## Header pass

Heading: What moved this week?

Date: Saturday, September 19, 2026

Covers: Monday, September 14 to Friday, September 18, from the 6:00 AM ET checks.

Disclaimer (beside the date, verbatim): SaveBrew is an educational digest, not financial advice. We are not a bank, a lender, a broker or a registered investment adviser, and we do not hold, move or manage money. Rates and offers come from public sources on the date shown and change without notice, so confirm them with the institution before you act. What you save depends on your own choices.

## The three moves

### Move one (spans columns one to two)

Thread: Rates

Headline: A quarter point from the Fed, and four of the twenty tracked accounts moved

On Wednesday, September 16, the FOMC raised the federal funds target range by a quarter point to 3.75 to 4.00 percent, its first rise in more than three years. By Friday, four of the twenty tracked accounts and CDs had moved. Bank B (illustrative) rose 0.05 to 3.90 percent on Tuesday, ahead of the decision. Bank D's one year CD went up 0.10 to 3.75 on Thursday. Bank C's money market went up 0.10 to 3.80 on Friday, and Bank E went down 0.05 to 3.70 the same morning, the week's only cut. The top tracked rate held at 4.00 percent all week.

The arithmetic: a quarter point on $10,000 is $25 a year if an account passes the move through, and the trackers we read put the usual lag at one to two weeks. Which will isn't promised by anyone, and Bank E shows a cut can land in a hike's week.

Worth doing this weekend: write down your account's published rate, dated, so the next two weeks can be measured against something.

### Move two (spans column three)

Thread: Cashback

Headline: The October categories are published, and the grocery cap has twelve days left

Both rotating category cards we track named their fourth quarter categories on Tuesday: warehouse clubs and select streaming services on one, online retail and drugstores on the other (illustrative pairs; the issuer's own notice is the record). Activation opens on Wednesday, September 23 on the first card and on October 1 on the second, and both categories run through December 31. Meanwhile the grocery category on the first card pays through September 30, and whatever is left of its $1,500 cap on that night is gone on October 1.

The arithmetic: 5 percent on the full $1,500 is $75; the card's base 1 percent on the same spend is $15; so the category itself is worth $60 a quarter, and only on groceries that were going to be bought anyway.

Worth doing: open the card's app and read the cap line, then decide which card carries the last grocery trips of September and which carries the warehouse run in October.

### Move three (spans columns four to five)

Thread: Seasonal

Headline: The patio clearance turned this week, 30 to 40 percent off at all three tracked home retailers

Two of the three home retailers we track cut their outdoor furniture on Tuesday and the third followed on Thursday. A four piece set listed at $899 in May is now between $549 and $599 at all three, and the grills followed on Friday, with a $399 gas grill listed at $279. The floor space under them is going to holiday stock in the last week of October, and a set in a stockroom until April costs the retailer more than the markdown does.

The arithmetic: $899 to $549 is $350 off, or 39 percent. The 65 inch TVs we track, by contrast, sit within $30 of their August prices, and their turn comes in the last week of November.

Worth doing: if a patio set or a grill was on the list for next spring, this is the window, and the return terms are worth reading first, because floor models sell as is. If what's on the list is a TV, the window isn't open yet.

## Where the tracked rates ended the week

Heading pass: Where did the tracked rates end the week?

Set as a small table (the build draws the rule lines; the knot matrix of art direction 3.19 sits beside it). Illustrative accounts and rates, from the Friday, September 18, 6:00 AM ET check; six of the twenty tracked.

```
Account                 | Product             | APY   | Change this week
Bank A (illustrative)   | High yield savings  | 4.00% | unchanged
Bank B (illustrative)   | High yield savings  | 3.90% | up 0.05
Bank C (illustrative)   | Money market        | 3.80% | up 0.10
Bank D (illustrative)   | 12 month CD         | 3.75% | up 0.10
Bank E (illustrative)   | High yield savings  | 3.70% | down 0.05
Bank F (illustrative)   | High yield savings  | 3.50% | unchanged
```

Line beneath the table: The average of the twenty tracked accounts and CDs ended the week at 3.55 percent, up 0.01 on the Friday before. Illustrative until the owner confirms the rate data source.

## Past Saturdays

Heading: Past Saturdays

Saturday, September 19, 2026: A quarter point from the Fed, the October categories, and the patio clearance. (this issue, /roundup/2026-09-19)

New roundups are added here each Saturday morning, each at its own stable address.


[[VERBATIM END: /home/claude/savebrew/spec/copy/roundup.md]]

### 7.5 The Guides index (/guides)

**Purpose.** The free library: the guides placed under the thread each belongs to, one line each, a knot each, no account.

**Head.** Title `head.guides.title` "The Guides: free explainers on saving money · SaveBrew". Meta `head.guides.meta` "Evergreen guides on high yield savings, rotating cashback categories, the 50/30/20 split and the seasonal buying cycle. Free to read, in any order.". Indexed. RSS at `/guides/feed.xml`.

**Scene.** A spool (kit icon, drawn on a lazy canvas in the left gutter) that unwinds a thread down the page as reading progress; the thread's length is the scroll fraction; static, fully unwound, under reduced motion.

**Text hover.** The thread underline unspools: an underline draws under the hovered title from a small spool glyph at its left end (Shuttle, 0.38s) and rewinds on leave; `:focus-visible` shows it drawn.

**Asset slots.** `photo.guides-header` (21:9 desktop, 4:5 phone), the four `photo.guide-hero.*` stills as 16:9 thumbnails on their cards, `kit.svg` (the four guide graphics as the cards' knots).

**Sections.**

1. **Header pass.** `guides.heading` "What's free to read?" over `photo.guides-header` graded; `guides.intro` "Evergreen explainers, each under the thread it belongs to. Free, and in any order.". Entrance: the header clip opens top to bottom.
2. **The guides in the warp columns.** Five columns headed `guides.column.rates` "Rates", `guides.column.cashback` "Cashback", `guides.column.coupons` "Coupons", `guides.column.seasonal` "Seasonal", `guides.column.paycheck` "Paycheck", each with its thread's icon. Each guide card: the guide graphic knot, the 16:9 thumbnail, the title, the dek, and the minutes line `guides.post.minutes.pattern` "about {minutes} minutes to read"; the whole card is the link. Rates carries two: "The national average savings rate is not a benchmark, it is a warning" (dek "The FDIC's 0.37 percent is the floor most savings sit on, and measuring an account against it flatters the wrong number.", about 5 minutes to read) → `/guides/the-national-average-is-a-warning`, and "A 4.00% account against the one you already have: the arithmetic on $10,000" (dek "The yearly difference in dollars, what a minimum balance and a promotional condition do to it, the hour it takes to move, and the cases where the hour isn't worth it.", about 6 minutes to read) → `/guides/four-percent-against-the-account-you-have`. Cashback carries "How to make a rotating cashback category actually pay" (dek "Activation takes thirty seconds; the cap, the timing against the paycheck and the interest are where the 5 percent goes missing.", about 5 minutes to read) → `/guides/make-a-rotating-category-pay`. Seasonal carries "Why patio furniture is cheap in October: the seasonal buying cycle, plainly" (dek "Clearance follows the retailer's floor space, not the shopper's needs, and the year turns twelve times on that one fact.", about 5 minutes to read) → `/guides/why-patio-furniture-is-cheap-in-october`. Coupons and Paycheck have no guide at launch, and no card links to a page that does not exist; those two columns carry the thread's icon and one honest line each pointing to where the thread is covered now: `add.guides.column.coupons.line` "No guide on this thread yet. The coupon codes we test run in the brief each weekday and in the Saturday Roundup." with the link **Open today's brief** → `/brief`; `add.guides.column.paycheck.line` "No guide on this thread yet. The paycheck frameworks run in the brief each weekday, and Your moves ranks this week's paycheck move for you." with the link **Open Your moves** → `/your-moves`. (Art Direction 3.24 proposes twelve guides at launch; four are written, and only written guides are listed.) Entrance: the five columns' icons draw, then each card lifts on its thread (Knot, 50ms stagger by column).
3. **Roundup cross link row.** `guides.crosslink.line` "Saturday's Roundup is the other free read: three of the week's moves and where the tracked rates ended." spanning columns one to three, the link `guides.crosslink.link` "Open this week's free roundup" → `/roundup` in columns four to five with the Roundup icon. Entrance: a weft pass right to left.
4. **Compact membership strip** (6.8) with `guides.compact.line` "The Guides stay free. The morning brief is what members pay for.". Entrance: a weft pass left to right.
5. **Footer** (6.2).

**Mobile.** The five columns stack in thread order, the tab strip jumping between them; cards full width with the thumbnail at 16:9.

### 7.6 to 7.9 The four guide posts (/guides/slug)

One template, four bespoke pages. Each post is a designed editorial page, not a wall of text: the body runs in CSS multicolumn (`columns: 34ch`, two columns at 1280, three at 1440, four at 1920, five at 2560) with the pull thread (the guide's `pull_thread` sentence) set as a weft pass across the columns in Big Shoulders 600, the guide's own kit graphic at the head of the body, and the post's own scene. The copy is the guide file, word for word, headings included (they are the questions the reader is asking). Front matter fields (title, slug, thread, dek, reading_minutes, date, pull_thread, membership_line, button_label) are data the template renders; they are not printed as YAML.

**Template sections.**

1. **Hero band.** The guide hero still (`photo.guide-hero.<slug>`, 16:9 desktop, 4:5 phone, IMG-019 crops, graded) with the thread's knot and name, the headline in Big Shoulders 800 across all five columns, the dek in Manrope 19px, and the line `guides.post.minutes.pattern` "about {minutes} minutes to read" with the date "September 24, 2026". Entrance: the still's clip opens left to right and the headline arrives tight (no Tightening on interior routes).
2. **The disclaimer** `disclaimer.text` directly under the hero, above the fold (`guides.post.disclaimer`).
3. **The body** in multicolumn with the pull thread across the columns, the guide graphic (kit.svg) at the head, and the guide's H2 questions as in file. Entrance: the columns wipe in one after another (Shuttle, 60ms stagger), the pull thread drawing last as a single weft pass.
4. **The membership line and the button.** The guide's `membership_line` sentence, then the Bobbin **Add the Daily to my cart** (`button_label`) → adds SB101 and opens the drawer. Entrance: the Bobbin's stitch draws.
5. **Read next** (`guides.post.readnext` "Read next"): the other three guides as three knots on one thread across columns one to five (thread's knot, title, minutes) → their routes. Entrance: the thread draws and the three knots tie.
6. **Compact membership strip** (6.8) with `guides.post.compact.line` "Members get one item on this thread most mornings, with the rest of the pass beside it." (`guides.post.compact.cards`). Entrance: one weft pass.
7. **Footer** (6.2).

**Mobile.** One column body (no multicolumn under 768), the pull thread as a full width band, the hero at 4:5, Read next stacked.

#### 7.6 /guides/make-a-rotating-category-pay

Head: `head.guide.rotating.title` "Make a rotating cashback category actually pay · SaveBrew"; `head.guide.rotating.meta` "Activation is the easy part. The cap, the timing against your paycheck and the real spend decide the 5 percent, with the arithmetic on a $1,500 cap.". Scene: the spool unwinds down the page (the guides family) and the post's own figure is a single indigo thread that loops back on itself once across the page head, the loop closing as the reader passes the cap arithmetic ("$60") and pulling tight at the last section (Knot). Text hover: the word loops: an underline draws as a small loop under the hovered heading (Shuttle) and pulls straight on leave. Kit graphic: the loop knot. Read next: the national average, the four percent comparison, patio furniture.

[[VERBATIM BEGIN: /home/claude/savebrew/spec/copy/guides/make-a-rotating-category-pay.md]]

```yaml
title: "How to make a rotating cashback category actually pay"
slug: "make-a-rotating-category-pay"
thread: "Cashback"
dek: "Activation takes thirty seconds; the cap, the timing against the paycheck and the interest are where the 5 percent goes missing."
reading_minutes: 5
date: "2026-09-24"
pull_thread: "The category pays 5 percent on the first $1,500 and the card's base rate on all of the spend after it, so the whole prize is $60 a quarter over what the card would have paid anyway."
membership_line: "The Daily carries each quarter's categories, their caps and the activation cutoff on the morning they're published, with the arithmetic already done on the spend."
button_label: "Add the Daily to my cart"
```

# How to make a rotating cashback category actually pay

The 5 percent is real. It pays out on the two rotating category cards we track, and we've done the sums on it often enough to say so plainly. What's also real is how often it doesn't pay, and the reasons are dull: the category wasn't activated, the spend didn't reach the cap, the spend went past the cap, or the balance carried interest that ate the quarter's reward in one statement. Activation is the step people know about. It's the other three that decide whether the card earned you $60 or nothing at all.

So here is the procedure, in the order the quarter runs, with the arithmetic on a $1,500 cap.

## What does the category actually pay?

Start with the ceiling, because the ceiling is the whole story. The category pays 5 percent on the first $1,500 and the card's base rate on all of the spend after it, so the whole prize is $60 a quarter over what the card would have paid anyway. The sum: 5 percent of $1,500 is $75. The same $1,500 at the card's base rate of 1 percent is $15. The category itself, the part you're doing the work for, is the $60 between those two numbers. Fill all four quarters and it's $240 a year. Most people don't fill four.

Put it against a flat 3 percent grocery card, the one the category is usually competing with in your wallet. On $1,500 of groceries that card pays $45. The rotating card wins by $30 in a quarter where the category is groceries, and loses by $30 in a quarter where the category is somewhere else, because groceries then earn its base 1 percent. Hold the $60. It's the number each later step gets measured against.

## Is the category where your money already goes?

The two cards we track have run these categories in 2026 (illustrative): grocery stores, gas stations, restaurants, warehouse clubs, online retail, drugstores, streaming services, home improvement. Some of those are where a working adult's money already goes. Some aren't.

The test is your last three statements. Add up what you actually spent in the category, not what you might spend if you tried. Grocery spend of $600 a quarter means the category pays $30, and the gain over the base rate is $24, not $60. Streaming at $45 a quarter pays $2.25, which isn't worth the thirty seconds of activation, let alone remembering which card to use.

The failure that costs the most is the one that looks like winning: spending toward the cap. Buying $1,500 of things you weren't going to buy, to collect $60, is a trade nobody wins. A category you don't spend in is worth exactly what you'd spend in it, and if that's nothing, skip the quarter without a second thought.

## When does the spend land against the paycheck?

The next quarter runs October 1 to December 31. If you're paid on alternate Fridays and a paycheck lands on October 2, the quarter holds seven paydays: October 2, 16 and 30, November 13 and 27, and December 11 and 25. Three of those fall in October, one of the two times this year (May was the other) that a fortnightly pay cycle hands you a spare paycheck.

The timing rule is simple to say and easy to get wrong. The category card goes to the front of the wallet for that category only, from the first payday of the quarter, and comes out of the front again on the last day. A big spend that belongs in the category (a warehouse run before Thanksgiving, a laptop from the online retailer if that's the category) lands inside the quarter rather than the week before it opens, because the cap doesn't carry. A quarter's unused cap on December 31 is gone on January 1, and the new quarter starts at zero whether you spent $1,500 or $15.

Activation has its own clock. On the cards we track, turning the category on part way through the quarter still applies to the quarter's earlier purchases, but each card has a cutoff, one in the middle of the quarter and one at its end, and spend after a missed cutoff earns the base rate for the whole quarter. Thirty seconds on the first morning removes the risk entirely.

## Does the balance get paid in full?

This is the step that decides everything, and it's the one the reward statement doesn't show you. Take a purchase APR of 24 percent, illustrative but not unusual on a rewards card. Carry $1,500 through one statement cycle and the interest is about $30. That's half the quarter's $60 prize gone in a single cycle. Carry it through two and the category paid you $0; carry it through three and the card is costing you money to hold, with the 5 percent as decoration.

The fix costs one setting. Autopay set to the statement balance, not the minimum, on the day after the paycheck lands. Then the card is a way to route spend you were doing anyway, and the interest line reads zero each cycle.

## What does the whole procedure look like, in order?

On the morning the category opens, activate it. The same morning, read the last three statements and write down the real spend in the category; if it's under $200, decide now whether the quarter is worth the wallet shuffle. Set autopay to the statement balance. From the first payday, put the card in front for the category only, and move any large category spend you've been holding off inside the quarter's dates. On the last day of the quarter, open the card's app and read the cap line, then take the card out of the front. Repeat in January.

Done that way, the category pays what the arithmetic says: up to $60 a quarter, on spend that was happening anyway, with the interest at zero. Done any other way, it pays the card.

The Daily carries each quarter's categories, their caps and the activation cutoff on the morning they're published, with the arithmetic already done on the spend.

Button: Add the Daily to my cart

SaveBrew is an educational digest, not financial advice. We are not a bank, a lender, a broker or a registered investment adviser, and we do not hold, move or manage money. Rates and offers come from public sources on the date shown and change without notice, so confirm them with the institution before you act. What you save depends on your own choices.


[[VERBATIM END]]

#### 7.7 /guides/the-national-average-is-a-warning

Head: `head.guide.average.title` "The national average savings rate is a warning · SaveBrew"; `head.guide.average.meta` "0.37 percent (FDIC, September 2026) isn't the middle of the market, it's the floor most money sits on. The honest comparison is the tracked top.". Scene: two threads side by side in the left gutter, one thin pale thread (0.37) and one thick indigo thread (4.00), the thick one drawing down the page as reading progress while the thin one stays a hair's width, so the gap is the page's own figure; static under reduced motion. Text hover: weight thickens: the hovered heading's wght animates 300 to 800 (Knot), thin to thick like the two threads; `:focus-visible` shows 800 with the stitch outline. Kit graphic: the two threads. Read next: the four percent comparison, the rotating category, patio furniture.

[[VERBATIM BEGIN: /home/claude/savebrew/spec/copy/guides/the-national-average-is-a-warning.md]]

```yaml
title: "The national average savings rate is not a benchmark, it is a warning"
slug: "the-national-average-is-a-warning"
thread: "Rates"
dek: "The FDIC's 0.37 percent is the floor most savings sit on, and measuring an account against it flatters the wrong number."
reading_minutes: 5
date: "2026-09-24"
pull_thread: "A deposit weighted average of where money sits is a map of where money is stuck, and most of it is stuck in accounts nobody chose on purpose."
membership_line: "Members type their own rate into the Rate Tracker once, and each weekday morning the comparison is drawn to the top of the twenty tracked accounts, not to the floor."
button_label: "Add the Daily to my cart"
```

# The national average savings rate is not a benchmark, it is a warning

The FDIC publishes a national rate for savings deposits, and for September 2026 it's 0.37 percent (the National Rate on Non Jumbo Deposits, Savings, updated September 21, with the next release due October 19). It's the most quoted number in writing about savings and the most misread. Writers use it as the middle of the market, the line an account has to clear to count as good, and banks print it beside their own rate as if clearing it were an achievement. It isn't the middle of anything. It's the floor.

## How is 0.37 percent worked out?

Not by averaging the rates on offer. The FDIC's national rate is a weighted average across insured institutions, and the weight is each institution's share of domestic deposits. An account paying 4.00 percent at a bank holding a small slice of the country's deposits barely moves the number; a standard savings account at one of the largest banks moves it a great deal, because that's where the deposits are. The standard savings accounts at the largest banks publish rates as low as 0.01 percent (checked on their own sites in September 2026), and they hold enormous shares.

So the number isn't telling you what savings accounts pay. A deposit weighted average of where money sits is a map of where money is stuck, and most of it is stuck in accounts nobody chose on purpose: the savings account that came with the checking account, opened in a branch years ago and not looked at since. That's what 0.37 percent measures. It's a census of inertia.

## What does the average flatter?

Any account that's bad but not terrible. An account paying 0.75 percent is "twice the national average", which is a true sentence, and on $10,000 it's still $325 a year behind an account paying 4.00 percent. Here is the arithmetic on $10,000 for a year: at 0.37 percent, $37. At 0.75 percent, $75. At 1.00 percent, $100. At 4.00 percent, $400. The gap between the average and the top tracked rate is $363, and an account that "beats the average" by double has closed $38 of it.

That's what makes the comparison dangerous rather than merely lazy. Beating the average is beating a number that was built from accounts that weren't competing for anyone. A bank that prints "five times the national average" beside 1.85 percent is telling the truth and hiding $215.

## What's the honest comparison?

The top of the market, dated. This week the competitive high yield savings accounts cluster between 3.80 and 4.21 percent (NerdWallet and CNBC Select, as of September 23 and 24, 2026), with the highest of those carrying conditions such as a linked checking account or a required deposit each cycle. The top tracked account on our own list sits at 4.00 percent with no condition attached, which is about eleven times the national average. Eleven times. Not a little better. Not a rounding error the big banks will close next quarter.

That's the comparison worth making, and it's worth making on your balance rather than on a percentage. On $10,000 the question is "$37 or $400?", which is a question with an answer. On $2,500 it's "$9 or $100?", which has the same answer at a smaller scale. The percentage disguises the dollars; the dollars are what you're deciding about.

## Why won't the Fed's move fix the average?

On Wednesday, September 16, the FOMC raised the federal funds target range by a quarter point to 3.75 to 4.00 percent, its first rise in more than three years. The competitive accounts tend to reprice within one to two weeks of a move like that, according to the rate trackers we read, though which ones and by how much isn't promised by anyone, and one of our twenty tracked accounts cut its rate in the same week. The national average moves on a different clock, because it's weighted toward institutions that weren't competing on the way up and have no reason to start now.

The next FDIC release is October 19. Watch it, and expect the floor to stay the floor.

## What is the average good for?

One thing, and it's useful: a warning light. If the published rate on your account is within a point of 0.37 percent, your money is in the floor, whatever the bank's marketing says about multiples. That's not a judgement on you. It's a description of a default, the account that was easiest to open a long time ago, and defaults are exactly what a working adult with four minutes doesn't get around to changing.

Two questions settle it. What's the published rate on your account this morning? And how far is that from 4.00? If the first answer is closer to the average than to the top, the average has done its one job, which is to warn you. All it's used for beyond that is flattery.

Members type their own rate into the Rate Tracker once, and each weekday morning the comparison is drawn to the top of the twenty tracked accounts, not to the floor.

Button: Add the Daily to my cart

SaveBrew is an educational digest, not financial advice. We are not a bank, a lender, a broker or a registered investment adviser, and we do not hold, move or manage money. Rates and offers come from public sources on the date shown and change without notice, so confirm them with the institution before you act. What you save depends on your own choices.


[[VERBATIM END]]

#### 7.8 /guides/four-percent-against-the-account-you-have

Head: `head.guide.fourpercent.title` "A 4.00% account against yours: the arithmetic · SaveBrew"; `head.guide.fourpercent.meta` "The yearly difference on $10,000, what a minimum balance and a promotional condition do to it, and when moving isn't worth it. Illustrative and dated.". Scene: a measuring tape thread (a woven tape edge drawn on the canvas along the page head) with tick knots that tie at $1, $37, $100, $350 and $400 as the reader reaches each figure in the body, the tape pulling taut at the closing line; static with all ticks under reduced motion. Text hover: the underline measures out: a dashed underline with small tick marks draws under the hovered heading (Shuttle) and the ticks pop (Knot); `:focus-visible` shows it drawn. Kit graphic: the tape edge. Read next: the national average, the rotating category, patio furniture.

[[VERBATIM BEGIN: /home/claude/savebrew/spec/copy/guides/four-percent-against-the-account-you-have.md]]

```yaml
title: "A 4.00% account against the one you already have: the arithmetic on $10,000"
slug: "four-percent-against-the-account-you-have"
thread: "Rates"
dek: "The yearly difference in dollars, what a minimum balance and a promotional condition do to it, the hour it takes to move, and the cases where the hour isn't worth it."
reading_minutes: 6
date: "2026-09-24"
pull_thread: "Under a quarter of a point on $10,000, the move is worth $25 a year, which is an hour of paperwork for the price of a lunch."
membership_line: "The Rate Tracker holds your own rate beside the twenty we check each morning and shows the gap in dollars on your balance, so this arithmetic is done for you before 6:30."
button_label: "Add the Daily to my cart"
```

# A 4.00% account against the one you already have: the arithmetic on $10,000

You have an account. Somewhere on a list there's one paying 4.00 percent. The question you're quietly asking is whether the difference is worth an afternoon, and the honest answer turns on four numbers: your rate, your balance, the conditions attached to the 4.00, and how long the money will sit there. Here's the arithmetic on $10,000, dated September 24, 2026, with no institution named and with the trade offs left in.

## What's the difference in dollars?

APY already includes compounding, so the sum is one multiplication. $10,000 at 4.00 percent APY earns $400 in a year, $100 a quarter. Now the account you have, at four levels an account might be at this week. At 0.01 percent, the standard rate at several of the largest banks: $1. At 0.37 percent, the FDIC national average for September 2026: $37. At 1.00 percent: $100. At 3.50 percent, which is where Bank F (illustrative) sits on our tracked list: $350.

The gaps are $399, $363, $300 and $50. The first three are an afternoon. The last one is a lunch.

Interest is taxable as ordinary income, so take the tax off before deciding. At a 22 percent marginal rate the $363 gap is about $283 after tax; at 12 percent it's about $319. Still an afternoon. And the $50 gap becomes $39 or $44, which is still a lunch, and a lunch is the right unit for it.

## What do the conditions do to it?

The highest published rates this week aren't 4.00. The top of the market is 4.21 percent (NerdWallet, as of September 24, 2026), and the accounts above 4.00 carry conditions: a linked checking account with qualifying deposits, or a required deposit each cycle of about $250, or a rate that applies only above a balance tier. Conditions are where the arithmetic changes, so here are three of them on $10,000.

A promotional rate with a condition. Call it 4.21 percent that drops to 3.00 for any cycle in which the condition is missed. Met each cycle for the year, it pays $421, which is $21 more than a flat 4.00. Missed for the year, it pays $300, which is $100 less. The condition is worth $21 to you if you'll meet it and costs you $100 if you won't, and only you know which.

A balance tier. Call it 3.75 percent from $5,000, with a base rate of 0.25 percent beneath it. On $10,000 it pays $375. If the balance dips to $4,000 for one quarter, that quarter pays at 0.25 instead of 3.75, which on $4,000 is $2.50 instead of $37.50, so the dip costs about $35. An emergency fund that gets used is exactly the balance that dips.

An introductory period. Call it 4.20 percent on new money for 90 days, reverting to 3.40. The promotional quarter pays $105, the three quarters after it pay $85 each, and the year comes to $360. A flat 4.00 with no clock on it pays $400. The bigger number on the sign is the smaller number in the year.

The rule that comes out of the three: compare the rate you'd actually earn in a year of your real behaviour, not the rate on the sign. Bank A (illustrative), at 4.00 percent with no minimum and no condition, is the top of our tracked list for that reason.

## How long does moving take?

About an hour, spread over a week, and most of it isn't the application. Opening an account online takes about fifteen minutes with a government ID, a Social Security number and the routing and account numbers of the account that funds it. The transfer takes one to three business days, and the money earns at the old rate until it lands, so a Monday transfer is earning 4.00 by Thursday at the outside.

The real cost is everything pointed at the old account: a direct deposit split, an autopay for the card, a standing transfer to a goal. Each takes a few minutes to repoint and each is a thing to remember. Keeping the old account open costs nothing at most institutions and avoids the remembering; closing it needs a zero balance and, sometimes, a phone call. Either way, at FDIC insured institutions both accounts are covered to $250,000 per depositor, per institution, per ownership category, so the move changes nothing about safety. It changes the rate and it changes the paperwork, and the paperwork is the hour.

## When is it not worth moving?

Four cases, and they come up more than the rate tables admit.

When the gap is small. Under a quarter of a point on $10,000, the move is worth $25 a year, which is an hour of paperwork for the price of a lunch. Bank F's 3.50 against the 4.00 top is $50 a year, and on a $4,000 balance it's $20. At that size the honest answer is that either account is fine and the hour is better spent on the cashback cap.

When the money is leaving soon. A balance that's paying the contractor in six weeks earns the difference for six weeks: on $10,000 across the $363 gap, that's about $42. Worth it if the account is already open; not worth opening one for.

When the old account is paying for something else. Some institutions discount a mortgage rate or waive a checking fee for holding deposits with them (illustrative, and the terms are on the institution's own site). A $10 checking fee waived twelve times a year is $120, which outruns a $50 rate gap.

When the 4.00 is about to move. It's a variable rate, and it can move the week after you arrive, in either direction. The FOMC raised its target range to 3.75 to 4.00 percent on September 16, and the direction from here isn't promised by anyone, which is the one reason to compare against a tracked list that's checked each morning rather than against a rate you read once in September.

The arithmetic, then, in one line: your balance times the gap, minus the tax, against an hour. On most balances over $5,000 with a gap over a point, the hour wins by a wide margin. On the rest, lunch.

The Rate Tracker holds your own rate beside the twenty we check each morning and shows the gap in dollars on your balance, so this arithmetic is done for you before 6:30.

Button: Add the Daily to my cart

SaveBrew is an educational digest, not financial advice. We are not a bank, a lender, a broker or a registered investment adviser, and we do not hold, move or manage money. Rates and offers come from public sources on the date shown and change without notice, so confirm them with the institution before you act. What you save depends on your own choices.


[[VERBATIM END]]

#### 7.9 /guides/why-patio-furniture-is-cheap-in-october

Head: `head.guide.patio.title` "Why patio furniture is cheap in October · SaveBrew"; `head.guide.patio.meta` "Clearance runs on the retailer's floor space, not your needs. The twelve turns of the seasonal buying cycle, plainly, and what to wait on.". Scene: one indigo thread across the page head with twelve small knots at even intervals, January to December, each knot tying as the reader passes that month in the "How does the year turn?" section, the October knot flashing butter (the 90ms flash of THE PASS, reused at small scale); static with all twelve tied under reduced motion. Text hover: four knots pop along the hovered heading's underline (Knot, 30ms stagger); `:focus-visible` shows them tied. Kit graphic: the four knots on one thread. Read next: the rotating category, the national average, the four percent comparison.

[[VERBATIM BEGIN: /home/claude/savebrew/spec/copy/guides/why-patio-furniture-is-cheap-in-october.md]]

```yaml
title: "Why patio furniture is cheap in October: the seasonal buying cycle, plainly"
slug: "why-patio-furniture-is-cheap-in-october"
thread: "Seasonal"
dek: "Clearance follows the retailer's floor space, not the shopper's needs, and the year turns twelve times on that one fact."
reading_minutes: 5
date: "2026-09-24"
pull_thread: "A patio set in October isn't a bargain because the retailer is generous; it's a bargain because the space it stands on is worth more as a stack of artificial trees."
membership_line: "The seasonal playbook lands on members' dashboards at each turn of the cycle, and the clearance shows up on the morning our tracked prices move, not the week after."
button_label: "Add the Daily to my cart"
```

# Why patio furniture is cheap in October: the seasonal buying cycle, plainly

A four piece patio set that was listed at $899 in May is listed at $549 this week at all three of the home retailers we track. The set didn't change. What changed is the date, and behind the date, the floor: in about six weeks that space holds artificial trees and lights, and the retailer would rather take $350 off the set than pay to store it until April. A patio set in October isn't a bargain because the retailer is generous; it's a bargain because the space it stands on is worth more as a stack of artificial trees.

That's the whole seasonal cycle in one sentence. The rest of this guide is the same sentence applied twelve times.

## What actually sets a clearance price?

Two things, and neither is you. The first is floor space, which is fixed, and which a retailer resets a few times a year: outdoor goods go in around late February, school supplies in July, the holiday floor in the last week of October, and a January reset clears whatever's left. Whatever is still standing on the floor when the reset arrives gets marked down in steps (illustratively 25, then 35, then 50 percent) until it's gone, because the alternative is a truck to a warehouse and a bill for the space.

The second is the cost of holding stock. A set in a stockroom until spring ties up money for half a year and takes a chance on next year's colours. The markdown is cheaper than the wait, so the markdown happens, on the retailer's schedule.

The same logic runs the other way at the start of a season. Outdoor furniture is at full price in April because the retailer knows the demand is arriving; the new TVs cost the most in September, the week they land. The shopper who buys when the need arrives buys at the top. The shopper who buys when the floor turns buys at the bottom. The need is the same in both cases. Only the date moved.

## How does the year turn?

Here's the cycle at the retailers we track, January to December, with what's cut in each turn (illustrative, and the retailer's own listing is the record).

January: bedding and towels, and the last of the holiday goods. TVs come down a step in the last two weeks before the big football game. Fitness equipment goes up, not down, because that's the week people buy it.

February: winter coats and boots begin to clear, and mattresses are cut over the long weekend. The outdoor floor goes in at the end of the turn, at full price.

March: winter sports gear clears, and luggage is cut ahead of spring travel.

April: vacuums and cleaning equipment, as the new models arrive. Outdoor goods are at their yearly high.

May: mattresses again and small kitchen appliances over the long weekend. Grills are at full price.

June: tools, ahead of Father's Day, and gym sign ups in the quiet weeks.

July: summer clothing begins to clear, the big online sale week lands in the middle of the turn, and school supplies open at full price.

August: school supplies and laptops are cut as the turn ends, and the summer floor (fans, coolers, pool goods) starts to clear. Last year's phones drop the week the new ones are announced.

September: the new phones arrive, and their predecessors are cut again. The first patio markdowns appear at the end of the turn, and denim starts to move.

October: patio sets, grills, the last outdoor goods, and denim, all at their low. Halloween goods hold at full price through October 31; the cut comes on November 1. The holiday floor goes in during the last week.

November: the big electronics turn in the last week, with the deepest TV prices of the year, and kitchen appliances and cookware alongside them.

December: toys in the last two weeks before Christmas, and decorations, wrapping and winter goods in the week after it.

Read down that list and the same pattern shows on nearly each line: an item is cheapest right after its season and dearest right before it. That's the floor talking. A patio set in October and a winter coat in February are the same bargain in different weather.

## What's worth waiting on right now?

TVs. The 65 inch sets we track sit within $30 of their August prices, and their turn is the last week of November. A set bought this week buys eight weeks of watching it early, at whatever the November cut turns out to be, and the cut is the part worth waiting to see.

Toys, until the middle of December. Laptops, unless one broke, until late November. Winter coats, until February, with one exception: if the coat is needed in November, a 25 percent code in November beats a 40 percent markdown in February, because February is too late to be warm.

Not worth waiting on: patio sets, grills and denim, which are at the bottom of their turn this week. The denim chains we track cut 40 percent at three of the four, and the fourth's published prices had not moved by six this morning.

## When is the cycle wrong for you?

When you don't have the room. A patio set bought in October lives somewhere for half a year, and a garage that's full is a real cost even though no one bills you for it.

When you don't have the cash. The cycle works for the shopper who pays for the set in October and uses it in April. It fails for the shopper who carries it: $549 on a card at a 24 percent purchase APR, carried for that half year, costs about $66 in interest, which eats a fifth of the $350 markdown. Carry it a year and $132 of the $350 is gone.

When the clearance item is the floor model, sold as is, without the box or the return window. It's still cheap. It's just not the same thing as the one in the box, and the listing says which it is if you read to the bottom.

So the cycle is a tool for the patient with cash and a trap for the impatient with a card, and knowing which one you are this week is most of the skill. The rest is knowing the date the floor turns, which is what we watch the tracked prices for.

The seasonal playbook lands on members' dashboards at each turn of the cycle, and the clearance shows up on the morning our tracked prices move, not the week after.

Button: Add the Daily to my cart

SaveBrew is an educational digest, not financial advice. We are not a bank, a lender, a broker or a registered investment adviser, and we do not hold, move or manage money. Rates and offers come from public sources on the date shown and change without notice, so confirm them with the institution before you act. What you save depends on your own choices.


[[VERBATIM END]]

### 7.10 Your moves (/your-moves, the interactive feature: a ranker)

**Purpose.** The one bespoke working tool (Art Direction 3.21, interactive_feature.md): six yes or no toggles about the visitor's money re-rank this week's public moves for that visitor, with the minutes each takes, using editorial weights rather than arithmetic, and end on the purchase CTA. Public, no account, no form, no email field. Not a quiz, not a calculator, not a sorter.

**Head.** Title `head.moves.title` "Your moves, ranked for you this week · SaveBrew". Meta `head.moves.meta` "Six yes or no questions about your money, and this week's public moves rank themselves for you, with the minutes each takes. No account needed.". Indexed.

**Scene.** The visitor's threads lifting out of the cloth: a lazy 2D canvas behind the ranked list draws one thread per candidate lying flat in a woven field; when a toggle changes, the affected threads lift out of the cloth in the new order (Knot, 0.38s), the ranked four standing highest; static under reduced motion.

**Text hover.** The word lifts 2px on a thread shadow: hovered headings and links translate up 2px with a 2px indigo thread drawn beneath as a shadow (Knot, 0.11s); `:focus-visible` the same plus the stitch outline.

**Asset slots.** `photo.ranker-edge` (4:5, the row's edge image in column five beside the toggles), `kit.svg` (the Your moves icon, the five thread icons on the candidates).

**Sections.**

1. **Heading pass.** `moves.heading` "Which threads should you pull first?" and the standfirst `moves.standfirst` "Answer six yes or no questions about your money and this week's moves are ranked for you, with the minutes each takes. Members get a ranked list like this each weekday morning.". Entrance: the weft pass draws under the heading, the standfirst wipes in.
2. **The six toggles.** Legend `moves.toggles.legend` "Which of these are true of your money?". Six switches (CUR-009, `role="switch"`, `aria-checked`, 44px targets, each a thread that pulls tight when on, state labels `moves.toggle.state.on` "Yes" and `moves.toggle.state.off` "No"), five in the warp columns and the sixth centred beneath, `photo.ranker-edge` filling the remaining track at 1024 to 1279 so no cell sits empty: `moves.toggle.1` "I have a high yield savings account"; `moves.toggle.2` "Some of my money sits in a big bank at under 1 percent"; `moves.toggle.3` "I carry a card with rotating categories"; `moves.toggle.4` "I'm saving toward a dated goal"; `moves.toggle.5` "I bought something over $200 in the last four weeks"; `moves.toggle.6` "I haven't looked at my paycheck split this year". All off on load. Entrance: the six threads tighten in turn (Knot, 50ms stagger).
3. **The ranked four and the greyed rest.** The state line above the list: with no toggle on, `moves.state.empty` "This is the editors' order for this week. Turn on what applies to you and the list reranks."; while toggling, `moves.state.progress.pattern` "{shown} of {total} shown for you" (example "4 of 7 shown for you"); with the result settled, `moves.state.result.pattern` "Ranked for you: four moves, about {minutes} minutes in all. The rest sit beneath with the reason each ranked lower." (example "Ranked for you: four moves, about 35 minutes in all. The rest sit beneath with the reason each ranked lower.", the minutes being the sum of the four). The top four, ranked one to four (marked by position on the thread, not numerals), each with its thread icon and name (aria `moves.rank.thread.aria.pattern` "{thread} thread"), the headline, `moves.rank.minutes.pattern` "about {minutes} minutes", the label `moves.rank.why.label` "Why here" with the candidate's `why` line, and the label `moves.rank.skip.label` "Skip this if" with its `skip_if` line. Beneath them the remaining candidates, greyed to muted indigo, each with the one line reason it ranked lower: the `moves.lower.N` line for the heaviest toggle in its weight vector that is off (`moves.lower.1` "ranked lower because you don't have a high yield savings account"; `moves.lower.2` "ranked lower because your money isn't sitting in a big bank at under 1 percent"; `moves.lower.3` "ranked lower because you don't carry a rotating category card"; `moves.lower.4` "ranked lower because you aren't saving toward a dated goal"; `moves.lower.5` "ranked lower because you haven't bought anything over $200 lately"; `moves.lower.6` "ranked lower because you've looked at your paycheck split this year"), or `moves.lower.default` "ranked lower in this week's editors' order" when no toggle is on. Controls beneath the list: **Copy this list** (`moves.copy.label`) → writes the four ranked headlines with their minutes to the clipboard and shows `moves.copy.done` "Copied. Your four moves, with their minutes, are on the clipboard." with a tick that draws (or `moves.copy.failed` "Copying didn't work in this browser. Select the list and copy it by hand."); **Print this list** (`moves.print.label`) → opens the print view (a print stylesheet on the same page) titled `moves.print.title` "Your moves, ranked on Thursday, September 24, 2026" with the note `moves.print.note` "From this week's Roundup candidates. Dollar amounts are about, not exact.", announcing `moves.print.done` "Opening the print view: today's date and the four moves as ranked.". Entrance: the candidates lift from the cloth in the editors' order (Knot, 60ms stagger). Re-ranking on each toggle change animates with GSAP Flip (Knot, 0.38s) so the threads visibly re-order; the count line updates in an aria live region.
4. **The Bobbin and the members' line.** **Add the Daily to my cart** (`moves.cta`) → adds SB101 and opens the drawer; beneath it `moves.cta.line` "Members get a ranked list like this each weekday morning, built on that morning's brief.". Entrance: the Bobbin's stitch draws (Shuttle, slow).
5. **The disclaimer** `disclaimer.text` at the foot, above the footer (`moves.disclaimer`). Entrance: fades up inside a clip.
6. **Footer** (6.2).

**Logic, client side and deterministic (Art Direction 3.21, moves.json).** The candidates ship with the page from `/data/moves.json` (copied into the project as a static asset and inlined at build time; no fetch is needed for first render). `score = (8 minus the candidate's position in editors_order, first position being 1) + the sum of its weights for toggles that are on`; ties broken by fewer minutes; the top four are shown ranked, the rest greyed. Worked example: no toggles on gives scores 7, 6, 5, 4, 3, 2, 1 in the editors' order, so the ranked four are "Write down your account's published rate before it moves", "Activate the October category on the morning it opens", "Patio sets are 30 to 40 percent off; TVs aren't yet" and "Put your rate against the tracked top: 4.00 percent on your balance", about 20 minutes in all, and the state line reads the editors' order line. Turning on toggle 3 alone (carries a rotating category card) adds 3 to the two cashback candidates, so the scores in the editors' order become 7, 9, 5, 4, 3, 5, 1: "Activate the October category on the morning it opens" ranks first at 9, "Write down your account's published rate before it moves" second at 7, and the two candidates tied at 5 are split by minutes, so "Read the cap line: how much of the $1,500 is left?" (4 minutes) ranks third and "Patio sets are 30 to 40 percent off; TVs aren't yet" (5 minutes) ranks fourth; "Put your rate against the tracked top" drops to the greyed list with `moves.lower.2`, because toggle 2 (weight 3) is its heaviest toggle that is off. QA reproduces this example by hand.

**States.** Empty (no toggles on): the editors' order with the empty state line. In progress: live re-rank on each change with the progress line. Result: the ranked four with the copy and print controls. Error: none possible; the data ships with the page. Works with motion disabled and on a 375px viewport with one thumb: the toggles stack in one column, the list stacks beneath, the Bobbin is full width. QA turns on toggles, watches the re-rank, copies the list and lands on the cart drawer from the CTA.

**Mobile.** One column; the edge image sits under the toggles at 4:5; the print view is reachable.

**The candidates, verbatim (/home/claude/savebrew/spec/copy/moves.json, shipped as /data/moves.json).**

```json
{
  "week_of": "2026-09-19",
  "note": "This week's public candidates for the Your moves ranker (art direction 3.21). Refreshed each Saturday with the Roundup. Dollar amounts are about, not exact; accounts and cards are illustrative. Weights follow toggle_order; each is an integer 0 to 3. Score = (8 minus position in editors_order) plus the weights of the toggles that are on; ties go to fewer minutes.",
  "toggle_order": [
    "has_high_yield_savings_account",
    "money_in_big_bank_account_under_1_percent",
    "carries_rotating_category_card",
    "saving_toward_dated_goal",
    "bought_something_over_200_recently",
    "paycheck_split_not_looked_at_this_year"
  ],
  "editors_order": [
    "rates_write_down_your_rate",
    "cashback_activate_october",
    "seasonal_patio_now_tv_later",
    "rates_compare_to_the_top",
    "paycheck_split_one_stub",
    "cashback_grocery_cap_check",
    "coupons_price_adjustment"
  ],
  "candidates": [
    {
      "id": "rates_write_down_your_rate",
      "thread": "Rates",
      "headline": "Write down your account's published rate before it moves",
      "minutes": 3,
      "why": "The Fed raised a quarter point Wednesday; tracked accounts tend to reprice within two weeks, and a dated number shows it.",
      "skip_if": "Your account is on a tracked list that already records its rate each morning.",
      "weights": [1, 3, 0, 1, 0, 1]
    },
    {
      "id": "cashback_activate_october",
      "thread": "Cashback",
      "headline": "Activate the October category on the morning it opens",
      "minutes": 2,
      "why": "Both tracked rotating cards named their fourth quarter categories this week; activation is free and the 5 percent starts October 1.",
      "skip_if": "You don't carry a rotating category card, or yours activates on its own.",
      "weights": [0, 0, 3, 0, 0, 0]
    },
    {
      "id": "seasonal_patio_now_tv_later",
      "thread": "Seasonal",
      "headline": "Patio sets are 30 to 40 percent off; TVs aren't yet",
      "minutes": 5,
      "why": "The outdoor aisle is being cleared for holiday stock; the tracked TVs sit within $30 of August and turn in late November.",
      "skip_if": "There's nowhere to keep a patio set until April, or the TV can't wait eight weeks.",
      "weights": [0, 0, 0, 1, 1, 0]
    },
    {
      "id": "rates_compare_to_the_top",
      "thread": "Rates",
      "headline": "Put your rate against the tracked top: 4.00 percent on your balance",
      "minutes": 10,
      "why": "On $10,000 the gap between 0.37 and 4.00 percent is $363 a year; your balance decides whether an hour is worth it.",
      "skip_if": "Your published rate is already within a quarter of a point of 4.00.",
      "weights": [0, 3, 0, 2, 0, 1]
    },
    {
      "id": "paycheck_split_one_stub",
      "thread": "Paycheck",
      "headline": "Split one pay stub three ways: needs, wants, and the 20 percent",
      "minutes": 10,
      "why": "October has three paydays for anyone paid on alternate Fridays from October 2, and the third has no bills assigned yet.",
      "skip_if": "You did the split this year and nothing about your pay or your rent has changed.",
      "weights": [0, 1, 0, 2, 0, 3]
    },
    {
      "id": "cashback_grocery_cap_check",
      "thread": "Cashback",
      "headline": "Read the cap line: how much of the $1,500 is left?",
      "minutes": 4,
      "why": "The grocery category pays through September 30 and unused cap doesn't carry; the card's app shows spend against it in one line.",
      "skip_if": "You've already passed the cap, or your groceries go on a flat 3 percent card.",
      "weights": [0, 0, 3, 0, 1, 0]
    },
    {
      "id": "coupons_price_adjustment",
      "thread": "Coupons",
      "headline": "Ask for a price adjustment on the big thing you bought recently",
      "minutes": 6,
      "why": "Patio sets and grills were cut 30 to 40 percent this week; some retailers' published policies refund the difference within 30 days.",
      "skip_if": "The published price on what you bought hasn't dropped since you paid it.",
      "weights": [0, 0, 0, 0, 3, 0]
    }
  ]
}

```

### 7.11 About (/about)

**Purpose.** Who checks the threads and where, in the craftsman's voice, with no invented heritage, ending on a purchase CTA.

**Head.** Title `head.about.title` "Who checks the threads? About SaveBrew". Meta `head.about.meta` "SaveBrew Inc., King of Prussia, Pennsylvania: who checks the savings rates, cashback windows and seasonal prices before six each weekday, and how.". Indexed.

**Scene.** The Selvedge Seal being woven row by row on a lazy canvas beside the copy: five warp threads crossed by seven weft rows, the S and B forming from the indigo and butter crossings as the visitor scrolls the body, the running stitch border last; static and complete under reduced motion.

**Text hover.** A butter dye wash behind the word: a butter #F6E7A1 highlight sweeps behind the hovered heading or link left to right (Shuttle, 0.38s) and stays while hovered; `:focus-visible` shows the wash at once with the stitch outline.

**Asset slots.** `photo.about-hero` (21:9 desktop, 4:5 phone) and `video.hero-loop` (the hero band plays the loop at 35 percent under the still's grade, poster first), `kit.svg` (the Selvedge Seal at 160px).

**Sections.**

1. **Hero band.** The heading pass "Who checks the threads?" over `photo.about-hero` with the hero loop beneath it, full width. Entrance: the band's clip opens from the centre outward, the heading arrives tight.
2. **The About copy** in CSS multicolumn (`columns: 34ch`) across columns one to three, the woven seal in columns four to five, the copy verbatim from about.md below (its H3 questions as in file), ending on the Bobbin **Add the Daily to my cart** → adds SB101 and opens the drawer. Entrance: the columns wipe in one after another while the seal weaves (Shuttle per row).
3. **How are items chosen?** One of the two variants from about.md, chosen by the owner's answer to Offering Spec 17.4: the "no referral fees" variant ships only on the owner's confirmation that SaveBrew takes no referral fees or commissions; otherwise the second variant, which makes no claim about fees. Entrance: a weft pass right to left.
4. **Where are we?** The band beneath, as a row across the five columns: the entity, the address, the phone (tel link), the email (mailto link) and the support hours line from about.md (hours proposed). Entrance: a knot ties at the address, then the row wipes in.
5. **Compact membership strip** (6.8) with its own one line: `add.about.compact.line` "A short brief, checked properly, on weekday mornings: that's the Daily." Entrance: one weft pass.
6. **Footer** (6.2).

**Mobile.** One column; the seal at 96px above the copy; the address band stacks.

**The About copy, verbatim.**

[[VERBATIM BEGIN: /home/claude/savebrew/spec/copy/about.md]]

# About (/about)

Heading pass: Who checks the threads?

The body below is the About copy, set in multicolumn beside the Selvedge Seal per art direction 3.23. It does not restate the home hero's promise or price; the compact membership strip beneath it carries those. Word count of the body: see manifest.md.

## The About copy

Most writing about saving money fails in one of two ways, and we've read enough of it to name both. The first is the list that's really a shop floor: the account at the top pays the writer something for being there, and you can't tell which lines were chosen for you and which were chosen for the commission. The second is the sentence that's true and useless. Pay yourself first. Automate your savings. Nobody with a paycheck and a rent payment learns anything from that, and the people who write it know.

SaveBrew is a new publication, built to do neither. There's no heritage to tell you about and we won't invent one: SaveBrew Inc. is in King of Prussia, Pennsylvania, the brew is money, and the work is new.

### What happens before six?

The work is a method, not a mood. Five threads run through a working adult's money: the rate on savings, the cashback windows on cards, the coupon codes that stack and the ones that don't, the seasonal prices that turn on the retailer's schedule rather than yours, and the paycheck itself. Each weekday morning, before six, we pull on all five.

Rates means opening the published rate of each of the twenty accounts and CDs on our tracked list and writing down what changed since yesterday, to the hundredth of a point. Cashback means reading the two rotating category cards we track for their categories, caps and activation windows. Coupons means putting a code into a live cart before it's written up, because a code that fails at checkout is worse than no code. Seasonal means watching the published prices of a fixed basket of goods at the retailers we track, so the clearance turn shows up the morning it starts. Paycheck means taking one framework at a time and doing its arithmetic on an illustrative pay stub, with the numbers shown.

Then we cut. A morning's checking turns up more than five things, and most of it doesn't make the pass. What's left is five items a person can read in about four minutes, one on each thread, each ending in one small action or in "not this week".

### Why so few?

Because the sifting is the product. Information about money isn't scarce; you can get thirty rate tables and forty coupon sites before breakfast. What's scarce is someone who has already read them, done the multiplication on a real balance, dated it, and thrown the rest away. Twenty accounts checked before six, cut to one line, is worth more than twenty accounts handed to you raw at noon.

We also hold two rules a reader can check. Each number on this site is either dated and attributed or marked illustrative. And SaveBrew is a digest, not a bank: we don't hold, move or manage anyone's money, which is why the same disclaimer sits at the foot of the brief, the Roundup and each guide.

That's the whole of it. A short brief, checked properly, on weekday mornings, from an office in King of Prussia.

If that's the kind of morning you want, the Daily is where it lands.

Button: Add the Daily to my cart

## "How items are chosen" (optional paragraph; the band sits between the About copy and "Where we are")

SHIP ONLY IF THE OWNER CONFIRMS: no referral fees

### How are items chosen?

No item on SaveBrew is paid for by the institution it's about. SaveBrew takes no referral fees and no commissions from the banks, cards or retailers it writes about, so an account is at the top of the tracked list because its published rate put it there, and a code is in the brief because it worked in a cart that morning. The editors choose on what a reader can act on, and on that alone.

SHIP IF THE OWNER DOES NOT CONFIRM (makes no claim about fees)

### How are items chosen?

An account sits at the top of the tracked list because its published rate put it there that morning. A code is in the brief because it worked in a live cart before six. A seasonal item is in because the tracked price moved, and a paycheck item is in because the arithmetic held on the illustrative stub. The editors choose on what a reader can act on, and the date on each item says when it was true.

## "Where we are" (the band beneath)

Heading: Where are we?

SaveBrew Inc.
660 American Ave, King Of Prussia, PA 19406
(888) 338 8809
support@savebrew.com

Support hours (proposed): Monday to Friday, 9:00 AM to 5:00 PM Eastern. Email is read on weekdays and answered by a person within one working day.

Note for the build: the phone is written with spaces in customer facing copy, matching Writer B's convention across the site and the dashboard's own "(555) 010 0123" pattern; the href is tel:+18883388809. The hours and the reply time are proposed and need the owner's confirmation before launch.


[[VERBATIM END: /home/claude/savebrew/spec/copy/about.md]]

### 7.12 Contact (/contact)

**Purpose.** The address, phone, email and hours, and a form a person reads. Support, not capture; secondary to buying but always present.

**Head.** Title `head.contact.title` "How to reach a person at SaveBrew". Meta `head.contact.meta` "SaveBrew Inc., 660 American Ave, King of Prussia, PA 19406. (888) 338 8809, support@savebrew.com, and a form a person reads.". Indexed.

**Scene.** A single knot tied at the address line: a lazy SVG thread runs from the heading pass down to the address block and ties one knot beside the entity name as the block enters the viewport (Knot); static and tied under reduced motion.

**Text hover.** Stitch dashes under links: a dashed underline appears dash by dash under the hovered link (Shuttle, 0.11s per dash); `:focus-visible` shows it complete.

**Asset slots.** `photo.contact-side` (4:5, beside the address), `kit.svg`.

**Sections.**

1. **Heading pass.** `contact.heading` "How do I reach a person?" and `contact.intro` "A person reads what comes in: on the phone during the hours below, and by email at any hour.". Entrance: the weft pass draws, the intro wipes in.
2. **The address, phone and email in three columns**, the support hours in the fourth, `photo.contact-side` in the fifth: `contact.address.entity` "SaveBrew Inc.", `contact.address.street` "660 American Ave", `contact.address.city` "King Of Prussia, PA 19406" (an `address` element); `contact.phone.label` "Phone" with `contact.phone` "(888) 338 8809" → `contact.phone.href` tel:+18883388809; `contact.email.label` "Email" with `contact.email` "support@savebrew.com" → mailto:support@savebrew.com; `contact.hours.label` "Support hours" with `contact.hours` "Monday to Friday, 9:00 AM to 5:00 PM Eastern" and `contact.reply` "Email gets a reply from a person within one working day." (both proposed, owner to confirm). Entrance: the knot ties at the address, then the four cells wipe in left to right and the still's clip opens.
3. **The form.** Heading `contact.form.heading` "Or write to us here". One column, top aligned labels always visible, placeholders as examples only, required and optional both marked (`contact.form.required.marker` "(required)", `contact.form.optional.marker` "(optional)"), the selvedge stitch as the underline that draws on focus (CUR-010), autocomplete tokens, Enter submits. Fields:
   - `contact.form.name.label` "Your name (required)", text, `autocomplete="name"`, placeholder `contact.form.name.placeholder` "First and last name"; error empty `contact.form.error.name` "Enter your name".
   - `contact.form.email.label` "Email address (required)", email, `autocomplete="email"`, hint `contact.form.email.hint` "The reply goes here.", placeholder `contact.form.email.placeholder` "name@example.com"; errors `contact.form.error.email.empty` "Enter your email address", `contact.form.error.email.format` "Enter an email address in the correct format, like name@example.com".
   - `contact.form.order.label` "Order number (optional)", text, hint `contact.form.order.hint` "It's in your confirmation email and helps us find your membership faster." (a proposed addition so both markers appear).
   - `contact.form.message.label` "Message (required)", textarea, placeholder `contact.form.message.placeholder` "What happened, or what would you like to know?"; error empty `contact.form.error.message` "Enter your message".
   - Submit, the Bobbin: **Send my message** (`contact.form.submit`) → validates, shows `contact.form.sending` "Sending your message" on the button while in flight, then the success line `contact.form.success.pattern` "Sent. A person will reply to {email} within one working day." (aria live polite) replacing the form. Errors: validate on blur with a short delay; message beside its field and repeated in a summary titled `contact.form.error.summary` "There is a problem" above the button, linked to the fields; values preserved; text plus a knot glyph, not colour alone. System failure: `contact.form.error.system` "Sorry, your message didn't send. Try again in a minute, or email support@savebrew.com directly.". The preview build sends nothing and still renders the success state.
   Entrance: the fields' stitch underlines draw one after another (Shuttle, 60ms stagger).
4. **Footer** (6.2).

**Mobile.** The five cells stack (address, phone, email, hours, image); the form is full width with 44px controls.

### 7.13 Cart (/cart)

The cart drawer of 6.5 rendered as a full page for the footer link and for visitors without JavaScript: `cart.heading` "Your cart" as the heading pass, the line item, the charge, the renewal sentence, the tax line, the cadence switch, **Remove**, the Bobbin **Go to checkout** → `/checkout`, and the empty state `cart.empty.line` "Your cart is empty." with **Choose a membership** → `/membership`. Head: `head.cart.title` "Your cart · SaveBrew"; `head.cart.meta` "One membership at a time: the Daily or the Daily for Two, monthly or yearly, with today's charge and the renewal date in plain words."; noindex. Scene: the knot sliding along a thread into the spool glyph (the drawer's scene, on the page head). Text hover: standard link states (the running stitch underline). Entrance: the line item wipes in, then the summary lines fade up inside the clip, the Bobbin's stitch draws. Mobile: one column, the Bobbin full width at the foot. This route is the "cart" step of the conventions floor sequence: product, cart, checkout, confirmation, nothing invented between.

### 7.14 Checkout (/checkout)

**Purpose.** The complete guest checkout of checkout_spec.md for a digital subscription: contact, billing address, payment, order summary, no shipping, no account step, each cost known before this page, one primary action. The plainest page on the site.

**Head.** Title `head.checkout.title` "Checkout · SaveBrew". Meta `head.checkout.meta` "Guest checkout with no account step: contact, billing address and payment, then a confirmation that opens your dashboard.". Noindex.

**Scene.** A running stitch down the left gutter (the selvedge) that advances one section at a time: it draws to the foot of Contact when Contact validates, to the foot of Billing address when that validates, and so on, tying a small knot at each section head (Knot); static and complete under reduced motion. No other motion beyond focus states.

**Text hover.** None beyond focus states: fields draw their stitch underline on focus (CUR-010), the Bobbin runs its stitch on hover and tightens on press.

**Layout.** One column on white, `max-width: none` (the form's column is the first warp column pair, and the order summary rides beside it in columns four to five on desktop, sticky, so the page still fills the width per 3.17; under 1024 the summary sits above the submit). Numbered section heads in Big Shoulders 600 (the numbering is the checkout spec's own sectioning and is exempt from the "nothing is numbered" rule of the marketing site). Top aligned labels always visible; required and optional both marked (`checkout.required.marker` "(required)", `checkout.optional.marker` "(optional)"); the autocomplete token on each field; validation on blur with a short delay, not while typing; each message beside its field and repeated in a summary near the submit; what the buyer typed is preserved, card fields included; nothing conveyed by colour alone.

**Sections and fields.**

0. **Guest checkout.** No account creation, no register, no sign in to continue, anywhere between the cart and the confirmation; no field is gated behind one. Heading `checkout.heading` "Checkout"; intro `checkout.intro` "No account needed. Your dashboard opens for the email address you enter here.". Empty cart: the page shows `checkout.empty` "Your cart is empty. Choose a membership to continue." with **Choose a membership** (`checkout.empty.link`) → `/membership` and no form.
1. **Contact** (`checkout.section.contact` "Contact"):
   - `checkout.contact.first.label` "First name (required)", text, autocomplete `given-name`; empty: `checkout.contact.first.error.empty` "Enter your first name".
   - `checkout.contact.last.label` "Last name (required)", text, autocomplete `family-name`; empty: `checkout.contact.last.error.empty` "Enter your last name".
   - `checkout.contact.email.label` "Email address (required)", email, autocomplete `email`, hint `checkout.contact.email.hint` "This becomes your dashboard sign in."; empty: `checkout.contact.email.error.empty` "Enter your email address"; format: `checkout.contact.email.error.format` "Enter an email address in the correct format, like name@example.com".
   - `checkout.contact.phone.label` "Phone number (required)", tel, autocomplete `tel`, inputmode tel, hint `checkout.contact.phone.hint` "Used for support and to confirm it is you if you ever lose access. Texts are sent only if you opt in on your dashboard." (the stated reason the checkout spec requires); empty: `checkout.contact.phone.error.empty` "Enter your phone number"; format: `checkout.contact.phone.error.format` "Enter a phone number with 10 digits, like (555) 010 0123".
2. **Shipping address.** Omitted: the offering is digital. No shipping section, no shipping line in the summary.
3. **Billing address** (`checkout.section.billing` "Billing address"), the full address, country first so the labels can switch:
   - `checkout.billing.country.label` "Country (required)", select, autocomplete `country`, default `checkout.billing.country.default` "United States"; empty: `checkout.billing.country.error.empty` "Select your country".
   - `checkout.billing.line1.label` "Address line 1 (required)", text, autocomplete `address-line1`; empty: `checkout.billing.line1.error.empty` "Enter the first line of your billing address".
   - `checkout.billing.line2.label` "Address line 2 (optional)", text, autocomplete `address-line2`.
   - `checkout.billing.city.label` "City (required)", text, autocomplete `address-level2`; empty: `checkout.billing.city.error.empty` "Enter your city".
   - `checkout.billing.state.label` "State (required)", a select of the states and territories for the United States (autocomplete `address-level1`; empty: `checkout.billing.state.error.empty` "Select your state"); for any other country the label becomes `checkout.billing.state.label.international` "State or province (required)" as a text field (empty: `checkout.billing.state.error.empty.international` "Enter your state or province").
   - `checkout.billing.zip.label` "ZIP code (required)", text, inputmode numeric, autocomplete `postal-code`; empty: `checkout.billing.zip.error.empty` "Enter your ZIP code"; format: `checkout.billing.zip.error.format` "Enter a ZIP code with 5 digits, like 19406"; for any other country the label becomes `checkout.billing.zip.label.international` "Postal code (required)" (empty: `checkout.billing.zip.error.empty.international` "Enter your postal code", no format check).
   City, state and ZIP may share one row on desktop as one genuine unit; everything else stacks.
4. **Payment** (`checkout.section.payment` "Payment"): the accepted card marks (Visa, Mastercard, American Express, Discover) as one small row near the card fields with the caption `checkout.payment.marks.caption` "Visa, Mastercard, American Express and Discover accepted.", and no other badge anywhere on the site.
   - `checkout.payment.name.label` "Name on card (required)", text, autocomplete `cc-name`; empty: `checkout.payment.name.error.empty` "Enter the name as it appears on your card".
   - `checkout.payment.number.label` "Card number (required)", text, inputmode numeric, autocomplete `cc-number`, formatted in groups of four as typed; empty: `checkout.payment.number.error.empty` "Enter your card number"; length or characters: `checkout.payment.number.error.format` "Enter a card number with 15 or 16 digits, using numbers only"; Luhn: `checkout.payment.number.error.check` "Enter the card number exactly as it appears on your card; one digit is out of place".
   - `checkout.payment.expiry.label` "Card expiry (required)": two selects side by side as one unit, `checkout.payment.expiry.mm.label` "MM" (autocomplete `cc-exp-month`, 01 to 12) and `checkout.payment.expiry.yyyy.label` "YYYY" (autocomplete `cc-exp-year`, this year to ten years out); empty: `checkout.payment.expiry.error.empty` "Select the expiry date printed on your card, MM then YYYY"; past: `checkout.payment.expiry.error.past` "Select an expiry date that hasn't passed".
   - `checkout.payment.cvv.label` "Security code (required)", text, inputmode numeric, autocomplete `cc-csc`, 3 or 4 digits, beside the expiry as one unit, with the help affordance `checkout.payment.cvv.help.label` "Where is it?" revealing `checkout.payment.cvv.help.text` "The 3 digits on the back of your card, to the right of the signature strip. On an American Express card, the 4 digits on the front above the card number."; empty: `checkout.payment.cvv.error.empty` "Enter the security code from your card"; format: `checkout.payment.cvv.error.format` "Enter the 3 digit code from the back of your card, or the 4 digit code from the front of an American Express card".
5. **Order summary** (`checkout.section.summary` "Order summary"), live, bound to the cart: `checkout.summary.membership.label` "Membership" with `checkout.summary.membership.pattern` "{membership}, billed {cadence}"; `checkout.summary.charge.label` "Today's charge" with the amount; `checkout.summary.renewal.label` "Renewal" with the cart's renewal sentence by cadence (`checkout.summary.renewal`); `checkout.summary.tax.label` "Tax and fees" with `checkout.summary.tax` "Sales tax included where it applies. No other fees."; `checkout.summary.total.label` "Total today" with the same amount (no number appears here for the first time: each figure was on the membership card and in the cart); the link **Back to your cart** (`checkout.summary.edit`) → opens the cart drawer. Then the one unchecked required box, separate from any marketing consent: `checkout.terms.label` "I am 18 or older and accept the Terms of Service and Privacy Policy." with "Terms of Service" → `/terms` and "Privacy Policy" → `/privacy` as links inside the label; unticked error `checkout.terms.error` "Confirm that you are 18 or older and accept the Terms of Service and Privacy Policy". No SMS consent box on the checkout (SMS consent lives only in the verbatim block).
6. **Submit.** The Bobbin `checkout.submit.pattern` "Pay {amount} now" with the amount bound to the cart total (example `checkout.submit.example` "Pay $7.99 now"); the note beneath it `checkout.note` "Preview build: no live charge is taken and no card details are stored. The form still completes to your confirmation."; while placing, the label reads `checkout.processing` "Placing your order". On submit: validate all required fields; on failure, focus the summary titled `checkout.error.summary` "There is a problem" with the hint `checkout.error.summary.hint` "Fix the fields below, then pay. What you've typed is still there." and each error linked to its field, values preserved; on success, write the order (a generated order number in the pattern SB1 followed by seven digits, the SKU, the cadence, the amount, the email, the last four digits, the time) to sessionStorage, empty the cart, and route to `/confirmation`. Enter submits; the browser back button returns to the cart.

**Entrance.** The four sections wipe in top to bottom one after another (Shuttle, 80ms stagger), the stitch drawing to the first section head.

**Mobile (375).** One column throughout, the summary above the submit, 44px controls, the whole purchase completable with one thumb (QA performs it).

### 7.15 Order confirmation (/confirmation)

**Purpose.** A real confirmation: the order, what was bought and charged, when it renews, the support contact, the dashboard opening for the checkout email, the optional password, the optional SMS step, and for the Daily for Two the second reader's invite. Account creation is offered only here, after the order, as an optional convenience.

**Head.** Title `head.confirmation.title` "Your membership is on · SaveBrew". Meta `head.confirmation.meta` "Order confirmed: what was bought, what was charged, when it renews, and your dashboard ready for the email you used.". Noindex. Without an order in sessionStorage the route shows `checkout.empty` "Your cart is empty. Choose a membership to continue." with **Choose a membership** → `/membership`.

**Scene.** The seal's last stitch tying off: the Selvedge Seal at 160px beside the heading, already woven, its border's final stitch drawing and knotting on load (Knot, slow 1.2s); static under reduced motion.

**Text hover.** The running stitch underline (standard).

**Sections.**

1. **The order.** Heading `confirm.heading` "Your membership is on." with the seal; `confirm.order.pattern` "Order {number}, placed {date in words} at {time} Eastern." (example "Order SB10000214, placed Thursday, September 24, 2026 at 9:14 AM Eastern."); `confirm.bought.label` "What you bought" with `confirm.bought.pattern` "{membership}, billed {cadence}" (example "SaveBrew Daily, billed monthly"); `confirm.charged.label` "What was charged" with `confirm.charged.pattern` "{amount} to the card ending {last four digits}." (example "$7.99 to the card ending 4242.") and the line `confirm.charged.preview` "No live charge was taken on this preview build."; `confirm.renewal.label` "Renewal" with the renewal sentence by cadence (`confirm.renewal`); `confirm.first.pass.pattern` "Your first pass goes out at 6:30 AM Eastern on {next weekday in words}." (example "Your first pass goes out at 6:30 AM Eastern on Friday, September 25.", computed as the next weekday); `confirm.support` "Questions about the order? support@savebrew.com or (888) 338 8809. Your order number is in the email we just sent." with the email and phone as links. Entrance: one weft pass across the block.
2. **What happens now?** Heading `confirm.dashboard.heading` "What happens now?"; `confirm.dashboard.ready.pattern` "Your dashboard is ready for {email}. Set a password to open it now, or use the sign in link we just emailed you."; the optional password field `confirm.password.label` "Password (optional)" with hint `confirm.password.hint` "At least 10 characters. Skip it and the emailed link signs you in instead.", autocomplete `new-password`, the button **Set my password** (`confirm.password.submit`) → validates (`confirm.password.error.short` "Enter a password with at least 10 characters") and shows `confirm.password.done` "Password set." Setting it is optional; the emailed link signs the member in. Entrance: the fields' stitch draws.
3. **Join Our SMS List, an optional step.** `confirm.sms.intro` "An optional step, separate from your order, which is already complete." then the verbatim block of 6.3 with both boxes unchecked, one program, its own success and error states, clearly separate from the order, which is already complete (`confirm.sms.block`). Entrance: the stitch draws under the field.
4. **Open my dashboard.** The Bobbin **Open my dashboard** (`confirm.open`) → sets the demo session for the checkout email and routes to `/today`. Entrance: the Bobbin's stitch draws.
5. **Invite your second reader** (SB201 and SB202 only). Heading `confirm.two.heading` "Invite your second reader"; `confirm.two.line` "Their email address is all we need. They'll get a link to set up their own sign in, their own brief view and their own text settings. You can also do this later from Membership on your dashboard."; field `confirm.two.email.label` "Second reader's email address (optional now)", email, autocomplete `email`; button **Send the invite** (`confirm.two.submit`) → validates (`confirm.two.error.format` "Enter an email address in the correct format, like name@example.com"; `confirm.two.error.same` "Enter an email address other than your own; the second reader needs their own sign in") and shows `confirm.two.done.pattern` "Invite sent to {email}. It's good for 7 days, and you can resend it from Membership on your dashboard.". Entrance: a weft pass right to left.
6. **Footer** (6.2).

**Mobile.** One column; the seal at 96px; the Bobbin full width.

### 7.16 to 7.19 The dashboard (/today, /rates, /goals, /archive)

**Purpose.** The product itself: the three views of Offering Spec 10.3 (Today, Rate Tracker, Goals) plus the archive, built as real interactive pages, not mockups, so the product shots are captured from the product and a reviewer can open the thing being sold. They sit behind a demo sign in: on this preview build any syntactically valid email address at /sign-in (or the checkout email on /confirmation) opens the illustrative member Jordan (initials JM, "Member since 2026", phone (555) 010 0123), and the pages say so. No real member data exists; all figures are illustrative and labelled.

**The demo session.** localStorage key `savebrew.session`: `{email, name: "Jordan", initials: "JM", since: 2026, sku, cadence, renewsOn, texts: {optedIn: true, rates: true, goals: true, billing: true}, phone: "(555) 010 0123", cancelled: false, accessEnds: null}`. /sign-in sets it with SB101 monthly renewing October 24, 2026 (the Offering Spec's example); /confirmation sets it from the order. A dashboard route with no session redirects to `/sign-in` client side (the server rendered shell carries the sign in prompt so nothing is blank without JavaScript). Sign out clears it.

**Head.** /today: `head.today.title` "Today's brief · SaveBrew dashboard", `head.today.meta` "Your five items for the morning, the rate strip, your goal snapshot and your text settings.". /rates: `head.rates.title` "Rate Tracker · SaveBrew dashboard", `head.rates.meta` "Twenty accounts and CDs, checked each morning, with a 30 day history and the alerts you set.". /goals: `head.goals.title` "Goals · SaveBrew dashboard", `head.goals.meta` "Up to six savings goals with a target, a date, a monthly deposit and the milestones along the way.". /archive: `head.archive.title` "The archive · SaveBrew dashboard", `head.archive.meta` "Each brief since launch, searchable by topic and by date.". All four noindex.

**The app frame (Offering Spec 10.1 to 10.3, on each dashboard route).** Light theme, white, Manrope with tabular numerals, Big Shoulders 600 for view headings, small caps tag style for section labels rendered as Manrope 600 13px sentence case per the Design System. The 56px app bar (48px on phone) is the top edge of the frame: the knot mark and the wordmark left at 24px (20px on phone), not centred, not mark only, not in a sidebar; the section tabs inline (Today → `/today`, Rates → `/rates`, Goals → `/goals`, Archive → `/archive`) with the thread strip as the tab indicator (the active thread pulled tight); at the right the date pill `dash.appbar.datepill` "Thu, Sep 24", the bell with the label `dash.bell.on.label` "Texts on" (tooltip `dash.bell.on.tip.pattern` "Texts on. Alerts you set on tracked rates and goals, billing notices and sign in codes go to {phone}. Reply STOP to any text to end them. Ending texts does not cancel your membership.", example "Texts on. Alerts you set on tracked rates and goals, billing notices and sign in codes go to (555) 010 0123. Reply STOP to any text to end them. Ending texts does not cancel your membership.") or `dash.bell.off.label` "Texts off" (tooltip `dash.bell.off.tip` "Texts off. Turn them on from the Texts card on Today; you'll be asked to opt in first, and no text is sent until you do."), the circular avatar "JM" which opens a small menu with `dash.appbar.membership` "Membership" (→ the membership panel, `#membership`) and `dash.signout` "Sign out" (→ clears the session, announces `dash.signout.done` "You're signed out.", routes to `/sign-in`). On phone the tabs become a horizontally scrolling row directly under the bar, one column beneath. Each data module carries a freshness stamp. The footer line inside the frame on each view: "Illustrative figures shown. Live rates move without notice. SaveBrew is a digest, not a bank." The disclaimer `disclaimer.text` beneath the frame. No dashes anywhere in UI copy; no real bank names; no live rates; no browser chrome, no device frame.

**Scene and hover.** The Art Direction (3.23) keeps the app fast: no scene beyond the thread strip. The thread strip is therefore the lightweight motion scene of each dashboard route, drawn on one small canvas in the app bar: on /today its five threads carry today's five knots and sag on the 7s idle cycle; on /rates the Rates icon's thread rises through its knot on load; on /goals the Goals thread fills its knot as the featured goal's bar fills; on /archive three stacked weft rows draw in. Tab change pulls the new tab's thread tight (Knot). Text hover: standard link states (the running stitch underline) and the tab threads tightening on hover; mirrored on `:focus-visible`. Entrances inside the app are quick and exact: modules populate top to bottom at 40ms stagger on load (Shuttle), toggles click (Knot), bars fill (Shuttle), rows tick. Reduced motion: everything at its end state.

**Interactive moments** (all client side, persisted in the session for the visit): the Texts toggles, the chips, the balance input, the sort and filter controls, the alert threshold, the goal deposit adjustments, the worksheet, the archive search, the membership panel and the two click cancellation.

#### 7.16 Today (/today)

Two columns under the app bar (main about 62 percent, right rail about 38 percent; one column on phone with the four tiles as a 2 by 2 grid and the rail cards stacked beneath the five items).

Main column, top to bottom (Offering Spec 10.3 Screen 1 with the copy step's date corrections):
- Eyebrow "TODAY'S BRIEF" (the app's own tag style), heading "Good morning, Jordan." on its own line with nothing after it, sub line `dash.today.subline` "Thursday, September 24 · 5 items · 4 minute read", status chip "Published 6:30 AM ET".
- The rate strip, four tiles: "Top tracked APY" 4.00% (no change); "Average of tracked" 3.60% (up 0.05 this week); "Your account" 3.50% (Bank F, illustrative); "Gap to top" 0.50 pts (about $50 a year on $10,000). Beneath: "Rates checked 6:00 AM ET. Illustrative figures." The "Your account" tile is editable: with no rate typed it shows `dash.rates.own.empty` "Type your account's rate to see the gap."; typing one recomputes the gap tile.
- The five items, each with its tag (RATES, CASHBACK, COUPON, SEASONAL, FRAMEWORK: the dashboard keeps the Offering Spec's tags), the headline, the two line summary and the chip, verbatim from the TODAY items of brief_items.md (7.1). The chips work: **Open tracker** → `/rates`; **Remind me** → adds "The rotating 5% category, grocery stores through September 30" to Saved items with the reminder date Wednesday, September 30 and announces it; **Save code** → adds "Stackable 20% code on winter tires, ends Friday, September 25" to Saved items and announces it; **Open playbook** → opens the October playbook as a sheet (the Seasonal item's summary, the "What's worth waiting on right now?" section of the patio guide as the buy now and wait list, and the link to the guide); **Open worksheet** → `/goals#worksheet`.
- The link row: **Yesterday's brief** (`dash.today.yesterday.link`, aria `dash.today.yesterday.aria` "Yesterday's brief, Wednesday, September 23") → `/archive#2026-09-23`; **Browse the archive** → `/archive`.
- On a Saturday or Sunday (computed from the Eastern clock) the main column shows `dash.today.weekend` "No brief on Saturdays and Sundays. This week's Roundup is free to read, and Monday's pass goes out at 6:30 AM Eastern." above the most recent weekday's brief.

Right rail, stacked cards (16px radius, hairline border, no shadows):
- "Goal snapshot": Emergency fund, $6,000 of $10,000, a 60 percent bar with tick marks at 25, 50, 75 and 100, "On track for Mar 2027", link **Add $250 this month** → `/goals`.
- "Texts", the account notification settings. When opted in (the demo default): three rows with switches (CUR-009, role switch): "Rate moves over 0.25 pts on tracked accounts" on, "Goal check ins and milestones" on, "Billing, renewal and sign in codes" on; footer "Sending to (555) 010 0123. Reply STOP to end texts. Ending texts does not cancel your membership."; and a small text link `add.dash.texts.end` "End texts" that sets opted in to false (in production STOP does the same). When not opted in: the bell reads "Texts off" and the card shows the verbatim Join Our SMS List block of 6.3 (`dash.texts.optin`), both boxes unchecked, one program; a valid submission with both boxes ticked sets opted in to true, restores the three switches (all on) and shows the block's success line. No text is sent by the preview build.
- "This week so far": "Rate changes tracked: 3", "Codes saved: 2", "Gap to top rate on your balance: about $50 a year".
- "Saved items": `dash.saved.empty` "No saved items yet. The Save code and Remind me chips on today's brief put codes, activations and deadlines here with their expiry dates." until a chip saves something, then the list with each item's expiry or reminder date.

#### 7.17 Rate Tracker (/rates)

- Header: "Rate Tracker", sub line "Twenty accounts and CDs, checked each morning", freshness pill `dash.rates.updated` "Updated Sep 24, 6:00 AM ET", primary button **Set an alert** → focuses the detail panel's alert input.
- Controls: filter chips (All, Savings, CDs, Money market) that filter the table; a "Balance" input prefilled "$10,000" that recomputes the earnings column (balance times APY, rounded, labelled "about"); a sort control "APY, high to low" (also low to high, and by 7 day change).
- Summary strip: "Top tracked" 4.00%, "Average tracked" 3.60%, "Moved up this week" 3, "Moved down this week" 1.
- The table (about 70 percent width) on one white surface with hairline dividers, no per row cards, no per row buttons, no bank logos (two letter monogram tiles). Columns: Institution, Product, APY, 7 day change, Minimum, At this APY $10,000 would earn about, Alert. The seven rows verbatim from Offering Spec 10.3 Screen 2 (Bank A to Bank G, Bank F tagged "Your account"), APY at about 20px and no larger, up moves green with an up arrow, down moves red with a down arrow, no change grey. The link "13 more" expands the table to twenty rows: Bank H (illustrative), High yield savings, 3.65%, +0.05 (from the brief items), then Bank I to Bank T (illustrative) stepping down in round values from 3.60% to 0.50%, so the sub line's twenty is true; a "Show 7" link collapses it. Selecting a row (click, Enter or Space) opens it in the detail panel.
- Right detail panel (about 30 percent) for the selected row, Bank A by default: "Bank A, High yield savings", "4.00% APY", a 30 day line stepping from 3.95 to 4.00 mid month with ticks at 3.75, 4.00, 4.25 (an SVG line that draws on select, Shuttle), a History list ("Sep 12: 3.95 to 4.00", "Aug 3: 3.90 to 3.95"), and the input "Alert me if this drops below" showing "3.90%"; changing it flips that row's Alert switch on and announces it; with no alert set on the selected row the panel shows `dash.rates.alerts.empty` "No alerts set yet. Open any tracked account and type the rate you want to hear about.". On phone the panel opens as a sheet.
- Under the table: "APY figures are illustrative, not live rates. SaveBrew tracks published rates and does not hold deposits."
- Phone: the summary strip as 2 by 2, the table as stacked rows (institution and product on line one, APY and change on line two).

#### 7.18 Goals (/goals)

- Header: "Goals", sub line "Three goals, $8,500 of $16,700" (recomputed as goals change), primary button **Add a goal** → an inline form (name, target, target month, monthly deposit; GOV.UK errors on empty fields) that adds a card, up to six; with no goals the view shows `dash.goals.empty` "No goals yet. Add one with a target, a date and a monthly deposit. SaveBrew records what you type; it holds no money.".
- Featured goal card: "Emergency fund", $6,000 with "of $10,000" beside it, a wide 60 percent bar with four small tick marks at 25, 50, 75 and 100, stat cells "Target: Mar 2027", "Monthly deposit: $250", "Status: On track" (green chip), a six bar deposit chart labelled Apr to Sep at $250 each with the caption "6 month streak", and the footnote "At 4.00% APY, $6,000 would earn about $20 a month. Illustrative."
- Two smaller cards side by side: "Holiday spending", $1,000 of $1,500, 67 percent, "Target: Dec 2026", "Monthly deposit: $250", "On track"; "New laptop", $1,500 of $5,200, 29 percent, "Target: Jun 2027", "Monthly deposit: $400", "Slightly behind" (amber chip) with the link **Adjust the deposit** → an inline field that changes the monthly deposit and recomputes the status (on track when deposits to the target month reach the target).
- Right rail: "From today's brief": "Moving to the top tracked rate: about $50 a year on your balance" and "This month's 5% grocery category: about $30 on $600 of groceries", each with the link **Apply to a goal** → a small chooser that notes the amount against the chosen goal. "Check ins by text": "Weekly goal check in" toggle off, "Milestone alerts at 25, 50, 75 and 100 percent" toggle on, "Next check in: Monday 8:00 AM".
- The worksheet (`#worksheet`, opened by the Today chip): "The 50/30/20 tune up": one input, net pay per paycheck, and three computed cells (needs 50 percent, wants 30 percent, the 20 percent), plus the three questions from the brief item's framing as prompts; figures labelled "about".
- Footer: "Illustrative figures shown. Goals are planning tools; SaveBrew does not hold or move money."
- Treatment: flat bars with a rounded end, text chips for status, no photo thumbnails, no ring charts, no hexagon badges, no piggy bank. Phone: featured card, then the two cards stacked, then the rail cards.

#### 7.19 The archive (/archive)

- Header: "Archive" as the tab, view heading "The archive", sub line `head.archive.meta` "Each brief since launch, searchable by topic and by date." (the same sentence as the meta description), freshness stamp "Updated Sep 24, 6:30 AM ET".
- Controls, one row: a search field labelled `add.dash.archive.search.label` "Search by topic" with the placeholder `notfound.search.placeholder` "rates, cashback, coupon, seasonal, paycheck", and a date select labelled `add.dash.archive.date.label` "Pick a date" listing the nine weekday briefs available on the preview build.
- The list: nine dated entries, newest first, each a row with the date in words, the five headlines of that morning (one per thread with its knot) and the morning's item count: Thursday, September 24 (TODAY), Wednesday, September 23 (YESTERDAY'S PASS), Tuesday, September 22 and Monday, September 21 (THIS WEEK SO FAR), and Friday, September 18 back to Monday, September 14 (LAST WEEK'S PASS), all from brief_items.md (7.1). Selecting an entry (or opening `/archive#2026-09-23`) shows that morning's whole pass in the Today layout, headlines and summaries, with the chips shown as members' actions. Searching filters the entries to briefs whose headlines or summaries mention the query; no match shows `dash.archive.empty.search` "No brief mentions {query}. Try a thread word (rates, cashback, coupon, seasonal, paycheck) or pick a date.".
- Footer line inside the frame; the disclaimer beneath.
- Phone: one column; the date select above the search.

#### The membership panel and the two click cancellation (on each dashboard route, `#membership`)

Click one: **Membership** in the avatar menu opens the panel as a sheet from the right (weft pass, Shuttle): heading `dash.membership.heading` "Your membership"; `dash.membership.summary.pattern` "{membership}, billed {cadence}. Renews on {date in words} for {amount}." (example "SaveBrew Daily, billed monthly. Renews on October 24, 2026 for $7.99."); **Switch to yearly** (`dash.membership.switch.yearly`) or **Switch to monthly** (`dash.membership.switch.monthly`) with the note `dash.membership.switch.note.pattern` "Takes effect on {date in words}: that day you're charged {amount} and the membership renews {cadence} from then on." (example "Takes effect on October 24, 2026: that day you're charged $72 and the membership renews yearly from then on."); **Update the card** (`dash.membership.card.update`) → a small card form (the same payment fields and errors as the checkout); for the Daily, **Move to the Daily for Two** (`dash.membership.two.move`) → confirms the move with the new price from the next renewal; for the Daily for Two, **Resend the invite** (`dash.membership.two.resend`) with `dash.two.invite.pending` "Your second reader hasn't accepted the invite yet. Shared goals show both deposits once they're in; resend the invite from Membership if it's gone astray." while pending. Click two: **Cancel membership** (`dash.membership.cancel`) → immediate, no retention offer, no survey, no "are you sure": the panel shows `dash.membership.cancelled.pattern` "Your membership is cancelled and no further charge will be made. Your dashboard stays open until {date in words}. Resume membership at any point before then and it carries on as before." (example "Your membership is cancelled and no further charge will be made. Your dashboard stays open until October 24, 2026. Resume membership at any point before then and it carries on as before."), the label `dash.membership.ends.label` "Access ends" with the date, and the link **Resume membership** (`dash.membership.resume`) which stays until that date and, when used, shows `dash.membership.resumed.pattern` "Your membership is back on. It renews on {date in words} for {amount}, as before." (example "Your membership is back on. It renews on October 24, 2026 for $7.99, as before."). Cancellation is also honoured by email to support@savebrew.com; STOP ends texts only. QA counts the clicks: two.

### 7.20 Sign in (/sign-in)

**Purpose.** The member's door: email plus an emailed sign in link by default, a password as the option. On the preview build any valid email opens the illustrative member's dashboard, and the page says so.

**Head.** Title `head.signin.title` "Sign in · SaveBrew". Meta `head.signin.meta` "Sign in to your SaveBrew dashboard with the email you used at checkout, by emailed link or by password.". Noindex.

**Scene.** The selvedge stitch draws around the sign in card as a border when the email field validates (Shuttle, base), tying off at the button (Knot); static under reduced motion. **Text hover.** Standard (the running stitch underline).

**Sections.**

1. Heading pass `signin.heading` "Sign in" (the H1), the sign in card in columns one to two with the thread strip in columns three to five (so the row fills).
2. The form, one column: `signin.email.label` "Email address", email, autocomplete `email`, hint `signin.email.hint` "The one you used at checkout."; the Bobbin **Email me a sign in link** (`signin.submit.link`) → validates (`signin.error.email.empty` "Enter your email address"; `signin.error.email.format` "Enter an email address in the correct format, like name@example.com"), shows `signin.sent.pattern` "Your sign in link is on its way to {email}. It works once and expires in 15 minutes. If it hasn't arrived in a couple of minutes, look in spam, then ask for another." with **Ask for another link** (`signin.sent.again`), and on the preview build sets the demo session and opens `/today` after the sent line has been readable for 1.5 seconds. Beneath: `add.signin.preview` "Preview build: any email address opens the illustrative member's dashboard, signed in as Jordan." The link **Sign in with a password instead** (`signin.password.toggle`) reveals `signin.password.label` "Password" (autocomplete `current-password`) and the button **Sign in** (`signin.password.submit`) with **Use the emailed link instead** (`signin.password.forgot`) to go back; errors `signin.error.password.empty` "Enter your password, or ask for a sign in link instead", `signin.error.password.wrong` "That password doesn't match this email address. Try again, or use the emailed link instead." (not shown on the preview build, where any password of ten or more characters opens the dashboard). Other states: `signin.error.unknown.pattern` "We can't find a membership for {email}. Try the email you used at checkout, or join from Membership." (production only), `signin.error.link.expired` "That sign in link has expired or was already used. Ask for a new one below." (shown when the route is opened with `?link=expired`). Error summary `signin.error.summary` "There is a problem". Enter submits.
3. Footer (6.2).

**Mobile.** One column; the card full width.

### 7.21 Terms of Service (/terms) and 7.22 Privacy Policy (/privacy)

**Purpose.** The complete legal text, live and linked from the footer, the SMS block and the checkout, with the SMS clauses and the [EIN Address] placeholder. `/terms-of-service` and `/privacy-policy` redirect here (301).

**Head.** /terms: `head.terms.title` "Terms of Service · SaveBrew", `head.terms.meta` "The terms for SaveBrew memberships and for the SaveBrew account notifications SMS program, from SaveBrew Inc.". /privacy: `head.privacy.title` "Privacy Policy · SaveBrew", `head.privacy.meta` "What SaveBrew Inc. collects, how it is used, and the promise that mobile information is not shared with third parties for marketing.". Both indexed.

**Scene.** The twill (generative surface two) as the page's margins, drawn once on a canvas at load with its diagonal crossings filling in over 1.2s (Shuttle); no further motion; static under reduced motion. **Text hover.** Underline only.

**Sections.** The heading pass `legal.terms.heading` "Terms of Service" or `legal.privacy.heading` "Privacy Policy", the standfirst `legal.contact.line` "SaveBrew Inc., [EIN Address]. Phone (888) 338 8809. Email support@savebrew.com." (the placement line for the registered address; the footer's King of Prussia address is not used here), then the complete text of section 8 in CSS multicolumn (two columns at 1280, three at 1440, four at 1920 and 2560, `columns: 34ch`) with the twill margin, the document's headings as H2s, the bulleted SMS terms as a list, [INSERT SHORT CODE] and [EIN Address] kept literally, the hyphens of the verbatim text kept as written. Entrance: the columns wipe in one after another (Shuttle, 80ms stagger). Then the footer. Mobile: one column.

### 7.23 The 404 page

**Purpose.** A designed, on brand not found page served with a real 404 status for any unknown path, with a search of the guides and links home, to the Roundup and to Membership.

**Head.** Title `head.notfound.title` "This thread isn't on the loom · SaveBrew". Meta `head.notfound.meta` "That address doesn't exist on savebrew.com. Search the guides, or open home, the Roundup or Membership.". Served by the catch all from `src/site/404/index.html` with status 404, not the home HTML.

**Scene.** A loose thread that curls: a lazy canvas draws one indigo thread across the page that curls out of the weave and settles (Knot, slow), over `photo.404` and the `texture.fabric` field; static under reduced motion. **Text hover.** The thread curls under the hovered link (a wavy underline, Shuttle).

**Sections.**

1. Heading pass `notfound.heading` "This thread isn't on the loom." across the five columns, `notfound.line` "The address you opened doesn't lead anywhere on savebrew.com.", the still in columns four to five. Entrance: the thread curls, the heading arrives tight.
2. The guides search: label `notfound.search.label` "Search the guides", placeholder `notfound.search.placeholder` "rates, cashback, coupon, seasonal, paycheck", button **Search** (`notfound.search.submit`) → a client side search over the four guides' titles, deks and bodies and the Roundup, listing matches as knots with the title and dek → their routes; no match shows `add.notfound.search.empty` "No guide mentions {query}. Try a thread word (rates, cashback, coupon, seasonal, paycheck)." Entrance: the field's stitch draws.
3. Three links on one thread: **Home** (`notfound.link.home`) → `/`; **This week's Roundup** (`notfound.link.roundup`) → `/roundup`; **Membership** (`notfound.link.membership`) → `/membership`. Entrance: the three knots tie.
4. Footer (6.2).

**Mobile.** One column; the still at 1:1 under the heading.

## 8. Full Legal Page Content

The complete text of the two generated documents (/home/claude/savebrew/legal/SaveBrew_TOS.docx and SaveBrew_Privacy_Policy.docx), extracted with python-docx and pasted inline unchanged, including the SMS section with [INSERT SHORT CODE] twice, the verbatim no sharing clauses, and the [EIN Address] placeholder in each Company Information block. The hyphens and the phone format inside this section are the documents' own and stay as written. /terms renders 8.1; /privacy renders 8.2.

### 8.1 Terms of Service (/terms)

[[VERBATIM BEGIN: SaveBrew_TOS.docx]]

### Terms of Service
SaveBrew Inc.

Welcome to SaveBrew. These Terms of Service ("Terms") govern your access to and use of the savebrew.com website and the resources and services made available through it (collectively, the "Services"), operated by SaveBrew Inc. ("SaveBrew," "we," "us," or "our"). By accessing or using the Services, you acknowledge that you have read, understood, and agree to be bound by these Terms. If you do not agree, please discontinue use of the Services.

#### 1. Company Information
Company: SaveBrew Inc.

Mailing Address: [EIN Address]

Phone: (888) 338-8809

Email: support@savebrew.com

#### 2. Nature of Services
SaveBrew Inc. publishes SaveBrew, a paid savings digest for consumers in the United States. Members pay a monthly or yearly subscription for access to a members only dashboard on savebrew.com that carries a short written brief each weekday morning on published savings account rates, cashback and coupon opportunities, seasonal spending patterns, budgeting frameworks and money management techniques, together with a rate tracker that records published rates for accounts the member chooses to watch, a savings goal dashboard in which the member records their own targets and deposits, a list of items the member saves from the brief, and an archive of past briefs. A two reader version of the subscription provides the same service to two people on one bill. A free weekly roundup and a library of guides are published on the public website and can be read without an account.

SaveBrew is an educational publication. It does not provide financial, investment, tax or legal advice, does not manage, hold, transfer or invest money, does not originate, broker or arrange loans, does not sell financial products, and is not a bank, a broker or a registered investment adviser. Rates and offers described in the service are gathered from public sources on the dates shown and may change without notice.

Members may opt in separately to receive text messages about their own subscription, account security and the rates and goals they track. Subscriptions are purchased and paid for online through this website, renew automatically at the stated price until cancelled, and cancellation is available at any time from the member dashboard in two steps, with access continuing to the end of the period already paid for. The Services include the website, the member dashboard, the digest and guide content, customer support, and the optional SMS program.

#### 3. Informational Content Disclaimer
All content available through the Services, including rate movements, cashback and coupon opportunities, budgeting frameworks and money management techniques, is provided for general informational and educational purposes only. It does not constitute financial, investment, tax or legal advice, is not a recommendation to open, close or move any account, and is not tailored to your individual circumstances. Consult a qualified professional before making financial decisions.

Interest rates, annual percentage yields, offers, promotions and terms are set by third party financial institutions and merchants, change frequently and without notice, and may differ by location, balance or eligibility. We do not warrant that any rate, offer or figure we report is current, complete or error free, and we are not affiliated with, endorsed by, or responsible for any institution or merchant we cover. SaveBrew Inc. does not hold, manage, lend or invest funds and does not sell financial products. Always verify current terms directly with the provider before acting. Use of the Services is at your own risk.

#### 4. Eligibility and Acceptable Use
You must be at least 18 years of age, or the age of majority in your jurisdiction, to use the Services. By using the Services, you represent that you meet this requirement and that any information you provide is accurate and current.

You agree to use the Services only for lawful purposes and in a manner that does not infringe the rights of, or restrict or inhibit the use of, the Services by any third party. You agree not to attempt to gain unauthorized access to any portion of the Services, disrupt their operation, or use them to transmit harmful or unlawful content.

#### 5. Intellectual Property
All content on the Services, including text, graphics, logos, icons, images, and the compilation thereof, is the property of SaveBrew Inc. or its content suppliers and is protected by applicable intellectual property laws. The SaveBrew name and logo are marks of the Company. You may not reproduce, distribute, modify, or create derivative works from any content without our prior written permission.

#### 6. Third-Party Content and Links
The Services may reference, summarize, or link to third-party content, products, and websites for convenience and informational purposes. Such references do not constitute endorsement, and we are not responsible for the accuracy, availability, or content of third-party materials. Your interactions with any third party are solely between you and that party.

#### 7. SMS Messaging: Promotional Marketing Only
SaveBrew Inc. operates an SMS messaging program strictly for promotional marketing purposes. By enrolling in this program, you acknowledge and agree to the following terms:

- Program Description: By opting in, you consent to receive recurring automated promotional marketing text messages from SaveBrew at the mobile number you provide. Consent to receive marketing text messages is not a condition of any purchase.
- Message Frequency: Message frequency varies.
- Message and Data Rates: Message and data rates may apply.
- Opting Out and Help: You may opt out of the SMS program at any time by texting the keyword STOP to [INSERT SHORT CODE]. After you send STOP, we will send a one-time message confirming that you have been unsubscribed, and no further messages will be sent. For assistance, text the keyword HELP to [INSERT SHORT CODE], or contact us at support@savebrew.com or (888) 338-8809.
- Supported Carriers: Supported carriers include AT&T, T-Mobile, Metro PCS, Verizon Wireless, US Cellular, Google Voice, Cellular One, Cellcom, Cellular South, Interop, and Clearsky. Carriers are not liable for delayed or undelivered messages.
- Privacy: No mobile information will be shared with third parties or affiliates for marketing or promotional purposes. Information sharing with subcontractors in support services, such as customer service, is permitted. All other use case categories exclude text messaging originator opt-in data and consent; this information will not be shared with any third parties.
#### 8. Disclaimer of Warranties
The Services are provided on an "as is" and "as available" basis without warranties of any kind, whether express or implied, including but not limited to implied warranties of merchantability, fitness for a particular purpose, and non-infringement. We do not warrant that the Services will be uninterrupted, error-free, or free of harmful components, or that any information provided is complete, accurate, or current.

#### 9. Limitation of Liability
To the fullest extent permitted by law, SaveBrew Inc. and its officers, directors, employees, and agents shall not be liable for any indirect, incidental, special, consequential, or punitive damages, or any loss arising from your access to, use of, or inability to use the Services, or reliance on any information provided through them, even if advised of the possibility of such damages.

#### 10. Indemnification
You agree to indemnify and hold harmless SaveBrew Inc. and its affiliates from and against any claims, liabilities, damages, losses, and expenses, including reasonable legal fees, arising out of or in any way connected with your use of the Services or your violation of these Terms.

#### 11. Governing Law
These Terms are governed by and construed in accordance with the laws of the State of Delaware, without regard to its conflict of law provisions. Any disputes arising under these Terms shall be subject to the exclusive jurisdiction of the courts located in Delaware.

#### 12. Changes to These Terms
We may update these Terms from time to time to reflect changes in our Services or applicable law. The current version will always be posted on this page, and your continued use of the Services after any update constitutes acceptance of the revised Terms.

#### 13. Contact Information
If you have questions about these Terms, please contact us:

Company: SaveBrew Inc.

Phone: (888) 338-8809

Email: support@savebrew.com

Address: [EIN Address]


[[VERBATIM END: SaveBrew_TOS.docx]]

### 8.2 Privacy Policy (/privacy)

[[VERBATIM BEGIN: SaveBrew_Privacy_Policy.docx]]

### Privacy Policy
SaveBrew Inc.

SaveBrew Inc. ("SaveBrew," "we," "us," or "our") respects your privacy and is committed to protecting the personal information you share with us. This Privacy Policy explains what information we collect through savebrew.com (the "Services"), how we use and protect it, and the choices available to you.

#### Company Information
Company: SaveBrew Inc.

Address: [EIN Address]

Phone: (888) 338-8809

Email: support@savebrew.com

#### 1. Information We Collect
We collect information you provide directly to us, such as your name, email address, and mobile phone number when you contact us, submit a form, or opt in to our SMS program. We also automatically collect limited technical information, such as device type, browser, and usage data, when you interact with the Services.

#### 2. How We Use Your Information
We use the information we collect to operate and improve the Services, respond to your inquiries, deliver the updates and SMS messages you request, maintain the security and integrity of the Services, and comply with legal obligations.

#### 3. How We Share Your Information
We do not sell your personal information. We may share information with trusted service providers who perform functions on our behalf (such as hosting, analytics, and customer support), and only to the extent necessary for them to provide those services. We may also disclose information when required by law or to protect our rights and the safety of others.

#### 4. SMS Messaging and Mobile Data
When you opt in to our SMS program, we collect your mobile phone number and your consent records in order to deliver the text messages you have requested. The categories of information collected through the SMS program are used solely to operate the program and send the messages you signed up to receive.

No mobile information will be shared with third parties or affiliates for marketing or promotional purposes. Information sharing with subcontractors in support services, such as customer service, is permitted. All other use case categories exclude text messaging originator opt-in data and consent; this information will not be shared with any third parties.

You may cancel SMS messages at any time by replying STOP, and you may request help by replying HELP. Message frequency varies, and message and data rates may apply.

#### 5. Cookies and Tracking Technologies
The Services may use cookies and similar technologies to remember your preferences, understand how the Services are used, and improve your experience. You can control cookies through your browser settings, although disabling them may affect certain features.

#### 6. Data Security
We implement reasonable administrative, technical, and physical safeguards designed to protect your information. However, no method of transmission or storage is completely secure, and we cannot guarantee absolute security.

#### 7. Data Retention
We retain personal information only for as long as necessary to fulfill the purposes described in this Policy, to comply with our legal obligations, resolve disputes, and enforce our agreements.

#### 8. Your Privacy Rights and Choices
Depending on your jurisdiction, you may have the right to access, correct, or delete your personal information, or to object to or restrict certain processing. To exercise these rights, contact us using the details below. You may also opt out of SMS messages at any time by replying STOP.

#### 9. Children's Privacy
The Services are intended for individuals who are at least 18 years of age. We do not knowingly collect personal information from children. If you believe a child has provided us with personal information, please contact us so we can take appropriate action.

#### 10. Third-Party Links
The Services may contain links to third-party websites. We are not responsible for the privacy practices or content of those sites, and we encourage you to review their privacy policies.

#### 11. Changes to This Privacy Policy
We may update this Privacy Policy from time to time. The most current version will always be available on this page, and your continued use of the Services indicates your acceptance of any changes.

#### 12. Contact Us
If you have questions or requests regarding this Privacy Policy or your personal information, please contact us:

Company: SaveBrew Inc.

Phone: (888) 338-8809

Email: support@savebrew.com

Address: [EIN Address]


[[VERBATIM END: SaveBrew_Privacy_Policy.docx]]

## 9. SMS Program and Sample Messages

Program name: SaveBrew. Use case: account notifications for paying members who opt in, about their own membership, their own security, and the rates and goals they themselves chose to track. Never promotional. The opt in is the verbatim block of 6.3 (unchecked, one program), shown on Home, on the order confirmation and inside the dashboard's Texts card; the checkout phone field is not consent; Daily for Two readers opt in separately from their own dashboards. The message flow copy follows compliance.md with SaveBrew's details; "subscribed" and "unsubscribed" are the compliance template's words and stay.

### 9.1 The program, from the Offering Spec (section 11, verbatim)

## 11. SMS TIE IN

Use case in one line: account notifications for paying members who opt in, about their own membership, their own security, and the rates and goals they themselves chose to track. Never promotional.

Program description, plain language, for the SMS terms and the verbatim opt in block: "SaveBrew account notifications: texts about your SaveBrew membership, such as billing and renewal notices, payment problems, sign in codes, confirmations when you change your settings, the alerts you set on the savings rates and goals you track, and replies from our support team. Msg frequency varies. Msg and data rates may apply. Reply STOP to cancel, HELP for help."

Offering description for the SMS tie in (the product description element): "SaveBrew is a paid daily savings digest. Members pay a monthly or yearly subscription for a dashboard on savebrew.com that carries a short brief each weekday morning on published savings rates, cashback and coupon opportunities, seasonal spending and budgeting techniques, plus a rate tracker, savings goal tools and an archive. Texts from SaveBrew are account notifications about the member's own subscription, security and tracked items."

What SMS may carry: billing and renewal notices; payment failures; sign in codes; confirmations of preference changes; alerts on the member's own tracked rates (threshold crossings and moves on accounts they watch); goal check ins and milestone alerts the member turned on; replies from support to a support request; the standard opt in confirmation, HELP and STOP replies.

What SMS may not carry: the brief itself or any teaser of it; coupon codes, cashback categories, merchant or card names; seasonal tips; saved item deadline reminders (these go to the dashboard and email; the product UI brief's "Cashback deadlines" text toggle is removed for this reason); win back offers after cancellation; upgrade or yearly discount nudges; referral asks; surveys; links to any third party offer; anything to a number that has not opted in through the verbatim block.

Sample messages (all under 160 characters, brand named, STOP on each):
1. "SaveBrew: Bank A (your tracked savings account) moved from 3.95% to 4.00% APY this morning. Details in your Rate Tracker. Reply STOP to opt out."
2. "SaveBrew: your yearly membership renews on Oct 24 for $72. Change or cancel it in two clicks from your dashboard. Reply STOP to opt out."
3. "SaveBrew: your sign in code is 482913. It expires in 10 minutes. If you did not ask for it, ignore this text. Reply STOP to opt out."
4. "SaveBrew: your Emergency fund goal just passed 75 percent. Next check in is Monday at 8 AM. Reply STOP to opt out."

Standard flow copy from compliance.md, with the brand filled in:
- Opt in confirmation: "You're subscribed to SaveBrew account alerts. Msg frequency varies. Msg&data rates may apply. Reply HELP for help, STOP to cancel."
- HELP: "SaveBrew alerts: for help, call (888) 338-8809 or email support@savebrew.com. Msg&data rates may apply. Reply STOP to cancel."
- STOP: "You've been unsubscribed from SaveBrew and will receive no further messages. Reply [keyword] to rejoin."

Mechanics: the opt in is the verbatim finalshot block, unchecked, one program, shown on the site's SMS section, on the order confirmation page and inside the dashboard's Texts card; the checkout phone field is not consent. Daily for Two: each reader opts in separately from their own dashboard. The Privacy Policy keeps the existing doc's line that the number is collected "for the sole purpose of delivering account related text messages".


### 9.2 Flow copy (copy.md)

- Opt in confirmation, `sms.optin.confirm`: You're subscribed to SaveBrew account alerts. Msg frequency varies. Msg&data rates may apply. Reply HELP for help, STOP to cancel.
- HELP reply, `sms.help`: SaveBrew alerts: for help, call (888) 338 8809 or email support@savebrew.com. Msg&data rates may apply. Reply STOP to cancel.
- STOP reply, `sms.stop`: You've been unsubscribed from SaveBrew and will receive no further messages. Reply START to rejoin. (START is the proposed rejoin keyword, confirmed with the aggregator at short code setup.)

### 9.3 The three sample account notifications (copy.md, all under 160 characters, brand named, STOP on each)

1. A tracked rate move, `sms.notification.rate`: SaveBrew: Bank A, a savings account you track, moved from 3.95% to 4.00% APY this morning. Details in your Rate Tracker. Reply STOP to opt out.
2. A goal milestone, `sms.notification.goal`: SaveBrew: your Emergency fund goal passed 75 percent, $7,500 of $10,000. Next check in is Monday at 8 AM. Reply STOP to opt out.
3. A yearly renewal notice, `sms.notification.renewal`: SaveBrew: your yearly membership renews on Oct 24 for $72. Change or cancel it in two clicks from your dashboard. Reply STOP to opt out.

A fourth message type the program may carry, the sign in code, is the Offering Spec's sample 3 in 9.1 above ("SaveBrew: your sign in code is 482913. It expires in 10 minutes. If you did not ask for it, ignore this text. Reply STOP to opt out.").

### 9.4 Where the program shows on the site

- The opt in block: Home row 9 (`/#sms`), /confirmation step 3, the dashboard Texts card when texts are off.
- The Texts card on /today: the three switches (rate moves over 0.25 points on tracked accounts; goal check ins and milestones; billing, renewal and sign in codes), the sending line with the number, "Reply STOP to end texts. Ending texts does not cancel your membership."
- The bell in the app bar: "Texts on" or "Texts off" with its tooltip.
- The inclusion "Account texts, if you opt in." on both membership cards, and the FAQ answer `home.faq.a6`.
- The Terms of Service section 7 and the Privacy Policy section 4 (section 8), with [INSERT SHORT CODE].
- Not carried by text, by design: the brief itself or any teaser of it, codes, categories, merchant or card names, seasonal tips, saved item deadline reminders (dashboard and email only), win back offers, upgrade nudges, referral asks, surveys, third party links.

## 10. Pre Launch Compliance QA Checklist

The direct-qa-loop runs this list as a chain of verification: for each item, open the built or live output, observe, state pass or fail with what was seen, fix each fail, and loop until each item passes (design_robustness.md rule 7, with the iteration cap). A missing measurement is a fail, not a skip. The list extends the design doc spec's checklist with the two run rules, the measured budgets, the per route total motion checklist, the asset gates, the WebAIM six, the conventions floor, guest checkout, deceptive design and the product UI trade dress check.

### A. Purchase path and CTAs

- [ ] A visitor can buy on the site right now at a visible price: /membership → cart drawer → /checkout → /confirmation → /today works end to end, on desktop and on a 375px viewport with one thumb.
- [ ] Each primary CTA is an explicit purchase action with the exact labels of Offering Spec section 8: "Add the Daily to my cart" (hero, nav, ranker, Daily card monthly, compact strips, About), "Add a year of the Daily to my cart", "Add the Daily for Two to my cart", "Add a year of the Daily for Two to my cart", "Go to checkout", "Pay $X now" with the live amount, "Open my dashboard". No "Get in Touch", "Learn More", "Get Started", "Sign Up", "Purchase", "Buy", "Subscribe", "See how it works" as a primary action anywhere.
- [ ] The price is in the hero standfirst and the card price line, not inside or directly under a marketing button. Both prices are printed on each card whichever cadence is selected; the renewal sentence sits at the same weight as the price; the tax line and the refund line are present; the inclusion lists are complete (eight and eleven) with descriptions and no "and more".
- [ ] No free signup form, no email capture, no trial, no add on, no upsell, no MOST POPULAR badge, no $0 card, no seat stepper, no TOTAL line, no rolling numerals.
- [ ] The cart holds one membership at a time, replacing announces the swap, the cadence switch works in the cart, the cart persists across two navigations, and the empty, remove last item and checkout with an empty cart states render as specified.
- [ ] Each cost is knowable before the checkout: price, renewal price and cadence, tax treatment, no fees; no number appears for the first time inside /checkout.
- [ ] One primary action per screen: the Bobbin is the single dominant control on each view; secondary links sit at clearly lower weight.

### B. Identity, NAP and the address roles

- [ ] The entity SaveBrew Inc. appears in the footer, on Contact, in the FAQ and on both legal pages, and nowhere is another entity or spelling used ("Save Brew", "SaveOnBrew").
- [ ] The footer and /contact carry 660 American Ave, King Of Prussia, PA 19406, (888) 338 8809 and support@savebrew.com; the phone is (888) 338-8809 only inside the verbatim SMS block and the legal text; the tel href is +18883388809 everywhere.
- [ ] [EIN Address] appears on /terms and /privacy only, in each Company Information and Contact block, and nowhere else; the footer address is not blank and not the EIN address. Reminder: the owner supplies the EIN address before vetting.
- [ ] No founding year is stated anywhere; no heritage claim; no "As Seen In"; no social icons; no testimonials; no ratings; nothing from the parking page or saveonbrew.com.

### C. Legal and SMS

- [ ] /terms and /privacy render the complete section 8 text, word for word, with [INSERT SHORT CODE] twice in the Terms, the carrier list, the Privacy no sharing clause ("No mobile information will be shared with third parties or affiliates for marketing or promotional purposes.") and the opt in data clause, and [EIN Address]; both are linked in the footer, from the SMS block's two labels and from the checkout's age and terms box; /terms-of-service and /privacy-policy redirect to them.
- [ ] The verbatim "Join Our SMS List" block is present on Home, on /confirmation and in the dashboard's Texts card; only the brand, the phone, the support email and the two links are substituted; both checkboxes are unchecked by default and toggle; the second consent text ends "Read our Terms and Privacy Policy"; the phone field validates; Submit shows the success state; the error states use the GOV.UK strings of 6.3.
- [ ] No SMS consent box on the checkout; the checkout phone field carries its helper text and is not consent; one opt in maps to one program.
- [ ] The flow copy (opt in confirmation, HELP, STOP) and the three sample messages of section 9 are present in the design record and, where shown in the product, match word for word; each sample is under 160 characters with the brand name and STOP.
- [ ] The disclaimer of section 3 runs on /brief (visible without scrolling at 1440 by 900 and 375 by 812), /roundup, each guide (above the fold), /your-moves, /rates, /goals, /archive and /today, and in the footer.

### D. Content, copy and writing

- [ ] The About copy, the four guides, the Roundup, the brief items and the ranker candidates render verbatim from section 7 (read each on the served site against this document); no summary, no rewrite, no shortening. The About is 518 body words; the guides are 982, 817, 1046 and 1083.
- [ ] Each string on the site is a copy.md string, a verbatim file, or an `add.` string from this document; microcopy the builder had to invent matches the craftsman voice and the vocabulary of section 7's preamble.
- [ ] No em dash, en dash, spaced hyphen or double hyphen anywhere in shipped text, including inside the product UI, except the verbatim legal text and the verbatim SMS block; no hyphen inside compound words in shipped copy (high yield, two click, check in, sign in, opt in, 30 day).
- [ ] No refused word in shipped customer facing text (plan, never, every, sample, calendar, month, log, row, figure, page, guaranteed, hack, "you should", "we saved you", subscribe, free member, and the exclusion brief's list), except the documented exceptions ("Daily", "12 month CD", "this month" in the fixed Seasonal item, "subscribed" and "unsubscribed" in the compliance flow copy, "Submit" in the verbatim block); no AI tell word from the content engine's kill list; no curly quotes.
- [ ] Each guide link opens a real, fully written page at its own route; no card links to a page that does not exist; the Coupons and Paycheck columns of /guides carry the honest lines, not "coming soon".
- [ ] Each figure that is not illustrative is dated and attributed (the FOMC move of September 16, 2026; the FDIC 0.37 percent for September 2026; the 3.80 to 4.21 percent band as of September 23 and 24, 2026); each illustrative figure is marked; no real bank, card issuer or retailer is named in the product or the Roundup table; no APY or savings guarantee; no income claim; no "we saved you".
- [ ] Head hygiene: each of the twenty three routes has its unique title and meta description from section 7; the favicon set and the OG image load; the dashboard, sign in, cart, checkout and confirmation routes are noindex; the public routes are indexable; the two RSS feeds resolve.

### E. THE ANTI SAMENESS RULE (section 3.2)

Run with the four live sister sites open beside the build and the three direction records to hand.

- [ ] DNA item 1, the nav treatment: the heading band as specified, no marker glyph, no condensing, no uppercase mono, no dateline, no perforation, no rule, no rail. Pass or fail.
- [ ] DNA item 2, the pinned hero: no `pin: true`, no sticky hero; the canvas is a fixed layer behind flowing DOM; the loom lays flat into the five column board; scroll length 1.25 to 1.75 viewport heights measured. Pass or fail.
- [ ] DNA item 3, the counting loader with a Flip: the selvedge stitch has no count, no percentage, no Flip into the hero, skip at the bottom centre. Pass or fail.
- [ ] DNA item 4, the section procession: the home order is that of 3.23; no numbered list with big numerals, no candour section, no MOST POPULAR, no giant numeral, no SMS block boxed in a narrow centred column. Pass or fail.
- [ ] DNA item 5, display plus mono: no monospace face loaded or used anywhere (check the font requests); no uppercase letter spaced kickers; figures in Manrope tabular. Pass or fail.
- [ ] DNA item 6, the 65 to 68ch measure with a left H2 per band: five columns edge to edge, 31 to 52ch measured per column, heading passes full width on butter. Pass or fail.
- [ ] DNA item 7, neutral field plus one accent: butter is a saturated second surface at 24 to 32 percent of the viewport area, white weft 62 to 70 percent, indigo solids 4 to 8 percent, measured on a desktop screenshot of each page. Pass or fail.
- [ ] DNA item 8, accent graded subject world photography of hands: no people, no hands, no faces, no desk, no counter, no cup; natural colour under the split tone. Pass or fail.
- [ ] DNA item 9, the hedged declarative register: the H1 is a question; H2s are questions; no two declarative sentence H1, no participle triad, no "[Noun], [past participle].", no number led headline, no hedge sentence, no "never" list. Pass or fail.
- [ ] DNA item 10, a candour device instead of testimonials: none present. Pass or fail.
- [ ] DNA item 11, "Purchase the [plan]" with the price beside it and "See how it works": none present; the labels are those of block A. Pass or fail.
- [ ] DNA item 12, the sisters' motion: none of the eighteen claimed easing curves appears in the CSS or JS (grep them); no fade up reveal; no lift, depress and breathe choreography; no Lenis; Shuttle and Knot only at 0.11s, 0.38s and 1.2s. Pass or fail.
- [ ] Exclusion brief 3.1 (fonts): none of the listed faces is loaded; the pairing Big Shoulders Display plus Manrope is used; no giant display numeral as the first read. Pass or fail.
- [ ] Exclusion brief 3.2 (archetypes and hero compositions): the hero is Warp Columns with the loom, none of the listed archetypes, no "left text, right product cluster", no "For [audience]" subhead, no price sentence under the button. Pass or fail.
- [ ] Exclusion brief 3.3 (fields, accents, colour stories): none of the listed hexes or stories; the build's hexes are those of section 5. Pass or fail.
- [ ] Exclusion brief 3.4 (nav and buttons): the Bobbin is none of the listed button treatments; no price in the button; no lift, depress, breathe; no "Purchase a Plan" label; no "See how it works" pairing. Pass or fail.
- [ ] Exclusion brief 3.5 (loaders): the selvedge stitch matches none of the listed loaders and does not reuse the hero motif as its metaphor. Pass or fail.
- [ ] Exclusion brief 3.6 (section orders and types): no numbered steps, no SMS sample shelf, no "Founded in 2026" card, no pull quote from a paper, no FAQ accordion, no table as a section, no log line footer, no colophon. Pass or fail.
- [ ] Exclusion brief 3.7 (headline formulas, CTA verbs, vocabulary, rhythm): checked against the served copy of each route. Pass or fail.
- [ ] Exclusion brief 3.8 (image styles, camera paths, motion, layout): no listed image style, camera path, motion or easing; no narrow centred column; no alternating kicker plus left H2 bands; no 65 to 68ch copy plus aside grids. Pass or fail.
- [ ] Art Direction part 0.3, the seven differences from Financing Bot and Addabill, each observed on the hero screenshots side by side. Pass or fail.
- [ ] Novelty vs the registry (Gate 5): check_novelty.py re-run against proposed.json and the augmented registry at QA time, all quotas clear; the hero screenshot compared with each archived hero. Pass or fail.

### F. THE FULL WIDTH RULE (section 3.3)

- [ ] Screenshots of /, /brief, /membership, /guides, /your-moves, /about, one guide post, /roundup, /checkout and /terms at 1280, 1440, 1920 and 2560, attached to the QA record.
- [ ] At each width, no row's content box is narrower than the viewport minus twice `--gutter`; no outer third of any row is empty; the loom, the week strip, the cloth bands, the heading passes, the membership row, the SMS row and the footer span the full width.
- [ ] The lint rule: no stylesheet declares `max-width` above 100 percent (or any px cap) on a block that holds a section; no `.container`, no `margin: 0 auto` wrapper, no `max(1720px, 86vw)`, no `min(100% minus 2 gutters, 1800px)`.
- [ ] Long text (About, the guides, the legal pages) is in CSS multicolumn (two columns at 1280, three at 1440, four at 1920, five at 2560) or beside a module; no lone 65ch column at any width.
- [ ] Each running text column measures between 30ch and 55ch at all four widths.
- [ ] No butter block taller than 40 percent of the viewport carries running text; no two adjacent rows are both butter; the butter to white to indigo proportions of Art Direction 0.1 hold.
- [ ] The collapse rules hold at 1024 to 1279 (three plus two, no empty cell), 768 to 1023 (two plus two plus one) and 375 to 767 (one column with the sticky tab strip).

### G. The measured budgets (measure_budgets.md; a number for each, pass or fail)

- [ ] Initial JS under 350KB gzipped excluding the lazily loaded Three.js bundle, summed from the built files before deploy (verify the loader code actually defers Three.js).
- [ ] LCP under 2.5s on Home with the loader active, on the live webflow.io site.
- [ ] CLS under 0.1 on Home and on /membership.
- [ ] INP under 200ms.
- [ ] 55fps or better on average sampled through the signature scroll.
- [ ] Signature scroll length between 1.25 and 1.75 viewport heights, read from the `?qa=arc` console output (the spec targets 1.3).
- [ ] Loader visible under 2s on broadband, hard cap 4s, skip visible from 0s; hero copy, nav and the Bobbin readable at 0.8s with the loader active; the three first viewport answers readable on desktop and at 375px before any animation completes.
- [ ] One WebGL context per page, dpr capped at 1.5 (1.0 on touch), render paused offscreen and on hidden tabs, disposed on navigation; low power fallback engages under 30fps.

### H. Per route total motion checklist (design_robustness.md; run for each of the twenty three routes)

For each of `/`, `/brief`, `/membership`, `/roundup`, `/guides`, the four guide posts, `/your-moves`, `/about`, `/contact`, `/cart`, `/checkout`, `/confirmation`, `/today`, `/rates`, `/goals`, `/archive`, `/sign-in`, `/terms`, `/privacy` and the 404:

- [ ] Its own scroll driven scene from section 7, distinct from each other route's, alive on load, scrubbed or driven by scroll, high contrast, with the reduced motion and mobile fallbacks, one canvas, lazy after first paint, paused offscreen.
- [ ] Its own text hover treatment, mirrored on `:focus-visible`, with a sensible tap behaviour on touch.
- [ ] Each section has its own distinct scroll into view entrance, none repeated on that route, snapping to the end state under reduced motion.
- [ ] Each button, link, heading, card, chip, toggle, icon and field moves: idle, hover or focus, and press, using Shuttle and Knot only; the Bobbin's stitch travels at idle; nothing interactive is static.
- [ ] At least one interactive moment beyond the hero, as named in section 7.
- [ ] The kit is present: the thread strip, the selvedge or weft pass dividers, the knots, the eleven icons, the seal where specified; no improvised one off shapes.
- [ ] Content is substantial; no thin section.
- [ ] The guide posts additionally: bespoke editorial layout, pull thread, own kit graphic, own scene, verbatim copy.
- [ ] All motion 60fps smooth, respecting reduced motion and the reduce motion control, not blocking reading or the purchase flow, not delaying LCP; `?qa=rm` produces the static path.
- [ ] Home additionally: THE PASS occurs at its specified position and reads as the visit's loudest beat; The Tightening runs once on load; the PULL A THREAD mobile hero works with a drag and a tap at 375.

### I. Asset gates

- [ ] Each slot in section 5.2 resolves to a real file at its path under /public/assets (or the kit and product UI imports); no placeholder box, no missing image, no broken poster.
- [ ] No hotlinked media: no external image, video, font file or texture URL survives in the build (fonts are subset and self hosted; the only external scripts are Three.js r128 and GSAP 3 from cdnjs).
- [ ] MEDIA_MANIFEST.json lists each shipped asset with filename, source URL or generator and prompt id, licence, usage location and alt text; each entry resolves; each licence is Unsplash, Pexels, Coverr, Poly Haven CC0 or the run's own generation.
- [ ] The weight budget of 5.2 holds: total under 9,000 KB, the hero loop under 2,600 KB desktop and 1,200 KB mobile, the product pan under 1,500 KB, each still under 180 KB at 1600 wide, each product shot under 260 KB, each kit SVG under 24 KB, the texture under 320 KB; WebP with srcset; below the fold lazy loaded.
- [ ] The hero loop is 12 seconds, four 3 second clips, 720p or better, no watermark, clean at the loop point; the product pan is 6 to 8 seconds and captured from the real dashboard views; each has a poster frame.
- [ ] Site photography: at least one photograph on each route that section 7 gives one, one on each guide, none reusing a video frame, none repeated; no people, no hands, no faces, no logos, no text, no coffee cup, no beer glass; each sourced or generated image under the one grade "morning light on cloth"; product screens ungraded.
- [ ] The brand kit is imported, not redrawn: the logo lockups, the favicon set, the OG banner, the knot, the seal, the dividers, the icons, the four guide graphics, the 404 thread.

### J. Accessibility: the WebAIM six and WCAG 2.2 AA

- [ ] Low contrast text: none; each pair in Art Direction 0.1 holds during and after each animation (automated scan plus spot checks on butter and indigo).
- [ ] Missing alt text: none; decorative canvases and dividers aria hidden; each photograph, product shot and the seal has meaningful alt.
- [ ] Missing form labels: none; each field on the SMS block, the contact form, the checkout, the sign in, the dashboard and the 404 search has a visible label; placeholders are not the only label.
- [ ] Empty links: none; each link has text or an accessible name (the spool cart glyph, the knots in the week strip, the icons).
- [ ] Empty buttons: none; each button has a label (the chips, the toggles, the close controls, the menu).
- [ ] Missing page language: none; `lang="en"` on each route.
- [ ] Keyboard: each interactive element reachable in a sensible order; the 2px indigo focus ring visible everywhere; the cart drawer and the mobile menu trap focus and close on Escape; the toggles are real switches with `aria-checked`; live regions announce cart, ranker, form and motion state changes; nothing essential is conveyed by motion or colour alone (arrows and words carry the up, down and behind states).
- [ ] The purchase flow, the forms and all content are fully usable with motion disabled, and on a mid range phone.

### K. The conventions floor (build_registry.md)

- [ ] Logo top left, linking home, on each route.
- [ ] Primary navigation horizontal at the top on desktop; not hidden behind an unlabelled icon on desktop.
- [ ] Cart top right; the search on the 404 in its own row (no header search).
- [ ] The footer carries the physical address, phone, support email, Privacy and Terms.
- [ ] Inline links visibly distinct from body text (indigo, the running stitch underline); buttons look like buttons (the Bobbin).
- [ ] The purchase sequence is product, cart, checkout, confirmation with no invented step.
- [ ] Forms submit on Enter; the browser back button works from each step; scrolling is native and not hijacked, trapped or reversed.
- [ ] The first viewport carries the value proposition, the audience signal and the primary action, on desktop and at 375px (the Comprehension Block, Art Direction 3.5): shown for five seconds, a stranger names what this is, who it is for and what to do next; the heading stack read alone tells the story; each nav label names its destination (the scent map).

### L. Guest checkout and the checkout spec (checkout_spec.md, Gate 6)

- [ ] A purchase completes end to end with no account created and no register or sign in step between the cart and the confirmation; account creation (the optional password) is offered only on /confirmation after the order.
- [ ] The same purchase completes on a 375px viewport with one thumb.
- [ ] Sections present and validated: Contact (first name, last name, email, phone with its helper), Billing address (country, line 1, line 2 optional, city, state or province, ZIP or postal code), Payment (the four card marks, name on card, card number formatted with Luhn, expiry month and year selects, security code with help), Order summary (membership, today's charge, renewal, tax and fees, total today, the unchecked age and terms box), one submit "Pay $X now". No shipping section (digital).
- [ ] One column; top aligned labels always visible; required and optional both marked on each field; the standard autocomplete tokens on each field (autofill works); values not cleared by a validation failure, card fields included.
- [ ] The GOV.UK error standard triggered deliberately on an empty required field and on an invalid field: the message names the problem and the fix, reuses the label's wording, sits beside the field and in the summary near the submit linked to the field, no generic message, no apology for routine validation, not colour alone, validation on blur with a delay and not while typing.
- [ ] The confirmation shows the order number, what was bought, what was charged, the renewal date and amount, the first pass line, the support contact, the dashboard section, the separate SMS step and "Open my dashboard"; for the Daily for Two the invite field works.
- [ ] The dashboard's two click cancellation works and is counted: Membership, then Cancel membership; the cancelled state shows the access end date and Resume membership; no retention offer, no survey, no modal.

### M. No deceptive design (compliance.md)

- [ ] No fabricated scarcity ("only N left", "N people viewing", low stock), no fabricated urgency (no countdown, no "ends tonight"), no confirmshaming, no hidden cost, no preselected add on, upsell, upgrade or consent (the SMS boxes and the age and terms box are unchecked; the cadence control defaults to the cheaper monthly), no subscription harder to cancel than to start, no trick wording, no invisible decline path, no hidden dismiss.
- [ ] Ratings: none shown (none exist); no badge wall (the four card marks at the payment fields are the only trust marks on the site).

### N. Product UI trade dress and consistency (Product UI Brief Parts C and E, Offering Spec 10.5)

Open the six product shots and both membership cards side by side, and the three live dashboard routes.

- [ ] Logo left aligned in the app bar with inline tabs; no centred logo; no sidebar; no icon only logo.
- [ ] No tilted or hand held phone; no photographed device; no browser chrome, no three dots, no URL strip; no black backdrop; the frame is the app's own 56px bar on the butter field.
- [ ] No blue masthead bar over the brief; the greeting stands on its own line with no quip after it.
- [ ] No donut chart as the first module; no per row shadowed rate cards; no giant blue APY numerals; no promo badge.
- [ ] No cream and orange with serif headlines; no photo thumbnails on goal rows; no avatar chip card; no Sankey; no overlapping floating cards; no phone overlapping the window corner.
- [ ] No red gradient header; no white card overlapping the header edge; no hexagon badges; no ring chart; no piggy bank; no "Payday in N days".
- [ ] No green on green hero; no pill chip row under a centred icon; no lime expert tip callout; no star ratings; no "LEARN MORE" per row.
- [ ] No asterisk masthead, no dark green date blocks, no three tile "MARKETS" strip in green caps.
- [ ] Each shot shows a freshness stamp and the footer "Illustrative figures shown. Live rates move without notice. SaveBrew is a digest, not a bank." (the corrected wording, not "Sample data for illustration").
- [ ] Institution names are placeholders marked illustrative; all APYs are round illustrative values; no real bank names or live rates.
- [ ] No em or en dash in any UI copy; the Texts card has the three rows and the "Ending texts does not cancel your membership." footer; "Monthly deposit" and "Adjust the deposit"; "Published 6:30 AM ET"; the tracker sub line with seven rows and "13 more".
- [ ] The same app bar, logo placement, palette, type, card radius and hairlines across all six shots and both cards; anything that drifts is rebuilt.
- [ ] No shot reads as Morning Brew, Raisin, Monarch, Rocket Money or NerdWallet.

### O. Routes, 404, deploy and the record

- [ ] Each route in section 7 loads at its own path with no redirect loop and no 404: `/`, `/brief`, `/membership`, `/roundup` (and `/roundup/2026-09-19`), `/guides`, the four guide posts, `/your-moves`, `/about`, `/contact`, `/cart`, `/checkout`, `/confirmation`, `/today`, `/rates`, `/goals`, `/archive`, `/sign-in`, `/terms`, `/privacy`; `/terms-of-service` and `/privacy-policy` redirect; `/nope` shows the designed 404 with a 404 status and not the home HTML.
- [ ] Each nav link, footer link and in page CTA goes to the right destination; each button works; the interactive feature runs end to end (toggles, re-rank, copy, print, the CTA to the cart); the demo sign in opens the dashboard; the dashboard chips, toggles, table controls, goal controls, worksheet, archive search and membership panel work.
- [ ] The SMS opt in works in all three places with both boxes unchecked by default.
- [ ] The signature loom and each route's scene render and animate on the live webflow.io site as well as locally.
- [ ] No leftover placeholder, lorem, internal note, demo text other than the honest preview lines specified, cut off or overflowing text, broken dropdown, or copy from another business; the public routes are indexable.
- [ ] The build is an Astro app with `output: 'server'`, the Webflow Cloud adapter, the server rendered `[...slug].astro` catch all, assets under /public/assets; `npm install && npm run build` passed in the sandbox before the push; the repo is `savebrew-site` (or the next free suffix); the app is in Harlem's Workspace; the custom domain is not attached.
- [ ] The Site of the Day verdict line is answered with its reason and the four sub scores.
- [ ] The registry entry is appended with the hero screenshot after deploy, each novelty quota clear, tier 1, engine profile baseline r128, no signature shader, media manifest true.
- [ ] The human gate (Step 7.5) was passed: the first viewport screenshots and the three questions handed over, an unaided purchase attempted, before the deploy.

### P. Owner confirmations outstanding (Offering Spec section 17, verbatim; none blocks the build, each is marked proposed on the site where it shows)

## 17. OPEN QUESTIONS FOR THE OWNER

1. Prices: confirm $7.99 monthly and $72 yearly for one reader, $11.98 monthly and $108 yearly for two readers, or adjust. All four are proposed.
2. Daily for Two: go or no go. If no, the ladder is the Daily at two cadences. If yes, confirm the name (Daily for Two, or Daily Duo).
3. Free content shape: confirm that the Weekly Roundup and the Guides are public with no account and no email form, and that "free members" language is retired.
4. Referral fees: is it true that SaveBrew takes no referral fees or commissions from the banks, cards and retailers it writes about? The "no referral fees" line ships only on a yes.
5. Publication cadence: the brief each weekday by 6:30 AM Eastern, the Roundup each Saturday. Confirm, or state seven mornings a week.
6. Rate data: who checks the published rates each morning, how many institutions are on the launch list (twenty proposed), whether their real names may appear in the product, and whether a data licence is needed.
7. Tax treatment: the spec proposes tax inclusive pricing ("the price shown is the price charged") so no cost first appears inside checkout. Confirm with the payment processor and accountant.
8. Refunds: 14 day full refund on yearly, none on monthly beyond cancellation. Confirm.
9. Sign in model: email plus optional password, with an emailed sign in link as the default. Confirm.
10. Dashboard location: savebrew.com/today, /rates, /goals, /archive, /membership (no app subdomain shown anywhere). Confirm.
11. Text alerts: confirm the allowed list in section 11 and that saved item deadline reminders go by dashboard and email only.
12. Whether an optional morning email copy of the brief should exist at all (the owner's brief says dashboard only). If yes it is a member setting, off by default, and never a marketing list.
13. The EIN address for the legal pages and confirmation that the domain purchase has completed (research brief, open questions 1 and 2).


Also proposed and needing confirmation (copy.md): the support hours (Monday to Friday, 9:00 AM to 5:00 PM Eastern) and the one working day reply; START as the SMS rejoin keyword; the cadence switch taking effect at the next renewal date; the seven day invite expiry; the 15 minute sign in link expiry; the optional order number field on the contact form; and whether "this month" in the fixed Seasonal item becomes "in October". The "How are items chosen?" band on About ships the "no referral fees" variant only on the owner's yes.
