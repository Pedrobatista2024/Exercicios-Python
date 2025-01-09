div = 0
numero = int(input('Digite um numero: '))
for c in range(0, numero):
    c += 1
    if numero % c == 0:
        div += 1
if div == 2:
    print('O numero: {} é primo'.format(numero))
else:
    print('O numero: {} não é primo'.format(numero))