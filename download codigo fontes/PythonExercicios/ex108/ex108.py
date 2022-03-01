'''
108-Adapte o código do desafio 107 criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
'''
import moeda
preco=float(input('Digite o preço: '))
taxa=int(input('Digite a taxa:[0-para indicar nenhuma taxa] '))

if taxa == 0:
    precoaumentado=moeda.moeda(moeda.aumentar(preco))
    print(f'O preço sem taxa nenhuma = R${precoaumentado}')
elif taxa > 0 :
    precoaumentado=moeda.moeda(moeda.aumentar(preco,taxa))
    precodiminuido=moeda.moeda(moeda.diminuir(preco,taxa))
    print(f'O preço com os {taxa}% = R${precoaumentado}')
    print(f'O preço sem os {taxa}% = R${precodiminuido}')
precodobrado=moeda.moeda(moeda.dobrar(preco))
print(f'O preço {moeda.moeda(preco)} dobrado = {precodobrado}')
metadedopreco=moeda.moeda(moeda.metade(preco))
print(f'A metade do preço {moeda.moeda(preco)} = {metadedopreco}')