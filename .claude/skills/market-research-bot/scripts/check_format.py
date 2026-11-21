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

REPORT_HEADINGS = [
    r"^# Market Research: .+$",
    r"^## 1\. Problems .+ Face$",
    r"^### Unqualified prospects that waste their time$",
    r"^## 2\. How .+ Currently Get Customers$",
    r"^## 3\. What Frustrates Them About Their Current Process \(TIMER\)$",
    r"^## 4\. Questions They're Thinking but Rarely Ask$",
    r"^## 5\. Competitors That Concern Them$",
    r"^### National and large competitors$",
    r"^### Local and regional competitors$",
    r"^### Online platforms and lead sources$",
    r"^## 6\. Their Most Desirable Projects, Services and Customers$",
    r"^### What they want more of$",
    r"^### Their ideal customers$",
    r"^## 7\. Fears About Hiring a Marketing Agency$",
    r"^### The biggest marketing objection$",
    r"^## 8\. The Strongest Marketing Angles$",
    r"^### Angle 1: .+$",
    r"^### Angle 2: .+$",
    r"^### Angle 3: .+$",
    r"^## 9\. What This Means for Your Offer$",
    r"^## Next: Turn This Research Into Marketing That Gets Responses$",
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
    "not direct interview quotations or verified survey findings",
    "**Target market:**",
    "**Marketing insight:**",
    "Using the TIMER framework (Time, Identity, Money, Energy, Reputation)",
    "**The deeper question:**",
    "channels that create price pressure, not necessarily direct competitors",
    "illustrative, not verified averages",
    "The ranking is a strategic judgment, not measured market demand.",
    "**The positioning I'd test first:**",
    "**What service do you offer",
]

PACKAGE_LINES = [
    "**Your service:**",
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

HYPE = ["10x", "skyrocket", "explode your", "guaranteed results", "crush it"]


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


def check_report(t, problems):
    check_order(t, REPORT_HEADINGS, "report", problems)
    for s in REPORT_LINES:
        if s not in t:
            problems.append(f"[report] fixed line missing: {s}")
    s1 = section(t, r"^## 1\.", r"^### Unqualified")
    count(problems, "1. problem groups A-E", len(re.findall(r"^### [A-E]\. ", s1, re.M)), 5)
    count(problems, "1. 'What this looks like' blocks", s1.count("**What this looks like:**"), 5)
    count(problems, "1. unqualified prospect rows", table_rows(section(t, r"^### Unqualified", r"^\*\*Marketing insight")), 5)
    count(problems, "2. channel rows", table_rows(section(t, r"^## 2\.", r"^## 3\.")), 8)
    s3 = section(t, r"^## 3\.", r"^## 4\.")
    for w in ["TIME", "IDENTITY", "MONEY", "ENERGY", "REPUTATION"]:
        if f"**{w}:**" not in s3:
            problems.append(f"[3. TIMER] missing **{w}:**")
    count(problems, "4. questions", len(re.findall(r"^\d+\. ", section(t, r"^## 4\.", r"^## 5\."), re.M)), 10)
    count(problems, "6. 'want more of' bullets", len(re.findall(r"^- ", section(t, r"^### What they want more of", r"^### "), re.M)), 5)
    count(problems, "6. ideal customer bullets", len(re.findall(r"^- ", section(t, r"^### Their ideal customers", r"^(\*Any|## )"), re.M)), 3)
    count(problems, "7. fear rows", table_rows(section(t, r"^## 7\.", r"^### The biggest")), 8)
    s8 = section(t, r"^## 8\.", r"^## 9\.")
    count(problems, "8. 'Target outcome' lines", s8.count("**Target outcome:**"), 3)
    count(problems, "8. 'Why it resonates' lines", s8.count("**Why it resonates:**"), 3)
    count(problems, "9. message rows", table_rows(section(t, r"^## 9\.", r"^\*\*The positioning")), 5)


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
