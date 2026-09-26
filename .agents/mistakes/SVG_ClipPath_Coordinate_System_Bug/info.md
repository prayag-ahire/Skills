# SVG clipPath Coordinate System Bug

**Symptom:**
The worker avatar image in both V1 and V2 worker profile screens appeared unclipped — the square image bled outside its intended rounded-corner box (rx=16), particularly visible at the top-left of the hero card area.

**Root Cause:**
This is a subtle but critical SVG specification behavior. A `<clipPath>` element always evaluates its coordinates in the **root SVG viewport coordinate system**, completely ignoring any parent `<g transform="translate(...)">` wrappers. 

So when the avatar clipPath was defined inside `<g transform="translate(36, 136)">` with `<rect x="24" y="24" width="80" height="80" rx="16">`, the browser interpreted the clip as being at absolute SVG position (24, 24) — not at the expected (36+24=60, 136+24=160). The clip was applied to a completely different region of the screen, far away from the actual image, rendering the image effectively unclipped.

**Resolution:**
Changed the `<clipPath>` to use `clipPathUnits="objectBoundingBox"` with normalized 0–1 coordinates. This makes the clip relative to the bounding box of the element it is applied to, not the root SVG. The rx was converted from `16px on an 80px element` = `0.2` in normalized units.

The fix was applied to both `v1/worker.svg` and `v2/worker.svg`.

**Prevention:**
Added a critical rule to `svg-master/SKILL.md`: "SVG clipPath Coordinate System (CRITICAL)" which documents this behavior and mandates the use of `clipPathUnits="objectBoundingBox"` for any clip paths applied to elements inside transformed `<g>` groups.
