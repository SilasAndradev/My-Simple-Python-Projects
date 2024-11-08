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

arquivo = 'elementos.txt'
config = {"estado": True}

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
        quizTemp(arquivo, config)
    elif resposta == 4:
        break