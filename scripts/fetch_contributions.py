"""
Fetches the public contribution calendar for GITHUB_USERNAME and writes
data/contributions.json. Uses GitHub's public HTML fragment endpoint —
no token, no GraphQL API, no rate-limited third-party service.
"""
import json
import os
import re
from datetime import date

import requests
from bs4 import BeautifulSoup

USERNAME = os.environ.get("GITHUB_USERNAME", "aneeqakazmi137")
URL = f"https://github.com/users/{USERNAME}/contributions"
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "contributions.json")


def fetch_html():
    resp = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
    resp.raise_for_status()
    return resp.text


def parse_days(html):
    soup = BeautifulSoup(html, "html.parser")
    cells = soup.find_all("td", class_="ContributionCalendar-day")

    days = []
    for cell in cells:
        d = cell.get("data-date")
        level = cell.get("data-level")
        if d is None or level is None:
            continue

        count = 0
        tooltip = soup.find("tool-tip", attrs={"for": cell.get("id")})
        if tooltip:
            m = re.search(r"(\d+)\s+contribution", tooltip.text)
            if m:
                count = int(m.group(1))

        days.append({"date": d, "level": int(level), "count": count})

    days.sort(key=lambda x: x["date"])
    return days


def compute_stats(days):
    total = sum(d["count"] for d in days)

    # current streak: consecutive days with count > 0, walking back from today
    current_streak = 0
    for d in reversed(days):
        if d["count"] > 0:
            current_streak += 1
        else:
            break

    # longest streak anywhere in the window
    longest_streak = 0
    running = 0
    for d in days:
        if d["count"] > 0:
            running += 1
            longest_streak = max(longest_streak, running)
        else:
            running = 0

    best_day = max(days, key=lambda x: x["count"]) if days else None

    return {
        "total_contributions": total,
        "current_streak": current_streak,
        "longest_streak": longest_streak,
        "best_day": best_day,
        "generated_on": date.today().isoformat(),
    }


def main():
    html = fetch_html()
    days = parse_days(html)
    stats = compute_stats(days)

    payload = {"username": USERNAME, "days": days, "stats": stats}

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(payload, f, indent=2)

    print(f"Wrote {len(days)} days, {stats['total_contributions']} total contributions -> {OUT_PATH}")


if __name__ == "__main__":
    main()
