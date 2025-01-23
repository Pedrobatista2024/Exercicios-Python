exp = str(input('Digite sua expressão: '))
expS = exp.count('(')
expS2 = exp.count(')')
if expS == expS2:
    print('Sua expressão é valida')
else:
    print('Sua expressão não é valida')