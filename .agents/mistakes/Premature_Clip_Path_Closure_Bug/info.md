# Premature Clip Path Closure Bug

**Symptom:**
When scrolling the Worker Profile screen, the avatar card and photos scrolled completely *over* the iPhone hardware bezels and into the grey background. The entire illusion of the screen boundaries was broken because the content was not being masked to the phone's shape.

**Root Cause:**
In `v1/worker.svg` and `v2/worker.svg`, there was an errant `</g>` placed immediately after the 3-dots menu button in the sticky header. Because the `<g clip-path="url(#screen-clip-2)">` wrapper was open, this rogue `</g>` prematurely closed the main screen clipping mask. As a result, the subsequent `<g id="scrollable-content">` block was rendered completely outside the clip path, causing it to bleed over the hardware frame when translated along the Y-axis.

**Resolution:**
I wrote a Python script to scan both SVG files, identify the rogue `</g>` tag immediately preceding the `<!-- Scrollable Body -->`, and strip it out. I then ran a `<g>` tag balance check to ensure the tags were perfectly balanced (37 open, 37 close in V2) so the `scrollable-content` is properly swallowed by the clip path.

**Prevention:**
The `qa-critic` protocol now mandates physical DOM verification. When moving elements around or injecting SVG chunks, agents must ensure they do not introduce unbalanced tags or prematurely close structural wrappers like the global `screen-clip`.
