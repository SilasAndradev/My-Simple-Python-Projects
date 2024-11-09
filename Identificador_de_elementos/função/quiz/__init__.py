from time import sleep
import random
import threading as th

class game:
    def quiz(txt, stop_event):

        # Abre o arquivo
        with open(txt, 'r', encoding='utf-8') as file:
            linhas = file.readlines()
            linhasCopy = linhas.copy()
        
        score = 0
        sleep(2)
        
        for j in range(0, 10):

            if stop_event.is_set():
                break

            # Escolhe um elemento químico aleatório
            linha = random.choice(linhasCopy)
            dado = linha.split(';')
            
            # Mostra a pergunta
            print(f"Qual o elemento químico que possui:\n - O número atômico: {dado[1]};\n - O símbolo: {dado[2]};\n - A massa atômica: {dado[3].strip()}.")

            # Guarda a resposta correta
            resposta_correta = dado[0]

            # Faz o pedido para o usuário escrever a resposta
            suaResp = input('\nDigite o elemento químico: ')

            # Verificar se a resposta está correta
            if suaResp == resposta_correta:
                score += 1
                print(f'\033[0;34mResposta correta.\033[0m')
            else:
                print(f'\033[0;34mResposta incorreta. A resposta correta seria {resposta_correta}\033[0m')

            # Remove a linha já utilizada para evitar repetição
            linhasCopy.remove(linha)
        
        print(f'Você marcou {score} pontos.')
        stop_event.set()


    def tempo(stop_event):
        timer = 60
        
        print('O jogo começou! Você tem 60 segundos para responder todas as questões.')
        sleep(2)

        while not stop_event.is_set():
            mins, secs = divmod(timer, 60)
            timeformat = f'{mins:02d}:{secs:02d}'
            if timer == 30:
                print('Restam 30 segundos')
            elif timer == 15:
                print('Restam 15 segundos')
            elif timer == 5:
                print('Restam 5 segundos')
            sleep(1)
            timer -= 1
            if timer == 0:
                break

        print('-=' * 30)
        if timer > 0:
            print(f'Você terminou com {timer} segundos restantes.')
        else:
            print(f'O tempo acabou!')

        print('-=' * 30)
        stop_event.set()
