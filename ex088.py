''''from random import randint
lista = []
numero = int(input('Quantos jogos você quer gerar?'))
for cont in range(1, numero + 1):
    cont = 0
    while True:
        sorteio = randint(1, 60)
        if sorteio not in lista:
            lista.append(sorteio)
            cont +=1
        if cont >= 6:
            break
    print(sorted(lista))
    lista.clear()
    print()'''
from random import randint
lista = []
jogos = []
tot = 1
jogo = int(input('Quantos jogos você quer??'))
print(f'Os numeros sorteados foram:')
while tot <= jogo:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont +=1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
