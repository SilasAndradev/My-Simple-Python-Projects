from Sistema_de_Mercado.Interface import *
from Sistema_de_Mercado.arquivos import *

arq = 'produtos.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    cabecalho('Mercado de Jadinho')
    resposta = menu()
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('ADICIONAR PRODUTOS')
        cod = leiaInt()
        nome = str(input('Digite o nome do produto: '))
        preco = leiafloat()
        adicionar(arq, cod, nome, preco)
    elif resposta == 3:
        cabecalho('REALIZAR COMPRAS')
        compras(arq)
    elif resposta == 4:
        cabecalho('Saindo do Sistema...')
        break