import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://pedrobatista2024.github.io/Meu-Portfo-lio/')
except urllib.error.URLError:
    print('O site Pudim não está acessivel no momento.')
else:
    print('consegui acessar o site Pudim com sucesso!')