idadeT = 0
idadeHV = 0
homV = 0
mm20 = 0
for c in range(1, 5):
    sexo = int(input('''A {}º pessoa é:
    [1]=MASCULINO
    [2]=FEMININO
    escolha a opção digitando  1 ou 2:'''.format(c)))
    if sexo == 1:
        nomeM = input('qual o {}º nome: '.format(c))
        idadeM = int(input('qual a idade da {}º pessoa: '.format(c)))
        idadeT += idadeM
        if idadeM > idadeHV:
            homV = nomeM
            idadeHV = idadeM
    else:
        nomeF = input('qual o {}º nome: '.format(c))
        idadeF = int(input('qual a idade da {}º pesso: '.format(c)))
        idadeT += idadeF
        if idadeF < 20:
            mm20 += 1
print('A soma de todas as idades é: {}'.format(idadeT))
print('O homem mais velho é o: {}'.format(homV))
print('No total {} pessoas do sexo Feminino tem menos de 20 anos'.format(mm20))
