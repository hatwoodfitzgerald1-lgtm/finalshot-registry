# Astroquanta: design record

Reconstructed 2026-09-26 from the build's finalshot-registry entry and its Build Log run record (astroquanta--20260915--build1), because the original design document lived in the building session's sandbox and was not archived at the time. Every value below is as the run recorded it. The live site is the other half of the record: `vibe-card.jpg`, `shots/`, `copy_fingerprint.json` and `code/` in this folder hold its screens, speech patterns and source.

- Live site: https://astroquanta-site.webflow.io/
- Built: 2026-09-15  ·  Repo: astroquanta-site

## Identity

- **domain**: astroquanta.com
- **brand type**: net new

## Governing idea and direction

- **governing idea**: The denominator is the design: every trial the agent ran stays on the screen in grey, so the six that survived can be priced.
- **archetype**: Sidebar-Anchored
- **signature move category**: Storytelling & Structure
- **signature move id**: STO-007
- **signature world**: {"object": "a lattice of 48 trial cells in depth (instanced cubes, 8 wide by 6 high, stacked through four gate planes)", "verb": "cull and hold", "camera_path": "single axis dolly forward through four gate planes, then a quarter turn to elevation over the six survivors"}
- **tier**: 1

## Type and color

- **heading font**: Schibsted Grotesk
- **body font**: IBM Plex Mono
- **typographic set piece**: The Fraction: 48 over 48 becomes 6 over 48 in display mono, the numerator stepping down at each gate while the denominator never leaves the screen
- **palette**: {"field": "dark", "hexes": ["0A0C0B", "1F2422", "3B423F", "7E8682", "D8DBD8", "9BE15D"], "accent_hue_family": "yellow green (phosphor)", "color_story": "grey ladder with one surviving phosphor"}

## Motion and interaction

- **motion signature**: {"easings": ["cubic-bezier(0.7, 0, 0.1, 1)", "cubic-bezier(0.12, 0.7, 0.16, 1)"], "durations": {"fast": "0.12s", "base": "0.36s", "slow": "0.9s"}}
- **loader transition**: trial grid fill gauge: 48 cells outline in step with real load, then Flip into the hero lattice
- **nav style**: persistent left status rail with ticking run clock and gate index, prompt glyph active marker, drawer on mobile
- **button style**: square hairline console button, prompt glyph slides in and label shifts one character on hover, inverted fill on press, kept green primary
- **interactive feature**: simulator
- **technique ids**: ["STO-007", "3DW-011", "MOT-005", "MOT-004", "MOT-015", "TYP-020", "COL-018", "TEX-014", "TRN-002", "EXP-002", "CUR-007", "CUR-010"]

## Brand graphic kit and media

- **motif**: the trial cell (a 12px square that is outlined, then filled grey or kept green) and the prompt glyph
- **media manifest**: False

## Voice and copy

- **voice stance**: sober quantitative recorder

## Pages and build

- **framework**: Astro, SSR catch-all
- **engine profile**: baseline-r128
