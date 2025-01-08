nota1 = float(input('Digite a 1º nota: '))
nota2 = float(input('Digite a 2º nota: '))
media = (nota1 + nota2) / 2
if media >= 7 :
    print('Parabens! você esta APROVADO. ')
elif media >= 5 and media < 6.9 :
    print('Você esta de RECUPERAÇÃO! estude mais ')
else :
    print('Droga você esta REPROVADO! ')
