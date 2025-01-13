dec = ''
lista = [1, 2, 3, 4, 5]
while dec != 5:
    n1 = int(input('Digite o 1º valor: '))
    n2 = int(input('Digite o 2º valor: '))
    dec = int(input('''Oque você deseja fazer:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA
    Escolha uma das opções: '''))
    if dec in lista:
        if dec != 4:
            if dec == 1:
                s = n1 + n2
                print('A soma entre {} e {} é :{} '.format(n1, n2, s))
            if dec == 2:
                mult = n1 * n2
                print('A multiplicação entre {} e {} é :{}'.format(n1, n2, mult))
            if dec == 3:
                if n1 > n2:
                    print('O 1º numero {} é maior que p 2º numero {}'.format(n1, n2))
                else:
                    print('O 2º numero {} é maior que o 1º numero {}'.format(n2, n1))
    else:
        print('opção invalida')


