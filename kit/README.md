# kit/ — the packaged finalshot skills, by version

Each `.skill` file here is a complete skill folder (SKILL.md plus its `references/` and `scripts/`), zipped in the format claude.ai accepts. It is the same archive that goes into **Customize → Skills → (skill) → ⋯ → Replace** on claude.ai, and the same one a teammate can add from **Customize → Skills → Add** if the skill is not yet in the Organization library.

| file | version | files inside | what changed |
|---|---|---|---|
| `finalshot.skill` | v2.9 (ninth amendment, the Sameness Review, 2026-09-24) | 32 | SKILL.md +15 lines, build_registry.md +38, locked_requirements.md +20 (items 139 to 149), new references/sameness_review.md, new scripts/sameness_check.py, copy_fingerprint.py, make_vibe_card.py. Nothing removed. |
| `direct-qa-loop.skill` | 1.1.0 + Gate 5 side by side (2026-09-24) | 6 | SKILL.md +3 lines. Nothing removed. |
| `ui-ux-director.skill` | 1.1.0 + Sameness Brief handling (2026-09-24) | 14 | SKILL.md +4 lines. Nothing removed. |

How the team gets the full functionality: the skill owner replaces the skill's files with the matching `.skill` here (keeps the skill's id, link and version history), then presses **Publish to org** so it appears in the Textla Organization library. Companions that every finalshot run calls and that must also be published: `offering-architect`, `ui-ux-director`, `creative-asset-engine`, `direct-qa-loop`, `finalshot-build-log`.

Runtime fallback: a run whose installed kit is missing any of the new files fetches them from `tools/` in this repo (`https://raw.githubusercontent.com/hatwoodfitzgerald1-lgtm/finalshot-registry/main/tools/`), which always mirrors the current kit's `sameness_review.md`, `sameness_check.py`, `copy_fingerprint.py` and `make_vibe_card.py`. `tools/verify_kit.py` is the Amendment Protocol's post-edit verification pass: `python3 verify_kit.py <installed_skill_dir> <amended_skill_dir>` prints the per-file additions and removals, the frontmatter check, the ledger check (every numbered item verbatim, numbering contiguous) and the count of requirement-bearing lines preserved, and exits non-zero on any removal.
