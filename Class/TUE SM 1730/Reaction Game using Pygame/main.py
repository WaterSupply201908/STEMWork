import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Reaction Game')
clock = pygame.time.Clock()

running = True
rect_visible = False
rect_x, rect_y = 0, 0
reaction_time, start_time = 0, 0

while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and rect_visible :
            reaction_time = pygame.time.get_ticks() - start_time
            print(f'Reaction Time : {reaction_time} ms')
            rect_visible = False

    screen.fill((0, 0, 0))

    if not rect_visible and random.random() < 0.05 :
        rect_visible = True
        rect_x = random.randint(0, WIDTH-50)
        rect_y = random.randint(0, HEIGHT-50)
        start_time = pygame.time.get_ticks()

    if rect_visible :
        pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, 50, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
