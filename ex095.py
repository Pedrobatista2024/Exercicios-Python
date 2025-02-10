jogador = {}
partida = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantantas partidas o jogador {jogador['nome']} fez? '))
    partida.clear()
    for c in range(0, tot):
        partida.append(int(input(f'Quantos gols na partida {c}: ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()
        if continua in ['S', 'N']:
            break
    if continua == 'N':
        break
print('*%*#*' * 12)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('*%*#*' * 12)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('*%*#*' * 12)
while True:
    busca = int(input('Você quer ver os numeros de qual jogador?? (999 para encerrar)'))
    if busca == 999:
        break
    if busca > len(time):
        print(f'não existe jogador {busca}. ')
    else:
        print(f'Dados do jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo {i} fez {g} gols')
    print('*%*#*' * 12)
print('VOLTE SEMPRE!')

