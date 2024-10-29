def quiz(questions):
    for perguntas, resposta in questions:
        print(f'{perguntas}')
        print(sorted(resposta))
        resposta_correta = resposta[0]
        suaResp = str(input(''))
        if suaResp == resposta_correta:
            print('Reposta correta')
        else:
            print('Respota incorreta')