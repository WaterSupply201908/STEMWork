import pygame
from sys import exit
from random import randint

def display_score() :
  current_time = (pygame.time.get_ticks() - start_time) // 1000
  score_surface = test_font.render(f'Score: {current_time}', False, 'Black')
  score_rect = score_surface.get_rect(center=(400, 50))
  screen.blit(score_surface, score_rect)

  return current_time

def obstacle_movement(obstacle_list) :
  if obstacle_list :
    for obstacle_rect in obstacle_list :
      obstacle_rect.x -= 5

      if obstacle_rect.bottom == 300 :
        screen.blit(snail_surface, obstacle_rect)
      else :
        screen.blit(fly_surface, obstacle_rect)

    obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

    return obstacle_list
  else :
    return []

def player_animation() :
  global player_surface, player_index

  if player_rect.bottom < 300 :
    player_surface = player_jump
  else :
    player_index += 0.1

    if player_index >= len(player_walk) :
      player_index = 0

    player_surface = player_walk[int(player_index)]

# Main
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 50)

sky_surface = pygame.image.load('Sky.png').convert_alpha()
ground_surface = pygame.image.load('ground.png').convert_alpha()
#score_surface = test_font.render('My Game', False, 'Black')
#score_rect = score_surface.get_rect(center=(400, 50))

snail_frame_1 = pygame.image.load('snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('snail2.png').convert_alpha()
snail_frame = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frame[snail_frame_index]

fly_frame_1 = pygame.image.load('fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('fly2.png').convert_alpha()
fly_frame = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frame[fly_frame_index]

snail_surface = pygame.image.load('snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

obstacle_rect_list = []

player_surface = pygame.image.load('player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_stand = pygame.image.load('player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

player_walk_1 = pygame.image.load('player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('jump.png').convert_alpha()

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))
game_message = test_font.render('Press space to run...', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 320))

obstacle_time = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_time, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

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
          player_gravity = -20
      elif e.type == obstacle_time :
        if randint(0, 2) :
          obstacle_rect_list.append(snail_surface.get_rect(midbottom=(600, 300)))
        else :
          obstacle_rect_list.append(fly_surface.get_rect(midbottom=(600, 210)))
    else :
      if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE :
        game_active = True
        snail_rect.left = 800
        start_time = pygame.time.get_ticks() // 1000

  if game_active :
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    score = display_score()
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
    player_animation()
    screen.blit(player_surface, player_rect)
 
    obstacle_rect_list = obstacle_movement(obstacle_rect_list)

    if player_rect.colliderect(snail_rect) :
      game_active = False
  else :
    screen.fill((94, 129, 162))
    screen.blit(player_stand, player_stand_rect)
    score_message = test_font.render(f'Your Score: {score}', False, (111, 196, 169))
    score_message_rect = score_message.get_rect(center=(400, 330))
    screen.blit(game_name, game_name_rect)
    if score == 0 :
      screen.blit(game_message, game_message_rect)
    else :
      screen.blit(score_message, score_message_rect)
 
  pygame.display.update()
  clock.tick(60)
