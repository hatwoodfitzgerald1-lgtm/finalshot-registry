#!/usr/bin/env python3
"""
copy_fingerprint.py: extract the speech structure fingerprint of a build's copy (ninth amendment,
2026-09-24, references/sameness_review.md).

Usage:
  python3 copy_fingerprint.py SITE_COPY.md --out copy_fingerprint.json [--brand "Addabill"]
  python3 copy_fingerprint.py pages_dir/ --out copy_fingerprint.json [--brand "Astroquanta"]

The first form reads the content engine's SITE_COPY.md (labelled lines such as "Hero H1:", "Heading:",
"Primary CTA (fixed):", "#### subhead", "### Post A (how to)" followed by "Title:" or "H1:").
The second form reads a folder of plain text page dumps (home.txt, about.txt, plans.txt, post-*.txt,
as saved from get_page_text on a live site) and infers headings from short lines.

The fingerprint records the H1 and its grammar shape, every headline and its shape, the CTA labels
and their phrasing class, the section names and their naming device, the blog titles and their
format, the opening lines and their shape, the rhetorical devices found, sentence statistics, and a
list of copy.* pattern tags. sameness_check.py compares fingerprints across builds.

Every classification is a plain heuristic and is meant to be stable, not clever: the same text always
produces the same tags, so two builds that share a device are caught the same way every time.
"""
import json, os, re, statistics, sys

IMPERATIVES = {"add", "buy", "purchase", "see", "start", "get", "pick", "choose", "put", "tap", "type", "keep",
               "read", "check", "open", "photograph", "watch", "try", "use", "build", "find", "compare", "let",
               "stop", "drop", "turn", "take", "make", "give", "look", "ask", "send", "save", "pay", "join",
               "learn", "meet", "know", "bring", "hold", "plan", "run", "set", "show", "tell", "walk", "write",
               "charge", "print", "count", "name", "file", "cut", "fold", "stack", "turn", "light", "clear", "sort", "weigh", "empty"}
PURCHASE_VERBS = ("purchase", "buy", "add to cart", "place order", "order", "use the free", "start free",
                  "subscribe", "get the", "choose", "select", "checkout", "go to checkout")
CTA_EXEMPT = {"place order", "add to cart", "checkout", "go to checkout", "continue", "submit", "remove",
              "update cart", "view cart", "back", "next", "cancel", "close"}
STOP = set("a an the and or of to in on for with by at from as is are was were be it its this that these those your you we our us their they them into onto per one".split())
SCENE_WORDS = {"house", "kitchen", "counter", "desk", "morning", "evening", "night", "parking", "car", "office",
               "table", "drawer", "porch", "door", "window", "envelope", "inbox", "shelf", "floor", "lot", "room",
               "somewhere", "tuesday", "monday", "friday", "sunday", "saturday", "wednesday", "thursday", "o'clock", "pm", "am"}
NUMBER_WORDS = "one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty|fifty|sixty|hundred"

def words(s):
    return re.findall(r"[A-Za-z0-9$%'’]+", s)

def content_words(s):
    return {w.lower().strip("'’") for w in words(s) if w.lower() not in STOP and len(w) > 2}

def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(])", text.strip())
    return [p.strip() for p in parts if p.strip()]

def first_word(s):
    w = words(s)
    return w[0].lower() if w else ""

