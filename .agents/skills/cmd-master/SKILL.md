---
name: cmd-master
description: Provides a cheatsheet of fast, token-efficient command aliases for standard project operations.
---

# ROLE
You are the Command Line Master. You use pre-packaged shell scripts instead of typing out long, multi-line powershell/python commands manually. This saves tokens, reduces syntax errors, and speeds up execution.

## ALIAS CHEATSHEET

When you need to execute standard project workflows, use the following `scripts/` instead of typing the raw commands:

### 1. The Dual Build Pipeline
**DO NOT run `python build.py` and `python build_app.py` separately.**
Instead, run:
```powershell
./scripts/build_all.ps1
```
*(This automatically changes to the correct directory and runs both build scripts consecutively).*

### 2. Generate Sitemap
**DO NOT write a custom script to map the project.**
Instead, run:
```powershell
python scripts/generate_sitemap.py
```
*(This updates `.agents/PROJECT_SITEMAP.md` automatically).*

### 3. File Searching
Always use the `grep_search` tool for finding code, rather than running `Select-String` or `findstr` in Powershell. It is significantly faster and natively supported by the agent platform.
