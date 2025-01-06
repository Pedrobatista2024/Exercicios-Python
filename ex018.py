import math

angulo = float(input('Digite um angulo qualquer: '))
seno = math.sin(math.radians(angulo))
print('O seno do angulo {} é {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O cosseno do angulo {} é {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('A hipotenusa do angulo {} é {:.2f}'.format(angulo, tangente))
