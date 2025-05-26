import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Runner/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('Runner/Sky.png').convert_alpha()
ground_surface = pygame.image.load('Runner/ground.png').convert_alpha()
score_surface = test_font.render('My Game', False, 'Black')
score_rect = score_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load('Runner/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

player_surface = pygame.image.load('Runner/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

game_active = True

while True :
  for e in pygame.event.get() :
    if e.type == pygame.QUIT :
      pygame.quit()
      exit()
    if e.type == pygame.KEYDOWN :
      if e.key == pygame.K_SPACE and player_rect.bottom >= 300 :
        player_gravity = -25

  if game_active :
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#C0E8EC', score_rect)
    pygame.draw.rect(screen, '#C0E8EC', score_rect, 10)
    screen.blit(score_surface, score_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0 :
      snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 300 :
      player_rect.bottom = 300
    screen.blit(player_surface, player_rect)
  
    if player_rect.colliderect(snail_rect) :
      game_active = False
  else :
    screen.fill('Yellow')
  
  pygame.display.update()
  clock.tick(60)
