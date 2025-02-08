import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

sky_surface = pygame.image.load('Runner/Sky.png')
ground_surface = pygame.image.load('Runner/ground.png')

while True :
  for e in pygame.event.get() :
    if e.type == pygame.QUIT :
      pygame.quit()
      exit()

  screen.blit(sky_surface, (0, 0))
  screen.blit(ground_surface, (0, 300))

  pygame.display.update()
  clock.tick(60)
