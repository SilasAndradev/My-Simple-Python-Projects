from time import sleep
import random
import threading as th
from função.arquivo import * 

def quiz(txt, config):
    
    score = 0
    elemento = dict()
    sleep(2)
    while config["estado"]:  # Continua enquanto 'estado' for True
        a = open(txt, 'rt')
        linha = txt.readlines()
        for j in range(10):
            random.choice(linha)
            dado = linha.split(';')
            
            # Mostra a pergunta
            print(f"Qual o elemento químico que possui:\n - O número atômico: {dado[1]};\n - O símbolo: {dado[2]};\n - A massa atômica: {dado[3].strip()}.")

            # Guarda a resposta correta
            resposta_correta = dado[0]

            # Faz o pedido para escrever a resposta
            suaResp = input('Digite o elemento químico: ')

            # Verificar a resposta
            if suaResp == resposta_correta:
                score += 1
                print('')
            else:
                print(f'\033[0;34Resposta incorreta. A resposta correta seria {resposta_correta}\033[m')
        config["estado"] = False

    print("O tempo acabou. Quiz encerrado.")
    print(f'Você marcou {score} pontos.')
   
def tempo(config):
    
    timer = 60 # Tempo

    print('O jogo começou! Você tem 60 segundos para responder todas as questões.')
    sleep(2)
    
    while timer > 0:

        # Calculando o tempo
        if config["estado"]:
            sleep(1)
            timer -= 1
        else:
            print(f'Você terminou com {timer} segundos restantes.')
            break 
        
        # Mostrar as mensagens de acordo com o tempo que passou
        if timer == 30:
            print('Restam apenas 30 segundos.')
        elif timer == 15:
            print('Restam apenas 15 segundos.')
        elif timer == 5:
            print('Restam apenas 5 segundos.')
        elif timer == 0:
            config["estado"] = False



def quizTemp():
    config = {"estado": True}

    principal = th.Thread(target=quiz, args=(questões, config))
    principal.start()

    # Inicia a thread do temporizador
    cont = th.Thread(target=tempo, args=(config,))
    cont.start()

    # Aguarda o término de ambas as threads
    cont.join()
    principal.join()