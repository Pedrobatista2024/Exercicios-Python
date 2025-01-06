numero = int(input('você quer a taboada de qual numero? '))
contador = 1
while contador <= 10:
    if contador == 1:
        print('-' * 14)
    taboada = numero * contador
    print('{} x {:2} = {:3} |'.format(numero, contador, taboada))
    contador = contador + 1

print('-' * 14)