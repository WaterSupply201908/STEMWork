import pygame
import random

pygame.init()

WIDTH, HEIGHT = 720, 720
c1 = random.randint(125, 255)
c2 = random.randint(0, 255)
c3 = random.randint(0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
color_list = [RED, GREEN, BLUE]

colox_c1 = 0
colox_c2 = 0
colox_c3 = 254
colox_c4 = 254

player_c = random.choice(color_list)

startl = (169, 169, 169)
startd = (100, 100, 100)
WHITE = (255, 255, 255)
start = (255, 255, 255)

lead_x, lead_y = 40, HEIGHT / 2
x, y = 300, 290
width_i, height_i = 100, 40
enemy_size = 50

text_font = pygame.font.SysFont('Corbel', 35)
text_s = text_font.render('Start', True, WHITE)
text_o = text_font.render('Options', True, WHITE)
text_e = text_font.render('Exit', True, WHITE)
colox = text_font.render('Colox', True, (c3, c2, c1))

x1 = random.randint(int(WIDTH/2), WIDTH)
y1 = random.randint(100, int(HEIGHT/2))
x2, y2, = 40, 40
speed = 15

count = 0
e1_p = [WIDTH, random.randint(50, HEIGHT-50)]
e2_p = [random.randint(WIDTH, WIDTH+100), random.randint(50, HEIGHT-100)]

pygame.draw.rect(screen, startd, [100, HEIGHT-100, 40, 20])
pygame.draw.rect(screen, startd, [WIDTH-180, HEIGHT-100, 40, 50])

def intro(colox_c1, colox_c2, colox, text_e, text_o, text_s) :
    intro = True

    while intro :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()

        screen.fill((65, 25, 64))
        mouse = pygame.mouse.get_pos()

        if x < mouse[0] < x+width_i and y < mouse[1] < y+height_i :
            pygame.draw.rect(screen, startl, [x, y, width_i, height_i])
        else :
            if x < mouse[0] < x+width_i+40 and y+70 < mouse[1] < y+height_i+70 :
                pygame.draw.rect(screen, startl, [x, y+70, width_i+40, height_i])
            else :
                if x < mouse[0] < x+width_i and y+140 < mouse[1] < y+height_i+140 :
                    pygame.draw.rect(screen, startl, [x, y+140, width_i, height_i])
                else :
                    pygame.draw.rect(screen, startl, [x, y, width_i, height_i])
                    pygame.draw.rect(screen, startl, [x, y+70, width_i+40, height_i])
                    pygame.draw.rect(screen, startl, [x, y+140, width_i, height_i])

        if event.type == pygame.MOUSEBUTTONDOWN :
            if x < mouse[0] < x+width_i and y < mouse[1] < y+height_i :
                game(lead_x, lead_y, speed, count)
            elif x < mouse[0] < x+width_i and y+140 < mouse[1] < y+height_i+140 :
                pygame.quit()

        pygame.draw.rect(screen, (c2, colox_c1, colox_c2), [0, 0, 40, HEIGHT])
        pygame.draw.rect(screen, (c2, colox_c1, colox_c2), [WIDTH-40, 0, 40, HEIGHT])

        text_font = pygame.font.SysFont('Corbel', 35)
        text_s = text_font.render('Start', True, WHITE)
        text_o = text_font.render('Options', True, WHITE)
        text_e = text_font.render('Exit', True, WHITE)
        colox = text_font.render('Colox', True, (c1, colox_c1, colox_c2))

        screen.blit(text_s, (312, 295))
        screen.blit(text_o, (312, 365))
        screen.blit(text_e, (312, 435))
        screen.blit(colox, (312, 50))

        clock.tick(60)
        pygame.display.update()

def game(lead_x, lead_y, speed, count) :
    pass

def game_over() :
    pass

intro(colox_c1, colox_c2, colox, text_e, text_o, text_s)
