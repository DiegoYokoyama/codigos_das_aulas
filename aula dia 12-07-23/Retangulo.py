class Retangulo:

    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
        

    def areaRetangulo(self):
        self.area = self.base * self.altura
        print(self.area)


    def Perimetro(self):
        self.perimetr = (self.base * 2) + (self.altura * 2)
        print(self.perimetr)
    
    
    def MudarValorDosLados(self,base_mudar,altura_mudar):
        self.base=base_mudar
        self.altura=altura_mudar
        self.area = self.base * self.altura

        self.perimetr = (self.base * 2) + (self.altura * 2)
        print('Novo valor da base: ',self.base)
        print('Novo valor da altura: ',self.altura)
    
    def QuinzePorcento (self,area):
        self.quinze*0.15

