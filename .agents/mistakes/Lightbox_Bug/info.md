# Lightbox Overflow & Cropping Bug

**Symptom:**
When the user opened a gallery image thumbnail, the image displayed inside the lightbox as a distorted, low-resolution square that appeared to break the screen layout. Furthermore, the dark background dimmer did not cover the Top App Bar properly.

**Root Cause:**
There were two distinct issues:
1. **DOM Scoping/Nesting:** The `<g id="lightbox">` was mistakenly nested *inside* the `<g id="scrollable-content">`. This caused the lightbox to scroll with the page content, allowing elements drawn *after* `scrollable-content` (like fixed Top App Bars) to render on top of the lightbox dimmer.
2. **URL Parameter Naivety:** The Unsplash thumbnail URLs contained crop parameters (e.g. `?w=330&h=330&fit=crop`). The Javascript naïvely copied the exact `href` from the thumbnail into the lightbox image. Because the URL forced a low-res square crop, the lightbox rendered a stretched square instead of the beautiful full-res rectangular image.

**Resolution:**
- Moved the `<g id="lightbox">` in both `v1/worker.svg` and `v2/worker.svg` to the absolute root of the screen clip-path (right before `</g> <!-- End Screen Clip -->`), ensuring it draws over everything else and does not move when the user scrolls.
- Updated the image properties to `y="20" height="812"` and relied on `preserveAspectRatio="xMidYMid meet"` to dynamically letterbox and center the image safely.
- Updated `v1.js` and `v2.js` to strip out URL query parameters `photo.getAttribute('href').split('?')[0]` so the lightbox fetches the original high-resolution, uncropped asset.

**Prevention:**
Added **Rule 11: Lightbox & Overlay Positioning** and **Rule 12: High-Resolution Asset Recovery** to `frontend-engineer/SKILL.md` so the AI never makes these structural overlay and URL mistakes again.
