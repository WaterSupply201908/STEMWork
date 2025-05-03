import pygame
from pygame import Vector2
import sys
import random

CELL_SIZE, CELL_NUMBER = 40, 20

class Snake :
  def __init__(self) :
    self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
    self.direction = Vector2(1, 0)

  def draw_snake(self) :
    for block in self.body :
      block_rect = pygame.Rect(block.x*CELL_SIZE, block.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
      pygame.draw.rect(screen, (183, 191, 122), block_rect)

class Fruit :
  def __init__(self) :
    # create x & y pos
    self.x = random.randint(0, CELL_NUMBER-1)
    self.y = random.randint(0, CELL_NUMBER-1)
    self.pos = Vector2(self.x, self.y)
  # draw a square
  def draw_fruit(self) :
    fruit_rect = pygame.Rect(self.pos.x*CELL_SIZE, self.pos.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

pygame.init()

screen = pygame.display.set_mode((CELL_SIZE*CELL_NUMBER, CELL_SIZE*CELL_NUMBER))
clock = pygame.time.Clock()
fruit = Fruit()
snake = Snake()

test_surface = pygame.Surface((100, 200))
test_surface.fill((0, 0, 255))
test_rect = test_surface.get_rect(center=(200, 250))

while True :
  for e in pygame.event.get() :
    if e.type == pygame.QUIT :
      pygame.quit()
      sys.exit()

  screen.fill((175, 215, 70))
  fruit.draw_fruit()
  snake.draw_snake()
  
  pygame.display.update()
  clock.tick(60)
