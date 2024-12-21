import pygame
from pygame import Vector2
import sys
import random


class Snake:

  def __init__(self):
    self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
    self.direction = Vector2(1, 0)

  def draw_snake(self):
    for block in self.body:
      block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size,
                               cell_size, cell_size)
      pygame.draw.rect(screen, (183, 191, 122), block_rect)

  def move_snake(self):
    body_copy = self.body[:-1]
    body_copy.insert(0, body_copy[0] + self.direction)
    self.body = body_copy

class Fruit:

  def __init__(self):
    self.x = random.randint(0, cell_number - 1)
    self.y = random.randint(0, cell_number - 1)
    self.pos = Vector2(self.x, self.y)

  def draw_fruit(self):
    fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size,
                             cell_size, cell_size)
    pygame.draw.rect(screen, (126, 166, 114), fruit_rect)


# Main program
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
fruit = Fruit()
snake = Snake()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      pygame.quit()
      exit()
    if e.type == SCREEN_UPDATE:
      snake.move_snake()
    if e.type == pygame.KEYDOWN:
      if e.key == pygame.K_UP:
        snake.direction = Vector2(0, -1)
      if e.key == pygame.K_RIGHT:
        snake.direction = Vector2(1, 0)
      if e.key == pygame.K_DOWN:
        snake.direction = Vector2(0, 1)
      if e.key == pygame.K_LEFT:
        snake.direction = Vector2(-1, 0)

  screen.fill((175, 215, 70))
  fruit.draw_fruit()
  snake.draw_snake()

  pygame.display.update()
  clock.tick(60)
