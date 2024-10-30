from função import *
import threading
questões = {
    "Quem descobriu o Brasil?":[
        "Pedro Álvares Cabral", 
        "Messi", 
        "cristiano Ronaldo", 
        "Não foi descoberto"
        ],
    "Qual a população da china?":[
        "1.411 Bilhão", 
        "1.509 Bilhão", 
        "1.659 Bilhão", 
        "1.312 Bilhão"
        ],
}

acabouQuest = 0
acabouTemp = 0
while acabouQuest == False or acabouTemp == False:
    
    acabouQuest = quiz_thread = threading.Thread(target=quiz, args=(questões, acabouTemp))
    acabouTemp = tempo_thread = threading.Thread(target=tempo, args=(acabouQuest))
    
    quiz_thread.start()
    tempo_thread.start()
    quiz_thread.join()
    tempo_thread.join()
    