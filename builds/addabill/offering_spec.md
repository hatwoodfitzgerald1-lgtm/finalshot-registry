# Addabill Offering Spec

Finalshot Step 2. All numbers are proposed.

## OFFERING TYPE
Consumer app subscription. Two plans, Free and Household. Household is bought through a complete guest checkout (contact, billing address, full card fields, no shipping), monthly or annual. Free is a subordinate path with no card. Account creation is offered only on the confirmation page.

## EVOLUTION
Net new: parked domain since 2022, no prior site. The name is the product: add a bill, see it on one calendar with every other bill, get a text before it is due, tap through to the biller's own page.

## LINE
Free | $0, no card, no time limit (proposed) | One person, 5 bills, text reminders | Use the Free plan

Household | $5 a month or $40 a year (proposed, $20 less than 12 monthly payments) | Unlimited bills, photo capture, 5 people, yearly summary | Purchase the Household plan (monthly), Buy the annual plan

Why:
* 5 free bills: the handful that cause late fees, so free proves the product; the brief's 8 to 15 billers cross 5 early, so buying is honest.
* $5 a month: a single purpose utility priced like one, under what budgeting apps charge.
* $40 a year: four months at no cost against $60 monthly, a 33 percent saving, about one late fee.

Second paid tier: no. Two plans is the calmer offer and the brief's own line; a multi home tier implies landlords, drifting toward business software and ADAPTABILL, and a third tier would force artificial gating. Five people covers roommate houses.

Companion single purchase: no. The yearly summary is already in Household and needs the household's own bills, so a standalone binder would charge twice or need an account before a guest could buy.

## INCLUSIONS, complete per plan
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

## DESCRIPTIONS
Free. Addabill Free is for one person keeping up to 5 bills straight. Type in each bill, see them all on one calendar, get a text before each is due, and tap once to open that biller's own payment page. No card, no fees on your bills. CTA: Use the Free plan.

Household. The Household plan is for the person who keeps the bills for everyone else. Add as many bills as the house gets, photograph the paper ones, and share the calendar with up to 4 other people so the reminder reaches whoever handles a bill. At year end you get a summary of what went to which biller, month by month. CTAs: Purchase the Household plan. Buy the annual plan.

## DEFAULT PLAN FOR THE HERO
Household, monthly, the lower commitment. The primary button reads "Purchase the Household plan", with "$5 a month or $40 a year. No fees on your bills. Cancel any time." beneath it and a plain link "or use the Free plan, up to 5 bills" as the subordinate path. On the Plans page, monthly and annual are equal purchase buttons, neither preselected.

## RENEWAL AND CANCELLATION, plain words
Household renews at the same price, $5 on the same date each month or $40 each year. A text and an email go out 7 days before an annual renewal, and a receipt follows every charge. Cancel any time under Plan in the app in two taps, or by emailing support@addabill.com. The plan runs to the end of the period paid for, then the household moves to Free and every bill stays. No cancellation fee. Annual plan: full refund within 14 days. Price changes carry 30 days notice.

## natureOfServices
Addabill Inc. provides a consumer household bill organizing application that lets users record household bills and due dates, view them on one calendar, receive reminders before each due date, and open a link to each biller's own payment page; Addabill does not process payments, hold funds, connect to any financial account or charge fees on bills, and its paid Household plan is sold as a monthly or annual subscription cancellable at any time.

## SMS TIE IN
Text reminders are the product's main output. In the app, the Addabill Bill Reminders notifications cover due date reminders, bill added and updated confirmations, login and verification codes, subscription billing and renewal notices and support replies. The website's Join Our SMS List block enrolls visitors in the separate Addabill alerts marketing program described in the Terms (decision 4A, 2026-09-23). At purchase, the required phone field ("for your receipt and your account texts") receives the receipt and renewal notice; the shared calendar texts each member at their own number under their own consent. Consent is a real unchecked checkbox, STOP and HELP work on every message, numbers never sold, rented or shared for marketing.

Samples:
1. Addabill: Water bill, $64.20, due Thu Oct 2. Tap to open your utility's payment page: [link]. Reply HELP for help, STOP to cancel.
2. Addabill: Household plan renews Oct 20, $40 for the year. Change or cancel under Plan in the app. Reply HELP for help, STOP to cancel.

## VISUAL SPEC (the app UI is the one packaging system)
Form factors: the phone app on an iPhone (primary, portrait, screen legible) and the same app in a 16:10 browser window (secondary), both real HTML from the brand tokens, screenshotted.

One shell: a top header bar carrying the Addabill wordmark at left in every shot, the current month centered and one "Add a bill" button at right; a month grid with bill chips on their due dates and a "Due next" list below; a bottom tab bar (Calendar, Bills, Household, Plan) that becomes a left rail on desktop. Bill rows: biller name as typed, amount, due date, paid check, "Open payment page" arrow. No charts, scores, gauges, payment form look or invoice vocabulary (clear of ADAPTABILL).

Changes per plan: data only. Free shows "4 of 5 bills" and one member; Household shows "14 bills", 5 members' initials, the camera sheet and the yearly summary card.

Never changes: header bar, calendar geometry, tab bar, bill row anatomy, tokens, device frame.

Master image: one phone screenshot of the October Calendar view, 11 bill chips, one bill card expanded (Water bill, $64.20, due Thu Oct 2, reminders Sep 25, Sep 29, Oct 1). Every other shot is the same build in another view. Hero: the phone on a kitchen counter in morning light beside two paper bills. Plan cards: one card system, only values differ.

## COMPLIANCE SCREEN
Purchasable at a visible price with explicit purchase CTAs, clear of every prohibited vertical.
* Lead capture, ambiguous CTAs: cleared, a priced plan bought through a full guest checkout, purchase labels only.
* Money movement, lending: cleared, no payments processed, funds held or accounts connected, no borrowing or relief topics.
* Hidden costs, hard to cancel: cleared, price, renewal, refund window and no fees on the Plans page at equal weight; two taps or one email to cancel.
* Fabricated trust, deceptive design: cleared, no testimonials, ratings, counts, press, partners, badges, scarcity, urgency, preselection or confirmshaming.
* SMS: cleared, account notifications only, unchecked consent, phone field explained, STOP and HELP.
* Identity, adjacency: cleared, the brief's legal name, address, phone and email on the Plans page, receipt and Terms; never invoicing.

## FOR THE OWNER TO CONFIRM
1. Free limit: 5 bills.
2. Household: $5 a month, $40 a year ($20 less).
3. Household size: 5 people.
4. Reminders: up to 3 per bill.
5. 14 day annual refund window, 7 day renewal notice, 30 days notice of price changes.
6. Two plans only, no companion product.
7. Hero default: Household monthly.
