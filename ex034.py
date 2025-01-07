salario = float(input('Digite seu salario: '))
if salario >= 1250 :
    novoSalario = salario * 0.10 + salario
    print('Seu novo salario é ${} '.format(novoSalario))
else :
    novoSalario = salario * 0.15 + salario
    print('Seu novo salario é ${} '.format(novoSalario))