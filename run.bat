@echo off
REM EvoShield AI - Windows Launcher Script
REM This script automatically runs the best available version of EvoShield AI

setlocal enabledelayedexpansion

title EvoShield AI - Cybersecurity Defense System

cls
echo.
echo ======================================================================
echo.
echo                    EvoShield AI - Launcher
echo.
echo              Advanced Cybersecurity Defense System
echo.
echo ======================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo.
    echo Please install Python 3.8+ from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo [OK] Python is installed
echo.

REM Check if we're in the right directory
if not exist "main.py" (
    echo [ERROR] main.py not found
    echo.
    echo Please run this script from the evoshield directory
    echo.
    pause
    exit /b 1
)

echo [OK] EvoShield AI files found
echo.

REM Show menu
echo ======================================================================
echo LAUNCH OPTIONS
echo ======================================================================
echo.
echo  1) Auto Mode (Try GUI, fall back to CLI)  [RECOMMENDED]
echo  2) CLI Mode (Terminal Dashboard)         [ALWAYS WORKS]
echo  3) GUI Mode (Desktop Dashboard)          [REQUIRES PyQt5]
echo  4) Demo Mode (Feature Demonstration)
echo  5) Test Mode (Run Core Tests)
echo  6) Setup Mode (Install Dependencies)
echo.
echo  0) Exit
echo.
echo ======================================================================
echo.

set /p choice="Select option (0-6): "

if "%choice%"=="1" (
    echo.
    echo Launching EvoShield AI in Auto Mode...
    echo (Will use GUI if available, otherwise CLI)
    echo.
    timeout /t 2 /nobreak
    python main.py
    goto end
)

if "%choice%"=="2" (
    echo.
    echo Launching EvoShield AI in CLI Mode...
    echo.
    timeout /t 2 /nobreak
    python cli.py
    goto end
)

if "%choice%"=="3" (
    echo.
    echo Launching EvoShield AI in GUI Mode...
    echo.
    timeout /t 2 /nobreak
    python main.py
    goto end
)

if "%choice%"=="4" (
    echo.
    echo Running EvoShield AI Demo...
    echo.
    timeout /t 2 /nobreak
    python demo.py
    goto end
)

if "%choice%"=="5" (
    echo.
    echo Running Core Module Tests...
    echo.
    timeout /t 2 /nobreak
    python test_core.py
    goto end
)

if "%choice%"=="6" (
    echo.
    echo Installing Dependencies...
    echo.
    python -m pip install -r requirements.txt
    if errorlevel 1 (
        echo.
        echo [WARNING] Installation had some issues
        echo Try running: pip install --user -r requirements.txt
    ) else (
        echo.
        echo [SUCCESS] Dependencies installed!
    )
    echo.
    pause
    goto menu
)

if "%choice%"=="0" (
    echo.
    echo Goodbye!
    echo.
    goto end
)

echo.
echo Invalid option. Please try again.
echo.
pause
goto menu

:menu
cls
echo.
echo Returning to menu...
echo.
timeout /t 1 /nobreak
goto start

:end
echo.
echo ======================================================================
echo Application terminated
echo ======================================================================
echo.
pause
exit /b 0
