import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 50) # ttf : true type font

sky_surface = pygame.image.load('Sky.png').convert()
ground_surface = pygame.image.load('ground.png').convert()
test_surface = test_font.render('My Game', False, 'Black')

snail_surface = pygame.image.load('snail1.png').convert_alpha()
snail_x_pos = 600

while True :
    for e in pygame.event.get() :
        if e.type == pygame.QUIT :
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(test_surface, (300, 50))
    snail_x_pos -= 4
    if snail_x_pos < -100 :
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 250))
    pygame.display.update()
    clock.tick(60)
