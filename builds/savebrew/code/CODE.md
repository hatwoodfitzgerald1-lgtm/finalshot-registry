# Code log: savebrew

- Repository: https://github.com/hatwoodfitzgerald1-lgtm/savebrew-site (public)
- Deployed commit: 782762acd489d1957c8fee9de93376de89442f32
- Permalink to the exact code: https://github.com/hatwoodfitzgerald1-lgtm/savebrew-site/tree/782762acd489d1957c8fee9de93376de89442f32
- Live site: https://savebrew-site.webflow.io (Webflow Cloud app `savebrew-site` in Harlem's Workspace, branch main, mount /, custom domain not attached)
- `savebrew-source.zip`: all 193 source files at that commit (Astro pages and route modules, components, CSS, TypeScript including the Three.js loom scene, the SVG brand and graphic kit, the vendored Three.js line classes and scroll timeline polyfill, data JSON, build scripts and lints, configs, docs). The 113 photo, video, poster, font and favicon files are not duplicated here; they stay in the repo at the same commit.
- Stack: Astro 7 with `output: 'server'` and `@astrojs/cloudflare` 14, every page server rendered through `src/pages/[...slug].astro` over the route map in `src/routes/index.ts`; GSAP 3.12.5 (ScrollTrigger, Flip) and Three.js r128 from cdnjs.
- Commits after the first deploy (all on main; Webflow Cloud cancels a build that a newer push supersedes, so the live site always runs the newest commit, verified after each push):
  - `a1d5638` cloud safe prebuild (the data step skips where the copy source is absent).
  - `03c6733` to `b0e6a48`, `f8d3f96` entrance hidden states gated on `html.sb-motion`; rows in the first viewport never replay; tall sections reveal on any intersection.
  - `70dbd3c` README.
  - `c224258` (PR #1, squash) the hero between 900 and 1279: the loom docks on the hero knot centres when the pass grid collapses, the H1 wraps in two balanced lines with no leading space, the loom poster ships in four framings picked by aspect ratio.
  - `782762a` three copy labels changed after the Step 8 sameness re check ("Read next", the reading time and the ranker's minutes).
- Archived 2026-09-26 at Step 8 (tenth amendment).
