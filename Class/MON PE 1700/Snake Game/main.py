import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 500))

while True :
    for e in pygame.event.get() :
        if e.type == pygame.QUIT :
            pygame.quit()
            sys.exit()

    # Game Logic
    pygame.display.update()
