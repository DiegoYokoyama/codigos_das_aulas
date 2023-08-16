import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QDialog
from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela")
        self.setFixedSize(800,400)
        
        self.button = QPushButton('abrir', self)
        self.button.clicked.connect(self.open_secondary_window)
        self.button.setGeometry(150,130,500,100)
        
    def open_secondary_window(self):
        self.secondary_window = SecondaryWindow()
        self.secondary_window.show()
        
class SecondaryWindow(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('janela_secundario')
        self.setGeometry(200,200,500,300)
        
        layout = QVBoxLayout()
        
        label = QLabel('foto 2 ')
        layout.addWidget(label)
        
        image_label = QLabel(self)
        pixmap = QPixmap('foto 2.jpg')
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)
        
        close_button = QPushButton('Fechar', self)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)
        
        self.setLayout(layout)
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    main_Window = MainWindow()
    main_Window.show()
    app.exec()
                    
  
        