from Função.Interface import *
import Função.arquivos as ar

arq = 'Sistema_de_Mercado/produtos.txt'

if not ar.arquivoExiste(arq):
    ar.criarArquivo(arq)

while True:
    cabecalho('Mercado de Jadinho')
    resposta = menu()
    if resposta == 1:
        ar.lerArquivo(arq)
    elif resposta == 2:
        cabecalho('ADICIONAR PRODUTOS')
        cod = leiaInt()
        nome = str(input('Digite o nome do produto: '))
        preco = leiafloat()
        ar.adicionar(arq, cod, nome, preco)
    elif resposta == 3:
        ar.lerArquivo(arq)
        linhas()
        print('REALIZAR COMPRAS'.center(60))
        ar.compras(arq)
    elif resposta == 4:
        cabecalho('Saindo do Sistema...')
        break