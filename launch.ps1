#!/usr/bin/env powershell
# EvoShield AI - Desktop Application Launcher (PowerShell Version)
# Usage: Right-click and "Run with PowerShell" or: powershell -ExecutionPolicy Bypass -File launch.ps1

Write-Host ""
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host " EvoShield AI - Desktop Application Launcher" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Python 3.8+ from https://www.python.org/" -ForegroundColor Yellow
    Write-Host "Make sure to check 'Add Python to PATH' during installation" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "Checking dependencies..." -ForegroundColor Yellow
Write-Host ""

# Check PyQt5
$pyqt5Check = python -c "from PyQt5.QtWidgets import QApplication; print('OK')" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "  ⚠ PyQt5 not found - Installing..." -ForegroundColor Yellow
    python -m pip install PyQt5 -q
}

# Check PyQtChart
$pyqtChartCheck = python -c "from PyQt5.QtChart import QChart; print('OK')" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "  ⚠ PyQtChart not found - Installing..." -ForegroundColor Yellow
    python -m pip install PyQtChart -q
}

# Run verification
Write-Host ""
Write-Host "Running pre-launch verification..." -ForegroundColor Cyan
python launch_verify.py

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "ERROR: Pre-launch verification failed" -ForegroundColor Red
    Write-Host ""
    Write-Host "Install missing dependencies:" -ForegroundColor Yellow
    Write-Host "  python -m pip install PyQt5 PyQtChart psutil scikit-learn numpy" -ForegroundColor White
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Launch the application
Write-Host ""
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host " Starting EvoShield AI Desktop Application..." -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

python main.py

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "ERROR: Application failed to start" -ForegroundColor Red
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}
