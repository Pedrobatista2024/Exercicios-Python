gabarito = []
while True:
    continua = ''
    nome = str(input('Nome: '))
    no1 = float(input('nota 1 : '))
    no2 = float(input('nota 2: '))
    media = (no1 + no2) / 2
    gabarito.append([nome, [no1, no2], media])
    while continua not in ['S', 'N']:
        continua = str(input('Quer continuar? [S/N]')).strip().upper()
    if continua == 'N':
        break
print(f'|{"No.":<4}|{"NOME":<10}|{"MEDIA":>8}|')
for i, a in enumerate(gabarito):
    print(f'|{i:<4}|{a[0]:<10}|{a[2]:>8.1f}|')
while True:
    aluno = int(input('Você quer ver a nota de qual Aluno?(999 interrompe): '))
    if aluno == 999:
        break
    if aluno <= len(gabarito) -1:
        print(f'Notas de {gabarito[aluno][0]} é: {gabarito[aluno][1]}')