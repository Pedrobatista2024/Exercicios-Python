def ficha(jog= '<<Desconhecido>>', gol=0):
    print(f'O jogador {jog} fez {gol}gol(s)')


n = str(input('Nome do jogador: '))
g = str(input('Numero de gol(s): ')).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gol=g)
else:
    ficha(n, g)