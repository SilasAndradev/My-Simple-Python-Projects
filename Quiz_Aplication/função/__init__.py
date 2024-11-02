import threading as th
from time import sleep
config = {"estado": True}

def tempo(config):
    timer = 60
    try:
        print('O jogo começou você tem 60 segundos para responder todas as questões')
        sleep(2)
        while timer > 0:
            if config["estado"]:
                sleep(1)
                timer -= 1
            else:
                print(f'Você acabou restando {timer} segundos')
                break
            if timer == 30:
                print('Restam apenas 30 segundos.')
            elif timer == 15:
                print('Restam apenas 15 segundos.')
            elif timer == 5:
                print('Restam apenas 5 segundos.')
            elif timer == 0:
                config["estado"] = False
                print('Acabou o tempo')
    except Exception as e:
        print(f"An error occurred: {e}")
        
    return config["estado"] == False
            
def quiz(questions, config):    
        sleep(2)
        while True:
            for perguntas, resposta in questions.items():
                if config["estado"]:
                    if not isinstance(perguntas, str) or not isinstance(resposta, list) or len(resposta) == 0:
                        raise ValueError("Invalid question: must be a non-empty string and the answer must be a non-empty list")
                        
                    print(f'{perguntas}')

                    print(f"{','.join(sorted(resposta))}\n")

                    resposta_correta = resposta[0]

                    suaResp = input('Escreva sua resposta: ')

                    if suaResp == resposta_correta:
                        print('Resposta correta')
                    else:
                        print(f'Resposta incorreta. A resposta correta seria {resposta_correta}')
                else:
                    break
            break
        return config["estado"] == False
                
            