import modulos

preço = float(input('Qual o preço dp produto: '))
print(f'O dobro do Preço: {modulos.dobro(preço)}')
print(f'A metade do preço: {modulos.metade(preço)}')
print(f'Apos o reajuste de 50%: {modulos.aumenta(preço, 50)}')
print(f'Apos o reajuste de 50% para menos: {modulos.dimimui(preço, 50)}')