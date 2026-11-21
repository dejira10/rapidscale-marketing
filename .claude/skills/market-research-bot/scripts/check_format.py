#!/usr/bin/env python3
"""Check a market-research-bot output against references/template.md.

Usage:
    python3 check_format.py report.md            # checks the report (message 2)
    python3 check_format.py package.md --package # checks the marketing package (message 3)
    python3 check_format.py full.md --all        # both, in one file

Exit code 0 = matches the locked format; 1 = something drifted (each problem is listed).
"""
import re
import sys

B = r"\*\*"  # headings in the report are bold, e.g. "## **1. Problems ...**"

REPORT_HEADINGS = [
    rf"^# {B}.+ Industry: Market Research & Customer Pain Points{B}$",
    rf"^## {B}1\. Problems .+ face{B}$",
    rf"^### {B}A\. .+{B}$",
    rf"^### {B}B\. .+{B}$",
    rf"^### {B}C\. .+{B}$",
    rf"^### {B}D\. .+{B}$",
    rf"^### {B}E\. Tire kickers and unqualified prospects{B}$",
    rf"^### {B}F\. Inconsistent growth throughout the year{B}$",
    rf"^### {B}G\. .+{B}$",
    rf"^## {B}2\. How .+ currently generate business{B}$",
    rf"^## {B}3\. Frustrations with their current processes: TIMER{B}$",
    rf"^## {B}4\. Questions .+ aren't asking out loud{B}$",
    rf"^## {B}5\. Competitors .+ worry about{B}$",
    rf"^## {B}6\. Most desirable clients and services{B}$",
    rf"^### {B}Most desirable offerings{B}$",
    rf"^### {B}Why one qualified client can be valuable{B}$",
    rf"^## {B}7\. Fears about hiring a marketing agency{B}$",
    rf"^### {B}\"I've tried marketing before, and it didn't work\.\"{B}$",
    rf"^### {B}\"I don't want .+ problems\.\"{B}$",
    rf"^### {B}\"I don't want to damage my reputation\.\"{B}$",
    rf"^### {B}\"I don't want more work unless it produces real business\.\"{B}$",
    rf"^### {B}\"How do I know the agency is worth the money\?\"{B}$",
    rf"^## {B}8\. The strongest marketing opportunities{B}$",
    rf"^## {B}9\. Marketing messages most likely to resonate{B}$",
    rf"^## {B}Next step: Turn this research into client-getting marketing{B}$",
    rf"^## {B}Would you like me to create these marketing assets\?{B}$",
]

PACKAGE_HEADINGS = [
    r"^# .+ Marketing Package$",
    r"^### Your Core Offer$",
    r"^## 1\. Three Handraiser Posts$",
    r"^### Handraiser 1: .+ \(Recommended first test\)$",
    r"^### Handraiser 2: .+$",
    r"^### Handraiser 3: .+$",
    r"^### Which handraiser should you test first\?$",
    r"^## 2\. Facebook Ad$",
    r"^### Facebook ad setup$",
    r"^### Suggested image$",
    r"^## 3\. Complete Website Copy$",
    r"^### Does This Sound Like You\? The Old Way$",
    r"^### The New Way$",
    r"^### How It Works$",
    r"^### Case Studies \(placeholders: replace with real results, these are not claims\)$",
    r"^### Frequently Asked Questions$",
    r"^### About .+$",
    r"^## What I Would Test First$",
    r"^## One Question to Make This Sharper$",
]

REPORT_LINES = [
    "Target audience:",
    "don't simply need more leads. They need",
    "These are research-informed market hypotheses, expressed in the language",
    "rather than verified interview quotations.",
    "Specific examples include:",
    "| Current process | How it typically works | Main limitation |",
    "These are the questions that can drive compelling marketing messages:",
    "The most commercially important distinction is between",
    "These are recognizable examples, not a location-specific competitive ranking.",
    "**Online and technology competitors:**",
    "**Local competitors:**",
    "A significant concern is not necessarily that these competitors",
    "Illustrative client segments and economics",
    "| Ideal client | Why ",
    "Not a profit or revenue guarantee.",
    "these are three promising pain points to build offers around.",
    "| Weaker, generic message | Stronger, symptom-specific angle |",
    "**The most powerful overall positioning:**",
    "The positioning should be adjusted to reflect the marketing service you actually deliver, with any outcome claims supported by evidence.",
    "What service do you provide?",
    "businesses do you want to target?",
]

