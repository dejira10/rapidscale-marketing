---
name: ad-spend-finder
description: Find companies in an industry and location that are actively paying for ads (Google Ads/PPC, Facebook/Instagram/Meta, LinkedIn, etc.) and produce a prospect list with evidence. Use for prospecting by ad spend for any marketer (Frankie, Saad, Aaron).
---

# Ad Spend Finder

A business already paying for ads has a marketing budget and is measuring
leads. That makes it a warm prospect for marketing services.

## Inputs
- Industry or keyword (e.g. "roofing", "med spa")
- Geography (city, metro, state)
- Optional: platforms to check, and how many results to return

## Sources (all public)

| Platform | Where | Notes |
|---|---|---|
| Google Search (PPC) | Live search for "<service> <city>" | Results labeled "Sponsored" are current advertisers. Run several buyer-intent keywords. |
| Google Ads Transparency Center | adstransparency.google.com | Search by advertiser name or domain to confirm and see their ad formats and regions. There's no official API, so use browser-use or Firecrawl. |
| Google Local Services Ads | "Sponsored" / "Google Guaranteed" units at the top of local searches | Common for home services. |
| Meta Ad Library | facebook.com/ads/library | Choose "All ads", set the country, and search a keyword or page name. Shows active ads and start dates. In the US the official API only covers political/issue ads, so read the website UI for commercial ads. |
| LinkedIn Ad Library | linkedin.com/ad-library | B2B advertisers. |
| Site tracking tags | `scripts/detect_ad_pixels.py` | Google Ads (`AW-`) tags, Meta Pixel, TikTok and LinkedIn Insight tags suggest active or recent campaigns. |

## Steps
1. Make 5–10 buyer-intent keywords for the industry and geography.
2. Collect advertisers from Google sponsored results and the Meta Ad Library.
3. Dedupe by domain. For each company, run
   `python3 -I .claude/skills/ad-spend-finder/scripts/detect_ad_pixels.py <domain> [...]`.
4. Confirm the strongest prospects in the Google Ads Transparency Center.
5. Enrich with the contact/owner name, phone, Google rating and review count,
   and whether it's a franchise (hand off to `franchise-finder` if so).

## Output (CSV or table)
`company, domain, city, platforms_seen, evidence_links, ad_start_date (if shown), pixels_found, rating, reviews, franchise(y/n), notes`

Each "running ads" claim needs an evidence link or a pixel hit. A tracking tag
alone means **tag present** (they have run or are set up to run ads), not that
ads are running now.
