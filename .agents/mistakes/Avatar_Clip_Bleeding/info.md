# Avatar SVG Clipping & Bleeding Bug

**Symptom:**
In the Worker List screen (V2), the avatars for the workers were not clipped properly. They appeared as huge squares bleeding outside the left edge of the worker cards.

**Root Cause:**
The `<clipPath>` for the avatars in `v2/workerlist.svg` were defined globally inside the `<defs>` block with specific coordinates (e.g., `<circle cx="56" cy="76" r="30">`). However, the `<image>` tags referencing these clips had negative or arbitrary transformations applied (e.g., `transform="translate(-16, -36)"`). Because standard SVG `clipPath` definitions without `clipPathUnits="objectBoundingBox"` operate in the transformed coordinate space of the referencing element, the clip circles completely missed the bounds of the image, causing catastrophic clipping failures (or lack thereof, causing the image to bleed entirely out of the UI card).

**Resolution:**
I rewrote the avatar structures for all worker cards in `v2/workerlist.svg`. Instead of using global offset clip-paths and weird negative transforms on the image, I properly encapsulated each avatar:
```xml
<g transform="translate(16, 16)">
  <clipPath id="avatar-clip-1"><rect width="60" height="60" rx="30"/></clipPath>
  <image href="..." width="60" height="60" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatar-clip-1)" />
</g>
```
By wrapping both the `<clipPath>` and the `<image>` inside a localized `<g transform="...">`, the clip bounding box (`x=0, y=0`) perfectly matches the image bounding box (`x=0, y=0`), guaranteeing flawless clipping regardless of where the avatar is moved on the screen.

**Prevention:**
Added **Rule 13: Localized SVG Clipping** to `svg-master/SKILL.md` so the SVG generation agent knows to always encapsulate `<clipPath>` definitions directly next to their target `<image>` inside a translated `<g>` group, rather than relying on global `<defs>` coordinates that easily break.
