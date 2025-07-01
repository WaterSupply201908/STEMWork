import pygame, random, sys
from pygame.locals import *

WIDTH, HEIGHT = 600, 499
screen = pygame.display.set_mode((WIDTH, HEIGHT))
elevation = HEIGHT * 0.8
game_images = {}
fps = 32
pipeImage = 'pipe.png'
backgroundImage = 'background.jpg'
birdImage = 'bird.png'
baseImage = 'base.jfif'

def flappygame() :
    pass

# Main
if __name__ == '__main__' :
    pygame.init()
    clock = pygame.time.Clock()

    pygame.display.set_caption('Flappy Bird')

    game_images['flappybird'] = pygame.image.load(birdImage).convert_alpha()
    game_images['base'] = pygame.image.load(baseImage).convert_alpha()
    game_images['background'] = pygame.image.load(backgroundImage).convert_alpha()
    game_images['pipe'] = pygame.image.load(pipeImage).convert_alpha()

    while True :
        horizontal = WIDTH//5
        vertical = int((HEIGHT-game_images['flappybird'].get_height())/2)
        ground = 0

        while True :
            for event in pygame.event.get() :
                if event.type == QUIT :
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_SPACE :
                    flappygame()
                else :
                    screen.blit(game_images['background'], (0, 0))
                    screen.blit(game_images['flappybird'], (horizontal, vertical))
                    screen.blit(game_images['base'], (ground, elevation))
                    pygame.display.update()
                    clock.tick(fps)
