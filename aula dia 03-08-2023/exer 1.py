from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Hello World!!!")
		button = QPushButton("Jho soy um butão")
		self.setCentralWidget(button)
		button.clicked.connect(self.imprimir)
	def imprimir(self):
		print("Professor Maurício")


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()