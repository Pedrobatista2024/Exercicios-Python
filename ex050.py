s = 0
for c in range(1, 7):
    numero = int(input('Digite o {}º valor: '.format(c)))
    if numero % 2 == 0:
        s += numero
print('A soma total de todos os numeros pares é: {}'.format(s))