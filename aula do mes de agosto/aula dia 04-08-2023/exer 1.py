import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check Box")
        self.label = QLabel("Aceita casar comigo ?")
        self.ck = QCheckBox("Aceito")
        self.ck2 = QCheckBox("NÃO ACEITO")
        self.label2 = QLabel()
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.ck)
        layout.addWidget(self.label2)
        layout.addWidget(self.ck2)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        self.ck.stateChanged.connect(self.state)
        self.ck2.stateChanged.connect(self.state2)
        
    def state(self, s):
        print(s)
        if s == 2:
            self.label2.setText("ACEITO")
            self.ck2.setChecked(False)
        else:
            self.ck2.setChecked(True)
            
    def state2(self, s):
        print(s)
        if s == 2:
            self.label2.setText("NÃO ACEITO")
            self.ck.setChecked(False)
        else:
            self.ck.setChecked(True)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()