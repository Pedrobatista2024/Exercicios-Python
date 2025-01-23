lista1 = []
lista2 = []
lista3 = []
while True:
    continua = ' '
    lista1.append(int(input('Digite um numero: ')))
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).strip().upper()
    if continua == 'N':
        break
print(f'Aqui esta sua lista completa {lista1}')
for n in lista1:
    if n % 2 == 0:
        lista2.append(n)
    else:
        lista3.append(n)
print(f'Lista com numeros pares {lista2}')
print(f'Lista com numeros impares {lista3}')