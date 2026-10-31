# Alabama Newsletter — n8n Automation Plan

**Status:** draft architecture. It still needs to be lined up with the Recap AI
n8n example the user has; share that workflow JSON or video and mirror its node
layout and patterns here before building.

## Pipeline (one workflow per stage, linked by a shared datastore)

1. **Schedule trigger** (weekly, e.g. Thursday 6am CT) sets the issue window.
2. **Ingest**, one sub-workflow per source group (`HTTP Request` + `RSS Read` nodes):
   - Congress.gov API, House/Senate roll-call XML, Federal Register API
   - Open States API (Alabama), ALISON scrape, governor releases
   - Alabama news RSS feeds (see `sources.md`)
   - Events calendars, AlabamaWorks/Commerce announcements
   Each item is normalized to `{id, type, title, url, date, raw_text, source}`
   and stored (Google Sheets, Airtable, Supabase or n8n Data Tables).
3. **Filter and score** (LLM node, Claude): drop anything without an Alabama
   angle; score impact 1–5; tag the section.
4. **Section writers** (LLM nodes): one prompt per section, built from the
   matching subskill's SKILL.md, fed only stored items and their URLs.
5. **Rep scorecard**: join roll-call votes to the current AL delegation
   (Congress.gov members API) and write the "What Have You Done for Me Lately?"
   block.
6. **Editor pass** (LLM node using `alabama-newsletter-editor`): fact and link
   check, fairness check, tone check. Failing items go to a review queue.
7. **Human approval**: send the draft to email or Slack with approve/edit
   buttons (n8n Wait node + webhook).
8. **Publish**: push to the ESP (beehiiv, ConvertKit/Kit, Mailchimp) through
   its API; archive to the web.

## Secrets needed
api.data.gov key (Congress.gov), Open States API key, LLM API key, ESP API key.
Store them in n8n credentials, never in workflow JSON.
