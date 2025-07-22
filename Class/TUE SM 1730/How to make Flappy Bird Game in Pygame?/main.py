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
    offset = HEIGHT / 3
    pipeHeight = game_images['pipe'][0].get_height()
    y2 = offset + random.randrange(0, int(HEIGHT-game_images['base'].get_height()-1.2*offset))
    y1 = pipeHeight - y2 + offset
    x = WIDTH + 10
    pipe = [
        {
            'x' : x,
            'y' : -y1
        },
        {
            'x' : x,
            'y' : y2
        }
    ]

    return pipe

def isGameOver(horizontal, vertical, up_pipes, down_pipes) :
    if vertical > elevation - 25 or vertical < 0 :
        return True
   
    for pipe in up_pipes :
        pipeHeight = game_images['pipe'][0].get_height()
        if vertical < pipeHeight + pipe['y'] and \
            abs(horizontal - pipe['x']) < game_images['pipe'][0].get_width() :
                return True
   
    for pipe in down_pipes :
        birdHeight = game_images['flappybird'].get_height()
        if vertical + birdHeight > pipe['y'] and \
            abs(horizontal - pipe['x']) < game_images['pipe'][0].get_width() :
                return True
       
    return False

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

        if birdVelY < birdMaxVelY and not birdFlapped :
            birdVelY += birdAccY

        if birdFlapped :
            birdFlapped = False

        birdHeight = game_images['flappybird'].get_height()
        vertical += min(birdVelY, elevation-vertical-birdHeight)

        for upperPipe, lowerPipe in zip(up_pipes, down_pipes) :
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        if 0 < up_pipes[0]['x'] < 5 :
            newpipe = createPipe()
            up_pipes.append(newpipe[0])
            down_pipes.append(newpipe[1])

        if up_pipes[0]['x'] < -game_images['pipe'][0].get_width() :
            up_pipes.pop(0)
            down_pipes.pop(0)

        screen.blit(game_images['background'], (0, 0))
        for upperPipe, lowerPipe in zip(up_pipes, down_pipes) :
            screen.blit(game_images['pipe'][0], (upperPipe['x'], upperPipe['y']))
            screen.blit(game_images['pipe'][1], (lowerPipe['x'], lowerPipe['y']))
        screen.blit(game_images['base'], (ground, elevation))
        screen.blit(game_images['flappybird'], (horizontal, vertical))

        numbers = [int(x) for x in list(str(score))] # e.g. 197 -> [1, 9, 7]
        width = 0
        for num in numbers :
            width += game_images['score'][num].get_width()
        offsetX = (WIDTH - width) / 1.1
        for num in numbers :
            screen.blit(game_images['score'][num], (offsetX, HEIGHT*0.02))
            offsetX += game_images['score'][num].get_width()

        pygame.display.update()
        clock.tick(fps)

# Main
if __name__ == '__main__' :
    pygame.init()
    clock = pygame.time.Clock()

    pygame.display.set_caption('Flappy Bird')

    game_images['flappybird'] = pygame.image.load(birdImage).convert_alpha()
    game_images['base'] = pygame.image.load(baseImage).convert_alpha()
    game_images['background'] = pygame.image.load(backgroundImage).convert_alpha()
    game_images['pipe'] = (
        pygame.transform.rotate(pygame.image.load(pipeImage).convert_alpha(), 180),
        pygame.image.load(pipeImage).convert_alpha()
        )
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
