cont = 0
parou = 0
soma = 0
maior = 0
ig = 1
ig2 = 1
while parou != 1:
    numero = int(input('Digite um numero: '))
    cont += 1
    soma += numero
    media = soma / cont
    ig = 1
    if numero > maior:
        maior = numero
    while ig == ig2:
        continua = str(input('Voce quer continuar ? [S/N] : '.lower().strip()))
        if continua in 'Nn':
            parou += 1
            ig += 1
        elif continua in 'Ss':
            ig += 1
        else:
            print('{} não é valida, digite uma opção valida.'.format(continua))
            ig = 1
            ig2 = 1
print('A media dos {} valores digitados é: {}'.format(cont, media))
print('O maior numero digitado foi: {}'.format(maior))


