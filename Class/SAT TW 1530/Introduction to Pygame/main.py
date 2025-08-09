import pygame
from sys import exit

def display_score() :
  current_time = (pygame.time.get_ticks() - start_time) // 1000
  score_surface = test_font.render(f'Score: {current_time}', False, 'Black')
  score_rect = score_surface.get_rect(center=(400, 50))
  screen.blit(score_surface, score_rect)

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 50)

sky_surface = pygame.image.load('Sky.png').convert_alpha()
ground_surface = pygame.image.load('ground.png').convert_alpha()
#score_surface = test_font.render('My Game', False, 'Black')
#score_rect = score_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load('snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

player_surface = pygame.image.load('player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_stand = pygame.image.load('player_stand.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center=(400, 200))
player_gravity = 0

game_active = False
start_time = 0

while True :
  for e in pygame.event.get() :
    if e.type == pygame.QUIT :
      pygame.quit()
      exit()
    if game_active :
      if e.type == pygame.KEYDOWN :
        if e.key == pygame.K_SPACE and player_rect.bottom >= 300 :
          player_gravity = -20
    else :
      if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE :
        game_active = True
        snail_rect.left = 800
        start_time = pygame.time.get_ticks()

  if game_active :
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    display_score()
#    pygame.draw.rect(screen, '#C0E8EC', score_rect)
#    pygame.draw.rect(screen, '#C0E8EC', score_rect, 10)
#    screen.blit(score_surface, score_rect)

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
    screen.fill((94, 129, 162))
    screen.blit(player_stand, player_stand_rect)
 
  pygame.display.update()
  clock.tick(60)
