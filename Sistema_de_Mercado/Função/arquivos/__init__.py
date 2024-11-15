from Função.Interface import *
from time import *
def arquivoExiste(txt):
    try:
        a = open(txt, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(txt):
    linhas()
    try:
        a = open(txt, 'wt+') 
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {txt} criado com sucesso')


def lerArquivo(txt):
    try:
        a = open(txt, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('LISTA DE PRODUTOS')
        mostrar(txt)
    finally:
        a.close()

def adicionar(txt, cod, nome, preco):
    try:
        a = open(txt, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{cod};{nome};{preco}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            (f'Novo produto adionado!')
            a.close()

def mostrar(txt):
    a = open(txt, 'rt')
    print(f'\033[0;34m{'Código':<20}{'Nome'.center(20)}{'Preço':>20}\033[m')
    for linha in a:
        dado = linha.split(';')
        dado[2] = float(dado[2].replace("\n", "").replace("'", ""))
        print(f"{dado[0].replace("'", ""):<20}{dado[1].replace("'", "").center(20)}{dado[2]:>20.2f}")
    a.close()

def InserirCodigo(txt, codigo):
    valor = 0
    encontrado = False
    a = open(txt, 'rt') 
    linhas = a.readlines()
    for linha in linhas:
        dado = linha.split(';')
        if codigo == int(dado[0]):
            encontrado = True
            print(f'{dado[1].replace("'", "")}, R${dado[2].replace("\n","")}')
            valor = float(dado[2].replace('\n',''))
    if not encontrado:
        print('Código não encontrado.')
    a.close()
    return valor

def compras(txt):
    valorTotal = 0
    print('-=' * 30)
    while True:
        try:
            codigo = int(input('Digite o código: '))
        except ValueError:
            print('\033[0;31mPor favor, digite um número inteiro.\033[m')
        else:
            if codigo > 0: 
                valor = InserirCodigo(txt, codigo)
                valorTotal += valor
            else:
                print('-=' * 30)
                print('Parando de fazer compras.')
                break
    print(f'O valor total da compra foi de {valorTotal}.')