distancia = float(input('qual a distancia do seu destino em km?: '))
if distancia <= 200 :
    valor = distancia * 0.50
    print('O valor da sua passagem é {:.2f}$ '.format(valor))
else :
    valor = distancia * 0.45
    print('O valor da sua passagem é {:.2f}$ '.format(valor))