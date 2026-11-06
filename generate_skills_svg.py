# Animated isometric skills dashboard for the GitHub profile README.
import math

skills = [
    ("Excel", 85, "#22c55e"),
    ("Power BI", 55, "#f59e0b"),
    ("SQL", 40, "#38bdf8"),
    ("Python", 40, "#facc15"),
    ("Tableau", 35, "#fb7185"),
    ("Pandas", 35, "#a78bfa"),
    ("ETL", 30, "#2dd4bf"),
]

def tag(v):
    return "STRONG" if v >= 75 else ("MID" if v >= 50 else "LEARNING")

def shade(hexc, f):
    h = hexc.lstrip("#")
    r, g, b = [int(h[i:i+2], 16) for i in (0, 2, 4)]
    r, g, b = min(255, int(r*f)), min(255, int(g*f)), min(255, int(b*f))
    return "#%02x%02x%02x" % (r, g, b)

W, H = 1280, 850
ox, oy = 360, 200
a = 24
b = a * math.tan(math.radians(30))
COLS = 20
DJ = 1.5

def P(i, j, h=0):
    jj = j * DJ
    return (ox + (i-jj)*a, oy + (i+jj)*b-h)

def pts(*ps):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in ps)

o = []
o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Fira Code, Consolas, Menlo, monospace">')
o.append("""<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#03050b"/><stop offset="0.6" stop-color="#081420"/><stop offset="1" stop-color="#04070d"/></linearGradient>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#0f2a3a" stroke-width="0.6" opacity="0.55"/></pattern>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#00f7ff" stop-opacity="0"/><stop offset="1" stop-color="#00f7ff" stop-opacity="0.35"/></linearGradient>
</defs>
<style>
.t{animation:rise .7s cubic-bezier(.2,.9,.2,1) both}
@keyframes rise{from{transform:scaleY(0);opacity:0}to{transform:scaleY(1);opacity:1}}
.fade{animation:fade 1.2s ease both}
@keyframes fade{from{opacity:0}to{opacity:1}}
.spin{animation:spin 6s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.blink{animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
.pulse{animation:pulse 2.2s ease-in-out infinite}
@keyframes pulse{0%,100%{opacity:.35}50%{opacity:1}}
.rad{animation:radin 1.4s .4s cubic-bezier(.2,.9,.2,1) both}
@keyframes radin{from{transform:scale(0)}to{transform:scale(1)}}
</style>""")
o.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
o.append(f'<rect width="{W}" height="{H}" fill="url(#grid)"/>')

for x, y, sx, sy in [(20,20,1,1),(W-20,20,-1,1),(20,H-20,1,-1),(W-20,H-20,-1,-1)]:
    o.append(f'<path d="M{x},{y+sy*28} L{x},{y} L{x+sx*28},{y}" fill="none" stroke="#00f7ff" stroke-width="2" opacity="0.7"/>')

o.append('<text x="60" y="78" fill="#00f7ff" font-size="30" font-weight="700" filter="url(#glow)">&gt; skills.scan()<tspan class="blink" fill="#00f7ff">_</tspan></text>')
o.append('<text x="60" y="108" fill="#6b8ba3" font-size="15">// Kishor G · Data Analytics &amp; Engineering · skill levels</text>')
o.append('<text x="60" y="132" fill="#3f5a6e" font-size="13">status: <tspan fill="#22c55e">LEARNING</tspan> · build: <tspan fill="#facc15">in progress</tspan> · every tile = 5%</text>')

tiles = []
for j, (name, val, col) in enumerate(skills):
    n = round(val/5)
    maxh = val * 0.95
    for i in range(COLS):
        filled = i < n
        if filled:
            k = i / max(n-1, 1)
            h = 5 + (k**1.7) * (maxh-5)
            light = 0.78 + 0.42*k
            top, left, right = shade(col, light), shade(col, light*0.52), shade(col, light*0.74)
        else:
            h, top, left, right = 2, "#1a2431", "#0e151e", "#131c27"
        tiles.append((i+j, j, i, h, top, left, right, filled, k if filled else 0, name, val, col, n))
tiles.sort(key=lambda t: (t[0], t[1]))

g = 0.07
for s, j, i, h, top, left, right, filled, k, name, val, col, n in tiles:
    A, B, C, D = P(i+g,j+g,h), P(i+1-g,j+g,h), P(i+1-g,j+1-g,h), P(i+g,j+1-g,h)
    B0, C0, D0 = P(i+1-g,j+g), P(i+1-g,j+1-g), P(i+g,j+1-g)
    bx, by = P(i+.5,j+.5)
    delay = i*0.045+j*0.10
    o.append(f'<g class="t" style="transform-origin:{bx:.1f}px {by:.1f}px;animation-delay:{delay:.2f}s"><polygon points="{pts(D,C,C0,D0)}" fill="{left}"/><polygon points="{pts(B,C,C0,B0)}" fill="{right}"/><polygon points="{pts(A,B,C,D)}" fill="{top}"/></g>')

