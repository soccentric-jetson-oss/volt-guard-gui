# SPDX-License-Identifier: MIT
"""
Volt Guard GUI - Application entry point.

Thin entry point that creates the QApplication and launches the
main window. All UI logic lives in src.app.VoltGuardApp.
"""

import sys
from PySide6.QtWidgets import QApplication
from src.app import VoltGuardApp


def main():
    """Create and run the Volt Guard GUI application."""
    app = QApplication(sys.argv)
    app.setApplicationName("Volt Guard")
    window = VoltGuardApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
