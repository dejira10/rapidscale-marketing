---
name: saad-market-research
description: Market research done Saad's way. Find an overlooked two-sided market ("industries nobody would think to go into") where money is already forced to move, through government funding, legal requirements, penalties, permanent demand or a fresh public trigger. Then find the public data that shows who just changed, decide which side pays, build verified lists for both sides, and check the economics for pricing. Use when researching a market, niche or lane for Saad's connector method. Not for Frankie or Aaron.
---

# Saad — Market Research

Saad's research isn't "pick a niche and find its pain points." He looks for two
sides that need each other, and for the boring public data that shows who just
moved. "The money is in the looking." [S06]

## Before you start

Load `saad-frameworks` and read:

- `references/frameworks.md`;
- `references/understanding-and-testing.md` (how he learns a market and tests
  it);
- `references/markets.md` (selection lenses, signals, data sources, list
  rules);
- `references/offers-and-pricing.md` §4 (pricing) and §5 (charging both sides).

## Steps

1. **Generate candidate lanes.** Run the selection lenses in `markets.md` §1
   and note which lens produced each idea:
   - "What does the government give money to? Work backwards." [S06]
   - "What is someone forced to pay for?" [S01]
   - "Who just got publicly penalized, with a deadline, and needs a
     specialist?" [S33]
   - "What do businesses buy every week, forever?" [S08]
   - "What had to happen before this?" Keep descending to the hidden event
     [S13].
   - "Who just lost a public bid?" [S06, S09]
   - Problems from the user's own life [S10, S14].
2. **Name both sides** for each lane: demand (the buyer with the need) and
   supply (the seller who wants that buyer). Write one plain sentence: "{A}
   needs {X}; {B} sells {X} and struggles to find {A} at the right moment."
3. **Score each lane** against:
   - the four ingredients [S40]: demand spikes, competing suppliers, cost of
     delay, timing asymmetry;
   - the "vibe check" [S14]: does it already spend money and invoice for work?
   - the penalty formula, where relevant [S33]: public shame, clock pressure,
     can't fix it alone, specialists bad at sales;
   - how rarely pitched the contacts are (Gmail or Yahoo addresses, no
     outbound) [S03, S10].

   Mark each criterion **pass / fail / unknown**, with evidence.
4. **Find the trigger data.** Look for a public source that timestamps the
   change: licenses, permits, registrations, trademark filings, procurement
   awards, enforcement actions, funding announcements or job posts. Use the
   catalog in `markets.md` §3 as a pattern library. For each lane, record:
   - the source URL;
   - the fields available (name, date, contact, amount);
   - how fresh it is;
   - the volume per week or month.

   If no public source exists, say so. **Don't invent a database.**
5. **Decide who pays** [S15, S16, S21]:
   - the side that already spends to acquire customers;
   - or the abundant side paying for access to the scarce side;
   - or both, for different services (transparently).
6. **Check the economics for pricing** with the four pricing questions [S15].
   Find, with sources:
   - typical contract or account size and margins;
   - lifetime value or renewal rates;
   - what the paying side currently spends to get customers (booths, ads,
     brokers).

   Turn that into a suggested non-round price range. Label it **suggested**,
   not Saad's.
7. **Learn the industry's words** from:
   - the businesses' own websites;
   - forums and Reddit (pain wording [S14]);
   - RFPs and regulatory notices.

   List 5–10 terms to use in copy, e.g. "wholesale accounts," "turnover,"
   "crews."
8. **Build both lists** using the rules in `markets.md` §4:
   - 100–1,000 per side;
   - titles that sign deals or hold the budget;
   - exclude noise;
   - 11–200 employees where relevant;
   - verified emails only;
   - a ledger to avoid repeats;
   - one state or city first.

   `ad-spend-finder` helps find suppliers that already pay to acquire
   customers. `franchise-finder` helps with multi-location buyers.

9. **Understand the market before you write a word** (`understanding-and-testing.md`
   Part A): map the money already moving, find the hidden event, translate the
   signal into pain, and collect the pain in their own words.
10. **Design the test** (Part B): list size per side, the first emails (via
    `saad-outreach`), follow-ups, dates, and which positive and warning signals
    to watch.
11. **After the test, decide** (Part C): keep, re-aim or drop, with the
    evidence.

## Output: a lane brief

For each lane:

- **The lane:** demand ↔ supply in one sentence, and the lens that produced it.
- **The scorecard:** each criterion marked pass, fail or unknown, with evidence
  links.
- **The trigger:** the data source, fields, freshness and volume (with links).
- **Who pays:** for which service, and why.
- **The suggested price** for each paying side, with the economics behind it.
  Mark it **inferred** where it's an estimate.
- **Industry vocabulary.**
- **List spec:** filters for each side, titles, decision-maker fallback order,
  and estimated counts.
- **Risks and flags:** legal status (e.g. cannabis), privacy, harm-sensitive
  lanes, and saturation.
- **The hand-off to `saad-outreach`:** the "I have X" line for each side.
- **The market-test brief** from `understanding-and-testing.md`, filled in
  as far as the facts allow.

Every claim needs a source link or a frameworks citation. Mark anything
inferred as **inferred**.
