# Meta-Mistake: System Amnesia (Failure of Autonomous Learning)

## Issue
The AI implemented complex logic for dual-flow prototyping (Figma Play mode, Canvas mode, Python build scripts, and safe JS injection) across multiple conversation turns. However, it FAILED to autonomously generalize and document this knowledge into `.agents/UI_UX_LEARNINGS.md` and the relevant `SKILL.md` files. The user had to manually remind the AI to update its skills.

## Root Cause
The AI prioritized "fixing the immediate code" (the syntax errors in `v1.js` and `v2.js`) but ignored its global directive (Rule 3 in `AGENTS.md`: Omnipresent Proactive Learning). The AI treated skill updating as a reactive task rather than a proactive baseline behavior.

## Prevention Rule
The `update-skills` meta-skill must actively monitor the AI's own behavior. Whenever a significant architectural shift is implemented (e.g., dual-flow prototypes, new infrastructure), the AI MUST immediately halt and run `replace_file_content` on the `SKILL.md` files and knowledge bases. If the AI waits for the user to say "update the skills," it has already failed. 
This rule is now being hardcoded into `update-skills/SKILL.md` to enforce self-triggering updates.
