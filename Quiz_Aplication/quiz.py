from função import tempo, quiz
import threading as th

# Configuração inicial
config = {'estado' : True}

# Dicionário de perguntas e respostas
questões = {
    "Quem descobriu o Brasil?": [
        "Pedro Álvares Cabral",
        "Messi",
        "Cristiano Ronaldo",
        "Não foi descoberto"
    ],
    "Qual a população da China?": [
        "1.411 Bilhão",
        "1.509 Bilhão",
        "1.659 Bilhão",
        "1.312 Bilhão"
    ],
    "Qual a maior empresa do mundo?":[
        "Strawberry Studio",
        "Nvidia",
        "Google",
        "Microsoft"
    ],
    "Qual a melhor linguagem de programção?":[
        "Python",
        "C++",
        "C",
        "JavaScript"
    ],
    "Qual é o mais inteligente?":[
        "Albert Eistein",
        "Nikolas Tesla",
        "Marie Curie",
        "Sócrates"
    ],
    "Qual o melhor jogo?":[
        "Minecraft",
        "Elden Ring",
        "GTA V",
        "Hollow Knight"
    ],
}

# Inicia a thread do quiz
principal = th.Thread(target=quiz, args=(questões, config))
principal.start()

# Inicia a thread do temporizador
cont = th.Thread(target=tempo, args=(config,))
cont.start()

# Aguarda o término de ambas as threads
cont.join()
principal.join()