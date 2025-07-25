import pygame
import random
import sys

# ------------------ Config ------------------
WIDTH, HEIGHT = 480, 640
PLAYER_RADIUS = 20
BLOCK_SIZE = 30
BLOCK_FALL_SPEED = 4          # initial pixels per frame
SPEED_INCREMENT = 0.2         # blocks speed up each spawn
SPAWN_EVENT = pygame.USEREVENT + 1
SPAWN_INTERVAL = 800          # ms
FPS = 60

# ------------------ Init ------------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 32)

# Player start
player_x = WIDTH // 2
player_y = HEIGHT - PLAYER_RADIUS*2
player_speed = 6

# Blocks list
blocks = []
block_speed = BLOCK_FALL_SPEED
pygame.time.set_timer(SPAWN_EVENT, SPAWN_INTERVAL)

# Score
start_ticks = pygame.time.get_ticks()
game_over = False

# ------------------ Helpers ------------------
def draw_player(x, y):
    pygame.draw.circle(screen, (50, 150, 255), (x, y), PLAYER_RADIUS)

def draw_blocks():
    for rect in blocks:
        pygame.draw.rect(screen, (200, 50, 50), rect)

def show_text(text, y):
    surf = font.render(text, True, (255, 255, 255))
    rect = surf.get_rect(center=(WIDTH//2, y))
    screen.blit(surf, rect)

# ------------------ Main Loop ------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SPAWN_EVENT and not game_over:
            x_pos = random.randrange(0, WIDTH-BLOCK_SIZE)
            blocks.append(pygame.Rect(x_pos, -BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            block_speed += SPEED_INCREMENT

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT] and player_x - player_speed - PLAYER_RADIUS > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x + player_speed + PLAYER_RADIUS < WIDTH:
            player_x += player_speed

    # Update block positions
    for rect in blocks:
        if not game_over:
            rect.y += block_speed

    # Collision check
    player_rect = pygame.Rect(player_x-PLAYER_RADIUS, player_y-PLAYER_RADIUS,
                              PLAYER_RADIUS*2, PLAYER_RADIUS*2)
    if any(rect.colliderect(player_rect) for rect in blocks):
        game_over = True

    # Remove off-screen blocks
    blocks = [r for r in blocks if r.y < HEIGHT]

    # Draw everything
    screen.fill((30, 30, 30))
    draw_player(player_x, player_y)
    draw_blocks()

    # Score display
    if not game_over:
        elapsed_ms = pygame.time.get_ticks() - start_ticks
    score_sec = elapsed_ms // 1000
    show_text(f"Score: {score_sec}", 30)

    if game_over:
        show_text("Game Over! Press R to Restart", HEIGHT//2)
        if keys[pygame.K_r]:
            # Reset everything
            blocks.clear()
            player_x = WIDTH // 2
            block_speed = BLOCK_FALL_SPEED
            start_ticks = pygame.time.get_ticks()
            game_over = False

    pygame.display.flip()
    clock.tick(FPS)
