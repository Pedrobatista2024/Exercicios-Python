'''mulheres = []
lista = []
while True:
    pessoas = {}
    sexo = ''
    continua = ''
    pessoas['nome'] = str(input('Nome: '))
    while sexo not in ['F', 'M']:
        sexo = str(input('Sexo: [M/F]')).strip().upper()
    if sexo == 'M':
        pessoas['sexoM'] = sexo
    else :
        pessoas['sexoF'] = sexo
        mulheres.append(pessoas['nome'])
    pessoas['idade'] = int(input('Idade: '))
    lista.append(pessoas)
    while continua not in ['S', 'N']:
        continua = str(input('Quer continuar? [S/N]')).strip().upper()
    if continua == 'N':
        break
totali = sum(lista["idade"] for lista in lista)
media =  (totali/len(lista))
print(f'{len(lista)} pessoas cadastradas')
print(f'A média de idade é :{media:.2f}')
print('As mulheres cadastradas foram: ')
for m in mulheres:
    print(m)
print('As pessoas com idade acima da média são: ')
for c in range(0, len(lista)):
    if lista[c]["idade"] > media:
        print(lista[c]["nome"])'''


galera = []
pessoa = {}
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
        if pessoa['sexo'] in ['M', 'F']:
            break
        print('Erro! por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).strip().upper()
        if resp in ['N', 'S']:
            break
        print('Erro! Responda apenas S ou N. ')
    if resp == 'N':
        break
print('*%*#*' * 15)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A media de idade é {media:.0f} anos.')
print('As mulheres cadastradas foram', end=' ')
for p in galera:
    if p["sexo"] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('lista das pessoas que estão acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
            print()
print('<<< Encerrado >>>')




