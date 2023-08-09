from formato import formato

class circulo(formato):
    def __init__(self,raio):
        super().__init__()
        
        self.raio = raio
        
    def area_circulo(self):
        
        resultado_circulo = 3.14*(self.raio**2)
        return resultado_circulo