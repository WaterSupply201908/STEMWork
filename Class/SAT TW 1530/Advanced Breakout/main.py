import pygame, random

# Constants
WIDTH, HEIGHT = 600, 800
FPS = 60

BRICK_ROWS = 6
BRICK_COLS = 10
BRICK_WIDTH = 54
BRICK_HEIGHT = 24
BRICK_GAP = 4

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 16
PADDLE_Y = HEIGHT - 50
PADDLE_SPEED = 9

BALL_RADIUS = 10
BALL_SPEED = 6

POWERUP_SIZE = 24
POWERUP_TYPES = ['expand', 'slow', 'multi']

# Classes
class Paddle :
    def __init__(self) :
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.rect = pygame.Rect((WIDTH-self.width)//2, PADDLE_Y, self.width, self.height)
        self.speed = PADDLE_SPEED

    def draw(self, screen) :
        pygame.draw.rect(screen, (220, 220, 255), self.rect, border_radius=10)

    def update(self, left, right) :
        if left and self.rect.left > 0 :
            self.rect.x -= self.speed
        if right and self.rect.right < WIDTH :
            self.rect.right += self.speed

    def expand(self) :
        self.width = int(self.width * 1.5)

        if self.width > WIDTH :
            self.width = WIDTH

        self.rect.width = self.width

    def shrink(self) :
        self.width = PADDLE_WIDTH
        self.rect.width = self.width

class Ball :
    def __init__(self, x, y, speed=BALL_SPEED) :
        self.x = x
        self.y = y
        self.vx = speed * random.uniform(-1, 1)
        self.vy = -speed
        self.radius = BALL_RADIUS

    def move(self) :
        self.x += self.vx
        self.y += self.vy

    def rect(self) :
        return pygame.Rect(int(self.x-self.radius), int(self.y-self.radius), self.radius*2, self.radius*2)

    def bounce_x(self) :
        self.vx = -self.vx

    def bounce_y(self) :
        self.vy = -self.vy

    def draw(self, screen) :
        pygame.draw.circle(screen, (255, 180, 170), (int(self.x), int(self.y)), self.radius)

class Brick :
    def __init__(self, x, y, color) :
        pass

    def draw(self, screen) :
        pass

class PowerUp :
    def __init__(self, x, y, kind) :
        pass

    def draw(self, screen) :
        pass

    def update(self) :
        pass
