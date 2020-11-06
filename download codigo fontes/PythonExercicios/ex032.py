import time
import datetime
#0 = 2019
ano = int(input('Digite o ano para analisar,coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
anobissexto = ano % 4
print('ANALISANDO....')
time.sleep(3)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
