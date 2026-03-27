#!/usr/bin/env pwsh
# EvoShield AI - Windows PowerShell Launcher
# This script automatically runs the best available version of EvoShield AI

Write-Host ""
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "                    EvoShield AI - Launcher" -ForegroundColor Cyan -BackgroundColor Black
Write-Host ""
Write-Host "              Advanced Cybersecurity Defense System" -ForegroundColor Cyan
Write-Host ""
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[OK] Python is installed: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Python 3.8+ from https://www.python.org/" -ForegroundColor Yellow
    Write-Host "Make sure to check 'Add Python to PATH' during installation"
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if we're in the right directory
if (-not (Test-Path "main.py")) {
    Write-Host "[ERROR] main.py not found" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please run this script from the evoshield directory" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[OK] EvoShield AI files found" -ForegroundColor Green
Write-Host ""

:menu
Clear-Host

Write-Host ""
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "LAUNCH OPTIONS" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  1) Auto Mode (Try GUI, fall back to CLI)  [RECOMMENDED]" -ForegroundColor Green
Write-Host "  2) CLI Mode (Terminal Dashboard)         [ALWAYS WORKS]" -ForegroundColor Green
Write-Host "  3) GUI Mode (Desktop Dashboard)          [REQUIRES PyQt5]" -ForegroundColor Yellow
Write-Host "  4) Demo Mode (Feature Demonstration)" -ForegroundColor Cyan
Write-Host "  5) Test Mode (Run Core Tests)" -ForegroundColor Cyan
Write-Host "  6) Setup Mode (Install Dependencies)" -ForegroundColor Cyan
Write-Host ""
Write-Host "  0) Exit" -ForegroundColor Red
Write-Host ""
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

$choice = Read-Host "Select option (0-6)"

switch ($choice) {
    "1" {
        Clear-Host
        Write-Host ""
        Write-Host "Launching EvoShield AI in Auto Mode..." -ForegroundColor Cyan
        Write-Host "(Will use GUI if available, otherwise CLI)" -ForegroundColor Yellow
        Write-Host ""
        Start-Sleep -Seconds 2
        python main.py
        break
    }
    "2" {
        Clear-Host
        Write-Host ""
        Write-Host "Launching EvoShield AI in CLI Mode..." -ForegroundColor Cyan
        Write-Host ""
        Start-Sleep -Seconds 2
        python cli.py
        break
    }
    "3" {
        Clear-Host
        Write-Host ""
        Write-Host "Launching EvoShield AI in GUI Mode..." -ForegroundColor Cyan
        Write-Host ""
        Start-Sleep -Seconds 2
        python main.py
        break
    }
    "4" {
        Clear-Host
        Write-Host ""
        Write-Host "Running EvoShield AI Demo..." -ForegroundColor Cyan
        Write-Host ""
        Start-Sleep -Seconds 2
        python demo.py
        break
    }
    "5" {
        Clear-Host
        Write-Host ""
        Write-Host "Running Core Module Tests..." -ForegroundColor Cyan
        Write-Host ""
        Start-Sleep -Seconds 2
        python test_core.py
        Read-Host "Press Enter to continue"
        goto menu
    }
    "6" {
        Clear-Host
        Write-Host ""
        Write-Host "Installing Dependencies..." -ForegroundColor Cyan
        Write-Host ""
        python -m pip install -r requirements.txt
        Write-Host ""
        Write-Host "[SUCCESS] Dependencies installed!" -ForegroundColor Green
        Write-Host ""
        Read-Host "Press Enter to continue"
        goto menu
    }
    "0" {
        Write-Host ""
        Write-Host "Goodbye!" -ForegroundColor Cyan
        Write-Host ""
        exit 0
    }
    default {
        Write-Host ""
        Write-Host "Invalid option. Please try again." -ForegroundColor Red
        Write-Host ""
        Read-Host "Press Enter to continue"
        goto menu
    }
}

Write-Host ""
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "Application terminated" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""
Read-Host "Press Enter to exit"
exit 0
