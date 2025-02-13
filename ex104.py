'''def leiaInt():
    while True:
        numero = str(input('Digite um numero: ')).strip()
        if numero.isnumeric():
            h = int(numero)
            print(f'Você digitou o numero:{h}')
            break
        else:
            print('ERRO! Digite um numero valido.')


seu_numero = leiaInt()'''

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um valor valido.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')
