import brazilcep 
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QVBoxLayout,QWidget, QLineEdit, QPushButton, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        

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
        

        self.label3 = QLabel("sexo:", self)
        self.label3.setGeometry(20, 85, 80, 30)


        self.button = QPushButton("cadastro", self)
        self.button.setGeometry(5, 460, 490, 20)


        self.label4 = QLabel("cep:", self)
        self.label4.setGeometry(20, 120, 80, 30)

        self.input4 = QLineEdit(self)
        self.input4.setGeometry(80, 125, 410, 20)


        self.label5 = QLabel("distrito:", self)
        self.label5.setGeometry(20, 160, 80, 30)

        self.input5 = QLineEdit(self)
        self.input5.setGeometry(80, 165, 410, 20)


        self.label6 = QLabel("cidade:", self)
        self.label6.setGeometry(20, 200, 80, 30)

        self.input6 = QLineEdit(self)
        self.input6.setGeometry(80, 205, 410, 20)

        
        self.label6 = QLabel("rua:", self)
        self.label6.setGeometry(20, 240, 80, 30)

        self.input6 = QLineEdit(self)
        self.input6.setGeometry(80, 245, 410, 20)

        #endereco = brazilcep.get_address_from_cep('')
        


        self.cb = QComboBox()
        self.cb.addItems(["MASCULINO", "FEMININO"])

        self.cb.currentIndexChanged.connect(self.mundanca_indice)
        self.cb.currentTextChanged.connect(self.mudanca_texto)

        self.cb.setEditable(True)  
        self.cb.setMaxCount(2)

    
    def mundanca_indice(self, i):
        print(i)

    def mudanca_texto(self, t):
        print(t) 

        if t == "MASCULINO":
            print('MASCULINO')
        elif t == 'FEMININO':
            print('FEMININO')

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
