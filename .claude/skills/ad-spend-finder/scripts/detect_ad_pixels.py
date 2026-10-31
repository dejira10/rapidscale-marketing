#!/usr/bin/env python3
"""Detect ad-platform tracking tags on a website's homepage.

Usage: detect_ad_pixels.py example.com [another.com ...]
Prints one CSV row per domain: domain,status,google_ads,meta_pixel,tiktok,linkedin,gtm
"""
import re
import sys
import urllib.request

PATTERNS = {
    "google_ads": re.compile(r"AW-\d{6,}|googleadservices\.com|googleads\.g\.doubleclick\.net"),
    "meta_pixel": re.compile(r"connect\.facebook\.net/[^\"']*/fbevents\.js|fbq\(\s*['\"]init"),
    "tiktok": re.compile(r"analytics\.tiktok\.com|ttq\.load"),
    "linkedin": re.compile(r"snap\.licdn\.com|_linkedin_partner_id"),
    "gtm": re.compile(r"GTM-[A-Z0-9]{4,}"),
}


def fetch(domain):
    url = domain if domain.startswith("http") else f"https://{domain}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (ad-pixel-check)"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read(2_000_000).decode("utf-8", errors="replace")


def main(domains):
    print("domain,status," + ",".join(PATTERNS))
    for domain in domains:
        try:
            html = fetch(domain)
        except Exception as exc:  # report and keep going
            print(f"{domain},error: {type(exc).__name__}," + ",".join("" for _ in PATTERNS))
            continue
        hits = ["yes" if p.search(html) else "no" for p in PATTERNS.values()]
        print(f"{domain},ok," + ",".join(hits))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
