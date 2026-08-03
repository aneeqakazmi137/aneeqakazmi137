"""
Hand-authored neofetch-style panel: title bar + fading key/value rows.
Static content (your role, stack, highlights) — edit ROWS below to update.
"""
import os

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "info-card.svg")

BG_PANEL = "#26264C"
BORDER = "#724972"
KEY_COLOR = "#B199DB"
VAL_COLOR = "#E9CCD3"
TITLE_BAR = "#45538A"

ROWS = [
    ("Now", "BSCS @ COMSATS Wah Campus"),
    ("Stack", "C++ · Python · TS/JS · Next.js"),
    ("Tools", "Tailwind · MySQL · Prolog · Git"),
    ("Building", "PakFuel Crisis Tracker"),
    ("Mindset", "Learning. Building. Repeating."),
]

WIDTH = 490
ROW_H = 30
TOP_PAD = 58
HEIGHT = TOP_PAD + len(ROWS) * ROW_H + 24


def build_svg():
    rows_svg = []
    for i, (key, val) in enumerate(ROWS):
        y = TOP_PAD + i * ROW_H
        delay = 0.5 + i * 0.22
        rows_svg.append(f"""
    <g class="row" style="animation-delay:{delay:.2f}s">
      <text x="34" y="{y}" class="key-text">{key}</text>
      <text x="150" y="{y}" class="val-text">{val}</text>
    </g>""")

    svg = f"""<svg viewBox="0 0 {WIDTH} {HEIGHT}" xmlns="http://www.w3.org/2000/svg" font-family="'Fira Code', 'Consolas', monospace">
  <style>
    .row {{
      opacity: 0;
      transform: translateX(-8px);
      animation: fadein 0.5s ease-out forwards;
    }}
    @keyframes fadein {{
      to {{ opacity: 1; transform: translateX(0); }}
    }}
    .key-text {{ fill: {KEY_COLOR}; font-size: 14px; font-weight: 700; }}
    .val-text {{ fill: {VAL_COLOR}; font-size: 13px; }}
    .bar-text {{ fill: {VAL_COLOR}; font-size: 13px; font-weight: 700; }}
  </style>

  <rect x="1" y="1" width="{WIDTH - 2}" height="{HEIGHT - 2}" rx="10"
        fill="{BG_PANEL}" stroke="{BORDER}" stroke-width="1.5"/>

  <rect x="1" y="1" width="{WIDTH - 2}" height="34" rx="10" fill="{TITLE_BAR}"/>
  <rect x="1" y="18" width="{WIDTH - 2}" height="17" fill="{TITLE_BAR}"/>
  <circle cx="20" cy="18" r="5" fill="#E9CCD3" opacity="0.85"/>
  <circle cx="38" cy="18" r="5" fill="#B199DB" opacity="0.85"/>
  <circle cx="56" cy="18" r="5" fill="#724972" opacity="0.85"/>
  <text x="{WIDTH / 2}" y="23" text-anchor="middle" class="bar-text">aneeqa@github</text>

  {''.join(rows_svg)}
</svg>
"""
    return svg


def main():
    svg = build_svg()
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
