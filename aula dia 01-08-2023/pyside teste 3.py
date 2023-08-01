from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QPushButton
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("exercicio 2")
        
        self.button = QPushButton('Button',self)
        self.button.setGeometry(190,10,100,70)
        self.setFixedSize(600,400)
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10,90,280,30)
        
        
        
        
        self.button.clicked.connect(self.imprimir)
        
        
    def imprimir(self):
        numero = 4
        if numero % 2 == 0:
            self.result_label.setText(f'Este numero e {numero} par')
        else:
            self.result_label.setText(f'Este numero e {numero} impar')    
        
        
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()