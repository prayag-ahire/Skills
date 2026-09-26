# Inconsistent System Chrome Bug

**Symptom:**
The user noticed that the V1 Worker List screen (labeled "ProWorker" home screen in the UI) lacked the standard iPhone notch, had a different time on the clock ("9:01" vs "14:47"), and used completely different icons in the bottom navigation bar compared to the other screens in the project. The user rightly pointed out that since we are working on the same project, the system chrome and navigation should be identical across all screens, even if the user's reference screenshots didn't include the notch.

**Root Cause:**
When `svg-master` generates a new screen, it sometimes hallucinates new SVG paths for standard system elements (like the status bar and bottom navigation) or blindly copies them from an uploaded reference screenshot (e.g. copying a 9:01 clock and missing notch from a user's screenshot). It fails to treat these system-level components as immutable, shared components that must be copy-pasted verbatim from the project's established design system.

**Resolution:**
I extracted the standardized `<g>` block for the `<!-- Status Bar -->` (which includes the 14:47 clock, the notch, and the battery/wifi icons) and the `<!-- Bottom Tab Bar -->` from `v2/worker.svg` and `v2/home.svg`. I then ran a python script to regex-replace the inconsistent custom blocks in `v1/workerlist.svg` with these standardized blocks.

**Prevention:**
Added **Rule 15: System Chrome Consistency** to `svg-master/SKILL.md` to mandate that `svg-master` MUST reuse the exact same SVG markup for Status Bars and Bottom Navigation Bars across every screen in a project, regardless of what the user's reference screenshot looks like.
