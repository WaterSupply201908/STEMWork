import pygame, random

pygame.init()
WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monkey Banana Catcher")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

monkey_img = pygame.Surface((60, 60), pygame.SRCALPHA)
pygame.draw.circle(monkey_img, BROWN, (30, 35), 30)           # head
pygame.draw.circle(monkey_img, (222, 184, 135), (30, 50), 15) # mouth
pygame.draw.circle(monkey_img, WHITE, (22, 35), 7)            # eyes
pygame.draw.circle(monkey_img, WHITE, (38, 35), 7)
pygame.draw.circle(monkey_img, BLACK, (22, 35), 3)            # pupils
pygame.draw.circle(monkey_img, BLACK, (38, 35), 3)
monkey_x = WIDTH // 2 - 30

class Falling :
    def __init__(self) :
        self.reset()

    def reset(self) :
        self.x = random.randint(20, WIDTH - 20)
        self.y = -40
        self.kind = random.choice(['banana', 'boot', 'hat'])

    def move(self) :
        self.y += 7

    def draw(self) :
        if self.kind == 'banana' :
            pygame.draw.ellipse(screen, YELLOW, (self.x, self.y, 30, 15))
            pygame.draw.line(screen, GREEN, (self.x+25, self.y+ 7), (self.x+30, self.y), 4)
        elif self.kind == 'boot' :
            pygame.draw.rect(screen, BLUE, (self.x, self.y, 25, 18))
            pygame.draw.rect(screen, BROWN, (self.x, self.y+12, 25, 8))
        elif self.kind == 'hat' :
            pygame.draw.rect(screen, RED, (self.x, self.y, 28, 15))
            pygame.draw.polygon(screen, WHITE, [(self.x, self.y), (self.x+14, self.y-12), (self.x+28, self.y)])

fallings = [Falling() for _ in range(3)]
score = 0
funny = False
funny_timer = 0
running = True

while running :
    for event in pygame.event.get() :
        if event.type == pygamge.QUIT :
            running = False

    screen.fill((200, 255, 200))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and monkey_x > 0 :
        monkey_x -= 8
    if keys[pygame.K_RIGHT] and monkey_x < WIDTH - 60 :
        monkey_x += 8
    screen.blit(monkey_img, (monkey_x, HEIGHT - 80))

    for falling in fallings :
        falling.move()
        falling.draw()

        if HEIGHT-90 < falling.y+20 < HEIGHT-20 and monkey_x < falling.x < monkey_x+60 :
            if falling.kind == 'banana' :
                score += 1
            else :
                funny = True
                funny_timer = pygame.time.get_ticks()
            falling.reset()
        elif falling.y > HEIGHT :
            falling.reset()

    if funny :
        pygame.draw.arc(screen, RED, (monkey_x+15, HEIGHT-40, 30, 20), 3.14, 0, 4)

        if pygame.time.get_ticks() - funny_timer > 800 :
            funny = False

    txt = font.render(f'Bananas: {score}', True, BLACK)
    screen.blit(txt, (10, 10))

    pygame.display.flip()
    clock.tick(40)
pygame.quit()
