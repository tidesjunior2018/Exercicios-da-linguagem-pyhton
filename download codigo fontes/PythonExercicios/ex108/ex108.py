'''
108-Adapte o código do desafio 107 criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
'''
import moeda
preco=float(input('Digite o preço: '))
taxa=int(input('Digite a taxa: '))

if taxa == 0:
    precoaumentado=moeda.aumentar(preco)
    precodiminuido=moeda.diminuir(preco)
    print(f'O preço normal é de R${precoaumentado}')
elif taxa > 0 :
    precoaumentado=moeda.aumentar(preco,taxa)
    precodiminuido=moeda.diminuir(preco,taxa)
    print(f'O preco aumentado com o(s) {taxa}% é de R${precoaumentado}')
    print(f'O preço diminuido em {taxa}% é de R${precodiminuido}')
precodobrado=moeda.dobrar(preco)
print(f'O preco dobrado é de R$ {precodobrado}')
metadedopreco=moeda.metade(preco)
print(f'A metade do R${preco} é R${metadedopreco:.2f}')