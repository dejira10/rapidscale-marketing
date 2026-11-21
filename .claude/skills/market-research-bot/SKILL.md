---
name: market-research-bot
description: Run Frankie-style market research for any industry, then turn it into marketing assets. Give it the type of business you serve (dentists, commercial roofers, med spas, staffing agencies…) and it produces a 9-part market research report (problems in their own words, how they get customers now, TIMER frustrations, questions they don't ask, competitors, ideal customers, fears about hiring a marketer, best angles, positioning). After asking what service you sell them, it writes 3 handraiser posts, 1 Facebook ad and full website copy. Modeled on how Frankie Fihn's "Market Research Bot v 2.0" GPT behaves. Use when the user names an industry or niche and wants research, handraisers, an ad, or landing-page copy for it.
---

# Market Research Bot (any industry)

This skill reproduces the **workflow and output format** of Frankie Fihn's "Market Research Bot v 2.0" GPT. It was observed by running the GPT in the user's ChatGPT account on 2026-11-21 for two industries: commercial roofing contractors, and dentists.

It's **not** a copy of that GPT's hidden instructions or knowledge files, which weren't accessed. The GPT's replies named four knowledge files: "GPT Handraiser Formula," "Example Handraisers," "FB Ad 37 merge" and "GPT Website Copy Format." Where Frankie's method is needed, this skill uses `frankie-frameworks` instead.

## The format is locked

**Every run must follow `references/template.md` exactly.** Read it before every run. Copy every heading, label and fixed line word for word, including the bold markers. Fill only the slots. Don't add, drop, rename or reorder sections. The counts are exact. Report: 7 problem groups (A–G, with E = tire kickers and F = seasonality), 10 channels, 5 TIMER lines, 12 questions, 6 national competitors, 7 ideal clients, 8 offerings, one illustrative value calculation, 5 fear groups, 3 opportunities and 5 message rows. Package: 3 handraisers, 6 Old Way bullets, 5 steps, 5 FAQs and 3 principles.

The report format comes from the user's reference run for wealth management (`docs/research/market-research-bot/run3-wealth-management.md`). It's stricter than Frankie's GPT, which changes its own headings between runs.

**Check before delivering.** When the output is saved to a file, run:

```
python3 .claude/skills/market-research-bot/scripts/check_format.py <file> --report    # message 2
python3 .claude/skills/market-research-bot/scripts/check_format.py <file> --package   # message 3
```

Fix anything it reports, then deliver. In chat, check the output against the template's headings and counts before sending.

Other references:

- `references/output-format.md`: notes on what the real GPT produced in each run, and how its two runs differed;
- `docs/research/market-research-bot/run3-wealth-management.md`: the user's reference report the template is built from;
- `docs/research/market-research-bot/test-wealth-management.md`: a complete report written by this skill in the locked format (passes the checker);
- `references/examples.md`: abridged real outputs (roofing and dentists), for tone and depth only. **The template, not the examples, decides the format.**

## The flow (always in this order)

1. **Ask who they serve, and only that.** "Who do you serve? Just give me the type of business (dentists, roofers, med spas…)." Don't ask anything else first.
2. **Write the market research report** (9 parts, exactly as in `template.md`). End with the two closing questions: **what service they offer** and **which segment of the industry to target**.
3. **Once they name the service and target,** write the marketing package:
   - the core offer;
   - **3 handraisers**, each on a different symptom, with a recommendation of which to test first;
   - **1 Facebook ad**, with an image suggestion;
   - **the complete website copy**;
   - a recommended first test.
4. **Ask one sharpening question** that would make the copy stronger. For example: "Do you only generate the leads, or do you also book the consultations?"

If the user gives the industry and service in the first message, skip straight through. Still deliver the report before the assets.

## Tone: Frankie's style guide

**All copy follows `frankie-frameworks/references/style-guide.md`** (the rulebook). The transcript evidence behind it is in `voice.md` in the same folder. Read both before writing.

- **The template decides the structure; the style guide decides the voice inside it.** If they ever seem to conflict, keep the template's headings and counts and write the words in the style guide's tone.
- **Where it matters most:**
  - the quotes in their voice (§3–4: street level, their own words);
  - the handraisers (§9: an invitation, not a pitch; a small, comfortable next step);
  - the Facebook ad and website (§5–6: specific outcomes, the old way vs the new way).
- **Lead with the result, not the tool** (§15). "Replacement calls in the slow season," not "we run Google Ads." Name the service only after the outcome.
- **Before delivering message 3**, run the guide's **§17 Final Quality Check** on every handraiser, the ad and the website copy. Rewrite any piece that fails a question. The guide's principle: "be clear before clever. Be specific before persuasive."

## Rules

- **Write in the customer's own words.** Problems and frustrations are written as things the owner would actually say ("I've got $40,000 in payroll coming Friday and we're still waiting on checks"). This is Frankie's "street level" symptom writing; see `frankie-frameworks/references/research.md`.
- **Use TIMER for frustrations:** Time, Identity, Money, Energy, Reputation. Each gets a one-line quote in their voice. Source: `frankie-frameworks/references/offers.md`.
- **Label the research honestly.** Say at the top that these are **industry-informed hypotheses and representative language, not verified interviews or survey data.** Mark example numbers "illustrative, not verified averages." Validate the top symptoms with real sources (reviews, forums, calls) using `frankie-market-research` before spending money.
- **Name real competitors only if you're confident they exist.** Otherwise describe competitor *types*. Note that lead platforms (bid networks, marketplaces) are channels that create price pressure, not necessarily direct competitors.
- **Handraisers follow Frankie's formula** (`frankie-frameworks/references/offers.md` "Handraiser"):
  - a call-out of the audience;
  - a symptom question;
  - 3–5 short empathy lines;
  - "What if…";
  - what we do, in plain words;
  - "No [annoying thing]" lines;
  - a one-word comment CTA ("Comment ROOFS").

  One symptom per post.
- **Promise only what the service controls.** No invented results, clients, case studies or guarantees. Case-study sections are **layouts with placeholders**, labeled as not real.
- **Sell the outcome, not the tool.** "Talk to commercial building owners, not homeowners looking for shingles," not "we run cold email."
- **Fit the copy to the service named.** A connector or intro service is written differently from an ads service (see the roofing example).
- **Compliance notes:** mention CAN-SPAM for email, and advertising rules for regulated niches (health, legal, finance).
- **No profanity, no hype** ("10X," "skyrocket," "revolutionary solution," "unlock unprecedented growth"), no fake urgency, no impersonating Frankie (style guide §15).

## Output length

The real GPT writes long: about 18,000 characters for the report and about 20,000 for the assets. The template's fixed counts produce similar depth. There's no short mode: the format is the same every time.

## Using it with the other skills

- **Validate the symptoms:** `frankie-market-research` (Reddit, Quora, reviews, a frequency × emotion score).
- **Find who to send it to:** `ad-spend-finder`, `franchise-finder`, or the Saad lane research (`saad-market-research`) for two-sided markets.
- **Turn handraisers into outreach:** `frankie-outreach` or `saad-outreach`, following `docs/design/02-outreach-standard.md` for honest claims.
