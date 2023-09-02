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
        self.lbl_nome = QLabel('Nome do Produto:')
        self.txt_nome = QLineEdit()
        self.lbl_preco = QLabel('Preço Unitário:')
        self.txt_preco = QLineEdit()
        self.lbl_quantidade = QLabel('Quantidade em Estoque:')
        self.txt_quantidade = QLineEdit()
        self.btn_cadastrar_button = QPushButton('Cadastrar')
        self.btn_cadastrar_button.clicked.connect(self.cadastrar_produto)
        self.layout.addWidget(self.lbl_nome)
        self.layout.addWidget(self.txt_nome)
        self.layout.addWidget(self.lbl_preco)
        self.layout.addWidget(self.txt_preco)
        self.layout.addWidget(self.lbl_quantidade)
        self.layout.addWidget(self.txt_quantidade)
        self.layout.addWidget(self.btn_cadastrar_button)
        self.setLayout(self.layout)

    def cadastrar_produto(self):
        nome = self.txt_nome.text()
        preco = float(self.txt_preco.text())
        quantidade = int(self.txt_quantidade.text())
        produtos = Produto(nome, preco, quantidade)
        self.mercado.produtos.append(produtos)
        self.txt_nome.clear()
        self.txt_preco.clear()
        self.txt_quantidade.clear()
        QMessageBox.information(self, 'Cadastro', 'Produto cadastrado com sucesso!')

class EstoqueWindow(QWidget):
    def __init__(self, mercado):
        super().__init__()
        self.mercado = mercado
        self.setWindowTitle('Estoque de Produtos')
        self.layout = QVBoxLayout()
        self.list_produtos = QListWidget()
        self.atualizar_lista_produtos()
        self.layout.addWidget(self.list_produtos)
        self.setLayout(self.layout)

    def atualizar_lista_produtos(self):
        self.list_produtos.clear()
        for produto in self.mercado.produtos:
            self.list_produtos.addItem(f'{produto.nome} - Preço: R${produto.preco_unitario:.2f} - Estoque: {produto.quantidade}')

class VendasWindow(QWidget):
    def __init__(self, mercado):
        super().__init__()
        self.mercado = mercado
        self.setWindowTitle('Realizar Venda')
        self.layout = QVBoxLayout()
        self.lista_produtos = QComboBox()
        self.atualizar_lista_produtos()
        self.layout.addWidget(self.lista_produtos)
        self.lbl_quantidade = QLabel('Quantidade Vendida:')
        self.txt_quantidade = QLineEdit()
        self.btn_calcular_button = QPushButton('Calcular Valor')
        self.btn_calcular_button.clicked.connect(self.calcular_valor)
        self.lbl_valor = QLabel('Valor Total:')
        self.layout.addWidget(self.lbl_quantidade)
        self.layout.addWidget(self.txt_quantidade)
        self.layout.addWidget(self.btn_calcular_button)
        self.layout.addWidget(self.lbl_valor)
        self.setLayout(self.layout)

    def atualizar_lista_produtos(self):
        self.lista_produtos.clear()
        for produto in self.mercado.produtos:
            self.lista_produtos.addItem(f'{produto.nome}')

    def calcular_valor(self):
        produto_index = self.lista_produtos.currentIndex()
        quantidade_vendida = int(self.txt_quantidade.text())
        if produto_index >= 0:
            produto = self.mercado.produtos[produto_index]
            if quantidade_vendida > 0 and quantidade_vendida <= produto.quantidade:
                valor_total = produto.preco_unitario * quantidade_vendida
                self.lbl_valor.setText(f'Valor Total: R${valor_total:.2f}')
                produto.quantidade -= quantidade_vendida
                self.atualizar_lista_produtos()
                QMessageBox.information(self, 'Venda', f'Venda realizada com sucesso! Total: R${valor_total:.2f}')
                self.txt_quantidade.clear()
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
        self.btn_cadastro_button = QPushButton('Cadastro')
        self.btn_estoque_button = QPushButton('Estoque')
        self.btn_vendas_button = QPushButton('Vendas')

        self.btn_cadastro_button.clicked.connect(self.mostrar_cadastro)
        self.btn_estoque_button.clicked.connect(self.mostrar_estoque)
        self.btn_vendas_button.clicked.connect(self.mostrar_vendas)

        self.layout.addWidget(self.btn_cadastro_button)
        self.layout.addWidget(self.btn_estoque_button)
        self.layout.addWidget(self.btn_vendas_button)

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