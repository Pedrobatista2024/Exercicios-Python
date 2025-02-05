'''par = []
impar = []
total = []
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        par.append(valor)
    else :
        impar.append(valor)
total.append(par)
total.append(impar)
print(f'Aqui esta a lista com todos os numeros digitados e separados em pares e impares {total}')
print(f'Lista de numeros pares em ordem crescente {sorted(total[0])}')
print(f'Lista dos numeros impares em ordem crescente {sorted(total[1])}')'''

lista = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
sorted(lista[0])
sorted(lista[1])
print(f'Lista de numeros pares em ordem crescente {lista[0]}')
print(f'Lista dos numeros impares em ordem crescente {lista[1]}')