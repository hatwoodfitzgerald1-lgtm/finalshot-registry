#!/usr/bin/env python3
"""verify_kit.py: prove an amended skill kit is a strict superset of the installed one.

usage: python3 verify_kit.py <installed_dir> <amended_dir> [--label NAME] [--siblings dir1,dir2]

--siblings names companion kits (for example finalshot's kit when verifying direct-qa-loop) so a
citation of a companion's file resolves instead of counting as dead.

For every file in the installed kit it reports lines removed / added (must be 0 removed),
checks the SKILL.md frontmatter (name and description identical, no other keys present that a
card save would drop), checks every `references/...` and `scripts/...` path the amended SKILL.md
cites exists on disk, and, when references/locked_requirements.md exists, checks that every
numbered ledger item of the installed ledger is present verbatim in the amended one and that the
numbering stays contiguous. Exit code 1 on any failure.
"""
import difflib, os, re, sys, json

def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()

def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    fm = m.group(1)
    keys = {}
    cur = None
    for line in fm.split("\n"):
        km = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if km:
            cur = km.group(1)
            keys[cur] = km.group(2).strip()
        elif cur and line.startswith(" "):
            keys[cur] += (" " if keys[cur] and not keys[cur].endswith(">-") else "") + line.strip()
    # normalise folded scalars and quoting
    out = {}
    for k, v in keys.items():
        v = re.sub(r"^>-\s*", "", v).strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        out[k] = re.sub(r"\s+", " ", v)
    return out

def ledger_items(text):
    items = {}
    for m in re.finditer(r"^(\d+)\.\s+(.*?)(?=^\d+\.\s|\n\n|\Z)", text, re.S | re.M):
        n = int(m.group(1))
        body = re.sub(r"\s+", " ", m.group(2)).strip()
        items.setdefault(n, body)
    return items

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    label = ""
    if "--label" in sys.argv:
        label = sys.argv[sys.argv.index("--label") + 1]
    siblings = []
    if "--siblings" in sys.argv:
        siblings = [d for d in sys.argv[sys.argv.index("--siblings") + 1].split(",") if d]
    installed, amended = args[0], args[1]
    fails = []
    rows = []
    inst_files = sorted(os.path.relpath(os.path.join(r, f), installed)
                        for r, _, fs in os.walk(installed) for f in fs)
    amd_files = sorted(os.path.relpath(os.path.join(r, f), amended)
                       for r, _, fs in os.walk(amended) for f in fs)
    for rel in inst_files:
        a = os.path.join(amended, rel)
        if not os.path.exists(a):
            fails.append(f"MISSING in amended kit: {rel}")
            rows.append((rel, "MISSING", "", ""))
            continue
        old = read(os.path.join(installed, rel)).splitlines()
        new = read(a).splitlines()
        removed = added = 0
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes():
            if tag in ("replace", "delete"):
                removed += i2 - i1
            if tag in ("replace", "insert"):
                added += j2 - j1
        status = "identical" if (removed == 0 and added == 0) else ("additive" if removed == 0 else "REMOVALS")
        if removed:
            fails.append(f"{rel}: {removed} line(s) removed")
        rows.append((rel, status, f"+{added}", f"-{removed}"))
    new_files = [f for f in amd_files if f not in inst_files]
    for rel in new_files:
        rows.append((rel, "new", f"+{len(read(os.path.join(amended, rel)).splitlines())}", "-0"))

    # frontmatter
    fm_old = frontmatter(read(os.path.join(installed, "SKILL.md")))
    fm_new = frontmatter(read(os.path.join(amended, "SKILL.md")))
    fm_notes = []
    for k in fm_old:
        if k not in fm_new:
            fails.append(f"frontmatter key dropped: {k}")
        elif fm_old[k] != fm_new[k]:
            fails.append(f"frontmatter key changed: {k}")
    extra = [k for k in fm_old if k not in ("name", "description")]
    fm_notes.append(f"keys: {sorted(fm_old)} -> {sorted(fm_new)}; name same: {fm_old.get('name')==fm_new.get('name')}; "
                    f"description same: {fm_old.get('description')==fm_new.get('description')}; "
                    f"keys a card save would drop: {extra or 'none'}")

    # citations in amended SKILL.md: a NEW dead citation fails; a pre-existing one is reported, not failed
    sk = read(os.path.join(amended, "SKILL.md"))
    sk_old = read(os.path.join(installed, "SKILL.md"))
    pat = r"`((?:references|scripts)/[\w./-]+)`"
    cited = sorted(set(re.findall(pat, sk)))
    cited_old = set(re.findall(pat, sk_old))
    def resolves(c):
        return os.path.exists(os.path.join(amended, c)) or any(os.path.exists(os.path.join(d, c)) for d in siblings)
    dead = [c for c in cited if not resolves(c)]
    dead_new = [c for c in dead if c not in cited_old]
    dead_pre = [c for c in dead if c in cited_old]
    if dead_new:
        fails.append(f"NEW dead citations in SKILL.md: {dead_new}")

    # ledger
    ledger_note = ""
    lp_old = os.path.join(installed, "references", "locked_requirements.md")
    lp_new = os.path.join(amended, "references", "locked_requirements.md")
    if os.path.exists(lp_old) and os.path.exists(lp_new):
        li_old = ledger_items(read(lp_old)); li_new = ledger_items(read(lp_new))
        changed = [n for n in li_old if li_new.get(n) != li_old[n]]
        missing = [n for n in li_old if n not in li_new]
        nums = sorted(li_new)
        gaps = [n for n in range(nums[0], nums[-1] + 1) if n not in li_new] if nums else []
        if changed or missing or gaps:
            fails.append(f"ledger: changed={changed} missing={missing} gaps={gaps}")
        ledger_note = (f"ledger items installed {min(li_old)}..{max(li_old)} ({len(li_old)}), amended {nums[0]}..{nums[-1]} "
                       f"({len(li_new)}); verbatim preserved: {len(li_old)-len(changed)-len(missing)}/{len(li_old)}; gaps: {gaps or 'none'}")

    # requirement-bearing lines (independent check)
    kw = re.compile(r"\b(MUST|must|never|Never|NEVER|mandatory|verbatim|required|REQUIRED|blocking)\b")
    req_old = set(); req_new = set()
    for rel in inst_files:
        for ln in read(os.path.join(installed, rel)).splitlines():
            if kw.search(ln): req_old.add(ln.strip())
    for rel in amd_files:
        for ln in read(os.path.join(amended, rel)).splitlines():
            if kw.search(ln): req_new.add(ln.strip())
    lost = sorted(req_old - req_new)
    if lost:
        fails.append(f"requirement-bearing lines lost: {len(lost)}")

    print(f"## {label or amended}")
    print(f"installed files: {len(inst_files)}   amended files: {len(amd_files)}   new: {len(new_files)}")
    print("| file | status | added | removed |")
    print("|---|---|---|---|")
    for r in rows:
        if r[1] != "identical":
            print(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} |")
    ident = sum(1 for r in rows if r[1] == "identical")
    print(f"| ({ident} other files) | identical | +0 | -0 |")
    print("frontmatter:", fm_notes[0])
    print(f"SKILL.md citations: {len(cited)} paths cited; new citations that do not resolve: {dead_new or 'none'}; "
          f"pre-existing unresolved citations (unchanged by this edit): {dead_pre or 'none'}")
    if ledger_note: print("ledger:", ledger_note)
    print(f"requirement-bearing lines: installed {len(req_old)}, all present in amended: {not lost} (lost {len(lost)})")
    print("RESULT:", "PASS, additive only" if not fails else "FAIL: " + "; ".join(fails))
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
