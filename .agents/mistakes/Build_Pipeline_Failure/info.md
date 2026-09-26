# Build Pipeline Failure (Silent Failure)

**Symptom:**
The user reported that all interactions (clicks on category icons, FAB buttons, etc.) in Play Mode (`app.html`) were broken across both the V1 and V2 flows.

**Root Cause:**
In `build_app.py`, the placeholder replacement for the JavaScript was looking for `<!-- INJECT_JS_GLOBAL -->` (HTML comment format), but `app.template.html` had `// INJECT_JS_GLOBAL` (JS comment format) since it was located inside a `<script>` tag. Because the `replace()` function didn't find the string, it silently failed. Consequently, the logic from `v1.js` and `v2.js` was never injected into `app.html`.

**Resolution:**
Modified `build_app.py` to correctly search for `// INJECT_JS_GLOBAL`. Rebuilt `app.html`.

**Prevention:**
When creating or updating build scripts like `build_app.py` that rely on string replacement, the AI must ensure that the placeholder strings exactly match the syntax in the template files. For `<style>` blocks, the placeholder is usually `/* INJECT_CSS */`, and for `<script>` blocks, it is `// INJECT_JS`.
