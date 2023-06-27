import re

# Texto de exemplo
texto = "O gato preto cruzou o caminho do cachorro preto."
# Padrão de expressão regular para substituir palavras
padrao_substituicao = r"preto"
# Substituir todas as ocorrências da palavra "preto" por "branco"
texto_substituido = re.sub(padrao_substituicao, "branco", texto)
print("Texto original:", texto)
print("Texto substituído:", texto_substituido)
#------------------------------------------------------

# Lista de endereços de e-mail de exemplo
emails = [
    "usuario@example.com",
    "usuario@dominio.com.br",
    "meu.email@empresa.co",
    "contato@123.abc",
    "email.invalido",
]
# Padrão de expressão regular para validar endereços de e-mail
padrao_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
# Verificar se os endereços de e-mail são válidos
for email in emails:
    if re.match(padrao_email, email):
        print(f"O endereço de e-mail '{email}' é válido.")
    else:
        print(f"O endereço de e-mail '{email}' é inválido.")
#------------------------------------------------------------------------

# Texto de exemplo
texto = "Olá! Meu número de telefone é (123) 456-7890. Por favor, me ligue."
# Padrão de expressão regular para encontrar números de telefone
padrao_telefone = r"\(\d{3}\) \d{3}-\d{4}"
# Procurar por números de telefone no texto
numeros_telefone = re.findall(padrao_telefone, texto)
# Imprimir os números de telefone encontrados
for numero in numeros_telefone:
    print("Número de telefone encontrado:", numero)