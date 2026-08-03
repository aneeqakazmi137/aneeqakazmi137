import os

def generate_hero_banner():
    out_path = os.path.join(os.path.dirname(__file__), "..", "assets", "hero-banner.svg")

    svg = """<svg viewBox="0 0 800 120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .title-text {
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, 'Helvetica Neue', sans-serif;
        font-size: 58px;
        font-weight: 800;
        fill: #B199DB;
        letter-spacing: -0.5px;
      }
    </style>
  </defs>

  <g transform="translate(400, 80)">
    <text text-anchor="middle" class="title-text">
      Hewwo! I'm Aneeqa
    </text>
  </g>
</svg>
"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Successfully wrote {out_path}")

if __name__ == "__main__":
    generate_hero_banner()
