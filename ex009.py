numero = int(input('você quer a taboada de qual numero? '))
contador = 1
while contador <= 10:
    taboada = numero * contador
    print('{} x {} = {}'.format(numero, contador, taboada))
    contador = contador + 1