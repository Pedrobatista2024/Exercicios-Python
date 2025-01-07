valor = int(input('Digite um valor de 0 a 9999: '))
u = valor // 1 % 10
d = valor // 10 % 10
c = valor //100 % 10
m = valor // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))