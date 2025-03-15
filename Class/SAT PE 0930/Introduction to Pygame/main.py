import pygame
from sys import exit
from random import randint

def display_score() :
  current_time = int(pygame.time.get_ticks()/1000) - start_time
  score_surface = test_font.render(f'Score : {current_time}', False, 'Black')
  score_rect = score_surface.get_rect(center = (400, 50))
  screen.blit(score_surface, score_rect)

  return current_time

def obstacle_movement(obstacle_list) :
  if obstacle_list :
    for obstacle_rect in obstacle_list :
      obstacle_rect.x -= 4

      if obstacle_rect.bottom == 300 :
        screen.blit(snail_surface, obstacle_rect)
      else :
        screen.blit(fly_surface, obstacle_rect)

    obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

    return obstacle_list
  else :
    return []

def collision(player, obstacles) :
  if obstacles :
    for obstacle_rect in obstacles :
      if player.colliderect(obstacle_rect) :
        return False

  return True
  
# Main program
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('Runner/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('Runner/Sky.png').convert_alpha()
ground_surface = pygame.image.load('Runner/ground.png').convert_alpha()
#score_surface = test_font.render('My Game', False, 'Black')
#score_rect = score_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('Runner/snail1.png').convert_alpha()
fly_surface = pygame.image.load('Runner/Fly1.png').convert_alpha()

obstacle_rect_list = []

player_stand = pygame.image.load('Runner/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press <space> to run...', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 320))

player_surface = pygame.image.load('Runner/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

obstacle_time = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_time, 1800)

game_active = False
start_time = 0
score = 0

while True :
  for e in pygame.event.get() :
    if e.type == pygame.QUIT :
      pygame.quit()
      exit()
    if game_active :
      if e.type == pygame.KEYDOWN :
        if e.key == pygame.K_SPACE and player_rect.bottom >= 300 :
          player_gravity = -25
      if e.type == obstacle_time :
        if randint(0, 2) :
          obstacle_rect_list.append(snail_surface.get_rect(midbottom=(randint(900, 1100), 300)))
        else :
          obstacle_rect_list.append(fly_surface.get_rect(midbottom=(randint(900, 1100), 210)))
    else :
      if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE :
        game_active = True
        start_time = int(pygame.time.get_ticks()/1000)

  if game_active :
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    #pygame.draw.rect(screen, 'pink', score_rect, border_radius=10)
    #screen.blit(score_surface, score_rect)
    score = display_score()

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 300 :
      player_rect.bottom = 300
    screen.blit(player_surface, player_rect)

    obstacle_rect_list = obstacle_movement(obstacle_rect_list)
    
    game_active = collision(player_rect, obstacle_rect_list)
  else :
    screen.fill((94, 129, 162))
    screen.blit(player_stand, player_stand_rect)
    obstacle_rect_list.clear()
    player_rect.midbottom = (80, 300)
    player_gravity = 0
    score_message = test_font.render(f'Your score : {score}', False, (111, 196, 169))
    score_message_rect = score_message.get_rect(center=(400, 330))
    screen.blit(game_name, game_name_rect)
    if score == 0 :
      screen.blit(game_message, game_message_rect)
    else :
      screen.blit(score_message, score_message_rect)
  
  pygame.display.update()
  clock.tick(60)
