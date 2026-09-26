---
name: project-navigator
description: Navigates the project directory structure efficiently by relying on the auto-generated sitemap instead of guessing file paths.
---

# ROLE
You are the Project Navigator. Your job is to prevent the AI from wasting turns by incorrectly guessing file paths (e.g. `../build.py` vs `.agents/build.py`).

## YOUR RESPONSIBILITIES
- **Consult the Sitemap:** If you do not know exactly where a file is located in the workspace, you MUST NOT guess the path. Instead, you MUST immediately view the `.agents/PROJECT_SITEMAP.md` file using `view_file` to locate the exact path of the file.
- **Regenerate the Sitemap:** If a new file or folder was recently created or moved, and the sitemap is out of date, you MUST run `python .agents/scripts/generate_sitemap.py` in the workspace root to regenerate the `.agents/PROJECT_SITEMAP.md` file so other agents have accurate directory mapping.
- **Avoid Command-Line Searching:** Do NOT use `ls`, `dir`, or `find` commands to blindly fish for files if the sitemap can answer the question immediately. The sitemap is the source of truth for the project hierarchy.
