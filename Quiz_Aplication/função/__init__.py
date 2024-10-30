from time import sleep
def tempo():
    j = 0
    for j in range(59, 0, -1):
        sleep(1)
        j+=1
        print(j)
    


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
