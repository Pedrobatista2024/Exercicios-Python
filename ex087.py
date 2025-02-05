matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = c3 = l2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma de todos os pares da matriz é: {spar}')
for l in range(0, 3):
    c3 += matriz[l][2]
print(f'A soma dos elementos da terceira coluna é: {c3}')
for l in range(0,3):
    l2 += matriz[1][l]
print(f'A soma de todos os elementos da linha 2 é: {l2}')
