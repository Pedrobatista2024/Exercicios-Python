from random import randint
v = 0
while True:
    pc = randint(1, 10)
    print('-='*20)
    print('VAMOS JOGAR [ PAR OI IMPAR ]')
    print('-='* 20)
    jogador = int(input('Escolha um valor: '))
    s = pc + jogador
    op = str(input('Par ou Impar? [P/I]')).strip().upper()
    print(f'A maquina escolheu {pc} e você {jogador} a soma é {s} e você: ',end='')
    if op == 'P':
        if s % 2 == 0:
            print('GANHOU')
            v += 1
        else:
            print('PERDEU')
            break
    if op == 'I':
        if s % 2 == 0:
            print('PERDEU')
            break
        else:
            print('GANHOU')
            v += 1
print(f'Você ganhou {v} vezes seguidas ')