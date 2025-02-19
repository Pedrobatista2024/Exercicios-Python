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

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número valido.033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu não digitar esse numero.\033[m')
            return 0
        else:
            return n


n = leiaint('Digite um numero: ')
n1 = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o numero {n}')
print(f'O numero real digitado foi {n1}')
