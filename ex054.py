from datetime import date
ano = date.today().year
idade = 0
total = 0
for c in range(1, 8):
    nasc = int(input('em que ano a pessoa {}º nasceu? '.format(c)))
    idade = ano - nasc
    if idade >= 18:
        total += 1
print('{} pessoas ja são maiores de idade.'.format(total))