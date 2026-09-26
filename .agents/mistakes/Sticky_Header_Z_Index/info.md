# Sticky Header Z-Index & Notch Bleeding Bug

**Symptom:**
When the user scrolled down on the Worker Profile screen (V1 and V2), the main scrolling content (photos, text, buttons) rolled straight over the top of the device notch (Dynamic Island) and the Top App Bar (Back button, title). This made the screen look broken and the content illegible as it collided with the system icons.

**Root Cause:**
In SVG, the drawing order determines the Z-index (elements drawn later appear on top of earlier elements). The `Status Bar` (which contains the notch and clock) and the `Top App Bar` (which contains the back button) were placed *before* the `<g id="scrollable-content">` block in the SVG structure.
When the user interacted with the screen, the JavaScript translated the `scrollable-content` upwards. Because it was drawn last, it effortlessly painted right over the notch and app bar. Additionally, the headers lacked a solid background to obscure the scrolling content passing underneath.

**Resolution:**
I cut the `Status Bar` and `Top App Bar` out of the top of `v1/worker.svg` and `v2/worker.svg`. I created a new sticky container right at the bottom of the document (after the `scrollable-content` but before the sticky footer/overlays):
```xml
<!-- STICKY HEADER -->
<g id="sticky-header">
  <rect x="20" y="20" width="375" height="100" fill="#F7F7F5" /> <!-- Solid background -->
  <!-- Status Bar and Top App Bar go here -->
</g>
```
By placing the header after the scrollable content, it correctly renders on top. The solid background `<rect>` acts as a mask, ensuring the scrolling photos cleanly disappear as they slide up the screen, preserving the integrity of the notch and system icons.

**Prevention:**
Added **Rule 14: Sticky Header Z-Index Hierarchy** to `svg-master/SKILL.md` to ensure the SVG AI always positions fixed headers at the bottom of the document tree with a solid background rect.
