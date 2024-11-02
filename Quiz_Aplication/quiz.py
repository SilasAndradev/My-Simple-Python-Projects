from função import tempo, quiz
import threading as th

config = {"estado": True}
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
}



# Inicia a thread principal do quiz
principal = th.Thread(target=quiz, args=(questões, config))
principal.start()

# Inicia a thread do temporizador
cont = th.Thread(target=tempo, args=(config,))
cont.start()

cont.join()
principal.join()