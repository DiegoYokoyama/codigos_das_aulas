import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("converter metros para centímetros")
        self.setGeometry(100, 100, 300, 150)

        self.label1 = QLabel("Número 1:", self)
        self.label1.setGeometry(10, 10, 80, 30)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100, 10, 80, 30)

        self.result_label = QLabel(self)
        self.result_label.setGeometry(10, 90, 280, 30)

        self.button = QPushButton("Calcular", self)
        self.button.setGeometry(190, 10, 100, 70)
        self.button.clicked.connect(self.calcular_metros)

    def calcular_metros(self):
        num1 = int(self.input1.text())
        soma = num1*100
        self.result_label.setText(f"converter metros para centímetros: {soma}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
