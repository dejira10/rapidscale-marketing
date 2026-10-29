---
name: franchise-finder
description: List every franchise brand in a given industry, then find the locations and franchise owners within a brand, so outreach can land one location and expand across the system. Use when the user asks for franchises in an industry, franchise owners, or multi-location expansion targets.
---

# Franchise Finder

Two modes. **Industry → brands**: every franchise system in an industry.
**Brand → owners**: the locations and franchisees inside one system.

## Mode 1: Industry → franchise brands

Sources (use several and cross-check them):
- **State franchise registries.** Registration states publish Franchise
  Disclosure Documents (FDDs) that can be searched by name or keyword:
  - California DFPI franchise search (docqnet.dfpi.ca.gov)
  - Wisconsin DFI franchise search (dfi.wi.gov)
  - Minnesota Commerce CARDS (cards.web.commerce.state.mn.us)
- **Directories and rankings**: International Franchise Association
  (franchise.org), Entrepreneur Franchise 500, Franchise Times Top 400,
  FranchiseDirect, Franchise Gator.
- **Web search** for "<industry> franchise opportunities" and the brands'
  own "own a franchise" pages.

For each brand, record: `brand, parent company, category, units (US), year
franchising began, initial investment range, website, franchise-dev contact,
source links`. Take the unit count from the FDD's Item 20 where you can, and
note which year's FDD it came from.

## Mode 2: Brand → locations and owners

1. **FDD Item 20 exhibit.** The FDD lists current franchisees (and those who
   left in the past year) with location and contact details. This is the most
   direct list of owners. Download the latest FDD from a state registry.
2. **Store locator** on the brand's site: scrape every location's address,
   phone and page URL.
3. **Owner names**: location pages ("locally owned by …"), Google Business
   Profile, LinkedIn ("Franchise Owner at <brand>"), state business-entity
   searches (the LLC behind each location), local news.
4. **Multi-unit operators**: group locations by owner or LLC. One operator with
   many units is the highest-value target.
5. Cross-reference with `ad-spend-finder` to see which locations already run ads.

## Output
A brand table (Mode 1) and/or a location table (Mode 2):
`brand, location, address, phone, owner_name, owner_entity, units_owned, source_links, running_ads`

Rules: cite a source for every owner name. FDD lists can be up to a year old,
so verify ownership before outreach. Don't guess personal emails. Use business
contact routes.
