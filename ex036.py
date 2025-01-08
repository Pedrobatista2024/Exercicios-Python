casa = float(input('Valor do imovel? '))
salario = float(input('qual o seu salario? '))
anos = int(input('em quantos anos voce vai pagar? '))
valorP = casa / (anos * 12)
miniP = salario * 0.30
if valorP > miniP :
    print('emprestimo negado')
else :
    print('emprestimo aprovado')