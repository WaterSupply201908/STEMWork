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

def flappygame() :
  pass

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
  game_images['pipe'] = pygame.image.load(pipe_image).convert_alpha()

  print('WELCOME TO THE FLAPPY BIRD GAME')
  print('Press space or enter to start the game')

  while True :
    horizontal = int(WIDTH/5)
    vertical = int((HEIGHT - game_images['flappybird'].get_height())/2)
    ground = 0

    while True :
      for event in pygame.event.get() :
        if event.type == pygame.QUIT :
          pygame.quit()
          sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
          flappygame()
        else :
          pass
