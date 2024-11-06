# Esse programa vai ler um arquivo txt, com as informções 
# de alguns elementos qúimicos
# 1. Fazer um jogo de adivinhação (descobrir qual é o 
# elemento químico sabendo suas propriedades)
# 2. Lista todos os elementos químicos, com e sem suas propriedades

from Identificador_de_elementos.função.arquivo import * 
from Identificador_de_elementos.função.interface import * 

arquivo = 'elementos.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

    