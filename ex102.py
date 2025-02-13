def fatorial(n, show = False):
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(c, end=' ')
            if c > 1:
                print('X ', end='')
            else:
                print('= ', end='')
        f *= c
    return f


numero = int(input('você quer ver o fatorial de qual numero? '))
cal = int(input('[1] ver calculo [0] não ver calculo: '))
print(fatorial(numero, cal > 0))