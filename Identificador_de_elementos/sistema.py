"""
Esse programa vai ler um arquivo txt, com as informções 
de alguns elementos qúimicos
E faz as seguintes coisas:
1. Mostra os nomes dos elementos químicos
    que estão no arquivo txt
2. Mostra os nomes e as propriedades dos elementos químicos
   que estão no arquivo txt
3. Faz um quiz em que o programa mostra as propriedades
    dos elementos químicos e o usuário tem que descobrir o seu nome
"""

from função.arquivo import * 
from função.quiz import *

# Declara a classe com as funções
jogo = game

# Declara a variável que vai coordenar o funcionamento
# das threads
stop_event = th.Event()

arquivo = "Identificador_de_elementos/elementos.txt"

# Se o não arquivo existe, ele cria 
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:

    linhas()
    resposta = menu()

    if resposta == 1:
        lerArquivoSEM(arquivo)

    elif resposta == 2:
        lerArquivoCOM(arquivo)

    elif resposta == 3:
        # Declara as duas threads
        t1 = th.Thread(target=jogo.quiz, args=(arquivo, stop_event,))
        t2 = th.Thread(target=jogo.tempo, args=(stop_event,))

        # Inicia as duas threads
        t1.start()
        t2.start()

        # Aguardar ambas as threads terminarem
        t1.join()
        t2.join()

    elif resposta == 4:
        break