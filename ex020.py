import random
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input("terceiro anolu: "))
n4 = str(input('quarto aluno: '))
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print('Ordem de apresentação: ')
for i, aluno in enumerate(alunos, start=1):
    print(F'{i}. {aluno}')