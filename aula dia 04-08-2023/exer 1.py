import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QVBoxLayout,QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CHECK BOX")
        self.label=QLabel("CLIQUE E ACEITE É ISSO")
        self.ck=QCheckBox("ACEITO!!!!")
        self.label2=QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.ck)
        layout.addWidget(self.label2)
        
        container=QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        self.ck.stateChanged.connect(self.state)            
    
    def state(self, s):
        if s == 2:
            self.label2.setText("NÃO!!")
        else:
            self.label2.setText("some daqui")    
    
app=QApplication(sys.argv)
w=MainWindow()
w.show()
app.exec()