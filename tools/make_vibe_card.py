#!/usr/bin/env python3
"""
make_vibe_card.py: build a build's one page vibe card from its vibe.json (ninth amendment, 2026-09-24,
references/sameness_review.md).

Usage:
  python3 make_vibe_card.py builds/<slug>/vibe.json [--out builds/<slug>/] [--no-render]
  python3 make_vibe_card.py --template > vibe.json

Writes vibe-card.html next to vibe.json (or into --out) and, when Playwright with Chromium is
available (it is in the Cowork sandbox), vibe-card.jpg at 1600px wide. Screenshot paths in vibe.json
are relative to the vibe.json folder; missing shots render as a labelled empty frame rather than
failing, so a partial card still ships and the gap is visible.

The card is the unit of the Sameness Review: Step 0 opens every previous build's card, and QA Gate 5
puts the new build's card beside each of them.
"""
import base64, html, json, mimetypes, os, sys

TEMPLATE = {
  "slug": "", "brand": "", "domain": "", "date": "", "tier": "", "live_url": "",
  "archetype": "", "heading_font": "", "body_font": "",
  "palette": {"hexes": [], "field": "", "accent_hue_family": "", "color_story": ""},
  "voice_stance": "", "signature_move_category": "", "signature_move_id": "", "governing_idea": "",
  "shots": {"home-1440": "shots/home-1440.jpg", "home-375": "shots/home-375.jpg", "plans-1440": "shots/plans-1440.jpg",
            "about-1440": "shots/about-1440.jpg", "post-1440": "shots/post-1440.jpg", "nav": "shots/nav.jpg", "button": "shots/button.jpg"},
  "speech": {"h1": "", "headlines": [], "ctas": [], "section_names": [], "blog_titles": [], "opening_about": "", "opening_post": ""},
  "patterns": [], "copy_tags": [],
  "brief": {"vibe": "", "hero": "", "type": "", "palette": "", "motion": "", "speech": "", "rhythm": "", "tags": ""},
}

def data_uri(path):
    if not path or not os.path.exists(path): return None
    mt = mimetypes.guess_type(path)[0] or "image/jpeg"
    return f"data:{mt};base64," + base64.b64encode(open(path, "rb").read()).decode("ascii")

def esc(s): return html.escape(str(s or ""))

def shot(base, rel, title, w, h, fit="cover"):
    uri = data_uri(os.path.join(base, rel)) if rel else None
    inner = f'<img src="{uri}" alt="{esc(title)}" style="object-fit:{fit}">' if uri else f'<div class="missing">{esc(title)}<br><small>no capture</small></div>'
    return f'<figure style="width:{w}px"><div class="frame" style="height:{h}px">{inner}</div><figcaption>{esc(title)}</figcaption></figure>'

