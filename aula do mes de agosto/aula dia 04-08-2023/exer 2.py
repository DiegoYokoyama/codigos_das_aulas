import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QVBoxLayout,QWidget, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ck = QCheckBox("masculino")
        self.ck2 = QCheckBox("feminino")
        

        self.setWindowTitle("cadastro")
        self.setGeometry(150, 150, 500, 500)

        self.label1 = QLabel("nome:", self)
        self.label1.setGeometry(20, 5, 80, 30)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(80, 10, 410, 20)

        self.label2 = QLabel("telefone:", self)
        self.label2.setGeometry(20, 45, 80, 30)

        self.input2 = QLineEdit(self)
        self.input2.setGeometry(80, 50, 410, 20)
        
        self.label3 = QLabel("endereço:", self)
        self.label3.setGeometry(20, 85, 80, 30)

        self.input3 = QLineEdit(self)
        self.input3.setGeometry(80, 90, 410, 20)
        
        self.label4 = QLabel("sexo:", self)
        self.label4.setGeometry(20, 125, 80, 30)

        self.button = QPushButton("cadastro", self)
        self.button.setGeometry(5, 460, 490, 20)

        layout = QVBoxLayout()

        layout.addWidget(self.ck)
        layout.addWidget(self.ck2)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        self.ck.stateChanged.connect(self.state)
        self.ck2.stateChanged.connect(self.state2)
        
    def state(self, s):
        print(s)
        if s == 2:
            self.ck2.setChecked(False)
        else:
            self.ck2.setChecked(True)
            
    def state2(self, s):
        print(s)
        if s == 2:
            self.ck.setChecked(False)
        else:
            self.ck.setChecked(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
