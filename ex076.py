listagem = ('borracha', 2, 'lapiz', 3, 'caderno', 30,
            'caneta', 5, 'bolsa', 100, 'estojo', 20,
            'livro', 34.90, 'compasso', 15.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'{listagem[pos]:>7.2f}')
print('-' * 40)