# Esse programa vai ler um arquivo txt, com as informções 
# de alguns elementos qúimicos
# 1. Fazer um jogo de adivinhação (descobrir qual é o 
# elemento químico sabendo suas propriedades)
# 2. Lista todos os elementos químicos, com e sem suas propriedades

from função.arquivo import * 
from função.quiz import * 

arquivo = 'elementos.txt'
config = {"estado": True}

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu()
    if resposta == 1:
        lerArquivoSEM(arquivo)
    elif resposta == 2:
        lerArquivoCOM(arquivo)
    elif resposta == 3:
        quiz()
    elif resposta == 4:
        break
