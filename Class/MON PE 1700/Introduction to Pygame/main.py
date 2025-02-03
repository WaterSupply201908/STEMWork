import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 50) # ttf : true type font

sky_surface = pygame.image.load('Sky.png').convert()
ground_surface = pygame.image.load('ground.png').convert()

score_surface = test_font.render('My Game', False, 'Black')
score_rect = score_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load('snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

player_surface = pygame.image.load('player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = -20

while True :
    for e in pygame.event.get() :
        if e.type == pygame.QUIT :
            pygame.quit()
            exit()
        if e.type == pygame.KEYDOWN :
            if e.key == pygame.K_SPACE :
                player_gravity = -20

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#C0E8EC', score_rect)
    screen.blit(score_surface, score_rect)

    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE] :
    #    print('jump')

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
        print('Yes')

    pygame.display.update()
    clock.tick(60)
