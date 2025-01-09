maiorP = 0
menorP = 10000000000.0
for c in range(1, 6):
    peso = float(input('qual o peso da {}º pessoa: '.format(c)))
    if peso > maiorP:
        maiorP = peso
    if peso < menorP:
        menorP = peso
print('O maior peso foi {}kg e o menor peso foi {}kg '.format(maiorP, menorP))