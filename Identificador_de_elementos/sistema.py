from função.arquivo import * 
from função.quiz import *
import threading as th

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
