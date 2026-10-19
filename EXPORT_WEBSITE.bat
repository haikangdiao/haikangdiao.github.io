@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel% equ 0 (
  py tools\export_static.py
) else (
  python tools\export_static.py
)
if errorlevel 1 (
  pause
) else (
  explorer "%~dp0_public"
)
