import random
valor = random.randint(1, 10)
chute = 0
tentativas = 0
print('Ola, bem vindo ao jogo de adivinhação,você deve adivinhar um numero entre 1 e 5,Boa sorte!')
while chute != valor:
    chute = int(input('digite um numero inteiro entre 1 e 10: '))
    tentativas += 1
    if chute == valor :
        print('Parabens! você acertou')
    else :
        print('Ops! você errou')
        print('tente novamente')
print('você precisou de {} tentativas para acertar'.format(tentativas))
