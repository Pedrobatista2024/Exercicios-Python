n = int(input('Digite a quantidade de numeros da sequencia de fibonacci você quer: '))
cont = 1
aux = 1
fi = 0
bo = 1
while cont <= n:
    print( fi , end=' ')
    aux = bo
    bo = fi + bo
    fi = aux
    cont += 1