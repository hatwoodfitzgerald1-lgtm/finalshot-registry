#!/usr/bin/env python3
"""archive_audit.py: prove every shipped finalshot build is fully archived and every run in flight is claimed.

Added 2026-09-24 (tenth amendment). Runs at Step 0 before any design work and again at Step 8 after the
archive push. Exit code 1 means the run must not proceed until the listed gaps are fixed.

usage:
  python3 archive_audit.py --registry registry.json --claims claims.json --builds builds_dir \
      [--runs runs_dir_or_json] [--self <slug>] [--json out.json]

  --registry  finalshot-registry/registry.json (shipped builds)
  --claims    finalshot-registry/claims.json (builds in flight)
  --builds    a local copy of finalshot-registry/builds/ (or a JSON listing {slug: [relative file paths]})
  --runs      optional Build Log dump: a folder of run JSON files or one JSON list; each run needs
              brand/slug, status and live_url when it has one
  --self      the slug of the run doing the audit (excluded from "in flight without a claim")

A build counts as SHIPPED when it has a registry entry, or a Build Log run whose status starts with
"shipped". A COMPLETE archive holds, under builds/<slug>/:
  vibe.json, vibe-card.jpg, shots/home-1440.* , copy_fingerprint.json,
  design_doc.md or DESIGN_RECORD.md, code/CODE.md
and, for builds shipped on or after 2026-09-26, item 140's full list as well: design_doc.md (not a
record), site_copy.md, art_direction_spec.md, offering_spec.md, asset_plan.json, brand_kit/.
A build is IN FLIGHT when a Build Log run exists that is not shipped; it must have a claim.
"""
import argparse, json, os, re, sys

REQUIRED = [
    ("vibe.json", lambda fs: "vibe.json" in fs),
    ("vibe-card.jpg", lambda fs: "vibe-card.jpg" in fs),
    ("shots/home-1440", lambda fs: any(f.startswith("shots/home-1440") for f in fs)),
    ("copy_fingerprint.json", lambda fs: "copy_fingerprint.json" in fs),
    ("design_doc.md or DESIGN_RECORD.md", lambda fs: "design_doc.md" in fs or "DESIGN_RECORD.md" in fs),
    ("code/CODE.md", lambda fs: "code/CODE.md" in fs),
]
# item 140's full list, enforced for every build shipped under the tenth amendment or later
FULL_SINCE = "2026-09-26"
FULL = [
    ("design_doc.md (the Step 5 document, not a record)", lambda fs: "design_doc.md" in fs),
    ("site_copy.md", lambda fs: "site_copy.md" in fs),
    ("art_direction_spec.md", lambda fs: "art_direction_spec.md" in fs),
    ("offering_spec.md", lambda fs: "offering_spec.md" in fs),
    ("asset_plan.json", lambda fs: "asset_plan.json" in fs),
    ("brand_kit/", lambda fs: any(f.startswith("brand_kit/") for f in fs)),
]


def norm_date(d):
    d = str(d or "")
    return f"{d[:4]}-{d[4:6]}-{d[6:8]}" if re.fullmatch(r"\d{8}", d) else d[:10]


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")


def load_builds(path):
    if not path:
        return {}
    if os.path.isfile(path):
        return {k: set(v) for k, v in json.load(open(path)).items()}
    out = {}
    for slug in sorted(os.listdir(path)):
        root = os.path.join(path, slug)
        if not os.path.isdir(root):
            continue
        out[slug] = {os.path.relpath(os.path.join(r, f), root).replace(os.sep, "/")
                     for r, _, fs in os.walk(root) for f in fs}
    return out


def load_runs(path):
    if not path:
        return []
    if os.path.isdir(path):
        runs = []
        for f in sorted(os.listdir(path)):
            if f.endswith(".json"):
                d = json.load(open(os.path.join(path, f)))
                runs.append(d.get("data", d))
        return runs
    d = json.load(open(path))
    return [x.get("data", x) for x in (d if isinstance(d, list) else d.get("runs", []))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", required=True)
    ap.add_argument("--claims", required=True)
    ap.add_argument("--builds", required=True)
    ap.add_argument("--runs")
    ap.add_argument("--self", dest="me", default="")
    ap.add_argument("--json")
    a = ap.parse_args()

    reg = json.load(open(a.registry))
    entries = reg.get("builds", reg) if isinstance(reg, dict) else reg
    cj = json.load(open(a.claims))
    claims = cj if isinstance(cj, list) else cj.get("claims", [])
    builds = load_builds(a.builds)
    runs = load_runs(a.runs)

    shipped = {}
    for e in entries:
        s = slugify(e.get("slug") or e.get("brand"))
        shipped[s] = {"brand": e.get("brand"), "live_url": e.get("live_url"), "source": "registry", "date": norm_date(e.get("date"))}
    for r in runs:
        s = slugify(r.get("slug") or r.get("brand"))
        st = str(r.get("status") or "").lower()
        if st.startswith("shipped") and s not in shipped:
            shipped[s] = {"brand": r.get("brand"), "live_url": r.get("live_url"), "source": "build log", "date": norm_date(r.get("date"))}

    gaps, report = [], {"shipped": {}, "in_flight": {}, "claims_to_close": []}
    for s, info in sorted(shipped.items()):
        fs = builds.get(s, set())
        missing = [name for name, ok in REQUIRED if not ok(fs)]
        d = info.get("date") or ""
        # a missing or unreadable date is treated as a new build, so the full list is required
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d) or d >= FULL_SINCE:
            missing += [name for name, ok in FULL if not ok(fs)]
        report["shipped"][s] = {"brand": info["brand"], "missing": missing}
        if missing:
            gaps.append(f"ARCHIVE INCOMPLETE {s}: missing {', '.join(missing)}")

    claimed = {slugify(c.get("slug") or c.get("brand")): c for c in claims}
    for r in runs:
        s = slugify(r.get("slug") or r.get("brand"))
        st = str(r.get("status") or "").lower()
        if s in shipped or s == slugify(a.me):
            continue
        report["in_flight"][s] = {"brand": r.get("brand"), "status": r.get("status"), "claimed": s in claimed}
        if s not in claimed:
            gaps.append(f"UNCLAIMED RUN {s}: a Build Log run is in flight with no entry in claims.json")

    for s, c in claimed.items():
        if s in shipped and str(c.get("status", "")).lower() not in ("shipped", "done", "archived"):
            report["claims_to_close"].append(s)
            gaps.append(f"CLAIM NOT CLOSED {s}: the build shipped; mark its claim shipped once its archive is complete")

    print(f"shipped builds: {len(shipped)}  complete archives: {sum(1 for v in report['shipped'].values() if not v['missing'])}  "
          f"runs in flight: {len(report['in_flight'])}  claims: {len(claims)}")
    for s, v in report["shipped"].items():
        print(f"  {'OK  ' if not v['missing'] else 'GAP '} {s}: " + ("complete" if not v["missing"] else "missing " + ", ".join(v["missing"])))
    for s, v in report["in_flight"].items():
        print(f"  {'OK  ' if v['claimed'] else 'GAP '} {s} (in flight, {v['status']}): {'claimed' if v['claimed'] else 'NO CLAIM'}")
    print("RESULT:", "PASS" if not gaps else "FAIL\n  " + "\n  ".join(gaps))
    if a.json:
        json.dump({"gaps": gaps, **report}, open(a.json, "w"), indent=1)
    return 1 if gaps else 0


if __name__ == "__main__":
    sys.exit(main())
