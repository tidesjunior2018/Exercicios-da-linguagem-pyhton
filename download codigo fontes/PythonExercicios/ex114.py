'''
114-Crie um código em pyhton para verificar se o site Pudim está acessivel pelo computador usado.
'''

import urllib
import urllib.request

try:
    site=urllib.request.urlopen('http://www.pudim.com.br/')    
except urllib.request.URLError:
    print('Não Consegui acessar o site pudim')
else:
    print('O site pudim foi acessado com sucesso')
