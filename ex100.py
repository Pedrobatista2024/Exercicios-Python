from random import randint
from time import sleep
from tokenize import endpats



def sorteia(lista):
    print('Sorteando 5 valores para lista: ', end='')
    for cont in range(1, 6):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO')

def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista}, temos {soma}')

lista = []
sorteia(lista)
somaPar(lista)
