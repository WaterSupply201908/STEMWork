import pygame
import random

pygame.init()
WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monkey Banana Catcher!")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# Colors
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLUE = (0, 150, 255)

# Monkey
monkey_img = pygame.Surface((60, 60), pygame.SRCALPHA)
pygame.draw.circle(monkey_img, BROWN, (30, 35), 30)  # head
pygame.draw.circle(monkey_img, (222, 184, 135), (30, 50), 15)  # mouth
pygame.draw.circle(monkey_img, WHITE, (22, 35), 7)  # eyes
pygame.draw.circle(monkey_img, WHITE, (38, 35), 7)
pygame.draw.circle(monkey_img, (0,0,0), (22, 35), 3)  # pupils
pygame.draw.circle(monkey_img, (0,0,0), (38, 35), 3)
monkey_x = WIDTH//2 - 30

# Falling objects
class Falling:
    def __init__(self):
        self.reset()
    def reset(self):
        self.x = random.randint(20, WIDTH-20)
        self.y = -40
        self.kind = random.choice(['banana','boot','hat'])
    def move(self):
        self.y += 7
    def draw(self):
        if self.kind == 'banana':
            pygame.draw.ellipse(screen, YELLOW, (self.x, self.y, 30, 15))
            pygame.draw.line(screen, GREEN, (self.x+25, self.y+7), (self.x+30, self.y), 4)
        elif self.kind == 'boot':
            pygame.draw.rect(screen, BLUE, (self.x, self.y, 25, 18))
            pygame.draw.rect(screen, BROWN, (self.x, self.y+12, 25, 8))
        else:
            pygame.draw.rect(screen, RED, (self.x, self.y, 28, 15))
            pygame.draw.polygon(screen, WHITE, [(self.x, self.y), (self.x+14, self.y-12), (self.x+28, self.y)])

fallings = [Falling() for _ in range(3)]
score = 0
funny = False
funny_timer = 0
run = True
while run:
    screen.fill((200, 255, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Move monkey
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and monkey_x > 0:
        monkey_x -= 8
    if keys[pygame.K_RIGHT] and monkey_x < WIDTH-60:
        monkey_x += 8
    screen.blit(monkey_img, (monkey_x, HEIGHT-80))
    # Move and draw fallings
    for f in fallings:
        f.move()
        f.draw()
        # Collision
        if HEIGHT-90 < f.y+20 < HEIGHT-20 and monkey_x < f.x < monkey_x+60:
            if f.kind == 'banana':
                score += 1
            else:
                funny = True
                funny_timer = pygame.time.get_ticks()
            f.reset()
        elif f.y > HEIGHT:
            f.reset()
    # Funny face
    if funny:
        pygame.draw.arc(screen, RED, (monkey_x+15, HEIGHT-40, 30, 20), 3.14, 0, 4)
        if pygame.time.get_ticks() - funny_timer > 800:
            funny = False
    # Draw score
    txt = font.render(f"Bananas: {score}", True, (0,0,0))
    screen.blit(txt, (10, 10))
    pygame.display.flip()
    clock.tick(40)
pygame.quit()
