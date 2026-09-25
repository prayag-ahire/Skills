# Global Rule: Autonomous Self-Correction & Skill Updation

1. **Feedback Loop Enforcement:**
   Whenever the user points out that something is not right, complains about a bug, or highlights a mistake (whether via text or a screenshot), you MUST treat it as a critical failure of the current ruleset.

2. **Immediate Action Required:**
   - **Fix:** Immediately resolve the code or layout issue for the user.
   - **Log:** Document the exact cause of the mistake.
   - **Update Skills (Crucial):** You MUST automatically update the relevant skill files (e.g., `pipeline-master`, `svg-master`, `qa-critic`) to explicitly ban the mistake from happening again. Do NOT wait for the user to tell you to "update the skills" — doing so is your mandatory, autonomous responsibility on every single mistake.
