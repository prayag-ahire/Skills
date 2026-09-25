# Worker Profile Mistakes Audit

## Mistake 1: Component Overlap (`mistake_overlap.png`)
**The Issue:** The dynamically swapped tab content (Photos grid) rendered directly on top of the Action Buttons ("Follow") and the Tab menu, covering them up.
**Root Cause:** The Hero Card was placed at absolute `Y=136` with a height of `280` (Bottom edge = `416`). However, the Tab Content group was erroneously placed at `transform="translate(36, 280)"`. Because 280 is mathematically inside the 136-416 range, it caused a severe overlap.
**The Fix:** Changed the translation of all dynamic tab groups to `translate(36, 436)` so they safely render below the Hero Card.
**Prevention Rule Added:** `qa-critic` was updated with a "Mathematical Overlap Audit" rule requiring absolute bounding-box calculations (`Y + Height < Next_Y`).

## Mistake 2: Alignment and Padding (`mistake_alignment.png`)
**The Issue:** The YouTube icon overlapped text, and the lower half of the screen was shifted 12px to the left, leaving empty space on the right.
**Root Cause:** 
1. The YouTube icon was hardcoded to `X=300, Y=44`, which collided with the wide text string `(2 reviews)`.
2. The Hero Card width is `343px` (centered in `375px` screen with 16px margins). The Tabs content (Reviews, About, Availability) was mistakenly given a width of `327px`. Placing a 327px card at the same starting X coordinate as a 343px card leaves `343 - 327 = 16px` of empty space on the right.
**The Fix:** 
1. Shifted the Socials group to `translate(304, 24)` and pushed the YT icon down by 10px.
2. Standardized all Tab Content widths to exactly `343px` and aligned them identically at `X=36`.

## Mistake 3: Broken Visual Grouping (Gestalt Proximity)
**The Issue:** When attempting to fix the YouTube icon overlap, I pushed the icon down so far (to `Y=84`) that it completely broke the visual grouping. It looked disconnected from the Instagram icon.
**Root Cause:** I prioritized clearing the text bounding box by blindly pushing the element downwards, without considering the "Gestalt Principle of Proximity" (related icons should be visually grouped).
**The Fix:** Instead of pushing the icon way below the text, I stacked it tightly under the Instagram icon (`Y=32` with an 8px gap). This perfectly restored the visual group, while also lifting it safely above the text line (Absolute `Y=76 < Y=82`), solving both problems elegantly.
**Prevention Rule Added:** `svg-master` was updated to ensure overlap fixes do not break visual groupings.

## Mistake 4: JavaScript Syntax Error Breaking the UI
**The Issue:** The user reported that clicking on tabs (Photos, Reviews, etc.) suddenly stopped working after I implemented the Lightbox and Star Ratings.
**Root Cause:** When inserting the new Javascript logic sequentially using a chunk replacer, I accidentally overwrote the closing brace `}` of an `if (tabsGroup) {` block. This caused an `Uncaught SyntaxError` in the browser, completely crashing the entire script block and preventing any event listeners (including the previously working Tabs and Follow button) from attaching.
**The Fix:** Restored the missing `}` brace in `proworker.html`, resolving the syntax error and restoring full interactivity.
**Prevention Rule Added:** When doing partial code replacements, the `frontend-engineer` must double-check block closures to prevent fatal JS errors.

## Mistake 5: Cross-Screen Javascript Collision
**The Issue:** The user reported that clicking and dragging on the "first screen" (Home Screen) was causing the scroll response to happen on the "second screen" (Worker Profile). 
**Root Cause:** The `frontend-engineer` used `document.querySelector('svg')` to attach scroll listeners. However, because both screens are rendered side-by-side in `.figma-canvas`, `querySelector` grabbed the FIRST svg (Home Screen), but applied the `updateScroll()` math to the SECOND screen's inner group.
**The Fix:** Added an explicit `id="worker-profile-svg"` to the second screen and updated the Javascript to target `document.getElementById('worker-profile-svg')`.
**Prevention Rule Added:** When building a multi-screen `.figma-canvas` document, NEVER use generic DOM selectors like `document.querySelector('svg')` or `document.querySelectorAll('circle')`. ALWAYS use strict, screen-specific IDs to prevent cross-screen interference.

## Mistake 6: Hidden Form Inputs in Empty States
**The Issue:** The user noticed the "Write a review" card showed only 5 stars and an ocean of white space, hiding the actual comment text box and submit button until a star was clicked.
**Root Cause:** `frontend-engineer` applied `display="none"` to the input group by default, leaving the 180px tall parent card mostly empty. This breaks UI affordance (the user doesn't know they *can* type a comment).
**The Fix:** Removed `display="none"` from `review-input-group` in `proworker.html` so the text box and submit button are always visible.
**Prevention Rule Added:** `svg-master` and `frontend-engineer` must NEVER hide primary form inputs inside an empty state card unless the card itself strictly collapses its height. If a card is sized to fit an input, the input MUST be visible by default.

## Mistake 7: JS Scope Bleed during A/B Flow Versioning
**The Issue:** When creating a V2 row to test new UI ideas, all Javascript interactivity (tabs, scrolling, modals) broke simultaneously across both the V1 and V2 flows.
**Root Cause:** The `frontend-engineer` duplicated the HTML DOM into two rows, resulting in duplicate `id` attributes. Since `getElementById` only returns the first match, and variables like `const followBtn` were redefined, it triggered JS syntax errors and cross-scope collisions that crashed everything.
**The Fix:** Wrote a script to strictly isolate the scopes. Wrapped both blocks in IIFEs (`(() => { ... })();`) and appended `-old` suffixes to all IDs in the V1 HTML/JS to ensure perfect separation.
**Prevention Rule Added:** Added the "Non-Destructive Versioning" rule to `frontend-engineer` mandating strict IIFE wrapping and ID suffixing whenever creating A/B canvas flows.

## Mistake 8: Sticky CTA Hardware Clipping Failure
**The Issue:** A sticky "Call [Name]" button pinned to the bottom of the screen had perfectly square corners that physically protruded outside the rounded black bezels of the iPhone frame. It also lacked a Home Indicator, making it look glued on.
**Root Cause:** The sticky CTA group was placed at the very end of the SVG, *outside* of the `<g clip-path="url(#screen-clip-2)">` tag. Because it wasn't clipped by the screen mask, it ignored the phone's `rx=40` border radius.
**The Fix:** 
1. Re-injected an iOS Home Indicator (`<rect height="5" rx="2.5">`) inside the sticky footer.
2. Moved the Sticky CTA inside the `clip-path` group. (Alternatively, drew the sticky background using a strict SVG `<path>` with `a40 40` arcs on the bottom corners to perfectly trace the phone bezels).
**Prevention Rule Added:** `svg-master` updated to mandate that all absolute overlays/sticky footers must either reside inside the main screen `clip-path` OR manually draw perfectly mirrored bottom border radii using `<path>` arcs.
