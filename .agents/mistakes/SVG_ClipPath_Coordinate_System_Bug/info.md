# Bug: Worker Profile Content Bleeding Outside Phone Bezel (Duplicate clipPath IDs)

## Screen
`screen/src/v2/worker.svg`

## Symptom
The top of the Worker Profile screen in Play Mode showed the title ("Worker Details") and 3-dots menu bleeding outside the phone's rounded bezel corners.

## Root Cause
The header elements were placed inside `<g clip-path="url(#v2w-screen-clip-2)">` but used **raw SVG canvas coordinates** that landed above the clip rect boundary:

```svg
<text x="167" y="14" ...>Worker Details</text>   <!-- y=14 is ABOVE screen start (y=20) -->
<rect x="315" y="-8" ...>                          <!-- y=-8 is way above screen -->
<circle cx="330" cy="2" ...>                       <!-- cy=2 is above screen -->
```

The clip rect is defined as `<rect x="20" y="20" width="375" height="812" rx="40" />`. Any element with `y < 20` sits above the clip boundary. SVG clips don't render outside their bounds — but the **phone bezel frame** (`rx="50"`) is drawn separately before the clip group, so elements above `y=20` paint on top of the bezel, creating the "bleeding out of rounded corners" look.

## Fix
1. Added a proper **Status Bar** block at `translate(20, 20)` matching other screens exactly.
2. Moved the **App Bar** (back arrow + title + 3-dots) to `translate(20, 76)` so all elements sit inside `y ≥ 20`.
3. Added a **back arrow** (`id="back-btn-worker"`) which was also missing.

## Prevention Rule
**NEVER** use raw Y coordinates close to 0 for elements inside a clip group whose clip rect starts at `y=20`. Always anchor headers using a `translate(20, N)` group where `N ≥ 20`. For any screen with a status bar + app bar, the pattern is:
- Status Bar: `translate(20, 20)` 
- App Bar / Header: `translate(20, 76)`
- First content: starts at `y ≥ 120`

## Second Root Cause (The Real One): Duplicate clipPath IDs

When both `v1/worker.svg` and `v2/worker.svg` are injected into the same HTML document (canvas or play mode), the browser has to resolve `url(#p1-clip)`, `url(#prod1-clip)` etc. Both SVGs used identical IDs for their photo and product clip paths. The browser picks **the first match** in the DOM — so the V2 worker's photo clips were being resolved to the V1 clip rect coordinates, causing images to render with the wrong clip geometry, creating the "bleeding outside bezel" visual.

## Final Fix
Namespaced all clipPath IDs:
- V2 worker: `p1-clip` → `v2w-p1-clip`, `prod1-clip` → `v2w-prod1-clip`, etc.
- V1 worker: `p1-clip` → `v1w-p1-clip`, `prod1-clip` → `v1w-prod1-clip`, etc.

## Prevention Rule
**Every SVG file injected into a shared HTML document MUST use fully namespaced IDs.** Generic IDs like `p1-clip`, `card-shadow`, `avatar-clip` will collide when multiple SVGs are in the same DOM. Always prefix with the screen+version identifier (e.g. `v2w-`, `v1wl-`). This applies to ALL `<clipPath>`, `<filter>`, `<linearGradient>`, `<mask>`, and `<symbol>` elements.
