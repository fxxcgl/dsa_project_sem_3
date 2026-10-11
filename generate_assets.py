import os

svgs = {
    'thumb-dark-circle': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#0d0f12"/>
  <circle cx="100" cy="100" r="70" fill="none" stroke="#2a2e39" stroke-width="2" stroke-dasharray="4 4"/>
  <circle cx="100" cy="100" r="54" fill="none" stroke="#ffffff" stroke-width="3"/>
  <path d="M100 46 A54 54 0 0 1 154 100" fill="none" stroke="#6366f1" stroke-width="4" stroke-linecap="round"/>
  <polygon points="154,94 162,102 148,105" fill="#6366f1"/>
  <circle cx="100" cy="100" r="8" fill="#ffffff"/>
  <text x="100" y="180" text-anchor="middle" fill="#64748b" font-size="11" font-family="sans-serif" font-weight="600" letter-spacing="1">CALC • SAMPLE</text>
</svg>""",

    'thumb-sculpture': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <defs>
    <linearGradient id="sculpGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="50%" stop-color="#e2e8f0"/>
      <stop offset="100%" stop-color="#94a3b8"/>
    </linearGradient>
    <radialGradient id="sculpLight" cx="40%" cy="35%" r="60%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="70%" stop-color="#cbd5e1"/>
      <stop offset="100%" stop-color="#64748b"/>
    </radialGradient>
  </defs>
  <rect width="200" height="200" fill="#eef2f6"/>
  <ellipse cx="100" cy="155" rx="60" ry="16" fill="#cbd5e1" opacity="0.6"/>
  <path d="M60 90 L60 145 C60 160 140 160 140 145 L140 90 Z" fill="url(#sculpGrad)"/>
  <ellipse cx="100" cy="90" rx="40" ry="16" fill="url(#sculpLight)"/>
  <circle cx="100" cy="65" r="22" fill="url(#sculpLight)"/>
</svg>""",

    'thumb-feather': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <defs>
    <linearGradient id="feath" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#22c55e"/>
      <stop offset="35%" stop-color="#84cc16"/>
      <stop offset="65%" stop-color="#eab308"/>
      <stop offset="90%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>
  </defs>
  <rect width="200" height="200" fill="#0f172a"/>
  <g transform="rotate(-20 100 100)">
    <path d="M100 20 C140 60 150 140 100 185 C50 140 60 60 100 20 Z" fill="url(#feath)"/>
    <line x1="100" y1="20" x2="100" y2="185" stroke="#ffffff" stroke-width="3" stroke-linecap="round" opacity="0.8"/>
    <path d="M100 50 Q130 55 140 70 M100 70 Q135 78 142 95 M100 90 Q135 100 140 120 M100 110 Q130 120 135 140" stroke="#ffffff" stroke-width="1.5" fill="none" opacity="0.4"/>
    <path d="M100 50 Q70 55 60 70 M100 70 Q65 78 58 95 M100 90 Q65 100 60 120 M100 110 Q70 120 65 140" stroke="#ffffff" stroke-width="1.5" fill="none" opacity="0.4"/>
  </g>
</svg>""",

    'thumb-moss': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#143818"/>
  <circle cx="50" cy="60" r="38" fill="#225424"/>
  <circle cx="140" cy="55" r="44" fill="#1c4a20"/>
  <circle cx="90" cy="110" r="52" fill="#2f6832"/>
  <circle cx="150" cy="135" r="40" fill="#3a7d3e"/>
  <circle cx="40" cy="145" r="35" fill="#255c28"/>
  <circle cx="85" cy="95" r="30" fill="#4d9e52"/>
  <circle cx="130" cy="105" r="25" fill="#62b568"/>
  <circle cx="65" cy="135" r="20" fill="#7acc80"/>
  <circle cx="90" cy="80" r="3" fill="#bbf7d0"/>
  <circle cx="115" cy="95" r="2" fill="#86efac"/>
  <circle cx="75" cy="115" r="3" fill="#bbf7d0"/>
  <circle cx="140" cy="125" r="2.5" fill="#86efac"/>
</svg>""",

    'thumb-landscape': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="70%" stop-color="#bae6fd"/>
      <stop offset="100%" stop-color="#f0f9ff"/>
    </linearGradient>
    <linearGradient id="hill" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#65a30d"/>
      <stop offset="100%" stop-color="#365314"/>
    </linearGradient>
  </defs>
  <rect width="200" height="200" fill="url(#sky)"/>
  <path d="M40 70 Q55 55 75 65 Q90 50 115 60 Q130 55 140 70 Z" fill="#ffffff" opacity="0.9"/>
  <path d="M110 90 Q125 80 145 85 Q160 75 175 88 Z" fill="#ffffff" opacity="0.85"/>
  <path d="M0 130 Q70 100 130 120 Q170 135 200 115 L200 200 L0 200 Z" fill="url(#hill)"/>
  <path d="M0 155 Q60 135 120 150 Q180 165 200 145 L200 200 L0 200 Z" fill="#4d7c0f"/>
</svg>""",

    'thumb-cyan-swirl': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <defs>
    <linearGradient id="swirl" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="40%" stop-color="#3b82f6"/>
      <stop offset="75%" stop-color="#eab308"/>
      <stop offset="100%" stop-color="#10b981"/>
    </linearGradient>
  </defs>
  <rect width="200" height="200" fill="#f8fafc"/>
  <path d="M50 40 C110 20 160 70 140 120 C120 170 60 160 50 120 C40 80 140 60 150 140" fill="none" stroke="url(#swirl)" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="100" cy="100" r="12" fill="#0284c7" opacity="0.8"/>
</svg>""",

    'thumb-amber-bottle': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <defs>
    <radialGradient id="amber" cx="50%" cy="55%" r="50%">
      <stop offset="0%" stop-color="#fde047"/>
      <stop offset="50%" stop-color="#d97706"/>
      <stop offset="90%" stop-color="#78350f"/>
    </radialGradient>
  </defs>
  <rect width="200" height="200" fill="#fffbeb"/>
  <rect x="82" y="28" width="36" height="28" rx="4" fill="#1e293b"/>
  <rect x="75" y="54" width="50" height="8" rx="2" fill="#0f172a"/>
  <path d="M88 62 L88 78 L55 96 C48 100 45 110 45 125 L45 155 C45 168 55 178 70 178 L130 178 C145 178 155 168 155 155 L155 125 C155 110 152 100 145 96 L112 78 L112 62 Z" fill="url(#amber)" stroke="#92400e" stroke-width="2"/>
  <circle cx="80" cy="130" r="8" fill="#fef08a" opacity="0.7"/>
  <circle cx="110" cy="145" r="12" fill="#fde047" opacity="0.6"/>
  <circle cx="95" cy="160" r="5" fill="#ffffff" opacity="0.8"/>
</svg>""",

    'thumb-mountain': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <defs>
    <linearGradient id="mtnSky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="70%" stop-color="#7dd3fc"/>
      <stop offset="100%" stop-color="#fed7aa"/>
    </linearGradient>
  </defs>
  <rect width="200" height="200" fill="url(#mtnSky)"/>
  <polygon points="100,45 160,165 40,165" fill="#475569"/>
  <polygon points="100,45 118,85 100,105 82,85" fill="#ffffff"/>
  <polygon points="145,95 190,175 100,175" fill="#334155"/>
  <polygon points="145,95 160,125 145,140 132,120" fill="#f1f5f9"/>
  <polygon points="55,110 95,180 15,180" fill="#64748b"/>
  <ellipse cx="100" cy="145" rx="70" ry="12" fill="#ffffff" opacity="0.6"/>
</svg>""",

    'thumb-cream': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <defs>
    <linearGradient id="creamGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="60%" stop-color="#f1f5f9"/>
      <stop offset="100%" stop-color="#cbd5e1"/>
    </linearGradient>
  </defs>
  <rect width="200" height="200" fill="#e2e8f0"/>
  <path d="M40 130 C60 100 110 80 155 105 C140 125 110 145 65 142 Z" fill="url(#creamGrad)"/>
  <path d="M65 115 C90 90 140 85 160 110 C130 115 100 125 75 130 Z" fill="#ffffff"/>
  <ellipse cx="100" cy="150" rx="55" ry="10" fill="#94a3b8" opacity="0.35"/>
</svg>""",

    'thumb-poppy': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#090a0f"/>
  <path d="M100 110 Q98 150 102 200" stroke="#15803d" stroke-width="4" fill="none"/>
  <ellipse cx="85" cy="95" rx="28" ry="36" transform="rotate(-25 85 95)" fill="#dc2626"/>
  <ellipse cx="115" cy="95" rx="28" ry="36" transform="rotate(25 115 95)" fill="#ef4444"/>
  <ellipse cx="100" cy="80" rx="34" ry="26" fill="#b91c1c"/>
  <ellipse cx="100" cy="110" rx="32" ry="22" fill="#f87171"/>
  <circle cx="100" cy="98" r="10" fill="#1e293b"/>
  <circle cx="100" cy="98" r="6" fill="#020617"/>
</svg>""",

    'thumb-skeleton-leaf': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#fafaf9"/>
  <g transform="rotate(35 100 100)">
    <path d="M100 30 C150 70 150 130 100 170 C50 130 50 70 100 30 Z" fill="none" stroke="#b45309" stroke-width="2" stroke-dasharray="3 3"/>
    <line x1="100" y1="30" x2="100" y2="170" stroke="#d97706" stroke-width="2"/>
    <path d="M100 60 L125 75 M100 80 L135 100 M100 100 L138 120 M100 120 L132 140 M100 140 L120 155" stroke="#d97706" stroke-width="1.5" opacity="0.7"/>
    <path d="M100 60 L75 75 M100 80 L65 100 M100 100 L62 120 M100 120 L68 140 M100 140 L80 155" stroke="#d97706" stroke-width="1.5" opacity="0.7"/>
  </g>
</svg>"""
}

os.makedirs('frontend/assets', exist_ok=True)
for k, v in svgs.items():
    with open(f'frontend/assets/{k}.svg', 'w', encoding='utf-8') as f:
        f.write(v)

print(f"Generated {len(svgs)} SVG files successfully in frontend/assets/.")
