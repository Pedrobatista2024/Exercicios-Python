continua = 'k'
barato = 'k'
preco = ac100 = s = cont = ba = 0
while True:
    cont += 1
    continua = 'k'
    nome = str(input('Nome do produto: ')).strip().lower()
    preco = float(input('preço do produto: '))
    if cont == 1:
        ba = preco
    s += preco
    if preco <= ba:
        ba = preco
        barato = nome
    if preco > 1000:
        ac100 += 1
    while not continua in 'SsNn':
        continua = str(input('Quer continuar? [S/N]'))
        if continua == 's':
            continue
    if continua == 'n':
        break
print(f'O preço total é R${s:.2f}')
print(f'{ac100} produtos acima de R$1000')
print(f'O seu produto mais barato foi {barato}')