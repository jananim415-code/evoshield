#!/usr/bin/env python3
"""
EvoShield AI - Advanced Cybersecurity Defense System
Professional desktop cybersecurity application with AI/ML threat detection

Main Desktop Application Entry Point

Author: EvoShield Team
Version: 1.0.0
"""

import sys
import os
import traceback
from pathlib import Path

# Add the project root to sys.path to ensure imports work
PROJECT_ROOT = Path(__file__).parent.absolute()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def main():
    """
    Main entry point - launches the EvoShield AI desktop application
    
    This is a proper desktop app using PyQt5. It opens a GUI window
    and does not print to terminal (background operation only).
    """
    
    try:
        # Import PyQt5 components
        from PyQt5.QtWidgets import QApplication
        from PyQt5.QtGui import QFont, QIcon
        from ui.main_window import EvoShieldWindow
        
        print("=" * 70)
        print(" EvoShield AI - Launching Desktop Application")
        print("=" * 70)
        print("\n✓ Initializing application...")
        
        # Create QApplication (must be done before creating any widgets)
        # Check if QApplication already exists
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        
        # Configure application properties
        app.setApplicationName("EvoShield AI")
        app.setApplicationVersion("1.0.0")
        app.setApplicationDisplayName("EvoShield AI - Cyber Defense System")
        app.setStyle('Fusion')  # Modern cross-platform style
        
        print("✓ Application initialized")
        print("✓ Creating main window...")
        
        # Create the main window
        window = EvoShieldWindow()
        
        # Configure window
        window.setWindowTitle("EvoShield AI - Advanced Cyber Defense System")
        
        print("✓ Showing window...\n")
        print("=" * 70)
        print(" Application is now running!")
        print(" Check the 'EvoShield AI' window that opened on your desktop")
        print("=" * 70 + "\n")
        
        # Show the window
        window.show()
        
        # Bring window to foreground (important for some systems)
        window.raise_()
        window.activateWindow()
        
        # Start the event loop
        # The application will stay running until the window is closed
        sys.exit(app.exec_())
        
    except ImportError as e:
        print(f"\n❌ ERROR: Failed to import required libraries")
        print(f"   {e}")
        print("\nTroubleshooting:")
        print("  1. Ensure PyQt5 is installed: python -m pip install PyQt5")
        print("  2. Run 'python setup.py' to install all dependencies")
        print("  3. Or use CLI version: python cli.py")
        sys.exit(1)
        
    except Exception as e:
        print(f"\n❌ ERROR: Application failed to start")
        print(f"   {type(e).__name__}: {e}")
        print("\nFull error details:")
        traceback.print_exc()
        print("\nTroubleshooting:")
        print("  1. Check that all core modules are present")
        print("  2. Verify all dependencies are installed: pip install -r requirements.txt")
        print("  3. Try the CLI version: python cli.py")
        sys.exit(1)


if __name__ == "__main__":
    main()
