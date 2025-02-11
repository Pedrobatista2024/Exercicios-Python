from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('*#' * 12)
    print(f'A contagem de {i} até {f} pulando de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont += p
        print('<<FIM>>')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont -= p
        print('<<FIM>>')


contador(1, 10, 1)
contador(10, 0, 2)
contador(i = int(input('Inicio: ')), f = int(input('Fim: ')), p = int(input('Passo: ')))