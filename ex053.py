frase = str(input('Digte uma frase: ')).strip().lower()
semsp = frase.replace(' ', '')
cont = list(reversed(semsp))
cont2 = list(reversed(cont))
print(cont)
print(cont2)
if cont == cont2:
    print('Essa frase é um PALÍNDROMO')
else:
    print('Essa frase não é um PALÍNDROMO')