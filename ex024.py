cidade = input('Digite o nome da sua cidade: ')
cidade1 = cidade.split()
resposta = 'santo' in cidade.lower().split()[0]
if resposta == True :
    resposta = 'SIM'
else :
    resposta = 'NÃO'
print('o nome da sua cidade começa com santo: {}'.format(resposta))