import wikipedia
busca=input('digite sua resposta: ')
wiki=wikipedia.set_lang('pt')
resposta=wikipedia.summary(busca)
print(resposta)