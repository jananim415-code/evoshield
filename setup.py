#!/usr/bin/env python3
"""
EvoShield AI - Setup and Installation Script
Automates environment setup and dependency installation
"""

import subprocess
import sys
import os


def run_command(cmd, description):
    """Run a command and display status"""
    print(f"\n{'='*60}")
    print(f" {description}")
    print(f"{'='*60}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    print("\n" + "="*60)
    print(" EvoShield AI - Setup and Installation Script")
    print("="*60)
    
    # Step 1: Check Python version
    print(f"\n✓ Python version: {sys.version}")
    
    if sys.version_info < (3, 8):
        print("✗ Python 3.8+ required!")
        sys.exit(1)
    
    # Step 2: Upgrade pip
    success = run_command(
        f"{sys.executable} -m pip install --upgrade pip",
        "Step 1: Upgrading pip"
    )
    if not success:
        print("⚠ pip upgrade had issues, continuing anyway...")
    
    # Step 3: Install requirements
    success = run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Step 2: Installing dependencies from requirements.txt"
    )
    
    if not success:
        print("\n⚠ Standard install failed, trying alternative method...")
        success = run_command(
            f"{sys.executable} -m pip install --user -r requirements.txt",
            "Step 2b: Installing with --user flag"
        )
    
    # Step 4: Verify installation
    print("\n" + "="*60)
    print(" Step 3: Verifying Installation")
    print("="*60)
    
    packages = ['PyQt5', 'psutil', 'sklearn', 'matplotlib', 'numpy']
    all_ok = True
    
    for package in packages:
        try:
            if package == 'sklearn':
                __import__('sklearn')
                print(f"✓ {package:15} installed")
            else:
                __import__(package)
                print(f"✓ {package:15} installed")
        except ImportError:
            print(f"✗ {package:15} NOT installed")
            all_ok = False
    
    # Step 5: Final instructions
    print("\n" + "="*60)
    if all_ok:
        print(" ✓ Installation Complete!")
        print("="*60)
        print("\nYou can now run EvoShield AI:")
        print(f"  {sys.executable} main.py")
    else:
        print(" ⚠ Some packages may not be installed")
        print("="*60)
        print("\nManual installation:")
        print(f"  {sys.executable} -m pip install PyQt5 psutil scikit-learn matplotlib numpy")
        print("\nThen run:")
        print(f"  {sys.executable} main.py")
    
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
