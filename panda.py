import pandas as pd
tabela_vendas=pd.read_excel('Vendas.xlsx')
print(tabela_vendas)
print(tabela_vendas.shape)
print(tabela_vendas.head())
print(tabela_vendas.describe())