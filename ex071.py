print('**'*20)
print('         OLA BEM_VINDO AO BANK ')
print('**'*20)
valor = int(input('Qual valor do saque? '))
c50 = valor // 50
c20 = (valor - 50 * c50) // 20
c10 = (valor - (c50 * 50 + c20 * 20)) // 10
c1 = (valor - (c50 * 50 + c20 * 20 + c10 * 10))
if c50 > 0:
    print(f'Total de {c50} cedulas de R$50')
if c20 > 0:
    print(f'Total de {c20} cedulas de R$20')
if c10 > 0:
    print(f'Total de {c10} cedulas de R$10')
if c1 > 0:
    print(f'Total de {c1} cedulas de R$1')