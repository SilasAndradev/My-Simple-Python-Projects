from função import tempo, quiz
import threading 




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

acabouQuest = False
acabouTemp = False


p1 = threading.Thread(target=quiz, kwargs={'questões': questões, 'acabouTemp': acabouTemp, })
p2 = threading.Thread(target=tempo, kwargs=({'acabouQuest': acabouQuest}))

while acabouTemp == False or acabouQuest == False:
        p1.start()
        p2.start()
        if p1.not_alive():
            p2.join()
            break
        elif p2.not_alive():
            p1.join()
            break
        

#while not p1.is_alive() or not p2.is_alive():
