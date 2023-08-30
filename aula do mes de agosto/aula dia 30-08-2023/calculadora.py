class calculadora():
    
    def calcular(self,op):
        if op == 'adição':
            resultado = self.__adicionar()
            return resultado
            
        elif op == 'subtração':
            resultado = self.__subtracao()
            return resultado
            
    def __adicionar(self):
        num = int(input("Digite um numero: "))
        num2 = int(input('Digite outro numero: ')) 
        
        soma = num + num2       
    
        return soma
    
    def __subtracao(self):
        num = int(input("Digite um numero: "))
        num2 = int(input('Digite outro numero: ')) 
        
        subtra = num - num2       
        
        return subtra
    
opcao = input('Digite a opção que você quer: ') 
calculadora_1 = calculadora()
print(calculadora_1.calcular(opcao))
