import os

def generate_ichigo_accent():
    out_path = os.path.join(os.path.dirname(__file__), "..", "assets", "ichigo-accent.svg")

    svg = """<svg viewBox="0 0 800 120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="reiatsu-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#26264C" stop-opacity="0" />
      <stop offset="30%" stop-color="#724972" stop-opacity="0.4" />
      <stop offset="50%" stop-color="#B199DB" stop-opacity="0.85" />
      <stop offset="70%" stop-color="#E9CCD3" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#26264C" stop-opacity="0" />
    </linearGradient>

    <linearGradient id="blade-glow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.9" />
      <stop offset="60%" stop-color="#B199DB" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#724972" stop-opacity="0.2" />
    </linearGradient>

    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Background Reiatsu Energy Wave -->
  <path d="M 50 60 Q 200 10 400 60 T 750 60" fill="none" stroke="url(#reiatsu-grad)" stroke-width="3" opacity="0.6"/>
  <path d="M 100 65 Q 300 100 500 50 T 700 70" fill="none" stroke="url(#reiatsu-grad)" stroke-width="1.5" opacity="0.4"/>

  <!-- Center Emblem Banner -->
  <g transform="translate(400, 60)">
    <!-- Stylized Getsuga Tensho Slash Accent -->
    <path d="M -160 15 L 160 -15 L 140 -8 L -140 22 Z" fill="url(#blade-glow)" filter="url(#glow)" />
    
    <!-- Japanese Kanji / Anime Quote Accent -->
    <text text-anchor="middle" y="32" font-family="'Cinzel', 'Georgia', serif" font-size="12" fill="#E9CCD3" letter-spacing="4" opacity="0.85">
      黒崎一護 · BLEACH · GETSUGA TENSHO
    </text>
  </g>
</svg>
"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {out_path}")

if __name__ == "__main__":
    generate_ichigo_accent()
