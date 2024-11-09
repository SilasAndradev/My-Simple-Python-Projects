from time import sleep
import random
import threading as th
from função.arquivo import *

stop_event = th.Event()  # Evento para controlar a execução

def quiz(txt, stop_event):
    perguntasRealizadas = 0
    with open(txt, 'r', encoding='utf-8') as file:
        linhas = file.readlines()
        linhasCopy = linhas.copy()
    
    score = 0
    sleep(2)
    
    while perguntasRealizadas < 10 and not stop_event.is_set():  # Continua enquanto o evento não for ativado e perguntas < 10
        # Escolhe um elemento químico aleatório
        if not linhasCopy:
            print("Não há mais elementos suficientes para perguntas.")
            break

        linha = random.choice(linhasCopy)
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
            print(f'\033[0;34mResposta correta.\033[0m')
        else:
            print(f'\033[0;34mResposta incorreta. A resposta correta seria {resposta_correta}\033[0m')

        # Remove a linha já utilizada para evitar repetição
        linhasCopy.remove(linha)
        perguntasRealizadas += 1  # Incrementa o contador de perguntas realizadas

    # Verifica se o evento foi ativado após o término do loop
    if stop_event.is_set():
        print("O jogo foi interrompido antes de completar as 10 perguntas.")
    else:
        print("Você respondeu todas as questões!")

    print(f'Você marcou {score} pontos.')
    return


def tempo(stop_event):
    timer = 60  # Tempo do jogo
    print('O jogo começou! Você tem 60 segundos para responder todas as questões.')
    sleep(2)
    
    while timer > 0 and not stop_event.is_set():  # Continuar enquanto o tempo não acabar e o evento não for ativado
        sleep(1)
        timer -= 1
        # Mostrar as mensagens de acordo com o tempo
        if timer == 30:
            print('\nRestam apenas 30 segundos.')
        elif timer == 15:
            print('\nRestam apenas 15 segundos.')
        elif timer == 5:
            print('\nRestam apenas 5 segundos.')  
        elif timer == 0:
            print(f'O tempo acabou!')
            linhas()  # Função para mostrar os resultados do tempo
            print(f'Você terminou com {timer} segundos restantes.')
            stop_event.set()  # Sinaliza que o tempo acabou e o quiz deve parar
            break

def quizTemp(txt, stop_event):
    # Criar e iniciar as threads
    principal = th.Thread(target=quiz, args=(txt, stop_event,))
    cont = th.Thread(target=tempo, args=(stop_event,))

    principal.start()
    cont.start()

    # Espera ambas as threads terminarem
    cont.join()
    principal.join()
