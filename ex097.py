def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'{msg.center(tamanho)}')
    print('~' * tamanho)

escreva(input('Escreva sua mensagem especial: '))

