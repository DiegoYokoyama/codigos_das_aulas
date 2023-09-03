from PySide6.QtWidgets import (QMainWindow, QApplication,QLineEdit,
QLabel, QPushButton, QWidget, QFrame, QVBoxLayout, QDateEdit, 
QTextBrowser, QComboBox, QCheckBox)
from datetime import datetime
from PySide6.QtGui import QIntValidator, QColor, QFont, QTextCursor
from PacienteTesing import *

# vbox.addSpacing(10)  # Adiciona 10 pixels de espaço vertical
# vbox.addStretch(1)  # Adiciona um espaço horizontal expansível
# vbox.addWidget(widget2)
# vbox.addWidget(widget1)
# vbox.addWidget(widget2)
# vbox.addStretch(1)  # Adiciona espaço expansível
# vbox.addWidget(widget3)
# vbox.setAlignment(Qt.AlignTop)  # Alinha widgets ao topo do layout


# self.central = QWidget(self)
# self.setCentralWidget(self.central)

# layout = QVBoxLayout(self.central)

# frame_Medium2 = QFrame(self)
# frame_Medium2.setFrameStyle(QFrame.Box)
# layout.addWidget(frame_Medium2)

# self.frame_layout = QVBoxLayout(frame_Medium2)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Initial()

    def Initial(self):
        self.setWindowTitle("Exercicio 04")
        self.setFixedSize(650,650)


        self.Color = QColor(31, 75, 222) #BackGround
        self.setStyleSheet(f"background-color: {self.Color.name()};")

        
        #Medium
        self.central = QWidget(self)
        self.setCentralWidget(self.central)

        layout = QVBoxLayout(self.central)

        frame_Medium2 = QFrame(self)
        frame_Medium2.setFrameStyle(QFrame.Box)
        layout.addWidget(frame_Medium2)

        self.frame_layout = QVBoxLayout(frame_Medium2)
        
        self.Color_White = QColor(255,255,255) #Medium
        self.Color_Black = QColor(240,240,240) #Check
        frame_Medium2.setStyleSheet(f"background-color: {self.Color_White.name()};")

        self.welcome = QLabel("      Bem-Vindo ao Cadastro da Fila", self)
        self.font = QFont()
        self.font.setPointSize(25)
        self.font.setBold(True)
        self.welcome.setFont(self.font)

        self.lbl_nome = QLabel("NOME:", self)
        self.lbd_nome = QLineEdit(self)
        self.lbd_nome.setPlaceholderText("Digite seu nome: ")

        self.lbl_telefone = QLabel("TELEFONE:", self)
        self.lbd_telefone = QLineEdit(self)
        self.lbd_telefone.setValidator(QIntValidator())
        self.lbd_telefone.setPlaceholderText("Digite seu numero de telefone")

        self.lbl_email = QLabel("EMAIL:", self)
        self.lbd_email = QLineEdit(self)
        self.lbd_email.setPlaceholderText("Digite seu email")

        self.lbl_genero = QLabel("GÊNERO:")
        self.ck_genero = QComboBox()
        self.ck_genero.addItem("Masculino")
        self.ck_genero.addItem("Feminino")
        self.ck_genero.addItem("Outro")
        self.ck_genero.setStyleSheet(f"background-color: {self.Color_Black.name()};")


        self.lbl_nascimento = QLabel("NASCIMENTO:", self)
        self.lbd_nascimento = QDateEdit()
        self.lbd_nascimento.setDisplayFormat("dd/MM/yyyy")
        self.lbd_nascimento.setCalendarPopup(True)
        self.lbd_idade = QLineEdit(self)
        self.lbd_idade.setPlaceholderText("Digite sua idade em anos")
        self.lbd_idade.setValidator(QIntValidator())
        
        self.ck_PCD = QCheckBox("PCD",self)

        self.button_cadastrar = QPushButton("Cadastrar Paciente")
        self.button_cadastrar.clicked.connect(self.Adiction)
        
        self.button_remove = QPushButton("Chamar Próximo")
        self.button_remove.clicked.connect(self.CallPatient)
        
        self.lista_espera = QTextBrowser(self)


        self.frame_layout.addWidget(self.welcome)
        self.frame_layout.addWidget(self.lbl_nome)
        self.frame_layout.addWidget(self.lbd_nome)
        self.frame_layout.addWidget(self.lbl_telefone)
        self.frame_layout.addWidget(self.lbd_telefone)
        self.frame_layout.addWidget(self.lbl_email)
        self.frame_layout.addWidget(self.lbd_email)
        self.frame_layout.addWidget(self.lbl_genero)
        self.frame_layout.addWidget(self.ck_genero)
        self.frame_layout.addWidget(self.lbl_nascimento)
        self.frame_layout.addWidget(self.lbd_nascimento)
        self.frame_layout.addWidget(self.lbd_idade)
        self.frame_layout.addWidget(self.ck_PCD)
        self.frame_layout.addWidget(self.button_cadastrar)
        self.frame_layout.addWidget(self.button_remove)
        self.frame_layout.addWidget(self.lista_espera)

        self.list = []

    def Adiction(self):
            __name = self.lbd_nome.text()
            __fone = self.lbd_telefone.text()
            __email = self.lbd_email.text()
            __genero = self.ck_genero.currentText()
            __hora = datetime.now()
            __horario_atual = __hora.strftime('%H:%M:%S')
            __nascimento = self.lbd_nascimento.date().toPython()
            __idade = self.lbd_idade.text() 
            # __name, __horario_atual, __nascimento, __email, __fone, __genero
            
            if self.ck_PCD.isChecked():
                paciente = TestingPacientePCD(__name, __horario_atual, __nascimento, __email, __fone, __genero)
                cursor = self.lista_espera.textCursor()
                cursor.movePosition(QTextCursor.Start)
                cursor.insertText(f"Paciente: {paciente}\n")
                cursor.movePosition(QTextCursor.Start)
            else:
                paciente = TestingPaciente(__name, __horario_atual, __nascimento, __email, __fone, __genero)
                self.lista_espera.append(f"Paciente: {paciente}")

            self.lbd_nome.clear()
            self.lbd_email.clear()
            self.lbd_telefone.clear()
            self.ck_PCD.setChecked(False)
            self.lbd_idade.clear()
            self.lbd_nascimento.setDate(datetime.now().date())

    def CallPatient(self):
        text = self.lista_espera.toPlainText()
        lines = text.split('\n')

        if lines:
            lines.pop(0)
        
        new_text = '\n'.join(lines)
        self.lista_espera.setPlainText(new_text)





            
if __name__ == "__main__":    
    import sys
    App = QApplication(sys.argv)
    Janela = MainWindow()
    Janela.show()
    App.exec()

