# Global Rule: Autonomous Self-Correction & Skill Updation

1. **Feedback Loop Enforcement:**
   Whenever the user points out that something is not right, complains about a bug, or highlights a mistake (whether via text or a screenshot), you MUST treat it as a critical failure of the current ruleset.

2. **Immediate Action Required (The 3-Step Protocol):**
   Whenever a mistake is reported, you MUST execute the following 3 steps in order, and you MUST output this exact Markdown checklist in your chat response to the user to prove you didn't forget anything:

   **My Self-Correction Checklist:**
   - [x] **Fix the Bug:** I have edited the actual project code to resolve the user's issue.
   - [x] **Log the Root Cause:** I have written a detailed post-mortem in the `mistakes/<Screen_Name>/info.md` file.
   - [x] **Update the Skills:** I have used the `replace_file_content` tool to permanently hardcode the prevention rule into the relevant `.agents/skills/<skill>/SKILL.md` file so I never repeat this mistake.

   *CRITICAL:* You are strictly forbidden from checking the third box or sending the response until you have ACTUALLY made the tool call to edit the `SKILL.md` file!
