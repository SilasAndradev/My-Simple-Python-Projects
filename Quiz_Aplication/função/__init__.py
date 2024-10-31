from time import sleep
def tempo(acabouQuest):
    acabou = False
    print('O jogo começou, boa sorte!')
    for j in range(59, 0, -1):
        if acabouQuest:
            print(f'Parabéns, você terminou faltando {j} segundos!')
            break
            
        sleep(1)

        if j == 30:
            print('Faltam 30 segundos!')

        elif j == 15:
            print('Faltam 15 segundos!')
            
        elif j == 5:
            print('Faltam 5 segundos!')

    return acabou == True

def quiz(questions, acabouTemp):
    acabou = False
    for perguntas, resposta in questions.items():

        if acabouTemp:
            break
        print(f'{perguntas}')
        print(sorted(resposta))
        resposta_correta = resposta[0]

        suaResp = input('Escreva sua resposta: ')
        
        if suaResp == resposta_correta:
            print('Resposta correta')
        else:
            print('Resposta incorreta')
    return acabou == True