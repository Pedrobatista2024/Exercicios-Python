continua = 1
numero = int(input('de qual numero começaremos? '))
razao = int(input('de quanto sera nosso salto? '))
termos = 9
contador = 1
cont = 0
while continua == 1:
    pa = numero
    while contador <= termos:
        if contador == 1:
            print('Aqui esta sua PA')
            print(numero, end=',')
        pa += razao
        print(pa, end=',')
        contador += 1
    print('Pausa')
    cont = int(input('''    [1] escolher aumentar numero de termos
    [2] encerrar o programa
    Escolha uma opção: '''))
    if cont == 1:
        numero = pa
        termos += int(input('você quer ver mais quantos numeros da sua PA: '))
    if cont == 2:
        continua += 1
