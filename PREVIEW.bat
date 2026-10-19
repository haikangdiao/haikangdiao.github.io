@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel% equ 0 (
  py tools\preview.py --open
) else (
  python tools\preview.py --open
)
if errorlevel 1 pause
