# Esse programa vai ler um arquivo txt, com as informções 
# de alguns elementos qúimicos
# 1. Fazer um jogo de adivinhação (descobrir qual é o 
# elemento químico sabendo suas propriedades)
# 2. Lista todos os elementos químicos, com e sem suas propriedades

from Identificador_de_elementos.função.arquivo import * 
from Identificador_de_elementos.função.back import * 

arquivo = 'elementos.txt'
config = {"estado": True}

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu()
    if resposta == 1:
        lerArquivoSEM()
    elif resposta == 2:
        lerArquivoCOM()
    elif resposta == 3:
        quiz()
    elif resposta == 4:
        break
