---
name: alabama-newsletter
description: Produce the weekly Alabama-only newsletter (Morning Brew style) covering federal and state policy that affects Alabamians, what Alabama's representatives actually did this week, a plain-language term explainer, community news, statewide events, and jobs and opportunities. Use for drafting, planning or automating any issue of the newsletter; it orchestrates the alabama-* subskills.
---

# Alabama Weekly — Newsletter Orchestrator

**Mission:** inform, educate and deliver real value to Alabama citizens every
week. Show what policy does to people's lives, what their representatives
actually voted for, and what the weaponized political terms really mean.
The aim is to cool the culture war and pull readers toward the middle with
facts, not labels.

**Scope:** Alabama only. A national story makes the cut only when there's a
concrete Alabama angle: a vote by Alabama's delegation, a dollar figure for
Alabama, or an Alabama agency, employer or community.

## Issue structure (default; see `references/style-guide.md`)

1. **Opener.** Two or three lines, warm and specific to the week.
2. **The Rundown.** 3–5 short policy items, federal and state, each ending
   with "What it means for you." → `alabama-policy-tracker`
3. **What Have You Done for Me Lately?** The weekly report on Alabama's
   members of Congress and key state legislators: votes, bills, statements
   versus actions. → `alabama-rep-scorecard`
4. **Word of the Week.** One weaponized term explained plainly (e.g. woke,
   socialism, communism, CRT, DEI). → `alabama-terms-explainer`
5. **Around the State.** Community wins, local spotlights, statewide events.
   → `alabama-community-jobs`
6. **Opportunity Board.** Jobs, hiring announcements, grants, training
   programs. → `alabama-community-jobs`
7. **Quick Hits and sign-off.** Short facts, a poll or question, and a
   referral ask.

## Weekly workflow

1. Set the issue window (default: the previous Monday–Sunday).
2. Run the subskills. Each returns items with source links.
3. Choose and order items by impact on Alabamians, not by outrage.
4. Write in the house voice from `references/style-guide.md`.
5. Run `alabama-newsletter-editor` (fact-check, fairness and tone pass). Don't
   publish anything it flags as unverified.
6. Output: subject line (plus 2 alternates), preheader, the issue in Markdown
   and HTML, and a source list.

## Non-negotiables

- Every factual claim links to a primary source (bill text, roll-call vote,
  agency release, official data) or a reputable outlet.
- Report votes, not vibes. When you say a vote cuts against constituents'
  interests, show the mechanism: what the bill does, who in Alabama it affects,
  and by how much.
- Apply the same standard to every party. Readers we want to reach will tune
  out a newsletter that only ever criticizes one side. Credibility is how we
  persuade.
- Explain, don't mock. No name-calling of readers, voters or groups.

Sources: `references/sources.md`. Automation: `references/n8n-pipeline.md`.
