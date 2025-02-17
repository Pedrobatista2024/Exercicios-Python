import modulos

preço = float(input('Qual o preço dp produto: '))
print(f'O dobro do Preço: {modulos.moeda(modulos.dobro(preço))}')
print(f'A metade do preço: {modulos.moeda(modulos.metade(preço))}')
print(f'Apos o reajuste de 50%: {modulos.moeda(modulos.aumenta(preço, 50))}')
print(f'Apos o reajuste de 50% para menos: {modulos.moeda(modulos.dimimui(preço, 50))}')