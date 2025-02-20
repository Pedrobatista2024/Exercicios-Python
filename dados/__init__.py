def LeiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço invalido!\033[m')
        else:
            valido = True
            return float(entrada)

def porganiza(lista):
    i = -1
    d = len(lista)
    for c in range(len(lista)):
        if c == 0:
            n = (max(lista[:]))
            lista.insert(d -i, n)
            lista.remove((max(lista[:-1])))
        else:
            n = (max(lista[:i]))
            lista.insert(d - (-i), n)
            lista.remove((max(lista[:i])))
            i = i + (-1)
    return lista