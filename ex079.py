num = []
while True:
    conti = ' '
    valor = int(input('Digite um valor: '))
    if valor not in num:
        num.append(valor)
    else:
        print('O valor ja esta na lista, ele não sera adicionado')
    while conti not in 'SN':
        conti = str(input('Quer continua? [S/N]')).strip().upper()
    if conti == 'N':
            break
print(f'Os valores digitados foram {sorted(num)}')