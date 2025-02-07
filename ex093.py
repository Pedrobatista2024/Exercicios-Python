'''dados = {}
gols = []
soma = 0
dados['nome'] = str(input('Nome: '))
dados['jogos'] = int(input(f'Quantas partidas {dados['nome']} jogou? '))
for c in range(1, dados['jogos'] + 1):
    golos = (int(input(f'Quantos gols na {c}º partida? ')))
    soma += golos
    gols.append(golos)
    dados['golsp'] = gols
dados['totgol'] = soma
print( '*%*#*'* 15)
print(dados)
print('*%*#*' * 15)
print(f'Nome = {dados['nome']}')
print(f'gols = {dados['golsp']}')
print(f'Total de gols = {dados['totgol']}')
print('*%*#*' * 15)
for i in range(len(dados['golsp'])):
    f = i + 1
    print(f'Na partida {f}, fez {dados['golsp'][i]}')'''

'''for i, g in enumerate(dados['golsp']):
    f = i + 1
    print(f'Na partida {f}, fez {g} gols')'''

jogador = {}
partida = []
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantantas partidas o jogador {jogador['nome']} fez? '))
for c in range(0, tot):
    partida.append(int(input(f'Quantos gols na partida {c}: ')))
jogador['gols'] = partida[:]
jogador['total'] = sum(partida)
print('*%*#*'* 15)
print(jogador)
print('*%*#*'* 15)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('*%*#*'* 15)
for i, v in enumerate(jogador['gols']):
    print(f' na partida {i}, fez {v} gols')