import pygame
import sys

class Fruit :
    def __init__(self) :
        # create x and y pos
        self.x = 5
        self.y = 4
        self.pos = pygame.math.Vector2(self.x, self.y)
        # draw a square

pygame.init()
CELL_SIZE = 40
CELL_NUMBER = 20
screen = pygame.display.set_mode((CELL_NUMBER*CELL_SIZE, CELL_NUMBER*CELL_SIZE))
clock = pygame.time.Clock()

while True :
    for e in pygame.event.get() :
        if e.type == pygame.QUIT :
            pygame.quit()
            sys.exit()

    # Game Logic
    screen.fill((175, 215, 70))

    pygame.display.update()
    clock.tick(60)
