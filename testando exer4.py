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

        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Nome")
        self.layout.addWidget(self.nome_input)

        self.telefone_input = QLineEdit()
        self.telefone_input.setPlaceholderText("Telefone")
        self.layout.addWidget(self.telefone_input)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.layout.addWidget(self.email_input)

        self.genero_combo = QComboBox()
        self.genero_combo.addItem("Masculino")
        self.genero_combo.addItem("Feminino")
        self.genero_combo.addItem("Outro")
        self.layout.addWidget(self.genero_combo)

        self.data_nascimento_input = QDateEdit()
        self.data_nascimento_input.setDisplayFormat("dd/MM/yyyy")
        self.data_nascimento_input.setCalendarPopup(True)
        self.layout.addWidget(self.data_nascimento_input)

        self.pcd_checkbox = QCheckBox("Pessoa com Deficiência")
        self.layout.addWidget(self.pcd_checkbox)

        self.cadastrar_botao = QPushButton("Cadastrar Paciente")
        self.cadastrar_botao.clicked.connect(self.cadastrar_paciente)
        self.layout.addWidget(self.cadastrar_botao)

        self.chamar_proximo_botao = QPushButton("Chamar Próximo")
        self.chamar_proximo_botao.clicked.connect(self.chamar_proximo_paciente)
        self.layout.addWidget(self.chamar_proximo_botao)

        self.exibir_fila_texto = QTextBrowser()
        self.layout.addWidget(self.exibir_fila_texto)

        self.central_widget.setLayout(self.layout)

        self.fila_espera = []

    def cadastrar_paciente(self):
        try:
            nome = self.nome_input.text()
            telefone = self.telefone_input.text()
            email = self.email_input.text()
            genero = self.genero_combo.currentText()
            data_nascimento = self.data_nascimento_input.date().toPython()
            pcd = self.pcd_checkbox.isChecked()
            
            paciente = Paciente(nome, telefone, email, genero, data_nascimento, pcd)
            self.adicionar_paciente_na_fila(paciente)
            
            self.exibir_fila_texto.append(f"Paciente cadastrado: {paciente}")
            
            self.nome_input.clear()
            self.telefone_input.clear()
            self.email_input.clear()
            self.genero_combo.setCurrentIndex(0)
            self.data_nascimento_input.setDate(datetime.now().date())
            self.pcd_checkbox.setChecked(False)
            
        except ValueError:
            QMessageBox.critical(self, "Erro de Entrada", "Certifique-se de que os campos foram preenchidos corretamente.")

    def adicionar_paciente_na_fila(self, paciente):
        if paciente.data_nascimento <= datetime.now() - timedelta(days=365*60):
            self.fila_espera.insert(0, paciente)  # Paciente com mais de 60 anos no início da fila
        else:
            self.fila_espera.append(paciente)  # Paciente no final da fila

        self.atualizar_fila()

    def atualizar_fila(self):
        self.fila_espera.sort(key=lambda paciente: (paciente.pcd, paciente.data_nascimento, paciente.chegada_fila))
        self.exibir_fila_texto.clear()
        for idx, paciente in enumerate(self.fila_espera):
            tempo_espera = datetime.now() - paciente.chegada_fila
            self.exibir_fila_texto.append(f"{idx+1}. {paciente.nome} - {'PCD' if paciente.pcd else 'Não PCD'} - Tempo de Espera: {tempo_espera}")
            
    def chamar_proximo_paciente(self):
        if self.fila_espera:
            paciente_chamado = self.fila_espera.pop(0)
            self.exibir_fila_texto.clear()
            self.exibir_fila_texto.append(f"Chamando: {paciente_chamado.nome}")
            self.atualizar_fila()
        else:
            self.exibir_fila_texto.clear()
            self.exibir_fila_texto.append("A fila está vazia.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    consultorio = Consultorio()
    consultorio.show()
    sys.exit(app.exec_())