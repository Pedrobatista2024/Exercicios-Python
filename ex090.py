'''dici = {}
dici['nome'] = str(input('Nome do Aluno: '))
dici['media'] = float(input(f'Media do {dici["nome"]}: '))
print(f'O nome é {dici["nome"]}')
print(f'A media foi: {dici["media"]}')
if dici['media'] < 6:
    print('Situação = REPROVADO')
else:
    print('Situação = APROVADO')'''


dici = {}
dici['nome'] = str(input('Nome do Aluno: '))
dici['media'] = float(input(f'Media do {dici["nome"]}: '))
if dici['media'] >= 7:
    dici['situação'] = 'Aprovado'
elif dici['media'] < 7:
    dici['situação'] = 'Recuperação'
else:
    dici['situação'] = 'Reprovado'
for k, v in dici.items():
    print(f' - {k} é igual a {v}')
