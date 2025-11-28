import pygame, random, sys

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Color Match")
clock = pygame.time.Clock()

# Constants
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
COLOR_NAMES = ["Red", "Green", "Blue", "Yellow"]

# Variables
score = 0
target_color = random.randint(0, 3)
current_color = random.randint(0, 3)
change_timer = 0
font = pygame.font.Font(None, 36)

# Functions
def init_color() :
    global current_color, change_timer

    current_color = random.randint(0, 3)
    change_timer = 0

running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                if target_color == current_color :
                    score += 1
                else :
                    score = max(0, score-1)

                # current_color = random.randint(0, 3)
                # change_timer = 0
                init_color()

    change_timer += 1
    if change_timer > 90 :
        # current_color = random.randint(0, 3)
        # change_timer = 0
        init_color()

    # Change display
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, COLORS[current_color], (200, 200), 100)
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    target_text = font.render(f'Match: {COLOR_NAMES[target_color]}', True, COLORS[target_color])
    screen.blit(score_text, (10, 10))
    screen.blit(target_text, (10, 350))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