for j, (name, val, col) in enumerate(skills):
    n = round(val/5)
    maxh = val * 0.95
    lx, ly = P(-0.4, j+0.5)
    o.append(f'<text x="{lx-8:.1f}" y="{ly+5:.1f}" text-anchor="end" fill="#e6edf3" font-size="15" font-weight="700">{name}</text>')
    tx, ty = P(n-0.5, j+0.5, maxh)
    o.append(f'<ellipse class="pulse" cx="{tx:.1f}" cy="{ty:.1f}" rx="20" ry="11" fill="{col}" opacity="0.45" filter="url(#glow)"/>')
    ex, ey = P(COLS+0.6, j+0.5)
    o.append(f'<g class="fade" style="animation-delay:{1.0+j*0.1:.1f}s"><line x1="{ex-14:.1f}" y1="{ey:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{col}" stroke-dasharray="2 3" opacity="0.7"/><text x="{ex+6:.1f}" y="{ey+6:.1f}" fill="{col}" font-size="20" font-weight="800">{val}%</text><text x="{ex+62:.1f}" y="{ey+5:.1f}" fill="#6b8ba3" font-size="11" letter-spacing="1">{tag(val)}</text></g>')

cx, cy, R = 1020, 285, 120
N = len(skills)
def rp(idx, frac):
    ang = -math.pi/2 + idx*2*math.pi/N
    return (cx+R*frac*math.cos(ang), cy+R*frac*math.sin(ang))

o.append(f'<text x="{cx}" y="{cy-R-62}" text-anchor="middle" fill="#00f7ff" font-size="15" font-weight="700" letter-spacing="2">SKILL RADAR</text>')
for ring in (0.25, 0.5, 0.75, 1.0):
    pl = [rp(i, ring) for i in range(N)]
    o.append(f'<polygon points="{pts(*pl)}" fill="none" stroke="#2b4a5c" stroke-dasharray="4 4" stroke-width="1"/>')
    o.append(f'<text x="{cx+4}" y="{cy-R*ring-2:.1f}" fill="#4f6b7d" font-size="10">{int(ring*100)}</text>')

for i, (name, val, col) in enumerate(skills):
    x, y = rp(i, 1.0)
    o.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#2b4a5c" stroke-dasharray="4 4"/>')
    lx, ly = rp(i, 1.24)
    anc = "start" if lx > cx+10 else ("end" if lx < cx-10 else "middle")
    o.append(f'<text x="{lx:.1f}" y="{ly+4:.1f}" text-anchor="{anc}" fill="{col}" font-size="13" font-weight="700">{name}</text>')

poly = [rp(i, v/100) for i, (n_, v, c) in enumerate(skills)]
o.append(f'<g class="rad" style="transform-origin:{cx}px {cy}px"><polygon points="{pts(*poly)}" fill="#00f7ff" fill-opacity="0.22" stroke="#00f7ff" stroke-width="2.5" filter="url(#glow)"/>')
for (x, y), (n_, v, c) in zip(poly, skills):
    o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{c}" stroke="#03050b" stroke-width="1.5"/>')
o.append('</g>')

o.append(f'<g class="spin" style="transform-origin:{cx}px {cy}px"><path d="M{cx},{cy} L{cx+R*1.05},{cy} A{R*1.05},{R*1.05} 0 0 0 {cx+R*1.05*math.cos(-0.55):.1f},{cy+R*1.05*math.sin(-0.55):.1f} Z" fill="url(#sweep)"/><line x1="{cx}" y1="{cy}" x2="{cx+R*1.05}" y2="{cy}" stroke="#00f7ff" stroke-width="1.5" opacity="0.8"/></g>')

dx, dy, ro, ri = 930, 690, 72, 42
cats = [("Analytics &amp; BI",3,"#22c55e"),("Programming",3,"#38bdf8"),("Data Engineering",1,"#a78bfa")]
tot = sum(c[1] for c in cats)
o.append(f'<text x="{dx-ro}" y="{dy-ro-22}" fill="#00f7ff" font-size="15" font-weight="700" letter-spacing="2">STACK MIX</text>')
ang = -math.pi/2
for name, cnt, col in cats:
    sweep = 2*math.pi*cnt/tot
    a1, a2 = ang, ang+sweep-0.04
    x1,y1 = dx+ro*math.cos(a1), dy+ro*math.sin(a1)
    x2,y2 = dx+ro*math.cos(a2), dy+ro*math.sin(a2)
    x3,y3 = dx+ri*math.cos(a2), dy+ri*math.sin(a2)
    x4,y4 = dx+ri*math.cos(a1), dy+ri*math.sin(a1)
    lg = 1 if (a2-a1) > math.pi else 0
    o.append(f'<path class="fade" d="M{x1:.1f},{y1:.1f} A{ro},{ro} 0 {lg} 1 {x2:.1f},{y2:.1f} L{x3:.1f},{y3:.1f} A{ri},{ri} 0 {lg} 0 {x4:.1f},{y4:.1f} Z" fill="{col}" stroke="#03050b" stroke-width="2"/>')
    ang += sweep

o.append(f'<text x="{dx}" y="{dy+2}" text-anchor="middle" fill="#e6edf3" font-size="26" font-weight="800">{tot}</text><text x="{dx}" y="{dy+20}" text-anchor="middle" fill="#6b8ba3" font-size="10" letter-spacing="1">SKILLS</text>')
ly0 = dy-34
for k, (name, cnt, col) in enumerate(cats):
    y = ly0+k*30
    o.append(f'<rect x="{dx+ro+30}" y="{y}" width="16" height="16" fill="{col}"/><text x="{dx+ro+54}" y="{y+13}" fill="#e6edf3" font-size="15">{name}</text>')

o.append('<text x="60" y="815" fill="#64748b" font-size="13">Kishor G · Data Analytics &amp; Engineering · 7 skills tracked</text>')
o.append('<text x="1240" y="40" text-anchor="end" fill="#4f6b7d" font-size="14">scan: generated on commit</text>')
o.append('</svg>')

with open("skills-3d-contrib.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(o))
print("Successfully generated skills-3d-contrib.svg")
