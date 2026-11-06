
from pathlib import Path
from html import escape

OUTPUT = Path("skills-3d-contrib.svg")

skills = [
    ("Advanced Excel", 95, "#22c55e"),
    ("SQL", 75, "#38bdf8"),
    ("Power BI", 70, "#facc15"),
    ("VBA", 85, "#a78bfa"),
    ("Power Query", 85, "#fb923c"),
    ("Python", 55, "#60a5fa"),
    ("ETL & Data Modeling", 65, "#f472b6"),
    ("Git & GitHub", 50, "#94a3b8"),
]

width, height = 1100, 570
parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" '
    f'width="{width}" height="{height}" '
    f'viewBox="0 0 {width} {height}">',
    """
    <defs>
      <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#111827"/>
        <stop offset="100%" stop-color="#020617"/>
      </linearGradient>
      <filter id="shadow" x="-30%" y="-30%" width="160%" height="180%">
        <feGaussianBlur stdDeviation="7"/>
      </filter>
    </defs>
    <rect width="1100" height="570" rx="24" fill="url(#bg)"/>
    <text x="55" y="65" fill="#f8fafc"
      font-size="30" font-family="Arial" font-weight="bold">
      MY DATA &amp; ANALYTICS SKILLS
    </text>
    <text x="57" y="96" fill="#94a3b8"
      font-size="15" font-family="Arial">
      Technology stack • Learning and development
    </text>
    """,
]

# Draw a subtle background grid.
for x in range(60, 1080, 40):
    parts.append(
        f'<path d="M{x} 125 V510" stroke="#334155" '
        'stroke-opacity=".18"/>'
    )

for i, (name, score, color) in enumerate(skills):
    x = 75 + (i % 2) * 510
    y = 145 + (i // 2) * 94
    bar_width = 390
    filled = bar_width * score / 100

    parts.append(f"""
    <g>
      <rect x="{x}" y="{y + 8}" width="430" height="66"
        rx="12" fill="#000000" opacity=".35"
        filter="url(#shadow)"/>
      <rect x="{x}" y="{y}" width="430" height="66"
        rx="12" fill="#1e293b" stroke="#334155"/>
      <text x="{x + 18}" y="{y + 26}" fill="#f8fafc"
        font-family="Arial" font-size="17" font-weight="bold">
        {escape(name)}
      </text>
      <text x="{x + 410}" y="{y + 26}" fill="{color}"
        font-family="Arial" font-size="15" text-anchor="end">
        {score}%
      </text>
      <rect x="{x + 18}" y="{y + 40}" width="{bar_width}"
        height="9" rx="4.5" fill="#334155"/>
      <rect x="{x + 18}" y="{y + 40}" width="{filled:.1f}"
        height="9" rx="4.5" fill="{color}"/>
    </g>
    """)

parts.append("""
  <text x="55" y="535" fill="#64748b"
    font-family="Arial" font-size="13">
    Kishor G • Data Analytics &amp; Engineering
  </text>
</svg>
""")

OUTPUT.write_text("\n".join(parts), encoding="utf-8")
print(f"Successfully generated {OUTPUT}")
