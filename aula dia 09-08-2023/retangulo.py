from formato import formato

class retangulo(formato):
    def __init__(self,base,altura):
        super().__init__()
        
        self.base = base
        self.altura = altura
        
    def area_retangulo(self):
        
        resultado_retangulo = self.base * self.altura
        return resultado_retangulo
        