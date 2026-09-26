@echo off
cd %~dp0\..
python build_app.py
python build.py
echo Both builds completed successfully.
