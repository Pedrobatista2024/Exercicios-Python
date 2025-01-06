import math
co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))
imp2 = math.pow(co,2) + math.pow(ca, 2)
imp = math.sqrt(imp2)
print('o valor da hipotenusa desse triangulo é {:.2f}'.format(imp))