def shape(line):
    """Grammar shape tags for a headline, H1 or opening line."""
    tags = []
    s = line.strip()
    sents = sentences(s)
    n = len(words(s))
    if s.endswith("?"):
        tags.append("question")
    if first_word(s) in IMPERATIVES:
        tags.append("imperative")
    if len(sents) >= 2 and all(len(words(x)) <= 7 for x in sents):
        tags.append("two-short-sentences")
    elif len(sents) >= 2:
        tags.append("multi-sentence")
    if ":" in s and not s.startswith("http"):
        tags.append("colon-setup")
    if re.match(r"^(\d+|%s)\b" % NUMBER_WORDS, s, re.I):
        tags.append("number-led")
    if re.search(r"\b(never|not|isn't|is not|doesn't|does not|won't|no)\b", s, re.I):
        tags.append("negation")
    if re.search(r"\b(you|your|you'd|you'll|you're)\b", s, re.I):
        tags.append("second-person")
    if re.search(r"\bevery \w+ on one \w+", s, re.I):
        tags.append("every-x-on-one-y")
    if re.match(r"^(the|a|an) \w+", s, re.I) and len(sents) == 1 and not s.endswith((".", "!", "?")):
        tags.append("noun-phrase")
    if re.match(r"^(how|what|why|when|where|who) ", s, re.I) and not s.endswith("?"):
        tags.append("wh-lead")
    if re.match(r"^\w+ (for|of) ", s) and n <= 8 and not s.endswith("."):
        tags.append("category-line")
    if n <= 3:
        tags.append("three-words-or-fewer")
    if re.search(r"\b\w+, \w+ and \w+\b", s):
        tags.append("rule-of-three")
    if re.search(r"\bnot [^.,;:]{2,40}, (but|it's|it is|with)\b", s, re.I) or re.search(r"\bnot with [^,]{2,30}, with\b", s, re.I):
        tags.append("not-x-but-y")
    if not tags:
        tags.append("declarative")
    return tags

def cta_class(label):
    s = label.strip().lower()
    s = re.sub(r"^(or )", "", s)
    if s in CTA_EXEMPT:
        return "exempt"
    if re.match(r"^purchase the [\w ]+ plan$", s): return "purchase-the-plan"
    if re.match(r"^purchase the ", s): return "purchase-the-noun"
    if re.match(r"^purchase ", s): return "purchase-noun"
    if re.match(r"^buy the [\w ]+ plan$", s): return "buy-the-plan"
    if re.match(r"^buy the ", s): return "buy-the-noun"
    if re.match(r"^buy a ", s): return "buy-a-noun"
    if re.match(r"^buy ", s): return "buy-noun"
    if re.match(r"^use the free", s): return "use-the-free-plan"
    if re.match(r"^(start|try) ", s): return "start-or-try"
    if re.match(r"^(get|choose|select|order|subscribe) ", s): return s.split()[0] + "-noun"
    return "other:" + re.sub(r"[^a-z]+", "-", s)[:30]

def section_device(name):
    s = name.strip()
    if s.endswith("?"): return "question"
    if re.match(r"^how \w+ works", s, re.I): return "how-x-works"
    if re.match(r"^what \w+ (never|does|doesn't|won't|is|isn't|costs)", s, re.I): return "what-x-does"
    if first_word(s) in IMPERATIVES: return "imperative"
    if ":" in s: return "colon-title"
    if re.match(r"^(\d+|%s)\b" % NUMBER_WORDS, s, re.I): return "number-led"
    if re.match(r"^the \w+ (you|you'd|you'll|that|who|which)", s, re.I): return "the-x-you-y"
    if len(words(s)) <= 3: return "short-noun"
    return "noun-phrase"

def blog_format(title):
    s = title.strip()
    if s.endswith("?"): return "question"
    if len(sentences(s)) >= 2: return "two-sentence"
    if re.match(r"^how to ", s, re.I) or re.search(r"\b(in an evening|in one evening|in an afternoon|in a weekend|in ten minutes|in an hour)\b", s, re.I): return "how-to"
    if re.search(r"\b(is not|isn't|myth|not a |never was|is no )", s, re.I): return "myth-negation"
    if re.match(r"^what ", s, re.I): return "what-explainer"
    if re.match(r"^why ", s, re.I): return "why-explainer"
    if re.match(r"^who ", s, re.I): return "who-explainer"
    if re.search(r"\b(vs\.?|versus|or the|, the \w+ and the)\b", s, re.I) or s.count(",") >= 2: return "comparison"
    if re.match(r"^(the|a|an) (evening|night|morning|day|ten seconds|hour|week|file|deed|score|funding)\b", s, re.I) or re.search(r"\b(the evening|the night|the morning|ten seconds|the day) (it|you|the)\b", s, re.I): return "narrative-time"
    if re.match(r"^(\d+|%s)\b" % NUMBER_WORDS, s, re.I): return "number-led"
    if first_word(s) in IMPERATIVES: return "imperative"
    return "noun-phrase"

