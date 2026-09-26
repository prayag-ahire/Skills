# Lightbox Clipping Syntax Bug

**Symptom:**
When the user tapped a photo on the V1 Worker Profile screen, the full-screen Lightbox overlay opened, but its black background `fill-opacity="0.95"` was a perfect rectangle with sharp corners at the bottom. It blatantly bled completely over the curved iPhone screen bezels. Furthermore, the image appeared to stretch over the borders.

**Root Cause:**
In a previous session, the Lightbox `<g id="lightbox-old">` was scrolling away with the rest of the photos, so the AI attempted to fix it by moving it to the root of the SVG, outside of the `<g id="scrollable-content-old">`. However, the AI incorrectly placed the Lightbox *after* the closing `</g>` tag of `<g clip-path="url(#screen-clip-2)">`.
Because the Lightbox was no longer a child of the screen-clip, it was no longer constrained by the 40px border radius of the device frame, causing it to render as a giant unclipped rectangle bleeding over the phone's bezel.

**Resolution:**
I moved the `<!-- OVERLAY: Lightbox -->` block strictly *inside* the `</g>` that closes the `screen-clip-2`. It is now properly sandwiched between the end of the sticky header/footer and the end of the screen clip.

**Prevention:**
The **Hardware Clipping & Bezels** rule in `svg-master/SKILL.md` already dictates that *all* overlays must be inside the `screen-clip`. I will add an explicit warning about Lightbox overlays to this existing rule to ensure they aren't accidentally exiled from the clip-path when fixing scroll bugs.
