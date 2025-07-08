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

def createPipe() :
    pass

def isGameOver(horizontal, vertical, up_pipes, down_pipes) :
    pass

def flappygame() :
    score = 0
    horizontal = int(WIDTH/5)
    vertical = int(HEIGHT/2)
    ground = 0
    tempHeight = 100

    first_pipe = createPipe()
    second_pipe = createPipe()

    down_pipes = [
        {
            'x' : WIDTH+300-tempHeight,
            'y' : first_pipe[1]['y'],
        },
        {
            'x' : WIDTH+300-tempHeight+(WIDTH/2),
            'y' : second_pipe[1]['y'],
        }
    ]
    up_pipes = [
        {
            'x' : WIDTH+300-tempHeight,
            'y' : first_pipe[0]['y'],
        },
        {
            'x' : WIDTH+300-tempHeight+(WIDTH/2),
            'y' : second_pipe[0]['y'],
        }
    ]

    pipeVelX = -4

    birdVelY = -9
    birdMaxVelY = 10
    birdMinVelY = -8
    birdAccY = 1

    birdFlapVel = -8
    birdFlapped = False

    while True :
        for event in pygame.event.get() :
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) :
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE :
                if vertical > 0 :
                    birdVelY = birdFlapVel
                    birdFlapped = True

        if isGameOver(horizontal, vertical, up_pipes, down_pipes) :
            return

        playerMidPos = horizontal + game_images['flappybird'].get_width()/2
        for pipe in up_pipes :
            pipeMidPos = pipe['x'] + game_images['pipe'][0].get_width()/2

            if pipeMidPos <= playerMidPos < pipeMidPos+4 :
                score += 1
                print(f'Score : {score}')

# Main
if __name__ == '__main__' :
    pygame.init()
    clock = pygame.time.Clock()

    pygame.display.set_caption('Flappy Bird')

    game_images['flappybird'] = pygame.image.load(birdImage).convert_alpha()
    game_images['base'] = pygame.image.load(baseImage).convert_alpha()
    game_images['background'] = pygame.image.load(backgroundImage).convert_alpha()
    game_images['pipe'] = pygame.image.load(pipeImage).convert_alpha()
    game_images['score'] = (
        pygame.image.load('0.png').convert_alpha(),
        pygame.image.load('1.png').convert_alpha(),
        pygame.image.load('2.png').convert_alpha(),
        pygame.image.load('3.png').convert_alpha(),
        pygame.image.load('4.png').convert_alpha(),
        pygame.image.load('5.png').convert_alpha(),
        pygame.image.load('6.png').convert_alpha(),
        pygame.image.load('7.png').convert_alpha(),
        pygame.image.load('8.png').convert_alpha(),
        pygame.image.load('9.png').convert_alpha()
    )

    print('WELCOME TO FLAPPY BIRD GAME!')
    print('Press <space> to start the game...')

    while True :
        horizontal = WIDTH//5
        vertical = int((HEIGHT-game_images['flappybird'].get_height())/2)
        ground = 0

        while True :
            for event in pygame.event.get() :
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) :
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
