#!/usr/bin/env python3
"""
sameness_check.py: the never-repeat quotas and the Pattern Ledger check (ninth amendment, 2026-09-24,
references/sameness_review.md). Runs IN ADDITION to check_novelty.py, never instead of it.

Usage:
  python3 sameness_check.py registry.json proposed.json [--claims claims.json] [--patterns patterns.json]
                            [--builds builds_dir] [--copy copy_fingerprint.json] [--allow tag,tag]
  python3 sameness_check.py --template > proposed_sameness.json

registry.json  the finalshot-registry file ({"builds": [...]} or a list), every entry counts, forever.
claims.json    builds in flight ({"claims": [...]} or a list); every claim counts exactly like a logged build.
patterns.json  the Pattern Ledger ({"tags": {"<tag>": ["slug", ...]}}); a tag on the ledger is banned.
builds_dir     finalshot-registry/builds/, read for each build's copy_fingerprint.json and vibe.json.
proposed.json  the NEW build's candidate choices: the registry schema fields plus
               "patterns" (list of tags), "hero_composition", "seal_form", "feature_shape".
copy_fingerprint.json  the new build's fingerprint from copy_fingerprint.py (checked when given).

Exit code 0 = every check clears. Exit code 1 = at least one FAIL, each printed with the build it
collides with and the overlap, so the fix is specific. A missing field is a FAIL, never a skip.

Checks (numbered after the seventeen in build_registry.md):
 18 heading font never repeated            19 body font never repeated
 20 archetype family AND cast never repeated  21 hero composition never repeated
 22 nav mechanism not a near match          23 button mechanism not a near match
 24 loader mechanism not a near match       25 motif kind not a near match
 26 seal form never repeated                27 accent hue family never repeated
 28 color story never repeated              29 voice stance never repeated
 30 feature shape never repeated            31 typographic set piece not a near match
 32 signature object not a near match       33 no pattern tag on the ledger or in any build or claim
 34 no copy tag shared with any logged fingerprint   35 no headline, CTA, section name or blog title a near duplicate
Near match = content word overlap (Jaccard) at or above 0.45 after the style stoplist; the overlapping
words are printed so a human can confirm. The conventions floor tags (--allow, plus the built-in list)
never count.
"""
import json, os, re, sys

FLOOR_TAGS = {
    "nav.logo-top-left", "nav.horizontal-desktop", "nav.cart-top-right", "nav.sticky",
    "footer.address-block", "footer.sms-block", "checkout.standard", "cta.one-primary-per-screen",
    "buy.product-cart-checkout-confirmation", "form.submit-on-enter", "copy.cta.exempt",
}
STOP = set("a an the and or of to in on for with by at from as is are was were be it its this that these those your you we our us their they them into onto per one two three four five six over under up down out off then than when while where which who whom whose what how all any each every both few more most other some such no nor not only own same so too very can will just should now".split())
STYLE_STOP = set("hover press click scroll label labels link links top left right bottom cart wordmark active idle button buttons nav header row rows bar fill fills line lines px percent page pages site brand colour color text type sans serif mono font weight size small large full width height radius border edge edges shadow soft slow fast base duration second seconds ms state states desktop mobile phone touch viewport hero home plans pricing checkout".split())
FIELDS_NEVER = [
    ("18 heading font never repeated", "heading_font"),
    ("26 seal form never repeated", "seal_form"),
    ("27 accent hue family never repeated", ("palette", "accent_hue_family")),
    ("28 color story never repeated", ("palette", "color_story")),
    ("29 voice stance never repeated", "voice_stance"),
    ("30 feature shape never repeated", "feature_shape"),
]
FIELDS_NEAR = [
    ("21 hero composition never repeated (near match)", "hero_composition"),
    ("22 nav mechanism not a near match", "nav_style"),
    ("23 button mechanism not a near match", "button_style"),
    ("24 loader mechanism not a near match", "loader_transition"),
    ("25 motif kind not a near match", "motif"),
    ("31 typographic set piece not a near match", "typographic_set_piece"),
    ("32 signature object not a near match", ("signature_world", "object")),
]
NEAR = 0.45
DUP = 0.6

