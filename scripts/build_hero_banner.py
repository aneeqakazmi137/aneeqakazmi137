import os

def generate_hero_banner():
    out_path = os.path.join(os.path.dirname(__file__), "..", "assets", "hero-banner.svg")

    svg = """<svg viewBox="0 0 900 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Cosmic Gradients -->
    <linearGradient id="space-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#14142B" />
      <stop offset="35%" stop-color="#26264C" />
      <stop offset="70%" stop-color="#3C2A54" />
      <stop offset="100%" stop-color="#1B1B36" />
    </linearGradient>

    <radialGradient id="nebula-glow" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#B199DB" stop-opacity="0.45" />
      <stop offset="40%" stop-color="#724972" stop-opacity="0.25" />
      <stop offset="80%" stop-color="#45538A" stop-opacity="0.1" />
      <stop offset="100%" stop-color="#26264C" stop-opacity="0" />
    </radialGradient>

    <!-- Title Gradient -->
    <linearGradient id="title-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="35%" stop-color="#F2E6ED" />
      <stop offset="70%" stop-color="#E9CCD3" />
      <stop offset="100%" stop-color="#C5B1E5" />
    </linearGradient>

    <linearGradient id="accent-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#724972" stop-opacity="0.2" />
      <stop offset="50%" stop-color="#B199DB" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#45538A" stop-opacity="0.2" />
    </linearGradient>

    <linearGradient id="border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#B199DB" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#724972" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#45538A" stop-opacity="0.7" />
    </linearGradient>

    <!-- Glow Filters -->
    <filter id="text-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="star-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="1.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <clipPath id="card-clip">
      <rect x="2" y="2" width="896" height="236" rx="18" />
    </clipPath>
  </defs>

  <!-- Outer Card Frame -->
  <rect x="1" y="1" width="898" height="238" rx="19" fill="url(#space-bg)" stroke="url(#border-grad)" stroke-width="2" />

  <g clip-path="url(#card-clip)">
    <!-- Nebula Ambient Light Clouds -->
    <circle cx="200" cy="80" r="180" fill="url(#nebula-glow)" />
    <circle cx="700" cy="160" r="220" fill="url(#nebula-glow)" />

    <!-- Organic Cosmic Dust Waves -->
    <path d="M -50 180 Q 250 80 500 160 T 950 100" fill="none" stroke="#724972" stroke-width="1.5" opacity="0.3" />
    <path d="M -50 120 Q 200 220 550 90 T 950 200" fill="none" stroke="#B199DB" stroke-width="1" opacity="0.25" />

    <!-- Ambient Glowing Stars & Constellations -->
    <g filter="url(#star-glow)">
      <!-- Bright Stars -->
      <path d="M 120 45 L 122 50 L 127 52 L 122 54 L 120 59 L 118 54 L 113 52 L 118 50 Z" fill="#FFFFFF" opacity="0.9" />
      <path d="M 780 55 L 782 60 L 787 62 L 782 64 L 780 69 L 778 64 L 773 62 L 778 60 Z" fill="#E9CCD3" opacity="0.85" />
      <path d="M 830 170 L 831.5 174 L 835.5 175.5 L 831.5 177 L 830 181 L 828.5 177 L 824.5 175.5 L 828.5 174 Z" fill="#B199DB" opacity="0.9" />
      <path d="M 90 180 L 91.5 184 L 95.5 185.5 L 91.5 187 L 90 191 L 88.5 187 L 84.5 185.5 L 88.5 184 Z" fill="#FFFFFF" opacity="0.8" />
      
      <!-- Small Star Dots -->
      <circle cx="240" cy="40" r="1.5" fill="#E9CCD3" opacity="0.8" />
      <circle cx="360" cy="195" r="2" fill="#B199DB" opacity="0.7" />
      <circle cx="620" cy="35" r="1.5" fill="#FFFFFF" opacity="0.9" />
      <circle cx="680" cy="205" r="2" fill="#E9CCD3" opacity="0.75" />
      <circle cx="480" cy="25" r="1.8" fill="#B199DB" opacity="0.8" />
      <circle cx="50" cy="110" r="1.2" fill="#FFFFFF" opacity="0.6" />
      <circle cx="860" cy="110" r="1.5" fill="#B199DB" opacity="0.7" />
    </g>

    <!-- Top Badge Header -->
    <g transform="translate(450, 56)">
      <rect x="-140" y="-14" width="280" height="26" rx="13" fill="#26264C" stroke="#724972" stroke-width="1" opacity="0.8" />
      <text text-anchor="middle" y="3" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif" font-size="11" font-weight="700" fill="#E9CCD3" letter-spacing="2.5">
        ✦ SOFTWARE ENGINEER ✦
      </text>
    </g>

    <!-- Main Title: Hewwo! I'm Aneeqa -->
    <g transform="translate(450, 142)">
      <text text-anchor="middle" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, 'Helvetica Neue', sans-serif" font-size="52" font-weight="800" fill="url(#title-grad)" letter-spacing="-0.5" filter="url(#text-glow)">
        Hewwo! I'm Aneeqa
      </text>
    </g>

    <!-- Bottom Decorative Accent -->
    <g transform="translate(450, 178)">
      <line x1="-120" y1="0" x2="120" y2="0" stroke="url(#accent-grad)" stroke-width="2" stroke-linecap="round" />
      <polygon points="0,-4 5,0 0,4 -5,0" fill="#B199DB" />
    </g>

    <!-- Subtitle Quote -->
    <g transform="translate(450, 206)">
      <text text-anchor="middle" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif" font-size="13" font-weight="500" fill="#B199DB" letter-spacing="1" opacity="0.9">
        Building software with curiosity, precision &amp; elegance
      </text>
    </g>
  </g>
</svg>
"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Successfully updated {out_path}")

if __name__ == "__main__":
    generate_hero_banner()
