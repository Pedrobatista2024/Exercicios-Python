import random
valor = random.randint(1, 5)
print('Ola, bem vindo ao jogo de adivinhação,você deve adivinhar um numero entre 1 e 5,Boa sorte!')
chute = int(input('digite um numero inteiro entre 1 e 5: '))
if chute == valor :
    print('Parabens! você acertou')
else :
    print('Ops! você errou')
    print('O numero correto era {}'.format(valor))