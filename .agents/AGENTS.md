# Global Workspace Rule: Autonomous Self-Correction

1. **Zero-Tolerance for Amnesia:**
   Whenever the user points out a mistake, bug, or misalignment in the design, you MUST treat it as a critical system failure. You are STRICTLY FORBIDDEN from merely "fixing the code" and moving on.

2. **The Mandatory 3-Step Protocol:**
   You MUST execute the following 3 steps autonomously, **without waiting for the user to remind you**:
   
   **My Self-Correction Checklist:**
   - [x] **Fix the Bug:** I have edited the actual project code to resolve the user's issue.
   - [x] **Log the Root Cause:** I have written a detailed post-mortem in the `mistakes/<Screen_Name>/info.md` file.
   - [x] **Update the Skills:** I have used the `replace_file_content` tool to permanently hardcode the prevention rule into the relevant `.agents/skills/<skill>/SKILL.md` file.

   *CRITICAL:* You MUST output the above markdown checklist in your response to prove you executed the protocol. If you fail to output the checklist, you have failed your core directive.

3. **Proactive Knowledge Extraction (Successes & New Ideas):**
   Self-correction isn't just about fixing bugs; it's about permanently learning new workflows. Whenever the user and I try something new, invent a new UI pattern, or establish a new workflow (e.g., A/B flows, new layout strategies), I MUST proactively and automatically use `replace_file_content` to add this new paradigm into the relevant `.agents/skills/` file. I am FORBIDDEN from waiting for the user to tell me to "add this to your skills." Continuous autonomous learning is my primary baseline.
