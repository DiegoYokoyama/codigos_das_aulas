import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial
    
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False
    
    def saque(self, valor):
        if valor > 0 and self.saldo >= valor + 5:
            self.saldo -= valor + 5
            return True
        return False


class BancoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Banco App")

        self.numero_conta_label = QLabel("Número da Conta:")
        self.nome_titular_label = QLabel("Nome do Titular:")
        self.valor_deposito_label = QLabel("Valor de Depósito:")
        self.valor_saque_label = QLabel("Valor de Saque:")

        self.numero_conta_input = QLineEdit()
        self.nome_titular_input = QLineEdit()
        self.valor_deposito_input = QLineEdit()
        self.valor_saque_input = QLineEdit()

        self.cadastrar_button = QPushButton("Cadastrar")
        self.deposito_button = QPushButton("Depósito")
        self.saque_button = QPushButton("Saque")

        layout = QVBoxLayout()
        layout.addWidget(self.numero_conta_label)
        layout.addWidget(self.numero_conta_input)
        layout.addWidget(self.nome_titular_label)
        layout.addWidget(self.nome_titular_input)
        layout.addWidget(self.valor_deposito_label)
        layout.addWidget(self.valor_deposito_input)
        layout.addWidget(self.cadastrar_button)
        layout.addWidget(self.valor_saque_label)
        layout.addWidget(self.valor_saque_input)
        layout.addWidget(self.deposito_button)
        layout.addWidget(self.saque_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.conta = None

        self.cadastrar_button.clicked.connect(self.cadastrar_conta)
        self.deposito_button.clicked.connect(self.realizar_deposito)
        self.saque_button.clicked.connect(self.realizar_saque)

    def cadastrar_conta(self):
        numero_conta = self.numero_conta_input.text()
        nome_titular = self.nome_titular_input.text()
        try:
            saldo_inicial = float(self.valor_deposito_input.text())
        except ValueError:
            saldo_inicial = 0

        self.conta = ContaBancaria(numero_conta, nome_titular, saldo_inicial)
        self.mostrar_dados_conta()

    def realizar_deposito(self):
        if self.conta:
            try:
                valor_deposito = float(self.valor_deposito_input.text())
                if self.conta.deposito(valor_deposito):
                    self.mostrar_dados_conta()
                else:
                    print("Valor de depósito inválido.")
            except ValueError:
                print("Valor de depósito inválido.")

    def realizar_saque(self):
        if self.conta:
            try:
                valor_saque = float(self.valor_saque_input.text())
                if self.conta.saque(valor_saque):
                    self.mostrar_dados_conta()
                else:
                    print("Valor de saque inválido.")
            except ValueError:
                print("Valor de saque inválido.")

    def mostrar_dados_conta(self):
        if self.conta:
            print("Número da Conta:", self.conta.numero_conta)
            print("Titular:", self.conta.nome_titular)
            print("Saldo Atual:", self.conta.saldo)
            print("=" * 30)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BancoApp()
    window.show()
    sys.exit(app.exec_())