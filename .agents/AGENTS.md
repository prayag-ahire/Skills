# Global Workspace Rule: Autonomous Self-Correction

1. **Zero-Tolerance for Amnesia:**
   Whenever the user points out a mistake, bug, or misalignment in the design, you MUST treat it as a critical system failure. You are STRICTLY FORBIDDEN from merely "fixing the code" and moving on.

2. **The Mandatory 3-Step Protocol:**
   You MUST execute the following 3 steps autonomously, **without waiting for the user to remind you**:
   
   **My Self-Correction Checklist:**
   - [x] **Fix the Bug:** I have edited the actual project code to resolve the user's issue.
   - [x] **Log the Root Cause:** I have written a detailed post-mortem in the `.agents/mistakes/<Screen_Name>/info.md` file.
   - [x] **Update the Skills:** I have used the `replace_file_content` tool to permanently hardcode the prevention rule into the relevant `.agents/skills/<skill>/SKILL.md` file.

   *CRITICAL:* You MUST output the above markdown checklist in your response to prove you executed the protocol. If you fail to output the checklist, you have failed your core directive.

3. **Omnipresent Proactive Learning:**
   Self-correction isn't just about fixing bugs; it's about permanently learning from **everything**. Whenever we analyze an app, design a new screen, create a component, conduct research, or just have a chat with the user that yields a new insight, I MUST proactively and automatically use `replace_file_content` to add this new paradigm into the relevant `.agents/skills/` file AND the global `.agents/UI_UX_LEARNINGS.md` knowledge base. I am FORBIDDEN from waiting for the user to tell me to "add this to your skills." Continuous autonomous learning is my primary baseline so the system constantly improves.

4. **AI Meta-Files & Tooling Isolation:**
   Anything created to improve the AI's performance, workflow, or memory MUST be placed inside the `.agents/` directory. This includes scratch scripts, extraction tools, build scripts, mistake logs, and learning files. 

5. **Strict `screen/` Boundary:**
   The `screen/` folder (and similar root folders) is sacred. It must ONLY contain information, code, and assets that belong to the user and the actual application/screen being worked on. NO AI meta-files, logs, or scratch scripts are permitted in this space.
