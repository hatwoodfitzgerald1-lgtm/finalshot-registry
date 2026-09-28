# Code log: savebrew

- Repository: https://github.com/hatwoodfitzgerald1-lgtm/savebrew-site (public)
- Deployed commit: 08506fe7342c4411099fc59e114379b20f99ea65
- Permalink to the exact code: https://github.com/hatwoodfitzgerald1-lgtm/savebrew-site/tree/08506fe7342c4411099fc59e114379b20f99ea65
- Live site: https://savebrew-site.webflow.io (Webflow Cloud app `savebrew-site` in Harlem's Workspace, branch main, mount /, custom domain not attached)
- `savebrew-source.zip`: all 196 source files at that commit (Astro pages and route modules, components, CSS, TypeScript including the Three.js loom scene, the SVG brand and graphic kit, the vendored Three.js line classes and scroll timeline polyfill, data JSON, build scripts and lints, the void scan, configs, docs). The 113 photo, video, poster, font and favicon files are not duplicated here; they stay in the repo at the same commit.
- Stack: Astro 7 with `output: 'server'` and `@astrojs/cloudflare` 14, every page server rendered through `src/pages/[...slug].astro` over the route map in `src/routes/index.ts`; GSAP 3.12.5 (ScrollTrigger, Flip) and Three.js r128 from cdnjs.
- Commits after the first deploy (all on main; Webflow Cloud cancels a build that a newer push supersedes, so the live site always runs the newest commit, verified after each push):
  - `a1d5638` cloud safe prebuild (the data step skips where the copy source is absent).
  - `03c6733` to `b0e6a48`, `f8d3f96` entrance hidden states gated on `html.sb-motion`; rows in the first viewport never replay; tall sections reveal on any intersection.
  - `70dbd3c` README.
  - `c224258` (PR #1, squash) the hero between 900 and 1279: the loom docks on the hero knot centres when the pass grid collapses, the H1 wraps in two balanced lines with no leading space, the loom poster ships in four framings picked by aspect ratio.
  - `782762a` three copy labels changed after the Step 8 sameness re check ("Read next", the reading time and the ranker's minutes).
  - `e7d3fdd` (PR #2, squash) no voids at wide widths: the Roundup moves in three equal columns with their text in 22ch columns and the thread's knots measured from the moves; the Guides board with the two Rates guides side by side and today's pass item under the Coupons and Paycheck lines; the Contact still taking the row height from the text; the 404 search cell listing every guide and the Roundup before any search.
  - `08506fe` (PR #3, squash) no ragged lanes on the Guides board at any width: between 768 and 1023 the two lanes with a guide share a row and the two lanes carrying today's pass item share the next (read down each column, so the focus order is the thread order); the Coupons and Paycheck pass items open with a drawn box like every guide card (`public/assets/kit/pass-graphics`); from 1280 to 1439 the deks take the 14.5px narrow column size; `qa/void-check.mjs` joins the repo.
- Archived 2026-09-26 at Step 8 (tenth amendment); code log and source snapshot refreshed 2026-09-28 at 08506fe.
