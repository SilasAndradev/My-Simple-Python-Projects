def linhas():
    print('-=' * 30)

def cabecalho(txt):
    linhas()
    print(txt.center(60))
    linhas()

def menu():
    print(' 1 - Listar os elementos químicos')
    print(' 2 - Listar os elementos químicos (com suas propriedades)')
    print(' 3 - Jogo da advinhação')
    print(' 4 - Sair do Sistema')
    linhas()
    while True:
        try:
            resposta = int(input('\033[0;33mSua Opção: \033[m'))
        except ValueError:     
            print('\033[0;31mERRO! O usuário não digitou um número inteiro válido.\033[m')
        else:
                if resposta > 4 or resposta < 1:
                    print('\033[0;31mERRO! O usuário digitou um número inteiro invállido.\033[m')
                else:
                    return resposta
                break
    linhas()        

def leiaInt():
    while True:
        try:
            numero = int(input('Digite o código do produto: '))    
        except KeyboardInterrupt:
            print('\033[0;31mO usuário prefiriu não digitar esse número.\033[m')
        except ValueError:
            print('\033[0;31mO usuário digitou um número inteiro invállido.\033[m')
        else:   
            return numero
        
def leiafloat():
    while True:
        try:
            numero = float(input('Digite o valor do produto: '))    
        except KeyboardInterrupt:
            print('\033[0;31mO usuário prefiriu não digitar esse número.\033[m')
        except ValueError:
            print('\033[0;31mO usuário digitou um número real invállido.\033[m')
        else:   
            return numero