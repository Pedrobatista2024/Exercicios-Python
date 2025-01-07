velocidade = float(input('qual a velocidade do carro? '))
veloM = 80
multa = (velocidade - veloM) * 7
if velocidade > veloM :
    print('você foi multado')
    print('sua multa vai custar {}$'.format(multa))
else :
    print('Ok, obrigado!')