class Quadrado:


    def __init__(self,tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    
    def AreaQuadrado(self):
        self.area = self.tamanho_do_lado **2
        print(self.area)
    

    def MudarValorLado (self,mudar_valor):
        self.tamanho_do_lado = mudar_valor
        self.area = self.tamanho_do_lado **2
        print(self.area)
        print(self.tamanho_do_lado)