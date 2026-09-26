# Avatar Clip Collision & Header Bleeding

**Symptom:**
In the V1 Worker Profile, two distinct visual bugs occurred:
1. The sticky header's white background bled completely over the rounded corners of the iPhone hardware bezel.
2. The worker's avatar image was drastically shifted and clipped into the top-left corner, showing only a sliver of the face.

**Root Cause:**
1. **Header Bleeding:** When I previously moved the `sticky-header-old` to the end of `v1/worker.svg` to fix its Z-index relative to the scrollable content, I accidentally placed it *outside* of the closing `</g>` for the `screen-clip` mask. Because it was no longer clipped by the phone's 40px radius, it drew square corners that bled over the bezel.
2. **Avatar Clip Collision:** Both `v1/worker.svg` and `v1/workerlist.svg` used the exact same ID `<clipPath id="avatar-clip">`. Because `proworker.html` (Canvas Mode) places multiple SVGs on the same HTML page, the DOM globally collapsed these IDs. The `avatar-clip` defined in `workerlist.svg` (which was positioned differently) overrode the clip path in `worker.svg`, causing the image to be clipped incorrectly based on global coordinates.

**Resolution:**
1. I wrote a Python script to locate and remove the premature `</g>` closing tag that sat before the `sticky-header-old`, ensuring the sticky header is now rendered *inside* the `screen-clip` wrapper.
2. I renamed `id="avatar-clip"` to `id="worker-avatar-clip-v1"` and `id="worker-avatar-clip-v2"` to prevent global DOM ID collision.
3. I ran the Dual Build Pipeline (`python build.py` and `python build_app.py`).

**Prevention:**
SVG IDs must ALWAYS be explicitly namespaced (e.g., `id="screen-v1-btn"`) to prevent collision when multiple prototype screens are compiled into a single Figma canvas view. I will add this rule to `svg-master/SKILL.md`.
