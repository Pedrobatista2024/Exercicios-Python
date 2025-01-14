cont = 0
soma = 0
numero = 0
while numero != 999:
    numero = int(input('Digite um numero: '))
    if numero != 999:
        soma += numero
        cont += 1
print('foram digitados: {} '.format(cont))
print('A soma de todos eles é: {} '.format(soma))