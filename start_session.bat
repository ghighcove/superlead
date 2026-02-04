@echo off
echo ================================================================
echo  AUTONOMOUS PROJECTILE GUIDANCE RESEARCH SYSTEM
echo ================================================================
echo.
echo Starting session with automatic source ingestion...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8+ first.
    pause
    exit /b 1
)

REM Run automatic ingestion
echo 🔍 Running automatic source ingestion...
echo.
python session_ingestion.py

echo.
echo ================================================================
echo  Session ready. You can now begin your research work.
echo ================================================================
echo.

REM Keep window open if there were errors
if errorlevel 1 (
    echo ❌ Ingestion encountered errors. Check above for details.
    pause
)