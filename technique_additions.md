# Technique additions

Techniques invented or combined on past finalshot builds that are not in the ui-ux-director database (230 entries). Each entry names the technique, what it is, how it was built, and the libraries, so the palette grows past 230. Dead database example links found during a run are noted at the bottom.

## The Collation

**Build:** Smart Augment (smartaugment.com), 2026-09-23, Tier 3, engine profile modern-three-0.185. Live at https://smartaugment-site.webflow.io (Home hero, pinned for 1.5 viewport heights).

**Category:** 3D & WebGL (fuses 3DW-007 scroll-driven 3D camera rig with 3DW-023 depth of field, on a bespoke paper stack world, with TEX-004 halftone as a post pass).

**What it is:** A committee memo rendered as a stack of five translucent paper sheets in depth (memo, comparables, model run, screen definition, disclosure file), joined by hairline provenance leaders that run from each figure on the front sheet to the exact row on the sheet behind that produced it. On scroll the flat, near orthographic reading view snaps into a raking perspective as the sheets fan apart in depth; a focus pull then walks from the memo at the front to the 9,240 row disclosure sheet at the back and returns (the held beat, with a mono DOM caption "9,240 rows in. Four pages out."); the sheets collate flat again with a reverse stagger and a 1.02 to 1.00 impression on landing, and the camera settles to a reading view held 6 degrees off axis. The whole scrub is spread over 1.5 viewport heights and smoothed with a 0.08 lerp. At rest the stack is alive: ink lines draw themselves, the six print sparkline plots, the sheets breathe on a 6 second idle cycle, and the stack tilts up to 1.5 degrees toward the pointer. Paper light travels from cool grey to warm cream across the scrub. It makes provenance literal without a word of explanation.

**How it was built:**
- Three.js 0.185 as an ES module via importmap (modern engine profile), loaded after first paint and idle behind a 1600 px WebP poster of the collated stack; the canvas cross dissolves over the poster in 0.44 s, and the poster stays with a two layer CSS parallax if init fails or exceeds 3 s.
- Paper: a custom RawShaderMaterial (GLSL ES 1.00). Vertex shader applies a two segment bow along u (uBow) plus an idle drift uniform so the sheets never read as flat cards. Fragment shader samples the baked sheet texture, adds paper fibre noise at 0.035 strength, a 1.5 percent inset rim darkening, and translucency at alpha 0.92 so the sheet behind shows through at 0.08. SHD-005 Fresnel rim at whisper strength (uRimPower 5.0, uRimStrength 0.12, Prussian blue) catches a blue line on fanned sheet edges.
- Sheet textures baked at runtime from the real product HTML screens at 2x (the memo, comparables, model run and screen definition sheets), so the 3D sheet and the product screen are the same artefact. The back disclosure sheet is a 2048 square canvas texture of 9,240 procedurally generated mono rows (invented pool labels), generated in a Web Worker so init never blocks the main thread.
- Provenance leaders: five thin Prussian blue segments (Line2 fat lines at 1.25 px, plain lines at dpr 1) from front sheet figures to the source rows behind; foreshortened to dots at rest, stretched into depth when fanned.
- Post chain in EffectComposer: BokehPass for the focus pull (focus distance scrubbed sheet to sheet, aperture 0.00004 at rest to 0.00022 during the pull, maxblur 0.011, half resolution on mobile class GPUs); SHD-012 Dither and Halftone Pass in halftone mode at engraving scale (uScale 3.2, uAngle 0.26 rad, ink 1A1A18, paper F6F3ED), thresholded above 0.82 luminance to pure paper so only shading and shadow tones are screened and baked type stays crisp, hero canvas only; SHD-008 Film Grain at 0.04 to unify the canvas with the graded photography.
- Camera: fov eases 12 to 38 and back to 14, a 34 degree right and 12 degree up swing, a 0.6 unit truck; sheet spacing 0.18 to 0.95 world units with 40 ms back to front stagger. Scroll scrubbed with GSAP ScrollTrigger (pin, scrub) on a Lenis rail, desktop only.
- Soft contact shadows are baked gradients on shadow planes; no shadow maps.
- Fallbacks: prefers-reduced-motion shows the curated poster at p 0.30 with the caption as static text and no canvas. Under 900 px or coarse pointer there is no WebGL; three CSS layers translate at different rates over 1.1 vh, leaders draw with stroke-dashoffset, and a tap fans the layers 12 px each.
- Measured live: LCP 864 ms, 60 fps average and 56 fps minimum through the pinned range, 0 frames over 33 ms, 0 console errors. A /qa/shaders harness route compiles both RawShaderMaterials and both post passes and prints status, frame time and dpr.

**Libraries:** Three.js 0.185.1 (core, EffectComposer, RenderPass, BokehPass, ShaderPass, Line2), custom RawShaderMaterial GLSL (paper, SHD-005 rim, SHD-012 halftone, SHD-008 grain), GSAP 3 with ScrollTrigger, Lenis, OffscreenCanvas in a Web Worker for the disclosure texture, CSS parallax and stroke-dashoffset for the mobile path.

**Reuse note:** the object (a translucent paper stack) and the camera grammar (focus pull and fov, not travel) are now logged in the registry and may not be repeated as a signature world. The recipe itself (baked HTML textures on bowed translucent planes with a BokehPass focus pull as the wow beat) can be recast on a different object.

## Dead database example links

None found on the 2026-09-23 run.

## TYP-024 The Long Receipt (Brainbrook, 2026-09-24)

**What it is.** The household's whole reimbursement ledger typeset onto one continuous thermal receipt tape that meanders like a brook across the page, with the camera riding the tape as scroll progress, faded print resolving crisp beneath it, HSA and FSA tags standing on the owed back lines, a lift to a held birdseye where the tape reads as a brook, and a tear off at the near end that hands the last line into the DOM product shot.

**How it was built.** Three.js r128 (self hosted, lazy after first paint, no post processing, no shadow maps). The tape is a `CatmullRomCurve3` swept into a `BufferGeometry` ribbon (width 1.2, 900 segments) with a `CanvasTexture` ledger drawn once at 1024 by 8192: the blocks are printed as a printer prints, the oldest receipt far away and today's line near the camera, with the canvas flipped vertically (`translate(0, TEX_H); scale(1, -1)`) so the type reads the right way up along the ride. A second, faded copy of the same canvas is a single `drawImage` through `filter: blur(1.2px) opacity(34%)`. A `ShaderMaterial` blends the faded and crisp textures by a `uReveal` scalar in tape length, adds a warm print colour, a tear mask (`uTear`) and fog to the celadon field. Camera: `rideAt(u, lateral)` puts the camera behind the reading point looking along the tangent (`p - tan * 1.8`, y 0.95, look `p + tan * 0.8`) with a lateral offset that eases out as the ride progresses; the lift goes to a birdseye with `camera.up = (1, 0, 0)` so the tape reads as a brook; the descent returns to the near end, the tear mask runs and the strip Flips (GSAP Flip) into the product shot. Scroll is a GSAP ScrollTrigger scrub through a CSS sticky 250vh track (no pinning API, so no layout shift). Reduced motion and phones get The Tear, a 2D canvas band that prints the same ledger and tears once.

**Library.** Three.js r128 plus GSAP 3 ScrollTrigger and Flip.

**Reuse notes.** The ledger content is the brand's real canonical dataset (household of four, 12 receipts owed back, the three plan dates), so the scene is also the product demo. The same rig takes any long, linear, typeset object (a ticker tape, a paper trail, a timeline strip).
