import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("divisão de Números")
        self.setGeometry(150, 150, 400, 230)

        self.label1 = QLabel("Número 1:", self)
        self.label1.setGeometry(10, 10, 80, 30)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100, 10, 80, 30)

        self.label2 = QLabel("Número 2:", self)
        self.label2.setGeometry(10, 50, 80, 30)

        self.input2 = QLineEdit(self)
        self.input2.setGeometry(100, 50, 80, 30)
        
        self.label3 = QLabel("Número 3:", self)
        self.label3.setGeometry(10, 90, 80, 30)

        self.input3 = QLineEdit(self)
        self.input3.setGeometry(100, 90, 80, 30)
        
        self.label4 = QLabel("Número 4:", self)
        self.label4.setGeometry(10, 130, 80, 30)

        self.input4 = QLineEdit(self)
        self.input4.setGeometry(100, 130, 80, 30)


        self.result_label = QLabel(self)
        self.result_label.setGeometry(100, 170, 280, 30)

        self.button = QPushButton("Calcular", self)
        self.button.setGeometry(190, 10, 100, 70)
        self.button.clicked.connect(self.calcular_div)

    def calcular_div(self):
        num1 = float(self.input1.text())
        num2 = float(self.input2.text())
        num3 = float(self.input3.text())
        num4 = float(self.input4.text())
        div = (num1 + num2 + num3 + num4)/4
        self.result_label.setText(f"A soma é: {div}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
