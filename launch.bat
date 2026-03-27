@echo off
REM EvoShield AI - Desktop Application Launcher
REM This script launches the EvoShield AI desktop application

echo.
echo ======================================================================
echo  EvoShield AI - Desktop Application Launcher
echo ======================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python 3.8+ from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo Checking dependencies...
echo.

REM Check PyQt5
python -c "from PyQt5.QtWidgets import QApplication" >nul 2>&1
if errorlevel 1 (
    echo WARNING: PyQt5 not found
    echo Installing PyQt5...
    python -m pip install PyQt5 -q
)

REM Check PyQtChart
python -c "from PyQt5.QtChart import QChart" >nul 2>&1
if errorlevel 1 (
    echo WARNING: PyQtChart not found
    echo Installing PyQtChart...
    python -m pip install PyQtChart -q
)

REM Run verification
echo.
echo Running pre-launch verification...
python launch_verify.py
if errorlevel 1 (
    echo.
    echo ERROR: Pre-launch verification failed
    echo Please check the errors above and install missing dependencies:
    echo   python -m pip install PyQt5 PyQtChart psutil scikit-learn numpy
    echo.
    pause
    exit /b 1
)

REM Launch the application
echo.
echo ======================================================================
echo  Starting EvoShield AI Desktop Application...
echo ======================================================================
echo.

python main.py

if errorlevel 1 (
    echo.
    echo ERROR: Application failed to start
    echo Check the errors above for details
    echo.
    pause
    exit /b 1
)
