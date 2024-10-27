# importar a biblioteca pygame
import pygame
import os
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'


pygame.mixer.init()

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()