TEMPLATE = {
  "slug": "", "brand": "", "heading_font": "", "body_font": "", "archetype": "", "hero_composition": "",
  "nav_style": "", "button_style": "", "loader_transition": "", "motif": "", "seal_form": "",
  "typographic_set_piece": "", "signature_world": {"object": "", "camera_path": ""},
  "palette": {"field": "", "accent_hue_family": "", "color_story": ""},
  "voice_stance": "", "interactive_feature": "", "feature_shape": "",
  "patterns": ["hero.<mechanism>", "nav.<mechanism>", "button.<mechanism>", "loader.<mechanism>", "type.<mechanism>",
               "motion.<idiom>", "object.<grammar>", "motif.<kind>", "seal.<form>", "section.<rhythm>", "color.<structure>",
               "feature.<idiom>", "voice.<family>"],
}

def norm(v): return re.sub(r"\s+", " ", str(v or "")).strip().lower()

def get(entry, key):
    if isinstance(key, tuple):
        cur = entry
        for k in key:
            cur = (cur or {}).get(k) if isinstance(cur, dict) else None
        return cur
    return entry.get(key)

def family(archetype):
    s = norm(archetype)
    s = re.split(r"\s*(\(|, cast as|cast as| as the )", s)[0]
    return s.strip(" ,")

def primary_font(v):
    s = norm(v)
    return re.split(r"\s*(\(| with | for | plus |;|,)", s)[0].strip()

def cwords(s):
    return {w for w in re.findall(r"[a-z][a-z'\-]+", norm(s)) if w not in STOP and w not in STYLE_STOP and len(w) > 2}

def jaccard(a, b):
    if not a or not b: return 0.0, set()
    inter = a & b
    return len(inter) / len(a | b), inter

def label(b):
    return b.get("slug") or b.get("brand") or b.get("domain") or "?"

def load_list(path, key):
    if not path: return []
    d = json.load(open(path))
    if isinstance(d, dict): return d.get(key, d.get("builds", []))
    return d

