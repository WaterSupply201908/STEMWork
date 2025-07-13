import pygame, sys, random

WIDTH, HEIGHT = 600, 499
screen = pygame.display.set_mode((WIDTH, HEIGHT))
elevation = HEIGHT * 0.8
game_images = {}
frame_rate = 32
pipe_image = 'pipe.png'
background_image = 'background.jpg'
bird_image = 'bird.png'
sealevel_image = 'base.jfif'

def createPipe() :
  offset = HEIGHT / 3
  pipe_height = game_images['pipe'][0].get_height()
  y2 = offset + random.randrange(0, int(HEIGHT - game_images['sealevel'].get_height() - 1.2 * offset))
  y1 = pipe_height - y2 + offset
  x = WIDTH + 10
  pipes = [
    {'x' : x, 'y' : -y1},
    {'x' : x, 'y' : y2}
  ]

  return pipes

def isGameOver(horizontal, vertical, up_pipes, down_pipes) :
  pass

def flappygame() :
  score = 0
  horizontal = int(WIDTH/5)
  vertical = int(WIDTH/2)
  ground = 0
  mytempheight = 100

  first_pipe = createPipe()
  second_pipe = createPipe()

  down_pipes = [
    {
      'x' : WIDTH+300-mytempheight,
      'y' : first_pipe[1]['y']
    },
    {
      'x' : WIDTH+300-mytempheight+(WIDTH/2),
      'y' : second_pipe[1]['y']
    }
  ]

  up_pipes = [
    {
      'x' : WIDTH+300-mytempheight,
      'y' : first_pipe[0]['y']
    },
    {
      'x' : WIDTH+300-mytempheight+(WIDTH/2),
      'y' : second_pipe[0]['y']
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
      if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP) :
        if vertical > 0 :
          birdVelY = birdFlapVel
          birdFlapped = True

    gameOver = isGameOver(horizontal, vertical, up_pipes, down_pipes)

    if gameOver :
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

    playerHeight = game_images['flappybird'].get_height()
    vertical += min(birdVelY, elevation-vertical-playerHeight)

    for upperPipe, lowerPipe in zip(up_pipes, down_pipes) :
      upperPipe['x'] += pipeVelX
      lowerPipe['x'] += pipeVelX

    if 0 < up_pipes[0]['x'] < 5 :
      newpipe = createPipe()
      up_pipes.append(newpipe[0])
      down_pipes.append(newpipe[1])

# Main
if __name__ == "__main__" :
  pygame.init()
  clock = pygame.time.Clock()

  pygame.display.set_caption('Flappy Bird Game')

  game_images['scoreimages'] = (
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
  game_images['flappybird'] = pygame.image.load(bird_image).convert_alpha()
  game_images['sealevel'] = pygame.image.load(sealevel_image).convert_alpha()
  game_images['background'] = pygame.image.load(background_image).convert_alpha()
  game_images['pipe'] = (
    pygame.transform.rotate(pygame.image.load(pipe_image).convert_alpha(), 180),
    pygame.image.load(pipe_image).convert_alpha()
                        )

  print('WELCOME TO THE FLAPPY BIRD GAME')
  print('Press space or enter to start the game')

  while True :
    horizontal = int(WIDTH/5)
    vertical = int((HEIGHT - game_images['flappybird'].get_height())/2)
    ground = 0

    while True :
      for event in pygame.event.get() :
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
          pygame.quit()
          sys.exit()
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP) :
          flappygame()
        else :
          screen.blit(game_images['background'], (0, 0))
          screen.blit(game_images['flappybird'], (horizontal, vertical))
          screen.blit(game_images['sealevel'], (ground, elevation))

          pygame.display.update()
          clock.tick(frame_rate)
