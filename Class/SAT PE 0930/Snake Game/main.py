import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill((0, 0, 255))
test_rect = pygame.Rect(100, 200, 100, 100)

while True :
  for e in pygame.event.get() :
    if e.type == pygame.QUIT :
      pygame.quit()
      sys.exit()

  screen.fill(pygame.Color('gold'))
  pygame.draw.rect(screen, (255, 0, 0), test_rect)
  screen.blit(test_surface, (200, 200))
  
  pygame.display.update()
  clock.tick(60)
