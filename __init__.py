from time import sleep
def marcacao():
    j = 0
    for j in range(59, 0, -1):
        sleep(1)
        j+=1
        if j == 60:
            print('O jogo começou, boa sorte!')
        elif j == 30:
            print(f'Faltam 30 segundos!')
        elif j == 15:
            print(f'Faltam 15 segundos!')
        elif j == 5:
            print(f'Faltam 5 segundos!')
    print('Acabou')
        
    


def quiz(questions):
    if not questions:
        print("Nenhuma pergunta fornecida.")
        return
    for perguntas, resposta in questions.items():
        print(f'{perguntas}')
        if not resposta or not isinstance(resposta, list):
            print("Opções de resposta inválidas fornecidas.")
            continue
        print(sorted(resposta))
        resposta_correta = resposta[0]
        try:
            suaResp = str(input(''))
        except EOFError:
            print("Ocorreu um erro de entrada.")
            continue
        if suaResp == resposta_correta:
            print('Resposta correta')
        else:
            print('Resposta incorreta')