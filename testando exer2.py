import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTextBrowser, QCheckBox

class Funcionario:
    def __init__(self, nome, horas_trabalhadas, valor_por_hora, terceirizado=False, despesa_adicional=0):
        self.nome = nome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_por_hora = valor_por_hora
        self.terceirizado = terceirizado
        self.despesa_adicional = despesa_adicional
    
    def calcular_pagamento(self):
        pagamento = self.horas_trabalhadas * self.valor_por_hora
        if self.terceirizado:
            pagamento += 1.1 * self.despesa_adicional
        return pagamento
    
    def __str__(self):
        return f"Nome: {self.nome}, Pagamento: {self.calcular_pagamento()}"

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora de Pagamento de Funcionários")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.info_label = QLabel("Digite os dados do funcionário:")
        self.layout.addWidget(self.info_label)

        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Nome")
        self.layout.addWidget(self.nome_input)

        self.horas_input = QLineEdit()
        self.horas_input.setPlaceholderText("Horas Trabalhadas")
        self.layout.addWidget(self.horas_input)

        self.valor_por_hora_input = QLineEdit()
        self.valor_por_hora_input.setPlaceholderText("Valor por Hora")
        self.layout.addWidget(self.valor_por_hora_input)

        self.terceirizado_checkbox = QCheckBox("Terceirizado")
        self.layout.addWidget(self.terceirizado_checkbox)

        self.despesa_adicional_input = QLineEdit()
        self.despesa_adicional_input.setPlaceholderText("Despesa Adicional (para funcionários terceirizados)")
        self.layout.addWidget(self.despesa_adicional_input)

        self.adicionar_botao = QPushButton("Adicionar Funcionário")
        self.adicionar_botao.clicked.connect(self.adicionar_funcionario)
        self.layout.addWidget(self.adicionar_botao)

        self.exibir_texto = QTextBrowser()
        self.layout.addWidget(self.exibir_texto)

        self.central_widget.setLayout(self.layout)

        self.funcionarios = []

    def adicionar_funcionario(self):
        nome = self.nome_input.text()
        horas_trabalhadas = float(self.horas_input.text())
        valor_por_hora = float(self.valor_por_hora_input.text())
        terceirizado = self.terceirizado_checkbox.isChecked()
        despesa_adicional = float(self.despesa_adicional_input.text()) if terceirizado else 0
        
        funcionario = Funcionario(nome, horas_trabalhadas, valor_por_hora, terceirizado, despesa_adicional)
        self.funcionarios.append(funcionario)

        self.exibir_texto.append(f"Funcionário adicionado: {funcionario}")
        
        self.nome_input.clear()
        self.horas_input.clear()
        self.valor_por_hora_input.clear()
        self.despesa_adicional_input.clear()
        self.terceirizado_checkbox.setChecked(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec_())