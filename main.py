# Nama  : Naufal Ihsanul Islam
# NIM   : F1D02310084
# Tugas 6 - Visualisasi Data

import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont
from main_window import DashboardWindow


def muat_stylesheet(app):
    # Muat file QSS
    qss_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "style.qss")
    if os.path.exists(qss_path):
        with open(qss_path, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())


def main():
    # Entry point aplikasi
    app = QApplication(sys.argv)

    # Font default
    font = QFont("Segoe UI", 9)
    app.setFont(font)

    # Terapkan stylesheet
    muat_stylesheet(app)

    # Tampilkan dashboard
    window = DashboardWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
