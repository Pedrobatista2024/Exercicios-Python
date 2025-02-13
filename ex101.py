'''from datetime import datetime
def voto(a):
    if a >= 18 and a <= 60:
        return 'Voto Obrigatorio.'
    elif a > 60:
        return 'Voto Opcional.'
    else:
        return 'Não Pode Votar.'


nasc = int(input('Qual o seu ano de nascimento?: '))
idade = datetime.now().year - nasc
print(idade)
print(voto(idade))'''
from datetime import date

def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não Vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional.'
    else:
        return f'Com {idade} anos: Voto Obrigatorio.'
nasc = int(input('Data de nascimento: '))
print(voto(nasc))