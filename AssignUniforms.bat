@echo off
echo Running AMB Uniform Assignment Program.
python Main.py
echo Done.

REM Wait so the user can read the messages
if %ERRORLEVEL% NEQ 0 (timeout /t 10 >nul) else (timeout /t 3 >nul)