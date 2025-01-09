partida = int(input('de qual numero começaremos? '))
salto = int(input('de quanto sera nosso salto? '))
prog = partida
for c in range(1, 10):
    if c == 1:
        print(partida)
    prog += salto
    print(prog)
print('FIM')