def notas(*num, sit = False):
    dicionario = {}
    dicionario['quantidade'] = len(num)
    dicionario['maior'] = max(num)
    dicionario['menor'] = min(num)
    dicionario['media'] = sum(num)/len(num)
    if sit:
        if dicionario['media'] >= 7:
            dicionario['situação'] = 'Boa'
        else:
            dicionario['situação'] = 'Ruin'
    return dicionario


resp = notas(5, 8, 9, 7, 5, sit= True)
print(resp)






