def leiaint(msg):
    while True:
        try:
            n= int(input((msg)))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def dobro(n = 0, formato = False):
    n = n * 2
    return n if formato is False else moeda(n)

def metade(n = 0, formato = False):
    n = n / 2
    return n if formato is False else moeda(n)

def aumenta(p = 0, n = 0, formato = False):
    p = p + (p * (n / 100))
    return p if formato is False else moeda(p)

def dimimui(p = 0, n = 0, formato = False):
    p = p - (p * (n / 100))
    return p if formato is False else moeda(p)

def moeda(p = 0, moeda = 'R$'):
    return  f'{moeda}{p:>8.2f}'.replace('.', ',')

def resumo(preço = 0, taxa = 10, taxaa = 5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print(f'Preço Analisado {moeda(preço)}'.center(30))
    print('-'* 30)
    print(f'Dobro do preço \t\t{dobro(preço, True)}')
    print(f'Metade do preço \t{metade(preço, True)}')
    print(f'{taxa}% de aumento \t\t{aumenta(preço, taxa, True)}')
    print(f'{taxaa}% de redução \t\t{dimimui(preço, taxaa, True)}')


def linha(tam = 42):
    return '-' * tam

def cabeçalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc
