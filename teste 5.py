import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QListWidget, QMessageBox

class Produto:
    def __init__(self, nome, preco_unitario, quantidade):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade

class CadastroWindow(QWidget):
    def __init__(self, mercado):
        super().__init__()
        self.mercado = mercado
        self.setWindowTitle('Cadastro de Produtos')
        self.layout = QVBoxLayout()
        self.nome_label = QLabel('Nome do Produto:')
        self.nome_input = QLineEdit()
        self.preco_label = QLabel('Preço Unitário:')
        self.preco_input = QLineEdit()
        self.quantidade_label = QLabel('Quantidade em Estoque:')
        self.quantidade_input = QLineEdit()
        self.cadastrar_button = QPushButton('Cadastrar')
        self.cadastrar_button.clicked.connect(self.cadastrar_produto)
        self.layout.addWidget(self.nome_label)
        self.layout.addWidget(self.nome_input)
        self.layout.addWidget(self.preco_label)
        self.layout.addWidget(self.preco_input)
        self.layout.addWidget(self.quantidade_label)
        self.layout.addWidget(self.quantidade_input)
        self.layout.addWidget(self.cadastrar_button)
        self.setLayout(self.layout)

    def cadastrar_produto(self):
        nome = self.nome_input.text()
        preco = float(self.preco_input.text())
        quantidade = int(self.quantidade_input.text())
        produto = Produto(nome, preco, quantidade)
        self.mercado.produtos.append(produto)
        self.nome_input.clear()
        self.preco_input.clear()
        self.quantidade_input.clear()
        QMessageBox.information(self, 'Cadastro', 'Produto cadastrado com sucesso!')

class EstoqueWindow(QWidget):
    def __init__(self, mercado):
        super().__init__()
        self.mercado = mercado
        self.setWindowTitle('Estoque de Produtos')
        self.layout = QVBoxLayout()
        self.lista_produtos = QListWidget()
        self.atualizar_lista_produtos()
        self.layout.addWidget(self.lista_produtos)
        self.setLayout(self.layout)

    def atualizar_lista_produtos(self):
        self.lista_produtos.clear()
        for produto in self.mercado.produtos:
            self.lista_produtos.addItem(f'{produto.nome} - Preço: R${produto.preco_unitario:.2f} - Estoque: {produto.quantidade}')

class VendasWindow(QWidget):
    def __init__(self, mercado):
        super().__init__()
        self.mercado = mercado
        self.setWindowTitle('Realizar Venda')
        self.layout = QVBoxLayout()
        self.lista_produtos = QComboBox()
        self.atualizar_lista_produtos()
        self.layout.addWidget(self.lista_produtos)
        self.quantidade_label = QLabel('Quantidade Vendida:')
        self.quantidade_input = QLineEdit()
        self.calcular_button = QPushButton('Calcular Valor')
        self.calcular_button.clicked.connect(self.calcular_valor)
        self.valor_label = QLabel('Valor Total:')
        self.layout.addWidget(self.quantidade_label)
        self.layout.addWidget(self.quantidade_input)
        self.layout.addWidget(self.calcular_button)
        self.layout.addWidget(self.valor_label)
        self.setLayout(self.layout)

    def atualizar_lista_produtos(self):
        self.lista_produtos.clear()
        for produto in self.mercado.produtos:
            self.lista_produtos.addItem(f'{produto.nome}')

    def calcular_valor(self):
        produto_index = self.lista_produtos.currentIndex()
        quantidade_vendida = int(self.quantidade_input.text())
        if produto_index >= 0:
            produto = self.mercado.produtos[produto_index]
            if quantidade_vendida > 0 and quantidade_vendida <= produto.quantidade:
                valor_total = produto.preco_unitario * quantidade_vendida
                self.valor_label.setText(f'Valor Total: R${valor_total:.2f}')
                produto.quantidade -= quantidade_vendida
                self.atualizar_lista_produtos()
                QMessageBox.information(self, 'Venda', f'Venda realizada com sucesso! Total: R${valor_total:.2f}')
                self.quantidade_input.clear()
            else:
                QMessageBox.warning(self, 'Venda', 'Quantidade em estoque insuficiente ou quantidade inválida.')
        else:
            QMessageBox.warning(self, 'Venda', 'Selecione um produto da lista.')

class MercadoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sistema de Cadastro e Gestão de Mercado')
        self.setGeometry(100, 100, 600, 400)
        self.produtos = []

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.cadastro_button = QPushButton('Cadastro')
        self.estoque_button = QPushButton('Estoque')
        self.vendas_button = QPushButton('Vendas')

        self.cadastro_button.clicked.connect(self.mostrar_cadastro)
        self.estoque_button.clicked.connect(self.mostrar_estoque)
        self.vendas_button.clicked.connect(self.mostrar_vendas)

        self.layout.addWidget(self.cadastro_button)
        self.layout.addWidget(self.estoque_button)
        self.layout.addWidget(self.vendas_button)

        self.central_widget.setLayout(self.layout)

    def mostrar_cadastro(self):
        self.cadastro_window = CadastroWindow(self)
        self.cadastro_window.show()

    def mostrar_estoque(self):
        self.estoque_window = EstoqueWindow(self)
        self.estoque_window.show()

    def mostrar_vendas(self):
        self.vendas_window = VendasWindow(self)
        self.vendas_window.show()

def main():
    app = QApplication(sys.argv)
    mercado_app = MercadoApp()
    mercado_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()