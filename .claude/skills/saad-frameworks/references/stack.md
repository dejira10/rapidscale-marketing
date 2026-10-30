# Saad — Tools and Settings

These are the tools Saad names in his videos. Prices are what he quoted at the
time, so check current pricing before you recommend anything. His own products
are marked **(his product)**. When he recommends one, note the conflict of
interest and offer the generic alternative.

## Connector-era stack

| Job | Tool(s) | Notes | Source |
|---|---|---|---|
| Research and list pulling | Claude Code in a terminal, running a "skill" (an instruction set) per lane | "load food safety skill" → "give me 1k on each side." Pro plan is enough; he uses a Max plan. Terminal is better than the chat app. Whisper for voice dictation | [S01, S02, S11] |
| Inboxes | ScaledMail (~$85 a month, ~35 inboxes, 50/50 Google and Microsoft); Hisend (~$30 a month for 100 Microsoft inboxes, bring your own domain); pre-warmed inboxes (~$3–4.50 each) | Avoid all-in-one platforms' add-on inboxes. Pre-warmed inboxes skip the 2-week warm-up | [S01, S02, S07, S33, S59] |
| Sending | Instantly (Hypergrowth plan, ~$97 a month); PlusVibe is a cheaper equivalent | The Instantly MCP lets Claude Code create campaigns and push leads | [S02, S13, S38] |
| Email finding and verification | AnyMailFinder (most consistent; charges only for found, valid emails); MailTester Ninja (cheapest, less consistent); mails.so; Find That Email; Hunter; Prospeo | Verify everything. Send to valid only | [S01, S24, S27, S56] |
| Lists | Apify actors (LinkedIn Jobs, Wellfound, Crunchbase, Apollo "leads finder," Clutch, Dice, Zillow, OSHA and SBA actors he built); Sales Navigator with Evaboot export (~$9); Apollo (API key enrichment); Instantly SuperSearch; Exa websets | Sales Nav "freshest, better than Apollo." Keep LinkedIn scrapes to ~2,500 a day per account | [S31, S33, S41, S43, S49, S50] |
| Business email for closing | Your own Gmail or Google Workspace (~$7 a month) | Move commercial threads out of the cold inbox | [S05, S12] |
| Payments | Stripe (via Atlas, Mercury bank); PayPal, Payoneer or Wise also work | A separate product for each side | [S08, S17] |
| Tracking | Linear (he tried ClickUp, Monday, Pipedrive); Google Sheets; an Instantly webhook on "lead marked as interested" → one sheet per side | Don't build a CRM before your first 3–5 customers | [S17, S39] |
| Replies at volume | An AI reply assistant | Only when there are too many replies to handle by hand | [S13] |
| Matching | ConnectOS **(his product)**: imports supply and demand datasets, scores matches, finds emails, writes intros | He says it's free and has a "founder tier." The matching logic is just "what does A need vs. what does B get paid to solve → score and reason." A spreadsheet or Claude can do the same | [S17, S31, S33, S49, S50] |
| Verification | "Purple Magic" / "Connector Agent" **(his product)** | Alternatives: AnyMailFinder, MailTester Ninja | [S01, S38, S49] |

## Instantly settings he uses

- Text-only first email [S02, S03].
- Schedule 7:00am–7:30pm, Monday–Saturday (sometimes every day) [S01, S50].
- Daily limit ~500–600 [S01]. Lower for small lists [S07].
- ESP routing: Google→Google, Microsoft→Microsoft [S39].
- Launch before all the leads have finished adding [S02].
- Avoid "risky" emails, because bounces hurt deliverability [S01].

## Earlier agency-era tooling (for pipelines only)

- **Make.com and n8n pipelines** [S20, S24, S27, S34, S42, S53, S54]:
  - scrape (Apify) → validate the email → AI-clean the company name, job title
    and date → scrape the website (Exa or SERP API, cheaper than HTTP plus
    HTML-to-text) → AI personalization line → push to Instantly.
  - Use a webhook to a second scenario to get past Make's 40-minute limit
    [S27, S42].
  - Use a fallback branch when the website won't scrape [S24, S53].
- **AI models**: Claude, GPT-4o, Gemini, Perplexity Sonar Pro for cleanups
  (Perplexity handled newlines better), and Azure-hosted models. Temperature
  ~0.3–0.5 [S19, S27, S42, S53].
- **Enrichment**:
  - People Data Labs (personal emails and mobiles). Flag it for privacy, TCPA
    and GDPR [S46].
  - Google Search API via RapidAPI ("{company} CEO") to find a decision maker
    [S26, S30].
- **Onboarding form** that turns into a formatted Google Doc. It asks for the
  offer, the target audience, guarantees, the biggest client pains, the job
  titles to target, and "something we should know about your ICP." That way
  you never re-ask after the kickoff [S52].

## Costs he cites

- About $150–200 in software for $15–18k of potential within 24 hours [S02].
- About $100–180 a month for a funding-signal system, compared with
  Crunchbase Pro or ZoomInfo [S32].

These are his claims.
