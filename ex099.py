from time import sleep



def maioral(* num):
    cont  = 0
    print('*#' * 12)
    print(f'Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
    print(f'Foram passados {len(num)} valores ao todo.')
    print(f'O maior numero passado foi: {max(num)}')


maioral(1,2,5,4,8,9,)
maioral(2,5,8,6,1,2)


