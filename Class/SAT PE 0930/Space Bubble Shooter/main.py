import pygame, random, math, sys

# Contants
WIDTH, HEIGHT = 640, 480
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (255, 165, 0),
    (128, 0, 128)
]
FLAMES = [(255, 165, 0), (255, 215, 0), (255, 69, 0)]

# Config
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Bubble Shooter')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Class
class Ship :
    def __init__(self) :
        self.x, self.y = WIDTH//2, HEIGHT-40
        self.speed = 5

    def draw(self) :
        # Ship Body
        pygame.draw.polygon(
            screen,
            WHITE,
            [
                (self.x, self.y),
                (self.x-20, self.y+30),
                (self.x+20, self.y+30)
            ]
        )

        # Thruster Flames
        pygame.draw.polygon(
            screen,
            random.choice(FLAMES),
            [
                (self.x, self.y+30),
                (self.x-10, self.y+40),
                (self.x+10, self.y+40)
            ]
        )

    def move(self, direction) :
        if direction == 'left' and self.x > 20 :
            self.x -= self.speed
        elif direction == 'right' and self.x < WIDTH-20 :
            self.x += self.speed

class Laser :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        self.speed = 7
        self.active = True

    def update(self) :
        self.y -= self.speed

        if self.y < 0 :
            self.active = False

    def draw(self) :
        pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x, self.y+15), 3)

class Bubble :
    def __init__(self) :
        self.reset()

    def update(self) :
        self.y += self.speed

        if self.y > HEIGHT + self.radius :
            self.reset()

    def reset(self) :
        pass

    def draw(self) :
        pass

# Main
ship = Ship()
lasers, bubbles, explosions = [], [Bubble() for _ in range(8)], []
score, game_over = 0, False

running = True
while running :
    # Event Queue
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        elif event.type == pygame.KEYDOWN :
            pass

    # Background
    screen.fill(BLACK)
    for _ in range(50) :
        pygame.draw.circle(screen, WHITE, (random.randint(0, WIDTH), random.randint(0, HEIGHT)), 1)

    # Game Logic
    if not game_over :
        ship.draw()
   
    # Update Display
    pygame.display.flip() # pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
