n1 = int(input('digite o 1º numero: '))
n2 = int(input('digite o 2º numero: '))
if n1 > n2 :
    print('O 1º numero {} é maior que o 2º numero {}'.format(n1, n2))
elif n1 < n2 :
    print('O 2º numero {} é maior que o 1º numero {}'.format(n2, n1))
else :
    print('O 1º numero {} e o 2º numero {} são iguais. '.format(n1, n2))
