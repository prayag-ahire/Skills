# Back Button Amnesia

**Symptom:**
The back buttons on secondary screens (e.g., Worker List, Worker Profile) were not interactive. The user had to explicitly ask for them to be wired up.

**Root Cause:**
When adding interactivity to the SVGs, the frontend-engineer skill logic was only focused on "primary" flow buttons (like category icons and main call-to-actions) and completely ignored standard navigation elements like back arrows because the user did not explicitly mention them in their prompt.

**Resolution:**
I added IDs to the back arrow groups in `v1/worker.svg`, `v2/worker.svg`, and `v2/workerlist.svg`. I then updated `v1.js` and `v2.js` to attach click listeners to these buttons that trigger `window.navigateTo` to route the user back to the previous logical screen in the flow.

**Prevention:**
Added **Rule 10: Back Navigation Empathy** to `frontend-engineer/SKILL.md`. The AI must now assume all back buttons are interactive by default, proactively assign them IDs, and wire them to the previous screen without waiting for explicit user instruction.
