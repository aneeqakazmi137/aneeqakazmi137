import base64
import os

def generate_hero_banner():
    bg_path = os.path.join(os.path.dirname(__file__), "..", "assets", "cosmic-bg.png")
    out_path = os.path.join(os.path.dirname(__file__), "..", "assets", "hero-banner.svg")

    with open(bg_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")

    svg = f"""<svg viewBox="0 0 900 220" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@600;800&amp;family=Plus+Jakarta+Sans:wght@500;700&amp;display=swap');
      .title {{
        font-family: 'Outfit', 'Plus Jakarta Sans', sans-serif;
        font-size: 50px;
        font-weight: 800;
        fill: url(#title-grad);
        letter-spacing: -0.5px;
        filter: drop-shadow(0px 4px 14px rgba(177, 153, 219, 0.55));
      }}
      .subtitle {{
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 13px;
        font-weight: 700;
        fill: #E9CCD3;
        letter-spacing: 3px;
        text-transform: uppercase;
        opacity: 0.95;
      }}
      .star {{
        animation: blink 3s ease-in-out infinite alternate;
      }}
      @keyframes blink {{
        0% {{ opacity: 0.3; transform: scale(0.8); }}
        100% {{ opacity: 1; transform: scale(1.2); }}
      }}
    </style>

    <linearGradient id="title-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="40%" stop-color="#E9CCD3" />
      <stop offset="80%" stop-color="#B199DB" />
      <stop offset="100%" stop-color="#9C77CD" />
    </linearGradient>

    <linearGradient id="overlay-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1F1F3D" stop-opacity="0.75" />
      <stop offset="50%" stop-color="#45538A" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#5E3A60" stop-opacity="0.7" />
    </linearGradient>

    <linearGradient id="border-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#724972" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#B199DB" stop-opacity="1" />
      <stop offset="100%" stop-color="#45538A" stop-opacity="0.9" />
    </linearGradient>
    
    <clipPath id="rounded-clip">
      <rect x="2" y="2" width="896" height="216" rx="16" />
    </clipPath>
  </defs>

  <!-- Container Box -->
  <rect x="1" y="1" width="898" height="218" rx="17" fill="#26264C" stroke="url(#border-grad)" stroke-width="2" />

  <g clip-path="url(#rounded-clip)">
    <!-- Cosmic Nebula Image Background -->
    <image href="data:image/png;base64,{img_b64}" x="0" y="-120" width="900" height="450" preserveAspectRatio="xMidYMid slice" opacity="0.85" />

    <!-- Soft Dark Color Overlay for Text Readability -->
    <rect x="0" y="0" width="900" height="220" fill="url(#overlay-grad)" />

    <!-- Ambient Glowing Stars -->
    <circle cx="100" cy="40" r="2.5" fill="#E9CCD3" opacity="0.9" />
    <circle cx="240" cy="170" r="1.8" fill="#B199DB" opacity="0.8" />
    <circle cx="780" cy="50" r="2.5" fill="#FFFFFF" opacity="0.9" />
    <circle cx="830" cy="150" r="1.5" fill="#E9CCD3" opacity="0.8" />
    <circle cx="450" cy="25" r="2" fill="#B199DB" opacity="0.85" opacity="0.8" />
    <circle cx="670" cy="180" r="2.2" fill="#FFFFFF" opacity="0.8" />

    <!-- Subtitle Badge -->
    <g transform="translate(450, 52)">
      <text text-anchor="middle" class="subtitle">✦ SOFTWARE ENGINEER &amp; CREATIVE DEVELOPER ✦</text>
    </g>

    <!-- Main Title -->
    <g transform="translate(450, 130)">
      <text text-anchor="middle" class="title">Hewwo! I'm Aneeqa</text>
    </g>

    <!-- Decorative Accent Line -->
    <line x1="360" y1="158" x2="540" y2="158" stroke="#B199DB" stroke-width="1.5" stroke-linecap="round" opacity="0.6" />
  </g>
</svg>
"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {out_path}")

if __name__ == "__main__":
    generate_hero_banner()
