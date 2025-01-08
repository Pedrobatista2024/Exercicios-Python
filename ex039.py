from datetime import date
nasc = int(input('qual a seu ano de nascimento? '))
ano = date.today().year
idade = ano - nasc
if idade == 18 :
    print('Ja esta na hora de se alistar! ')
elif idade > 18 :
    dev = idade - 18
    print('Você ja deveria ter se alistado a {} anos. '.format(dev))
else :
    dev = 18 - idade
    print('faltam {} anos para você ir se alistar '.format(dev))

