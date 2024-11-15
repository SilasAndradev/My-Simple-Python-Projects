from time import sleep

config = {"estado": True}

# Função do temporizador
def tempo(config):
    
    timer = 60 # Tempo
    
    try:
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

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Função principal do quiz
def quiz(questions, config):
    score = 0
    sleep(2)
    while config["estado"]:  # Continua enquanto 'estado' for True
        for perguntas, resposta in questions.items():
            if config["estado"]:

                # Mostrar as perguntas e respostas
                print(f'{perguntas}')
                print(f"{', '.join(sorted(resposta))}")

                # Guarda a resposta correta
                resposta_correta = resposta[0]

                # Faz o pedido para o usuário escrever a resposta
                suaResp = input('\033[0;34mSua resposta: \033[0m')

                # Verificar a resposta
                if suaResp.upper() == resposta_correta.upper():
                    score += 1
                    print(f'\033[0;34mResposta correta\033[0m')
                else:
                    print(f'\033[0;33mResposta incorreta. A resposta correta seria {resposta_correta}\033[0m')
        
            else:
                print("O tempo acabou. Quiz encerrado.")
                print(f'Você fez {score} pontos')
                break
        config["estado"] = False 
    print(f'Você marcou {score} pontos.')
    # Encerra o quiz