def build_html(v, base):
    pal = v.get("palette") or {}
    sw = "".join(f'<span class="sw" style="background:#{h.strip("#")}" title="#{h.strip("#")}"></span><code>{esc(h.strip("#"))}</code>' for h in pal.get("hexes") or [])
    sp = v.get("speech") or {}
    br = v.get("brief") or {}
    def li(items): return "".join(f"<li>{esc(x)}</li>" for x in items or []) or "<li class='dim'>none recorded</li>"
    tags = "".join(f'<code class="tag">{esc(t)}</code>' for t in (v.get("patterns") or []) + (v.get("copy_tags") or [])) or "<span class='dim'>none recorded</span>"
    known = {"home-1440", "home-375", "plans-1440", "about-1440", "post-1440", "nav", "button"}
    extras = [(k, r) for k, r in (v.get("shots") or {}).items() if k not in known and r]
    extra_row = ('<div class="row">' + "".join(shot(base, r, k, 420, 228) for k, r in extras[:3]) + "</div>") if extras else ""
    brief_rows = "".join(f"<tr><th>{esc(k)}</th><td>{esc(br.get(k))}</td></tr>" for k in ("vibe", "hero", "type", "palette", "motion", "speech", "rhythm", "tags"))
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{esc(v.get('brand'))} vibe card</title>
<style>
:root{{--ink:#1a1a1a;--paper:#fff;--rule:#d9d9d9;--dim:#777}}
*{{box-sizing:border-box}} body{{margin:0;width:1600px;background:var(--paper);color:var(--ink);font:14px/1.4 system-ui,Segoe UI,Helvetica,Arial,sans-serif}}
header{{padding:24px 32px 12px;border-bottom:2px solid var(--ink);display:flex;gap:32px;align-items:flex-start}}
header h1{{font-size:34px;margin:0 0 4px;font-weight:700}} header .meta{{color:var(--dim);font-size:13px}}
.kv{{display:grid;grid-template-columns:auto 1fr;gap:2px 12px;font-size:13px;margin-top:8px}} .kv b{{font-weight:600}}
.sw{{display:inline-block;width:22px;height:22px;border:1px solid var(--rule);vertical-align:middle;margin:0 2px 0 8px;border-radius:3px}} code{{font:12px/1 ui-monospace,Menlo,monospace}}
.row{{display:flex;gap:16px;padding:16px 32px;border-bottom:1px solid var(--rule);align-items:flex-start}}
figure{{margin:0}} .frame{{border:1px solid var(--rule);background:#f4f4f4;overflow:hidden;display:flex;align-items:flex-start;justify-content:center}}
.frame img{{width:100%;height:100%;object-fit:cover;object-position:top}} figcaption{{font-size:12px;color:var(--dim);margin-top:4px}}
.missing{{padding:24px;color:var(--dim);text-align:center;font-size:13px;align-self:center}}
.cols{{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;padding:16px 32px;border-bottom:1px solid var(--rule)}}
h2{{font-size:13px;text-transform:uppercase;letter-spacing:.08em;color:var(--dim);margin:0 0 6px}} ul{{margin:0;padding-left:18px}} li{{margin:2px 0}} .dim{{color:var(--dim)}}
.h1{{font-size:22px;font-weight:600;margin:0 0 10px}} .tag{{display:inline-block;margin:0 6px 6px 0;padding:3px 6px;border:1px solid var(--rule);border-radius:4px;background:#fafafa}}
table.brief{{border-collapse:collapse;width:100%}} table.brief th{{text-align:left;width:110px;padding:6px 8px;border-top:1px solid var(--rule);vertical-align:top;font-weight:600;text-transform:capitalize}} table.brief td{{padding:6px 8px;border-top:1px solid var(--rule)}}
footer{{padding:10px 32px;color:var(--dim);font-size:12px}}
</style></head><body>
<header>
  <div style="flex:1"><h1>{esc(v.get('brand'))} <span class="meta">{esc(v.get('domain'))} · shipped {esc(v.get('date'))} · tier {esc(v.get('tier'))}</span></h1>
    <div class="meta">{esc(v.get('governing_idea'))}</div>
    <div class="kv"><b>Archetype</b><span>{esc(v.get('archetype'))}</span><b>Type</b><span>{esc(v.get('heading_font'))} with {esc(v.get('body_font'))}</span>
    <b>Palette</b><span>{sw} <span class="dim">{esc(pal.get('field'))} field · accent {esc(pal.get('accent_hue_family'))} · {esc(pal.get('color_story'))}</span></span>
    <b>Voice</b><span>{esc(v.get('voice_stance'))}</span><b>Signature</b><span>{esc(v.get('signature_move_category'))} {esc(v.get('signature_move_id'))}</span><b>Live</b><span>{esc(v.get('live_url'))}</span></div>
  </div>
</header>
<div class="row">
  {shot(base, (v.get('shots') or {}).get('home-1440'), 'Home, first viewport at 1440', 880, 477)}
  {shot(base, (v.get('shots') or {}).get('home-375'), 'Home at 375', 200, 416)}
  {shot(base, (v.get('shots') or {}).get('plans-1440'), 'Plans at 1440', 420, 228)}
</div>
<div class="row">
  {shot(base, (v.get('shots') or {}).get('about-1440'), 'About at 1440', 420, 228)}
  {shot(base, (v.get('shots') or {}).get('post-1440'), 'A blog post at 1440', 420, 228)}
  {shot(base, (v.get('shots') or {}).get('nav'), 'Nav strip', 420, 32, 'contain')}
  {shot(base, (v.get('shots') or {}).get('button'), 'Primary button', 220, 80, 'contain')}
</div>
{extra_row}
<div class="cols">
  <div><h2>H1 and headlines</h2><p class="h1">{esc(sp.get('h1'))}</p><ul>{li(sp.get('headlines'))}</ul></div>
  <div><h2>CTA labels</h2><ul>{li(sp.get('ctas'))}</ul><h2 style="margin-top:12px">Section names</h2><ul>{li(sp.get('section_names'))}</ul></div>
  <div><h2>Blog titles</h2><ul>{li(sp.get('blog_titles'))}</ul></div>
  <div><h2>Opening lines</h2><p><b>About:</b> {esc(sp.get('opening_about'))}</p><p><b>Post:</b> {esc(sp.get('opening_post'))}</p></div>
</div>
<div class="cols" style="grid-template-columns:1fr 1fr">
  <div><h2>Pattern tags (banned for every later build)</h2>{tags}</div>
  <div><h2>The eight line brief</h2><table class="brief">{brief_rows}</table></div>
</div>
<footer>finalshot vibe card · {esc(v.get('slug'))} · generated by make_vibe_card.py</footer>
</body></html>"""

def render(html_path, jpg_path):
    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print("Playwright unavailable, HTML only:", e); return False
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1600, "height": 1000})
        pg.goto("file://" + os.path.abspath(html_path)); pg.wait_for_timeout(300)
        pg.screenshot(path=jpg_path, type="jpeg", quality=82, full_page=True); b.close()
    return True

def main():
    if "--template" in sys.argv:
        print(json.dumps(TEMPLATE, indent=2)); return 0
    if len(sys.argv) < 2:
        print(__doc__); return 1
    src = sys.argv[1]; base = os.path.dirname(os.path.abspath(src))
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else base
    os.makedirs(out, exist_ok=True)
    v = json.load(open(src, encoding="utf-8"))
    hp = os.path.join(out, "vibe-card.html"); jp = os.path.join(out, "vibe-card.jpg")
    open(hp, "w", encoding="utf-8").write(build_html(v, base)); print("wrote", hp)
    if "--no-render" not in sys.argv and render(hp, jp): print("wrote", jp, os.path.getsize(jp), "bytes")
    return 0

if __name__ == "__main__":
    sys.exit(main())
