from random import randint
from time import sleep
from operator import itemgetter
jogadas = {}
for c in range(1, 5):
   jogadas[f'jogador {c}'] = randint(1, 6)
ranking = ()
for k, v in jogadas.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f' {i+1}º Lugar: {v[0]} com {v[1]}. ')
    sleep(1)



'''posição = 0
jogadas = {}
for c in range(1, 5):
   jogadas[f'jogador {c}'] = randint(1, 6)
for i, v in enumerate(jogadas.values()):
    print(f'O jogador {i+1} tirou {v}')
    sleep(1)
print('RANKING')
organizado = dict(sorted(jogadas.items(), key=lambda item: item[1]))
for chave, valor in reversed(organizado.items()):
    posição +=1
    print(f'{posição}º Lugar {chave}: com {valor}')
    sleep(1)'''
