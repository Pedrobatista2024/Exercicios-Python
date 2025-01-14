numero = int(input('de qual numero começaremos? '))
razao = int(input('de quanto sera nosso salto? '))
contador = 1
pa = numero
while contador <= 9:
    if contador == 1:
        print('Aqui esta sua PA')
        print(numero, end=',')
    pa += razao
    print(pa, end=',')
    contador += 1
print(' FIM')