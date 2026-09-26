# JS Syntax Errors during HTML Injection (Play Mode Breakage)

## Issue
The user reported that nothing was working in the Play Mode (Home Screen, Plumber Icon, Quick Request). 

## Root Cause
When building the `app.html` Play Mode, `build_app.py` concatenates `v2.js` and `v1.js` into a single `<script>` block.
1. `v1.js` was missing its opening `(() => {` but retained its closing `})();`.
2. `v2.js` had a dangling `(() => {` at the end.
These mismatched IIFE wrappers caused a fatal `SyntaxError: Unexpected token ')'` in the browser, completely crashing the entire script block in `app.html`. Because of this, NO event listeners (including standard navigation) were attached.

Additionally, a ReferenceError was identified in `v2.js` because a variable `workerProfileSvg` was queried but it was named `workerSvg` earlier in the file. 

## Prevention Rule
When managing multiple JS files (`v1.js`, `v2.js`) that are injected into a single global HTML file:
1. **Always verify IIFE boundaries:** Ensure every injected script is perfectly wrapped in an IIFE `(() => { ... })();` to avoid scope pollution and syntax errors.
2. **Beware of runtime reference errors:** Variable renames or copy-pasting code between V1 and V2 can leave undefined variables. Always ensure variable names are consistent (e.g., `workerSvg`).
3. **Null-check event listeners:** Always wrap DOM queries in `if (element) { element.addEventListener(...) }` because in a combined Play Mode, not all SVGs are visible or present on every screen flow.
