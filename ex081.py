lista = []
cont = 0
while True:
    cont += 1
    continua = ' '
    lista.append(int(input(f'Digite o {cont}º numero: ')))
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).strip().upper()
    if continua == 'N':
        break
print(f'Você digitou {len(lista)} numeros.')
print(f'A lista de valores {sorted(lista,reverse=True)}')
if 5 in lista:
    print('O 5 esta na lista')
else:
    print('5 não esta na lista')
