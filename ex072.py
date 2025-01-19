tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'deseseis', 'desesete', 'desoito', 'desenove', 'vinte')
numero = 21
while numero not in (1, 2, 3, 4,5, 6, 7 ,8 , 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20):
    numero = int(input('digite um numero entre 0 e 20: '))
print(tupla[numero])