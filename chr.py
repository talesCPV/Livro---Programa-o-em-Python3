import pygame
from pygame.locals import *

screen = pygame.display.set_mode((320,640), 0, 32)
pygame.display.set_caption('Open NES Roms Images - CHR Files')

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill([0, 0, 0])
    for row in range(32):
        for col in range (64):
            pygame.draw.rect(screen, (255, 0, 0),[row*10, col*10] + [9,9], 0)

    pygame.display.update()