PACKAGE_LINES = [
    "**Your service:**",
    "**Your target:**",
    "**Your strongest positioning:**",
    "avoids invented results",
    "**Angle:**",
    "| CTA button |",
    "| Landing page |",
    "**Problem side:**",
    "**Outcome side:**",
    "There's a better way.",
    "**[Watch the video below]**",
]

# Hype and banned phrases, including style-guide.md §15 (frankie-frameworks)
HYPE = ["10x", "skyrocket", "explode your", "guaranteed results", "crush it",
        "revolutionary solution", "unlock unprecedented growth", "act now", "limited spots"]


def section(text, start_pat, end_pat=None):
    lines = text.splitlines()
    out, on = [], False
    for ln in lines:
        if re.match(start_pat, ln):
            on = True
            continue
        if on and end_pat and re.match(end_pat, ln):
            break
        if on:
            out.append(ln)
    return "\n".join(out)


def table_rows(block):
    rows = [l for l in block.splitlines() if l.strip().startswith("|")]
    return max(0, len(rows) - 2)  # minus header and divider


def check_order(text, pats, label, problems):
    lines = text.splitlines()
    pos = -1
    for p in pats:
        hit = next((i for i, l in enumerate(lines) if i > pos and re.match(p, l)), None)
        if hit is None:
            any_hit = any(re.match(p, l) for l in lines)
            problems.append(f"[{label}] heading {'out of order' if any_hit else 'missing'}: {p}")
        else:
            pos = hit


def count(problems, label, got, want):
    if got != want:
        problems.append(f"[{label}] expected {want}, found {got}")


def bullets(block, quotes_only=False):
    pat = r'^- "' if quotes_only else r"^- "
    return len(re.findall(pat, block, re.M))


def check_report(t, problems):
    check_order(t, REPORT_HEADINGS, "report", problems)
    for s in REPORT_LINES:
        if s not in t:
            problems.append(f"[report] fixed line missing: {s}")
    H = lambda L: rf"^### \*\*{L}\. "
    want = {"A": 5, "B": 5, "C": 4, "D": 5, "F": 4, "G": 4}
    nxt = {"A": "B", "B": "C", "C": "D", "D": "E", "E": "F", "F": "G"}
    for L, n in want.items():
        end = H(nxt[L]) if L in nxt else r"^## \*\*2\."
        blk = section(t, H(L), end)
        count(problems, f"1.{L} quotes", bullets(blk, True), n)
        if "**Underlying pain:**" not in blk:
            problems.append(f"[1.{L}] missing **Underlying pain:**")
    e = section(t, H("E"), H("F"))
    count(problems, "1.E tire-kicker examples", bullets(e), 6)
    if "**Underlying pain:**" not in e:
        problems.append("[1.E] missing **Underlying pain:**")
    count(problems, "2. channel rows", table_rows(section(t, r"^## \*\*2\.", r"^## \*\*3\.")), 10)
    s3 = section(t, r"^## \*\*3\.", r"^## \*\*4\.")
    for w in ["Time", "Identity", "Money", "Energy", "Reputation"]:
        if not re.search(rf'^\*\*{w} — ".+"\*\*$', s3, re.M):
            problems.append(f'[3. TIMER] missing line: **{w} — "…"**')
    count(problems, "4. questions", len(re.findall(r"^\d+\. ", section(t, r"^## \*\*4\.", r"^## \*\*5\."), re.M)), 12)
    s5 = section(t, r"^## \*\*5\.", r"^## \*\*6\.")
    if not re.search(r"^NATIONAL .+ COMPETITORS$", s5, re.M):
        problems.append("[5] missing line: NATIONAL [INDUSTRY] COMPETITORS")
    names = len(re.findall(r"^\*\*[^*:]+\*\*$", s5, re.M))
    if names != 6 and "No other national names verified." not in s5:
        problems.append(f"[5. national competitors] expected 6 (or the 'No other national names verified.' line), found {names}")
    count(problems, "6. ideal client rows", table_rows(section(t, r"^## \*\*6\.", r"^### \*\*Most desirable")), 7)
    count(problems, "6. desirable offerings", bullets(section(t, r"^### \*\*Most desirable offerings", r"^### ")), 8)
    calc = section(t, r"^### \*\*Why one qualified client", r"^## \*\*7\.")
    if not re.search(r"^ILLUSTRATIVE ", calc, re.M):
        problems.append("[6. calculation] missing ILLUSTRATIVE … label")
    count(problems, "6. calculation values", len(re.findall(r"^# \*\*.+\*\*$", calc, re.M)), 2)
    fears = [(r'^### \*\*"I\'ve tried', 3), (r'^### \*\*"I don\'t want (?!to damage|more work)', 4),
             (r'^### \*\*"I don\'t want to damage', 3), (r'^### \*\*"I don\'t want more work', 3),
             (r'^### \*\*"How do I know', 4)]
    for i, (pat, n) in enumerate(fears):
        end = fears[i + 1][0] if i + 1 < len(fears) else r"^## \*\*8\."
        count(problems, f"7. fear group {i+1} quotes", bullets(section(t, pat, end), True), n)
    s8 = section(t, r"^## \*\*8\.", r"^## \*\*9\.")
    count(problems, "8. opportunities", len(re.findall(r"^\*\*Opportunity \d: .+\*\*$", s8, re.M)), 3)
    count(problems, "8. 'Potential offer' lines", s8.count("**Potential offer:**"), 3)
    count(problems, "8. 'Quick-relief outcome' lines", s8.count("*Quick-relief outcome:*"), 3)
    s9 = section(t, r"^## \*\*9\.", r"^\*\*The most powerful")
    count(problems, "9. message rows", table_rows(s9), 5)
    if not re.search(r"^> We help ", t, re.M):
        problems.append("[9] positioning must be a quote line starting '> We help'")
    tail = section(t, r"^## \*\*Would you like me")
    svc = section(tail, r"^What service do you provide\?", r".*businesses do you want to target\?")
    count(problems, "service options", bullets(svc), 6)
    count(problems, "target options", bullets(section(tail, r".*businesses do you want to target\?")), 4)


