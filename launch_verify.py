#!/usr/bin/env python3
"""
EvoShield AI - Pre-Launch Verification Script
Verifies all dependencies and systems before launching the desktop application
"""

import sys
import os
from pathlib import Path

def check_python_version():
    """Verify Python version"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor} (requires 3.8+)")
        return False

def check_module(name, import_path=None):
    """Check if a module is available"""
    if import_path is None:
        import_path = name
    
    try:
        __import__(import_path)
        print(f"✓ {name} - Installed")
        return True
    except ImportError as e:
        print(f"✗ {name} - NOT FOUND: {e}")
        return False

def check_core_modules():
    """Check if core threat detection modules exist"""
    core_dir = Path("core")
    required_files = [
        "anomaly_detector.py",
        "malware_simulator.py",
        "ai_threat_detector.py",
        "adaptive_model.py",
        "risk_engine.py",
        "defense_system.py",
        "__init__.py"
    ]
    
    all_found = True
    for file in required_files:
        file_path = core_dir / file
        if file_path.exists():
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} - MISSING")
            all_found = False
    
    return all_found

def check_ui_modules():
    """Check if UI modules exist"""
    ui_dir = Path("ui")
    required_files = [
        "main_window.py",
        "styles.qss",
        "__init__.py"
    ]
    
    all_found = True
    for file in required_files:
        file_path = ui_dir / file
        if file_path.exists():
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} - MISSING")
            all_found = False
    
    return all_found

def test_imports():
    """Test critical imports"""
    print("\n🔍 Testing imports...")
    
    tests = [
        ("PyQt5.QtWidgets", "PyQt5 Widgets"),
        ("PyQt5.QtCore", "PyQt5 Core"),
        ("PyQt5.QtGui", "PyQt5 GUI"),
        ("PyQt5.QtChart", "PyQt5 Charts"),
        ("psutil", "System Monitor"),
        ("sklearn", "ML Library"),
        ("numpy", "NumPy"),
    ]
    
    all_ok = True
    for import_path, display_name in tests:
        if not check_module(display_name, import_path):
            all_ok = False
    
    return all_ok

def test_core_imports():
    """Test core module imports"""
    print("\n🔍 Testing core modules...")
    
    try:
        from core import (
            AnomalyDetector,
            MalwareSimulator,
            AIThreatDetector,
            AdaptiveModel,
            RiskEngine,
            DefenseSystem
        )
        print("✓ All core modules importable")
        return True
    except ImportError as e:
        print(f"✗ Core module import failed: {e}")
        return False

def test_ui_imports():
    """Test UI module imports"""
    print("\n🔍 Testing UI modules...")
    
    try:
        from ui.main_window import EvoShieldWindow
        print("✓ Main window importable")
        return True
    except ImportError as e:
        print(f"✗ UI import failed: {e}")
        return False

def main():
    """Run all verification checks"""
    
    print("=" * 70)
    print(" EvoShield AI - Pre-Launch Verification")
    print("=" * 70)
    
    print("\n📋 System Information")
    print("-" * 70)
    
    all_checks = []
    
    # Python version
    all_checks.append(check_python_version())
    
    # Check directories
    print("\n📁 Checking project structure...")
    print("  Core modules:")
    all_checks.append(check_core_modules())
    print("  UI modules:")
    all_checks.append(check_ui_modules())
    
    # Test imports
    all_checks.append(test_imports())
    all_checks.append(test_core_imports())
    all_checks.append(test_ui_imports())
    
    # Final report
    print("\n" + "=" * 70)
    if all(all_checks):
        print(" ✅ ALL CHECKS PASSED - Ready to launch!")
        print("=" * 70)
        print("\n🚀 To start the application, run:")
        print("   python main.py")
        print("\n✨ The EvoShield AI desktop window will open in a few seconds...")
        return 0
    else:
        print(" ⚠️  Some checks failed - See above for details")
        print("=" * 70)
        print("\n🔧 To fix issues:")
        print("   1. Install missing dependencies:")
        print("      python -m pip install PyQt5 PyQtChart psutil scikit-learn numpy")
        print("   2. Or run the setup script:")
        print("      python setup.py")
        print("   3. Then try again:")
        print("      python launch_verify.py")
        return 1

if __name__ == "__main__":
    sys.exit(main())
