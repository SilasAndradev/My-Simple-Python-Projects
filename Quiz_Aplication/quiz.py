from função import tempo, quiz
from threading import Thread
from threading import Event




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



p1 = Thread(target=quiz, args=(questões, acabouTemp))
p2 = Thread(target=tempo, args=(acabouQuest,))
thread2 = MyThread(p1)
thread2.start()
thread1 = MyThread(p2)
thread1.start()

if p1 == True or p2 == False:
   p1.set()
   thread1.join()
   p2.set()
   thread2.join()