def main():
    if "--template" in sys.argv:
        print(json.dumps(TEMPLATE, indent=2)); return 0
    if len(sys.argv) < 3:
        print(__doc__); return 1
    args = sys.argv[1:]
    def opt(name):
        return args[args.index(name) + 1] if name in args else None
    builds = load_list(args[0], "builds")
    p = json.load(open(args[1]))
    claims = load_list(opt("--claims"), "claims")
    ledger = json.load(open(opt("--patterns"))) if opt("--patterns") else {"tags": {}}
    builds_dir = opt("--builds")
    fp = json.load(open(opt("--copy"))) if opt("--copy") and opt("--copy") != "none" else None
    allow = FLOOR_TAGS | set((opt("--allow") or "").split(",")) - {""}
    history = [dict(b, _kind="build") for b in builds] + [dict(c, _kind="claim") for c in claims]
    myslug = norm(p.get("slug"))
    history = [h for h in history if norm(h.get("slug")) != myslug or not myslug]

    results = []
    def check(name, ok, detail): results.append((name, ok, detail))
    def need(path, val):
        if val in ("", [], None, {}):
            check(path, False, f"missing field '{path}' in proposed.json (a sparse spec cannot dodge a check)"); return False
        return True

    # 18, 26..30: exact never-repeat across all builds and claims
    for name, key in FIELDS_NEVER:
        val = norm(get(p, key))
        if need(key if isinstance(key, str) else ".".join(key), val):
            hits = [label(h) for h in history if norm(get(h, key)) == val]
            check(name, not hits, f"'{val}'" + (f" already used by {hits}" if hits else ""))
    # 19 body font (primary face)
    bf = primary_font(p.get("body_font"))
    if need("body_font", bf):
        hits = [label(h) for h in history if primary_font(h.get("body_font")) == bf]
        check("19 body font never repeated", not hits, f"'{bf}'" + (f" already used by {hits}" if hits else ""))
    # 20 archetype family and cast
    arch = norm(p.get("archetype"))
    if need("archetype", arch):
        fam = family(arch)
        fam_hits = [label(h) for h in history if family(h.get("archetype")) == fam]
        cast_hits = [label(h) for h in history if norm(h.get("archetype")) == arch]
        check("20a archetype family never repeated (invent one when the catalog is spent)", not fam_hits, f"'{fam}'" + (f" already used by {fam_hits}" if fam_hits else ""))
        check("20b archetype cast never repeated", not cast_hits, f"'{arch[:80]}'" + (f" already used by {cast_hits}" if cast_hits else ""))
    # 21..25, 31, 32: near match on the mechanism description
    for name, key in FIELDS_NEAR:
        val = get(p, key)
        if need(key if isinstance(key, str) else ".".join(key), norm(val)):
            mine = cwords(val); worst = (0.0, set(), None)
            for h in history:
                sim, inter = jaccard(mine, cwords(get(h, key)))
                if sim > worst[0]: worst = (sim, inter, label(h))
            ok = worst[0] < NEAR
            check(name, ok, f"closest {worst[2]} at {worst[0]:.2f}" + ("" if ok else f", shared: {sorted(worst[1])}"))
    # 33 pattern tags
    tags = [norm(t) for t in (p.get("patterns") or [])]
    if need("patterns", tags):
        banned = {}
        for t, slugs in (ledger.get("tags") or {}).items(): banned.setdefault(norm(t), set()).update(slugs)
        for h in history:
            for t in (h.get("patterns") or []): banned.setdefault(norm(t), set()).add(label(h))
        if builds_dir and os.path.isdir(builds_dir):
            for slug in os.listdir(builds_dir):
                vj = os.path.join(builds_dir, slug, "vibe.json")
                if os.path.exists(vj):
                    try:
                        for t in (json.load(open(vj)).get("patterns") or []): banned.setdefault(norm(t), set()).add(slug)
                    except Exception: pass
        me = {myslug, norm(p.get("brand")).replace(" ", "-")}
        def slugify(x): return norm(x).replace(" ", "-")
        banned = {t: {slugify(x) for x in v} - me for t, v in banned.items()}
        hits = {t: sorted(banned[t]) for t in tags if t in banned and banned[t] and t not in allow}
        placeholder = [t for t in tags if "<" in t]
        check("33 no pattern tag on the ledger, in a build or in a claim", not hits and not placeholder,
              (f"collisions: {hits}" if hits else "") + (f" placeholders left: {placeholder}" if placeholder else "") or f"{len(tags)} tags, all new")
    # 34, 35 copy
    if fp:
        logged = []
        if builds_dir and os.path.isdir(builds_dir):
            for slug in sorted(os.listdir(builds_dir)):
                cj = os.path.join(builds_dir, slug, "copy_fingerprint.json")
                if os.path.exists(cj) and slug != myslug:
                    try: logged.append((slug, json.load(open(cj))))
                    except Exception: pass
        for h in history:
            if isinstance(h.get("copy_fingerprint"), dict): logged.append((label(h), h["copy_fingerprint"]))
        mytags = set(norm(t) for t in fp.get("tags") or []) - allow
        hits = {}
        for slug, lf in logged:
            shared = mytags & set(norm(t) for t in lf.get("tags") or [])
            if shared: hits[slug] = sorted(shared)
        check("34 no copy tag shared with any logged fingerprint", not hits, f"collisions: {hits}" if hits else f"{len(mytags)} copy tags vs {len(logged)} fingerprints, all clear")
        mine_lines = [x for x in ([fp.get("h1") or ""] + [h["text"] for h in fp.get("headlines") or []] + (fp.get("ctas") or []) + (fp.get("section_names") or []) + [b["text"] for b in fp.get("blog_titles") or []]) if x]
        dups = []
        for slug, lf in logged:
            theirs = [x for x in ([lf.get("h1") or ""] + [h["text"] for h in lf.get("headlines") or []] + (lf.get("ctas") or []) + (lf.get("section_names") or []) + [b["text"] for b in lf.get("blog_titles") or []]) if x]
            for a in mine_lines:
                wa = cwords(a)
                if len(wa) < 2: continue
                for b in theirs:
                    sim, inter = jaccard(wa, cwords(b))
                    if sim >= DUP and norm(a) not in ("purchase the household plan",) and norm(a) not in {t for t in FLOOR_TAGS}:
                        dups.append((slug, a, b, round(sim, 2)))
        check("35 no headline, CTA, section name or blog title a near duplicate", not dups, f"{dups[:6]}" if dups else "no near duplicates")
    elif opt("--copy") != "none":
        check("34/35 copy fingerprint", False, "no --copy copy_fingerprint.json given; run copy_fingerprint.py first (required at Step 3 and Gate 5; at Step 2.5 pass --copy none)")

    fails = [r for r in results if not r[1]]
    print(f"\n=== Sameness check vs {len(builds)} logged build(s) + {len(claims)} claim(s), {len((ledger.get('tags') or {}))} ledger tags ===")
    for name, ok, detail in results:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}   ({detail})")
    print(f"\nVERDICT: {'ALL SAMENESS CHECKS CLEAR' if not fails else str(len(fails)) + ' CHECK(S) FAILING: fix before committing the direction'}")
    return 0 if not fails else 1

if __name__ == "__main__":
    sys.exit(main())
