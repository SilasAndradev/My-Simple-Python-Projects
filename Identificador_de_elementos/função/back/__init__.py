from time import sleep
from Identificador_de_elementos.função.arquivo import * 
import threading as th

def questões():
    lerArquivo()

def quiz(questions, config):
    score = 0
    sleep(2)
    while config["estado"]:  # Continua enquanto 'estado' for True
        for perguntas, resposta in questions.items():
            if config["estado"]:
                
                # Valida a resposta
                if not isinstance(perguntas, str) or not isinstance(resposta, list) or len(resposta) == 0:
                    raise ValueError("Pergunta inválida: deve ser uma string não vazia e a resposta deve ser uma lista não vazia")

                # Mostrar as perguntas e respostas
                print(f'{perguntas}')
                print(f"{', '.join(sorted(resposta))}")

                # Guarda a resposta correta
                resposta_correta = resposta[0]

                # Faz o pedido para escrever a resposta
                suaResp = input('Escreva sua resposta: ')

                # Verificar a resposta
                if suaResp == resposta_correta:
                    score += 1
                    print('Resposta correta')
                else:
                    print(f'Resposta incorreta. A resposta correta seria {resposta_correta}')
            
            else:
                config["estado"] = False
                print("O tempo acabou. Quiz encerrado.")
                print(f'Você fez {score} pontos')
                break
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