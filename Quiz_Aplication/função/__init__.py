import threading
from time import sleep
def tempo(acabou=False):
    timer = 60
    while timer > 0:
        sleep(1)
        timer -= 1
        if acabou:
            break
        if timer == 30:
            print('Restam apenas 30 segundos.')
        elif timer == 15:
            print('Restam apenas 15 segundos.')
        elif timer == 5:
            print('Restam apenas 5 segundos.')
        elif timer == 0:
            print('Acabou o tempo')
            break
    return acabou

        

def quiz(questions):
    conta = len(questions)
    cont = 0
    while True:
        acabou = False
        tempo(acabou)
        
        for perguntas, resposta in questions.items():
            print(f'{perguntas}')

            print(','.join(sorted(resposta)))

            resposta_correta = resposta[0]

            suaResp = input('Escreva sua resposta: ')

            if suaResp == resposta_correta:
                print('Resposta correta')
            else:
                print('Resposta incorreta')
            cont += 1
        if cont == conta:
            acabou = True
            break
            