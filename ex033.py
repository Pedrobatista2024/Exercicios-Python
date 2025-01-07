n1 = float(input('Digite o 1º numero: '))
n2 = float(input('Digite o 2º numero: '))
n3 = float(input('Digite o 3º numero: '))
numeros = [n1, n2, n3]
maior = max(numeros)
menor = min(numeros)
print('\033[31;40mO maior numnero é {} \033[m'.format(maior))
print('\033[32;40mO menor numero é {} \033[m'.format(menor))