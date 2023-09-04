class TestingPaciente():
    def __init__(self, nome, hora, nascimento, email, telefone, genero) -> None:
       self.nome = nome
       self.hora = hora
       self.nascimento = nascimento
       self.email = email
       self.telefone = telefone
       self.genero = genero 
        
    def __str__(self):
        return f"{self.nome} do genero {self.genero} entrou {self.hora} nascido em {self.nascimento}"
    
class TestingPacientePCD(TestingPaciente):
    def __init__(self, nome, hora, nascimento, email, telefone, genero) -> None:
        super().__init__(nome, hora, nascimento, email, telefone, genero)

    def __str__(self):
        return f"{self.nome} PCD, do genero {self.genero} entrou {self.hora} nascido em {self.nascimento}"
    
class TesingPaciente60(TestingPacientePCD):
    def __init__(self, nome, hora, nascimento, email, telefone, genero, idade) -> None:
        super().__init__(nome, hora, nascimento, email, telefone, genero)

        self.idade = idade

    def __str__(self):
        return f"{self.nome} PCD, do genero {self.genero} entrou {self.hora} nascido em {self.nascimento} ({self.idade})"