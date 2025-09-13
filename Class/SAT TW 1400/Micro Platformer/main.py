import pygame, sys, random

WIDTH, HEIGHT = 800, 600
BLUE, BROWN, GREEN, WHITE, GOLD = (80, 120, 255), (139, 69, 19), (0, 150, 0), (255, 255, 255), (255, 215, 0)

player = pygame.Rect(50, HEIGHT-150, 30, 50) # HEIGHT-150 -> HEIGHT-90
velocity_y = 0
isJumping = False
gravity = 0.5
jumpStrength = 12
moveSpeed = 5

PLATFORMS = [
    [0,   HEIGHT-40,  WIDTH, 40], # Ground
    [100, HEIGHT-120, 150,   20],
    [400, HEIGHT-200, 200,   20],
    [100, HEIGHT-280, 150,   20],
    [500, HEIGHT-350, 200,   20]
]

FOODS = [
    [170, HEIGHT-140, False],
    [470, HEIGHT-220, False],
    [170, HEIGHT-300, False],
    [570, HEIGHT-370, False]
]

score = 0
running = True

# Main
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Micro Platformer")
clock = pygame.time.Clock()

while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] :
        player.x -= moveSpeed
    elif keys[pygame.K_RIGHT] :
        player.x += moveSpeed
    elif keys[pygame.K_SPACE] and not isJumping :
        isJumping = True
        velocity_y = -jumpStrength

    player.y += velocity_y
    velocity_y += gravity

    for p in PLATFORMS :
        platform = pygame.Rect(p[0], p[1], p[2], p[3])

        if player.colliderect(platform) and velocity_y > 0 and player.bottom <= p[1] + 15 :
            player.bottom = p[1]
            isJumping = False
            velocity_y = 0

    for f in FOODS :
        food = pygame.Rect(f[0], f[1], 20, 20)

        if not f[2] and player.colliderect(food) :
            f[2] = True
            score += 1

    screen.fill((135, 206, 235))

    for p in PLATFORMS :
        pygame.draw.rect(screen, BROWN, p)

    for f in FOODS :
        if not f[2] :
            pygame.draw.circle(screen, GOLD, (f[0]+10, f[1]+10), 10)

    pygame.draw.rect(screen, BLUE, player)

    screen.blit(pygame.font.SysFont(None, 36).render(f"Score: {score}/4", True, WHITE), (10, 10))

    if score == 4 :
        winText = pygame.font.SysFont(None, 72).render("You Win!", True, WHITE)
        screen.blit(winText, (WIDTH//2 - winText.get_width()//2, HEIGHT//2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
