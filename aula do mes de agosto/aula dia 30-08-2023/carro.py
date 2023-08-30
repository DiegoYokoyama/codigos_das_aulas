class carro:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca
        
    def acelerar(self):
        print('Acelerar')
        
    def freiar(self):
        print('Freiar')
        
    def passar_marcha(self,marcha):
        print(f'Passar Marcha {marcha}')
        

carro_1 = carro ('Chevrolet', 'Toyota')
carro_2 = carro ('Volkswagen','BMW')

print('modelo do carro 1: ',carro_1.modelo, 'modelo do carro 2:', carro_2.modelo)
print('marca do carro 1: ', carro_1.marca, 'marca do carro 2: ', carro_2.marca)
carro_1.passar_marcha (1)