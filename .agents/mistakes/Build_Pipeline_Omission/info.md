# Build Pipeline Omission

**Symptom:**
The user observed that `proworker.html` (the Figma Canvas mode) was still displaying the buggy V1 Home Screen with the incorrect "9:01" status bar, missing notch, and inconsistent navigation icons, even though I explicitly patched `v1/workerlist.svg` (which acts as the V1 Home Screen) to have the standard system chrome in an earlier turn.

**Root Cause:**
After patching the SVG files, I only executed `python build_app.py` to regenerate `app.html` (Play Mode). I completely forgot to execute `python build.py` to regenerate `proworker.html` (Canvas Mode). Because the Canvas Mode was never rebuilt, it continued to serve the stale, buggy SVG markup to the user, creating confusion and making it appear as if the bug was never fixed.

**Resolution:**
I immediately ran `python build.py` to inject the updated SVGs into `proworker.html`. The Canvas mode now accurately reflects the standardized System Chrome fixes.

**Prevention:**
The AI must strictly adhere to the build pipeline rules. Whenever an SVG or JS file is modified, *both* `build.py` and `build_app.py` must be executed to ensure both the Canvas and Play modes are synchronously updated. I will add this explicit dual-build rule to `frontend-engineer/SKILL.md`.
