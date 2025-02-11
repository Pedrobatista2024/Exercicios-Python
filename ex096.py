'''def area(a, b):
    result = a * b
    print(f'A area de um terredo de {a}x{b} é de {result}')
a =  b = 0
area(a = float(input('Largura do terreno: ')),b = float(input('Comprimento do terreno: ')))'''


def àrea(l, c):
    a = l * c
    print(f'A área de um terreno {l}X{c} é de {a}m².')

print('Contrle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
àrea(l, c)
