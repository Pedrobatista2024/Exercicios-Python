m18 = cont = homC = menos20 = 0
sex = 'h'
continua = 'k'
while True:
    continua = 'k'
    sex = 'h'
    cont += 1
    print('**'* 20)
    print(f'        CADASTRE A {cont}º PESSOA')
    print('**'* 20)
    idade = int(input('Idade: '))
    while not sex in 'MmFf':
        sex = str(input('[M/F]?: ')).strip().upper()
        if idade > 18:
            m18 += 1
        if sex == 'M':
            homC += 1
        if idade < 20:
            if sex == 'F':
                menos20 += 1
    while not continua in 'SsNn':
        continua = str(input('Quer continuar ? [S/N]')).strip().lower()
        if continua == 's':
            continue
    if continua == 'n':
            break
print(f'Pessoas com mais de 18 anos: {m18}')
print(f'Homens cadastrados: {homC}')
print(f'Mulheres com menos de 20 anos: {menos20}')