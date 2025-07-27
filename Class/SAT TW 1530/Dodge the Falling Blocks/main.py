import pygame
import random
import sys

WIDTH, HEIGHT = 480, 640
PLAYER_RADIUS = 20
BLOCK_SIZE = 30
BLOCK_FALL_SPEED = 4
SPEED_INCREMENT = 0.2
SPAWN_EVENT = pygame.USEREVENT + 1
SPAWN_INTERVAL = 800
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dodge the Falling Blocks')
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 32)

player_x = WIDTH // 2
player_y = HEIGHT - PLAYER_RADIUS*2
player_speed = 6

blocks = []
block_speed = BLOCK_FALL_SPEED
pygame.time.set_timer(SPAWN_EVENT, SPAWN_INTERVAL)

start_ticks = pygame.time.get_ticks()
game_over = False

def draw_player(x, y) :
    pygame.draw.circle(screen, (50, 150, 255), (x, y), PLAYER_RADIUS)

def draw_blocks() :
    for rect in blocks :
        pygame.draw.rect(screen, (200, 50, 50), rect)

def show_text(text, y) :
    surf = font.render(text, True, (255, 255, 255))
    rect = surf.get_rect(center=(WIDTH//2, y))
    screen.blit(surf, rect)

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        elif event.type == SPAWN_EVENT and not game_over :
            x_pos = random.randrange(0, WIDTH-BLOCK_SIZE)
            blocks.append(pygame.Rect(x_pos, -BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            block_speed += SPEED_INCREMENT

    keys = pygame.key.get_pressed()
    if not game_over :
        if keys[pygame.K_LEFT] and player_x - player_speed - PLAYER_RADIUS > 0 :
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x + player_speed + PLAYER_RADIUS < WIDTH :
            player_x += player_speed

    pygame.display.flip()
    clock.tick(FPS)
