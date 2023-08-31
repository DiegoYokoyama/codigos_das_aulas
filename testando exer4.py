import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTextBrowser, QCheckBox, QComboBox, QDateEdit, QMessageBox
from datetime import datetime, timedelta

class Paciente:
    def __init__(self, nome, telefone, email, genero, data_nascimento, pcd=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.genero = genero
        self.data_nascimento = data_nascimento
        self.pcd = pcd
        self.chegada_fila = datetime.now()
    
    def __str__(self):
        return self.nome

class Consultorio(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Consultório Médico")
        self.setGeometry(100, 100, 400, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.info_label = QLabel("Digite os dados do paciente:")
        self.layout.addWidget(self.info_label)

        self.txt_nome = QLineEdit()
        self.txt_nome.setPlaceholderText("Nome")
        self.layout.addWidget(self.txt_nome)

        self.txt_telefone = QLineEdit()
        self.txt_telefone.setPlaceholderText("Telefone")
        self.layout.addWidget(self.txt_telefone)

        self.txt_email = QLineEdit()
        self.txt_email.setPlaceholderText("Email")
        self.layout.addWidget(self.txt_email)

        self.cb_genero = QComboBox()
        self.cb_genero.addItem("Outro")
        self.cb_genero.addItem("Masculino")
        self.cb_genero.addItem("Feminino")
        self.layout.addWidget(self.cb_genero)

        self.txt_data_nascimento = QDateEdit()
        self.txt_data_nascimento.setDisplayFormat("dd/MM/yyyy")
        self.txt_data_nascimento.setCalendarPopup(True)
        self.layout.addWidget(self.txt_data_nascimento)

        self.ck_pcd = QCheckBox("Pessoa com Deficiência")
        self.layout.addWidget(self.ck_pcd)

        self.btn_cadastrar_botao = QPushButton("Cadastrar Paciente")
        self.btn_cadastrar_botao.clicked.connect(self.cadastrar_paciente)
        self.layout.addWidget(self.btn_cadastrar_botao)

        self.btn_chamar_proximo_botao = QPushButton("Chamar Próximo")
        self.btn_chamar_proximo_botao.clicked.connect(self.chamar_proximo_paciente)
        self.layout.addWidget(self.btn_chamar_proximo_botao)

        self.txtb_exibir_fila = QTextBrowser()
        self.layout.addWidget(self.txtb_exibir_fila)

        self.central_widget.setLayout(self.layout)

        self.fila_espera = []

    def cadastrar_paciente(self):
        try:
            nome = self.txt_nome.text()
            telefone = self.txt_telefone.text()
            email = self.txt_email.text()
            genero = self.cb_genero.currentText()
            data_nascimento = self.txt_data_nascimento.date().toPython()
            pcd = self.ck_pcd.isChecked()

            hora_chegada = datetime.now() #tentar arrumar o horario 

            paciente = Paciente(nome, telefone, email, genero, data_nascimento, pcd)
            paciente.chegada_fila = hora_chegada  #tentar arrumar o horario

            self.adicionar_paciente_na_fila(paciente)

            self.txtb_exibir_fila.append(f"Paciente cadastrado: {paciente}")

            self.txt_nome.clear()
            self.txt_telefone.clear()
            self.txt_email.clear()
            self.cb_genero.setCurrentIndex(0)
            self.txt_data_nascimento.setDate(datetime.now().date())
            self.ck_pcd.setChecked(False)

        except ValueError:
            QMessageBox.critical(self, "Erro de Entrada", "Certifique-se de que os campos foram preenchidos corretamente.")

    def adicionar_paciente_na_fila(self, paciente):
        if paciente.data_nascimento <= (datetime.now() - timedelta(days=365*60)).date():
            self.fila_espera.insert(0, paciente)
        else:
            self.fila_espera.append(paciente)

        self.atualizar_fila()

    def atualizar_fila(self):
        self.fila_espera.sort(key=lambda paciente: (paciente.pcd, paciente.data_nascimento, paciente.genero, paciente.chegada_fila,))
        self.txtb_exibir_fila.clear()
        for idx, paciente in enumerate(self.fila_espera):
            tempo_espera = datetime.now() - paciente.chegada_fila
            self.txtb_exibir_fila.append(f"{idx+1}. {paciente.nome} - {'PCD' if paciente.pcd else 'Não PCD'} data de nascimento: {paciente.data_nascimento} - genero: {paciente.genero} - Tempo de Espera: {tempo_espera}")
            
    def chamar_proximo_paciente(self):
        if self.fila_espera:
            paciente_chamado = self.fila_espera.pop(0)
            self.txtb_exibir_fila.clear()
            self.txtb_exibir_fila.append(f"Chamando: {paciente_chamado.nome}")
            self.atualizar_fila()
        else:
            self.txtb_exibir_fila.clear()
            self.txtb_exibir_fila.append("A fila está vazia.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    consultorio = Consultorio()
    consultorio.show()
    sys.exit(app.exec())