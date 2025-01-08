num = int(input('Digite um numero inteiro: '))
conv = int(input('''Escolha a base de conversão
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal
Sua opção: '''))
if conv == 1 :
    print('{} convertido para binario é: {}'.format(num, bin(num)[2:]))
elif conv == 2 :
    print('{} convertido para octal é: {}'.format(num, oct(num)[2:]))
elif conv == 3 :
    print('{} convertido para hexadecimal é: {}'.format(num, hex(num)[2:]))
else :
    print('Opção invalida')
