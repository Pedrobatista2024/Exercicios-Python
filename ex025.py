nome = input('Digite o nome da seu nome: ')
resposta = 'silva' in nome.lower()
if resposta == True :
    resposta = 'SIM'
else :
    resposta = 'NÃO'
print('No seu nome contem (Silva): {}'.format(resposta))