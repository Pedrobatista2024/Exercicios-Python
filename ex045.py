import random
from time import sleep
op = ['Pedra', 'Papel', 'Tesoura']
pc = random.choice(op)
print('''Ola! Bem vindo ao jogo
----O jogo é Pedra,Papel Tesoura----
--------Preparado?--------''')
go = int(input("""1º Pedra
2º Papel
3º Tesoura
Escola uma Opção: """))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if pc == 'Papel' and go == 1 :
    print('''Pc {}
    Você venceu'''.format(pc,))
elif pc == 'Papel' and go == 2 :
    print('''Pc {}
        Jogo empatado'''.format(pc, ))
elif pc == 'Papel' and go == 3 :
    print('''Pc {}
    Você perdeu'''.format(pc))
elif pc == 'Pedra' and go == 1 :
    print('''Pc {}
            Jogo empatado'''.format(pc, ))
elif pc == 'Pedra' and go == 2 :
    print('''Pc {}
        Você venceu'''.format(pc, ))
elif pc == 'Pedra' and go == 3 :
    print('''Pc {}
        Você perdeu'''.format(pc))
elif pc == 'Tesoura' and go == 1 :
    print('''Pc {}
        Você venceu'''.format(pc, ))
elif pc == 'Tesoura' and go == 2 :
    print('''Pc {}
            Você perdeu'''.format(pc))
elif pc == 'Tesoura' and go == 3 :
    print('''Pc {}
                Jogo empatado'''.format(pc, ))
else :
    print('opção invalida')
