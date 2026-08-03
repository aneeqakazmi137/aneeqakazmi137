"""
Reads data/contributions.json and writes contrib-heatmap.svg — a 53x7
contribution grid in the cosmic palette, animated once on load (diagonal
reveal), then frozen. Pure SVG + CSS keyframes, no external service.
"""
import json
import os
from datetime import datetime

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "contributions.json")
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "contrib-heatmap.svg")

# Cosmic palette, empty -> brightest
PALETTE = ["#20203c", "#45538A", "#724972", "#B199DB", "#E9CCD3"]
BG = "transparent"
TEXT_COLOR = "#B199DB"
MUTED_COLOR = "#8A8AB0"

BOX = 11
GAP = 3
LEFT_PAD = 30
TOP_PAD = 40


def load_data():
    with open(DATA_PATH) as f:
        return json.load(f)


def to_weeks(days):
    """Group the flat day list into columns (weeks) of 7, Sun-aligned."""
    weeks = []
    current_week = []
    for d in days:
        dow = datetime.strptime(d["date"], "%Y-%m-%d").weekday()  # Mon=0..Sun=6
        dow = (dow + 1) % 7  # convert to Sun=0..Sat=6
        if dow == 0 and current_week:
            weeks.append(current_week)
            current_week = []
        # pad the first week so day-of-week rows line up
        while len(current_week) < dow:
            current_week.append(None)
        current_week.append(d)
    if current_week:
        weeks.append(current_week)
    return weeks


def build_svg(payload):
    weeks = to_weeks(payload["days"])
    stats = payload["stats"]
    n_weeks = len(weeks)

    width = LEFT_PAD + n_weeks * (BOX + GAP) + 160
    height = TOP_PAD + 7 * (BOX + GAP) + 50

    cells = []
    max_delay_step = n_weeks + 7  # diagonal index range

    for wi, week in enumerate(weeks):
        for di in range(7):
            d = week[di] if di < len(week) else None
            x = LEFT_PAD + wi * (BOX + GAP)
            y = TOP_PAD + di * (BOX + GAP)
            if d is None:
                continue
            level = d["level"]
            color = PALETTE[min(level, 4)]
            delay = (wi + di) * (0.9 / max_delay_step)
            title = f"{d['count']} contribution{'s' if d['count'] != 1 else ''} on {d['date']}"
            cells.append(
                f'<rect class="cell" x="{x}" y="{y}" width="{BOX}" height="{BOX}" '
                f'rx="2.5" ry="2.5" fill="{color}" '
                f'style="animation-delay:{delay:.3f}s">'
                f"<title>{title}</title></rect>"
            )

    legend_x = LEFT_PAD + n_weeks * (BOX + GAP) - (5 * (BOX + GAP)) 
    legend_y = height - 20
    legend_cells = []
    for i, color in enumerate(PALETTE):
        lx = legend_x + i * (BOX + GAP)
        legend_cells.append(
            f'<rect x="{lx}" y="{legend_y}" width="{BOX}" height="{BOX}" rx="2.5" fill="{color}"/>'
        )

    footer = (
        f"{stats['total_contributions']} contributions in the last year "
        f"&#183; current streak {stats['current_streak']}d "
        f"&#183; longest streak {stats['longest_streak']}d"
    )

    svg = f"""<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', 'Helvetica Neue', sans-serif">
  <style>
    .cell {{
      opacity: 0;
      transform: translate(-6px, -6px);
      animation: reveal 0.5s ease-out forwards;
    }}
    @keyframes reveal {{
      to {{ opacity: 1; transform: translate(0, 0); }}
    }}
    .title-text {{ fill: {TEXT_COLOR}; font-size: 15px; font-weight: 600; }}
    .footer-text {{ fill: {MUTED_COLOR}; font-size: 11px; }}
    .legend-text {{ fill: {MUTED_COLOR}; font-size: 10px; }}
  </style>

  <rect width="100%" height="100%" fill="{BG}"/>

  <text x="{LEFT_PAD}" y="22" class="title-text">✦ contributions.sh</text>

  {''.join(cells)}

  <text x="{legend_x - 34}" y="{legend_y + 9}" class="legend-text">Less</text>
  {''.join(legend_cells)}
  <text x="{legend_x + 5 * (BOX + GAP) + 6}" y="{legend_y + 9}" class="legend-text">More</text>

  <text x="{LEFT_PAD}" y="{height - 4}" class="footer-text">{footer}</text>
</svg>
"""
    return svg


def main():
    payload = load_data()
    svg = build_svg(payload)
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
