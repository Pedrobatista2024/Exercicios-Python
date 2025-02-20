import modulos
from time import sleep

import arquivo
from arquivo import lerArquivo
from modulos import cabeçalho

arq = 'cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)
while True:
    resposta = modulos.menu(['Ver Pessoas cadastradas','Cadastrar Nova Pessoa', 'Sair do Sistema'] )
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)