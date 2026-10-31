# Outreach System: Design Documents

These three documents turn the casebook research into the rules an outreach system (a skill, a GPT, or a person following a checklist) needs before it writes or answers a single email. They're **design documents**, not skills. Building the skills comes after they're reviewed.

| # | Document | Answers |
|---|---|---|
| 1 | `01-opportunity-brief.md` | What must we know about a market, a transaction and a prospect before writing? What are we allowed to claim? |
| 2 | `02-outreach-standard.md` | Which first message do we send, how is it built, how do we follow up, and how do we diagnose a campaign that isn't working? |
| 3 | `03-reply-framework.md` | When someone replies, what does it mean, what's the next move, and how do we close (usually without a call) or stop? |

The order matters. A good reply depends on a good first email, and a good first email depends on the brief. **The opportunity brief is the system's input; nothing is written without one.**

## Evidence base

| Source | Location | Notes |
|---|---|---|
| Claude casebook | `docs/research/casebook/` | 21 case files with **exact** wording verified against the transcripts (A01–A21). Part B covers the sales documents; Part C has the cross-case findings. Cited as `[A07]`, `[Part C §3]` |
| ChatGPT casebook | `docs/research/saad-frankie-casebook-2026-10-30/` | The parallel edition (C01–C17). Its own note says some wording is reconstructed. Its "four kinds of truth" and "why this reply?" table are adopted here. Cited as `[CG C12]` |
| Saad skills | `.claude/skills/saad-frameworks/` | Doctrine and the user's guide U1 (the rulebook) |
| Frankie skills | `.claude/skills/frankie-frameworks/` | Handraisers, conversations, Loom/Doc closing, the style guide G1 |

## Shared vocabulary

**Evidence state.** This is what we actually know about one side of a deal. It's tracked separately for each side and decides what any message may claim. It merges our four honesty levels with the ChatGPT casebook's "four kinds of truth."

| State | Name | What's true | Example |
|---|---|---|---|
| **E0** | Hypothesis | We think a market exists; nothing is verified | "Daycares probably buy meals" |
| **E1** | Public signal | A verifiable, dated public fact about this company or market | A license issued on September 4; a lost bid; a warning letter |
| **E2** | Engaged | This person replied with interest, capacity or questions | "Yes, we have room" |
| **E3** | Qualified | Specific need or capacity, requirements, fit, authority and timing are confirmed, and they agree in principle to be introduced | "Still short on RNs, LPNs, GNAs; we're in Laurel; send them over" |
| **E4** | Committed | Written terms accepted and payment received where required | The invoice is paid |
| **E5** | Delivered | The introduction has been made, with permission, as promised | The intro email is sent |

After E5 there are **downstream outcomes** (they met, they signed, revenue followed). Those are separate, and are never claimed as our result.

**Handraiser type.** This is what the first message is trying to learn.

| Type | Goal | Typical side |
|---|---|---|
| **Discovery** | Is the need real and still live? | Buyer (demand) |
| **Capacity** | Can and will this supplier take this kind of work? | Supplier |
| **Opportunity** | Do you want access to this specific, substantiated situation? | Either; only at E3 on the other side |

**Paying side and free side.** The paying side is the one invoiced for a defined service. The free side receives the introduction at no cost. Both sides can pay only for **different named services**, with disclosure.

**Permissioned handoff.** An introduction is made only after **both** sides have agreed to it. Names are revealed only after payment, if the paying side pays, **and** after the other side has agreed to be introduced.

## Rules that override everything in these documents

1. **Never claim a higher evidence state than the one we're in.** No invented buyers, suppliers, results, experience, counts, dates or urgency.
2. **No AI or automation that presents itself as a person,** and no made-up reasons for writing (`[Part B §4]`).
3. **Disclose when both sides pay.**
4. **Respect a "no" or an opt-out immediately.** Follow CAN-SPAM for email; get consent before texts or automated calls (TCPA).
5. **Sensitive lanes need a check by the user before use:** regulated referral fees (healthcare, finance, legal), cannabis, and harm-related situations (fatalities, enforcement).
6. **No profanity, and no impersonating Saad or Frankie.**