def opening_shape(line):
    s = line.strip()
    if s.endswith("?"): return "question"
    if first_word(s) in IMPERATIVES: return "imperative"
    if re.match(r"^(you|your)\b", s, re.I): return "second-person"
    low = {w.lower() for w in words(s)}
    if low & SCENE_WORDS: return "scene"
    if re.search(r"\b(was|were|came|had|went|sat|stood|opened|paid|drafted)\b", s): return "past-tense-story"
    if len(words(s)) <= 6: return "short-claim"
    return "claim"

def devices(text, headlines):
    d = {}
    def put(k, n):
        if n: d[k] = n
    put("numbered-01-02-03", len(re.findall(r"^\s*0\d[.)]?\s+\w", text, re.M)))
    put("counting-as-story", len(re.findall(r"\b(%s|\d+) of (these|them|those)\b" % NUMBER_WORDS, text, re.I))
        + len(re.findall(r"\b(%s|\d+) in, (%s|\d+) (back|out)\b" % (NUMBER_WORDS, NUMBER_WORDS), text, re.I))
        + len(re.findall(r"\b(%s) (lights|shops|threads|sheets|steps|doors|windows|cards|rows|things)\b.*\b\1\b" % NUMBER_WORDS, text, re.I)))
    put("every-x-on-one-y", len(re.findall(r"\bevery \w+ on one \w+", text, re.I)))
    put("not-x-but-y", len(re.findall(r"\bnot [^.,;:]{2,40}, (but|it's|it is|with)\b", text, re.I)))
    put("rule-of-three-headlines", len([h for h in headlines if re.search(r"\b\w+, \w+ and \w+\b", h)]))
    put("second-person-conditional", len(re.findall(r"\bif you\b", text, re.I)))
    put("one-word-sentences", len(re.findall(r"(?:^|[.!?] )([A-Z][a-z]+)\.(?= |$)", text, re.M)))
    put("question-headlines", len([h for h in headlines if h.strip().endswith("?")]))
    put("never-list", len(re.findall(r"^\s*(row \d+\.\s*)?never ", text, re.I | re.M)))
    put("the-x-you-d-get", len(re.findall(r"\bthe \w+ you'?d (get|see|pay|keep)\b", text, re.I)))
    return d

def stats(text):
    sents = [s for s in sentences(re.sub(r"\s+", " ", text)) if len(words(s)) >= 2]
    lens = [len(words(s)) for s in sents] or [0]
    wc = sum(lens) or 1
    contractions = len(re.findall(r"\b\w+['’](t|s|re|ll|ve|d|m)\b", text))
    return {
        "sentences": len(sents),
        "words": wc,
        "mean_sentence_words": round(statistics.mean(lens), 1),
        "sentence_length_stdev": round(statistics.pstdev(lens), 1) if len(lens) > 1 else 0,
        "share_short_sentences_le5": round(sum(1 for l in lens if l <= 5) / max(1, len(lens)), 2),
        "share_long_sentences_ge25": round(sum(1 for l in lens if l >= 25) / max(1, len(lens)), 2),
        "contractions_per_100_words": round(100 * contractions / wc, 1),
        "questions_per_100_sentences": round(100 * sum(1 for s in sents if s.endswith("?")) / max(1, len(sents)), 1),
    }

# ---------- parsers ----------

LABEL_RE = re.compile(r"^\s*(?:\d+\.\s*)?(?P<label>Hero H1|H1|H2|H3|Heading|Headline|Title|Subhead|Section heading|Section|Primary CTA[^:]*|Secondary CTA[^:]*|[\w ()]*CTA[^:]*|Button[^:]*|Label[^:]*|Free CTA|Household CTA|Link[^:]*):\s*(?P<text>.+?)\s*$")

