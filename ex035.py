r1 = float(input('Digte o comprimento da 1º resta: '))
r2 = float(input(' Digite o comprimento da 2º reta: '))
r3 = float(input('Digite o comprimento da 3º reta: '))
soma = r1 + r2 > r3
soma2 = r1 + r3 > r2
soma3 = r2 + r3 > r1
triangulo = soma == True and soma2 == True and soma3 == True
if triangulo == True :
    print('\033[32;40mSim, esses parametros formam um triangulo.\033[m')
else :
    print('\033[31;40mNão, esses parametros não formam um  triangulo.\033[m')