galera = []
lista = []
pesados = []
maneiros = []
cont = 0
while True :
    continua = ' '
    lista.append(str(input('Digite o nome: ')))
    lista.append(int(input('Digite o peso: ')))
    galera.append(lista[:])
    lista.clear()
    cont +=1
    while continua not in ['S', 'N']:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continua == 'N':
        break
print(f'Ao todo {cont} pessoas foram cadastradas')
for p in galera:
    if p[1] > 80:
        pesados.append(p[0])
    else :
        maneiros.append(p[0])
print('As pessoas mais pesadas (acima de 80kg) são: ')
for p in pesados:
    print(p)
print('As pessoas mais maneiras(abaixo de 80kg) são: ')
for p in maneiros:
    print(p)