def parse_markdown(text):
    h1 = None; headlines = []; ctas = []; sections = []; blog_titles = []; openings = []
    part = None; in_post = False; want_opening = False; want_title = False; page = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if re.match(r"^## ", line):
            part = line[3:].strip().upper(); in_post = False; page = None
            want_opening = part.startswith("ABOUT")
            continue
        if part and part.startswith("BLOG") and re.match(r"^### ", line):
            in_post = True; want_title = True; continue
        if part and part.startswith("COPY") and re.match(r"^### ", line):
            page = line[4:].strip(); continue
        if re.match(r"^#### ", line):
            headlines.append(line[5:].strip()); continue
        m = LABEL_RE.match(line)
        if m:
            label = m.group("label").strip().lower(); t = m.group("text").strip()
            if "cta" in label or label.startswith("button"):
                t = re.sub(r"\s*\((?:to |/)[^)]*\)\s*$", "", t).strip()
                if len(words(t)) <= 6: ctas.append(t)
                else: headlines.append(t)
            elif label in ("hero h1",) or (label == "h1" and page and page.lower().startswith("home")):
                h1 = h1 or t
            elif in_post and want_title and label in ("title", "h1", "heading", "headline"):
                blog_titles.append(t); want_title = False; want_opening = True
            elif label in ("heading", "h2", "h3", "section heading", "section", "subhead", "title"):
                headlines.append(t)
                if part and part.startswith("COPY"): sections.append(t)
            continue
        if in_post and re.match(r"^(Route slug|Angle|Theme|Standfirst|Body|Meta|Slug|Photo|Graphic|Alt)\b", line.strip()):
            continue
        if line.strip() and not line.startswith(("#", "*", "(", "Row ", "Text ", "Brand:", "Note")) and want_opening:
            first = sentences(line.strip())
            if first and len(words(first[0])) >= 3:
                openings.append(first[0]); want_opening = False
    return h1, headlines, ctas, sections, blog_titles, openings

def parse_pages(dirpath):
    """Plain text page dumps as the run's extractor writes them: headings first (h1, h2, h3 in DOM order),
    then CTA labels, then the first body paragraphs. home.txt's first line is the H1; a post-*.txt file's
    first line is the post title; blog-titles.txt lists one title per line; about.txt and post files give
    the opening lines."""
    h1 = None; headlines = []; ctas = []; sections = []; blog_titles = []; openings = []
    for name in sorted(os.listdir(dirpath)):
        if not name.endswith(".txt"): continue
        base = name.lower()
        lines = [l.strip() for l in open(os.path.join(dirpath, name), encoding="utf-8", errors="ignore").read().splitlines() if l.strip()]
        if not lines: continue
        if base.startswith("blog-titles"):
            blog_titles += lines; continue
        body = [l for l in lines if len(words(l)) >= 12]
        short = [l for l in lines if 2 <= len(words(l)) <= 14 and l not in body and not re.match(r"^(\$|©|\d{3}\D)", l)]
        if base.startswith("home") and lines: h1 = h1 or lines[0]
        if base.startswith("post"):
            blog_titles.append(lines[0])
            if body: openings.append(sentences(body[0])[0])
        if base.startswith("about") and body:
            openings.append(sentences(body[0])[0])
        for l in short:
            low = l.lower()
            if low.startswith(PURCHASE_VERBS) or re.match(r"^(use the free|start free|try|subscribe)", low):
                ctas.append(l)
            elif low in ("join our sms list",) or l == h1 or (base.startswith("post") and l == lines[0]):
                continue
            else:
                headlines.append(l)
                if not base.startswith("post"): sections.append(l)
    return h1, headlines, ctas, sections, blog_titles, openings

# ---------- main ----------

def dedupe(seq):
    out = []; seen = set()
    for x in seq:
        k = x.strip().lower()
        if k and k not in seen:
            seen.add(k); out.append(x.strip())
    return out

