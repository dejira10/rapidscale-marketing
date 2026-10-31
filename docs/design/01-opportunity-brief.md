# 1. Opportunity Brief

**Purpose:** the input record the system must complete before it writes any outreach, and keep updated as replies arrive. It answers: who needs whom, why now, what's proven, what we may claim, and what the deal is worth.

**Principle:** "Find the strongest truthful reason to contact this particular company right now." A strong email is mostly a by-product of a strong brief. Frankie: "60% list, 30% offer, 10% copy." Saad: "The money is in the looking." `[Part C §9]`

There are two levels:

- **Market brief:** one per market or lane. Written before a campaign.
- **Prospect card:** one per company contacted. Written before its first email, then updated with every reply.

---

## Part A: Market brief

### A1. The transaction

| Field | What to write | Required | Source / why |
|---|---|---|---|
| `market_name` | e.g. "New Alabama restaurants ↔ commercial kitchen-exhaust cleaners" | Yes | |
| `demand_side` | Who has the need, specifically: business type, size, region | Yes | Saad's "who needs whom" |
| `supply_side` | Who sells the solution, specifically. **Split adjacent services** (hood cleaning ≠ grease-trap pumping) | Yes | User note; `[A16]` |
| `one_sentence` | "[Demand] needs [X]; [supply] sells [X] and struggles to find [demand] at the right moment." | Yes | `saad-market-research` step 2 |
| `selection_lens` | Which lens found it: forced spending, government money, sell-to-the-losers, penalty-based, permanent demand, "what had to happen before this?", personal experience | Yes | `markets.md` §1 |
| `money_already_moving` | What the supply side already spends to get customers (booths, ads, brokers); what demand already buys | Yes | `[A07]` PBJ data; `[A18]` booths |
| `value_of_one_customer` | Contract size × margin, renewal × years, with sources | Yes | `[A05]` $433k lifetime value; `[A02]` |
| `what_is_blocked` | What can't happen until the problem is solved (harvest sale, opening, filled beds) | Yes | `[A12]` |
| `scarce_side` | Which side is scarce. The abundant side usually pays; keep the scarce side close | Yes | `[A12]` |
| `who_pays_and_for_what` | Paying side, and the named service (e.g. "qualified account origination" vs "supplier sourcing") | Yes | `[A04]` |
| `price_hypothesis` | A suggested non-round fee, plus the four-question reasoning (how bad, how badly, how hard, what's blocked). Labeled **suggested** | Yes | `offers-and-pricing.md` §4 |
| `deliverable` | Exactly what's delivered (e.g. one email intro with full context; or 3–6 opportunities over 60–90 days) | Yes | `[A07]` "That's my entire delivery" |
| `guarantee` | Replacement only, scoped to what we control | Yes | `[A01]` |
| `legal_flags` | Regulated referral fees, licensing, cannabis, harm sensitivity, privacy | Yes | README rule 5 |

### A2. The trigger and the data

| Field | What to write | Required |
|---|---|---|
| `trigger_event` | The change that creates the need: new license, permit, filing, lost bid, citation, funding, hiring, backorder, registration | Yes |
| `trigger_to_need` | The signal-to-pain translation: why this event creates spending | Yes |
| `data_source` | URL or system for each side; fields available; how fresh; volume per week | Yes |
| `decision_maker_order` | Titles to contact, in fallback order; the budget holder over HR | Yes |
| `exclusions` | Noise to filter out (wrong subtypes, sizes, regions) | Yes |
| `industry_vocabulary` | 5–10 of their own terms, taken from their websites and replies | Yes |
| `pain_in_their_words` | Quotes from forums, reviews, RFPs or replies, with links | Recommended |

If there's no public data source that timestamps the change, write **"no trigger data found"** and say so. **Never invent a database.**

### A3. Market readiness gate (before any campaign)

All must be **yes**, or the gap is recorded and accepted by the user:

- [ ] Both sides are named, and reachable with verified emails.
- [ ] A trigger exists, with a real data source.
- [ ] Who pays, for what, and a price hypothesis grounded in the value of one customer.
- [ ] The deliverable and guarantee are defined, and limited to what we control.
- [ ] Legal and sensitivity flags reviewed.
- [ ] A test plan: about 100 per side to start (50–65 if the intent is high), with the first 10 per side written by hand.

---

## Part B: Prospect card (one per company)

| Field | What to write | Updated when |
|---|---|---|
| `company`, `contact`, `title`, `side` | Basics; `side` = demand or supply | Before sending |
| `is_budget_holder` | Yes / no / unknown | As learned |
| `evidence_state` | E0–E5 for **this** prospect | Every reply |
| `trigger_fact` | The specific dated fact, with source link (e.g. "license issued 2026-09-04, [state site]") | Before sending |
| `why_this_company` | The one-line commercial reason, not a compliment | Before sending |
| `handraiser_type` | Discovery, capacity or opportunity (see document 2) | Before sending |
| `stated_need_or_capacity` | **Verbatim quotes** from their replies | Each reply |
| `stated_requirements` | Verbatim: geography, licenses, volumes, timing, rules (e.g. "approved supplier only") | Each reply |
| `fit_evidence` | What we verified ourselves, with links (website, public records) | Before the close |
| `qualification` | The checklist in B1 | Each reply |
| `introduction_permission` | Has this side agreed to be introduced? Yes / no, plus the quote | Before naming them |
| `names_revealed` | What we've told them about the other side (never a company name before payment) | Each message |
| `open_questions` | Which of the five buyer questions are unanswered: who are you, can you deliver, what am I paying for, what happens after I pay, what if it doesn't work | Each message |
| `next_move` | From document 3 | Each reply |
| `opt_out` | Yes / no. If yes, stop | Each reply |

### B1. Qualification checklist (moving a prospect from E2 to E3)

**Demand side:**

- [ ] Specific need confirmed in their words (the service, scope, volume).
- [ ] Requirements known (licenses, compliance, geography, approved-vendor rules).
- [ ] Timing (now, or a dated window).
- [ ] Authority (the decision maker or budget holder, or the route to one).
- [ ] Agrees in principle to be introduced.
- Budget: optional. Saad rarely asks, and prices from the deal's economics instead `[A07, A12]`.

**Supply side:**

- [ ] Capacity now.
- [ ] Capability matches the demand's requirements (verified from their own published work where possible).
- [ ] Serves the geography.
- [ ] Open to the commercial arrangement (fee, retainer or referral structure).
- [ ] Agrees in principle to be introduced.

### B2. Claim permissions by evidence state

What a message may say about **the other side**, depending on that side's state:

| Other side's state | Allowed | Not allowed |
|---|---|---|
| E0–E1 (signal only) | "[Public fact about the market]…" / "I'm tracking [signal] in [area]…" / "I'm finding out which [suppliers] want to be in front of [demand]…" | "I have…," "I'm working with…," "I'm speaking with…," "actively looking…" |
| E2 (engaged) | "I'm speaking with a [type] in [area] that [their words]…" (no name) | "Confirmed," "ready to buy," invented details |
| E3 (qualified) | "I have a [type] that confirmed it needs [X] and is open to an introduction…" | The company name before payment and permission |
| E4 / E5 | Full names in the introduction | Claiming downstream results |

What a message may say about **us:** only true statements. For example: "I track [signal] and connect [A] with [B] when the timing's right." Never claim experience we don't have `[A05, A08, A15]`.

### B3. Close-readiness gate (before sending a fee or invoice)

- [ ] The paying side is E3.
- [ ] The free side is E3, including permission to be introduced.
- [ ] Fit verified by us, with evidence links.
- [ ] Price and deliverable written; replacement clause; transparency line if both pay.
- [ ] All five buyer questions answerable in writing.
- [ ] No names revealed yet.

---

## Worked example (from a real case: A07, nursing staffing, S11)

**Market brief (abridged):**

```yaml
market_name: Maryland nursing homes ↔ nurse staffing agencies
demand_side: nursing homes already paying agencies for contract hours
supply_side: nurse staffing agencies placing RNs, LPNs, CNAs/GNAs in long-term care
selection_lens: money already moving (public payroll data)
money_already_moving: "PBJ data: e.g. 23,000 contract hours Jan–Mar 2026 at one home"
value_of_one_customer: "~100 agency hrs/week × 52 × ≥$18.62/hr ≈ $95k+/yr per facility"
scarce_side: none dominant; supply competes for facilities
who_pays_and_for_what: agency — "qualified nursing home introduction"
price_hypothesis: "$8,000 flat (suggested; small vs ≥$95k/yr)"
deliverable: one email introduction with full context; "no meetings or calls needed with me"
guarantee: replace if the facility materially differs from what's described
trigger_event: facility reports contract-staff hours (PBJ, quarterly)
data_source: Medicare PBJ public files; agency lists by state
decision_maker_order: [administrator, director of nursing]  # demand
industry_vocabulary: [facility, residents, shifts, agency hours, RN, LPN, GNA]
legal_flags: [healthcare referral fees — user to confirm permissibility]
```

**Prospect card at close time:**

```yaml
company: (withheld) nursing home, Laurel MD
side: demand
evidence_state: E3
stated_need_or_capacity: "still using quite a bit of agency… short on RNs, LPNs and GNAs plus some management coverage"
stated_requirements: "Where is the agency based?"  # location matters
introduction_permission: implied by "Let me know if you have anyone" — confirm explicitly
names_revealed: none
open_questions: none for this side (free)
---
company: (withheld) staffing agency
side: supply
evidence_state: E3 → E4 after payment
stated_need_or_capacity: "We can start supplying staff within 48 to 72 hours after signing"
stated_requirements: "please send your fees and facility name"
fit_evidence: website FAQ (staffs LPNs, CNAs, RNs for facilities); also based in Laurel
names_revealed: none until paid
next_move: close email with fee, deliverable, replacement clause (document 3, close path)
```
