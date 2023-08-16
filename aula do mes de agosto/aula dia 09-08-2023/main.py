from app import ShapeApp
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShapeApp()
    window.show()
    sys.exit(app.exec_())