def check_package(t, problems):
    check_order(t, PACKAGE_HEADINGS, "package", problems)
    for s in PACKAGE_LINES:
        if s not in t:
            problems.append(f"[package] fixed line missing: {s}")
    hr = section(t, r"^## 1\. Three Handraiser", r"^### Which handraiser")
    count(problems, "handraiser 'Symptom' lines", hr.count("**Symptom:**"), 3)
    count(problems, "handraiser 'What if' lines", len(re.findall(r"^What if ", hr, re.M)), 3)
    count(problems, "handraiser 'Just' lines", len(re.findall(r"^Just ", hr, re.M)), 3)
    count(problems, "handraiser one-word CTAs", len(re.findall(r"^Comment [A-Z0-9]+ ", hr, re.M)), 3)
    count(problems, "handraiser 'Target outcome' lines", hr.count("**Target outcome:**"), 3)
    count(problems, "'Recommended first test' tags", t.count("(Recommended first test)"), 1)
    fb = section(t, r"^## 2\. Facebook Ad", r"^### Facebook ad setup")
    for s in ["Here's a different way. We:", "Your first conversation looks like:", "You focus on"]:
        if s not in fb:
            problems.append(f"[facebook ad] missing: {s}")
    count(problems, "Old Way bullets", len(re.findall(r"^- ", section(t, r"^### Does This Sound", r"^\*\*So what do you do"), re.M)), 6)
    count(problems, "'So what do you do' bullets", len(re.findall(r"^- ", section(t, r"^\*\*So what do you do", r"^There's a better way"), re.M)), 4)
    count(problems, "How It Works steps", len(re.findall(r"^\d\. ", section(t, r"^### How It Works", r"^(\*\*|###)"), re.M)), 5)
    count(problems, "case study placeholders", len(re.findall(r"^- \*\*\[Client name\]:\*\*", t, re.M)), 3)
    count(problems, "FAQ questions", len(re.findall(r"^\*\*Q:\*\*", section(t, r"^### Frequently", r"^### About"), re.M)), 5)
    count(problems, "About Us principles", len(re.findall(r"^\d\. ", section(t, r"^### About", r"^## "), re.M)), 3)
    count(problems, "CTA buttons", len(re.findall(r"^\*\*\[Request your .+\]\*\*$", t, re.M)), 5)
    q = section(t, r"^## One Question to Make This Sharper")
    count(problems, "sharpening questions", q.count("?"), 1)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    t = open(sys.argv[1], encoding="utf-8").read()
    t = re.sub(r"(?<=\S) {2,}", " ", t)  # ignore padding inside tables
    t = re.sub(r"\|\s*-{3,}\s*", "|---", t)
    mode = sys.argv[2] if len(sys.argv) > 2 else "--report"
    problems = []
    if mode in ("--report", "--all"):
        check_report(t, problems)
    if mode in ("--package", "--all"):
        check_package(t, problems)
    for w in HYPE:
        if w in t.lower():
            problems.append(f"[style] hype phrase: {w}")
    if problems:
        print(f"FAIL: {len(problems)} problem(s)")
        for p in problems:
            print(" -", p)
        sys.exit(1)
    print("PASS: matches the locked format")


if __name__ == "__main__":
    main()
