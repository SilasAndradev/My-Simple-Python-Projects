def linhas():
    print('-=' * 30)

def linhasSimples():
    print('--' * 30)

def cabecalho(txt):
    linhas()
    print(txt.center(60))
    linhas()

def menu():
    # Mostrar as opções de ações do usuário
    print(' 1 - Listar os elementos químicos')
    print(' 2 - Listar os elementos químicos (com suas propriedades)')
    print(' 3 - Jogo da advinhação')
    print(' 4 - Sair do Sistema')
    linhas()
    while True:
        try:
            resposta = int(input('\033[0;33mSua Opção: \033[m'))
        except ValueError:     
            print('\033[0;31mERRO! O usuário não digitou um número inteiro.\033[m')
        else:
                if resposta > 4 or resposta < 1:
                    print('\033[0;31mERRO! O usuário digitou um número inteiro invállido.\033[m')
                else:
                    return resposta
                break
    linhas()        


def arquivoExiste(txt):
    # Verifica se o arquivo existe
    try:
        a = open(txt, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(txt):
    # Cria um arquivo
    try:
        a = open(txt, 'wt+') 
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {txt} criado com sucesso')

def lerArquivoSEM(txt):
    # Ler o arquivo mostrando apenas o nome
    try:
        linhas()
        a = open(txt, 'rt')
        print(f'{'\033[0;34mLista dos Elementos\033[m'.center(30)}')
        for linha in a:
            dado = linha.split(';')
            print(f'\033[0;34mNome: \033[m{dado[0]}')
    except:
        print('Erro ao ler o arquivo!')
def lerArquivoCOM(txt):
    # Ler o arquivo mostrando o nome e suas propriedades
    try:
        linhas()
        a = open(txt, 'rt')
        print(f'{'\033[0;34mLista dos Elementos\033[m'.center(30)}')
        for linha in a:
            linhasSimples()
            dado = linha.split(';')
            print(f'\033[0;34mNome: \033[m{dado[0]}')
            print(f'\033[0;34mNúmero Atômico: \033[m{dado[1]}')
            print(f'\033[0;34mSímbolo: \033[m{dado[2]}')
            print(f'\033[0;34mMassa Atômica: \033[m{dado[3]}')

    except:
        print('Erro ao ler o arquivo!')