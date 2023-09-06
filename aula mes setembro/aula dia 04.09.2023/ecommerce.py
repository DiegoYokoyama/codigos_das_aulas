class CarrinhoCompra():
    def __init__(self) :
        self.produto =[]
        
    def inserir_produto(self, produtos: str):
        self.produto.append(produtos)
    
    def lista_produto(self):
        for produto in self.produto:
            print(produto.nome, produto.preco)
    
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total +=produto.preco
            return total
        
    
class produto:
    def __init__(self,nome,preco) -> None:
        self.nome = nome
        self.preco = preco
        
carrinho = CarrinhoCompra