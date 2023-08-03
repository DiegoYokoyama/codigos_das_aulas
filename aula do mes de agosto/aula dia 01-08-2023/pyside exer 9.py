import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("total do salario do mes")
        self.setGeometry(100, 100, 500, 150)

        self.label1 = QLabel("quanto você ganha por hora:", self)
        self.label1.setGeometry(10, 10, 155, 30)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(170, 10, 80, 30)

        self.label2 = QLabel("horas trabalhadas no mês:", self)
        self.label2.setGeometry(10, 50, 150, 30)

        self.input2 = QLineEdit(self)
        self.input2.setGeometry(170, 50, 80, 30)

        self.result_label = QLabel(self)
        self.result_label.setGeometry(10, 90, 280, 30)

        self.button = QPushButton("Calcular", self)
        self.button.setGeometry(300, 10, 100, 70)
        self.button.clicked.connect(self.calcular_ganho_mes)

    def calcular_ganho_mes(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            total = num1 * num2
            self.result_label.setText(f"ganho do mes: {total}")
        except ValueError:
            print( 'Digite apenas numeros sem spaço ou letras')

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