def main():
    if len(sys.argv) < 2:
        print(__doc__); return 1
    src = sys.argv[1]
    out = None; brand = ""
    if "--out" in sys.argv: out = sys.argv[sys.argv.index("--out") + 1]
    if "--brand" in sys.argv: brand = sys.argv[sys.argv.index("--brand") + 1]
    if os.path.isdir(src):
        text = "\n".join(open(os.path.join(src, f), encoding="utf-8", errors="ignore").read() for f in sorted(os.listdir(src)) if f.endswith(".txt"))
        h1, headlines, ctas, sections, blog_titles, openings = parse_pages(src)
    else:
        text = open(src, encoding="utf-8", errors="ignore").read()
        h1, headlines, ctas, sections, blog_titles, openings = parse_markdown(text)
    headlines = dedupe(headlines); ctas = dedupe(ctas); sections = dedupe(sections)
    blog_titles = dedupe(blog_titles); openings = dedupe(openings)
    shp = {}
    for h in headlines:
        for t in shape(h): shp[t] = shp.get(t, 0) + 1
    cta_classes = sorted({cta_class(c) for c in ctas} - {"exempt"})
    sec_dev = {}
    for s in sections:
        d = section_device(s); sec_dev[d] = sec_dev.get(d, 0) + 1
    blog_fmt = sorted({blog_format(t) for t in blog_titles})
    open_shapes = sorted({opening_shape(o) for o in openings})
    dev = devices(text, headlines)
    # Tags are the policed subset: distinctive structure, not every observation. Generic shapes
    # (noun-phrase, declarative) and near universal devices (second person, one word sentences)
    # stay in the profile and the stats but never become a tag, so a collision means something.
    GENERIC_SHAPES = {"noun-phrase", "declarative", "multi-sentence", "three-words-or-fewer"}
    DISTINCTIVE_DEVICES = {"numbered-01-02-03": 1, "counting-as-story": 2, "every-x-on-one-y": 1,
                           "never-list": 3, "the-x-you-d-get": 1, "not-x-but-y": 2, "rule-of-three-headlines": 3}
    tags = []
    if h1: tags += ["copy.h1." + t for t in shape(h1) if t not in GENERIC_SHAPES] or ["copy.h1.plain-declarative"]
    tags += ["copy.cta." + c for c in cta_classes if not c.startswith("other:")]
    if sec_dev:
        dom, n = max(sec_dev.items(), key=lambda kv: kv[1])
        if dom != "noun-phrase" or n / max(1, len(sections)) >= 0.7:
            tags.append("copy.section." + dom)
    tags += ["copy.blog." + f for f in blog_fmt]
    if openings: tags.append("copy.open." + opening_shape(openings[0]))
    tags += ["copy.device." + k for k, n in dev.items() if k in DISTINCTIVE_DEVICES and n >= DISTINCTIVE_DEVICES[k]]
    top_shapes = [(t, n) for t, n in sorted(shp.items(), key=lambda kv: -kv[1]) if t not in GENERIC_SHAPES and n >= 3][:2]
    tags += ["copy.headline." + t for t, n in top_shapes]
    fp = {
        "brand": brand, "source": os.path.basename(src.rstrip("/")),
        "h1": h1, "h1_shapes": shape(h1) if h1 else [],
        "headlines": [{"text": h, "shapes": shape(h)} for h in headlines],
        "headline_shape_profile": dict(sorted(shp.items(), key=lambda kv: -kv[1])),
        "ctas": ctas, "cta_classes": cta_classes,
        "section_names": sections, "section_naming_devices": sec_dev,
        "blog_titles": [{"text": t, "format": blog_format(t)} for t in blog_titles], "blog_title_formats": blog_fmt,
        "opening_lines": [{"text": o, "shape": opening_shape(o)} for o in openings], "opening_shapes": open_shapes,
        "devices": dev, "stats": stats(text), "tags": sorted(set(tags)),
    }
    js = json.dumps(fp, indent=2, ensure_ascii=False)
    if out:
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        open(out, "w", encoding="utf-8").write(js + "\n"); print("wrote", out)
        print("tags:", ", ".join(fp["tags"]))
    else:
        print(js)
    return 0

if __name__ == "__main__":
    sys.exit(main())
