from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("exercicio 4")
        self.setGeometry(100,100,300,150)
        
        self.label1 = QLabel('Numero 1:', self)
        self.label1.setGeometry(10,10,80,30) 
        
        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100,10,80,30)
        
        self.label2 = QLabel('Numero 2:', self)
        self.label2.setGeometry(10,50,80,30) 
        
        self.input2 = QLineEdit(self)
        self.input2.setGeometry(100,50,80,30)
        
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10,90,280,30)
        
        self.button = QPushButton('Calcular', self)
        self.button.setGeometry(190,10,100,70)
        
    def calcular_soma(self):
        num1 = int(self.input1.texto())
        num2 = int(self.input2.text())
        soma = num1 + num2
        self.result_label.setText(f'')
        

app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()