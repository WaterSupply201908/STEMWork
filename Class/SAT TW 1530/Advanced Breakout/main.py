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
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        self.color = color
        self.alive = True

    def draw(self, screen) :
        if self.alive :
            pygame.draw.rect(screen, self.color, self.rect, border_radius=6)
            pygame.draw.rect(screen, (30, 30, 30), self.rect, 2, border_radius=6)

class PowerUp :
    def __init__(self, x, y, kind) :
        self.x = x
        self.y = y
        self.kind = kind
        self.rect = pygame.Rect(self.x, self.y, POWERUP_SIZE, POWERUP_SIZE)
        self.fall_speed = 4

    def draw(self, screen) :
        icons = {'expand':(180, 255, 150), 'slow':(150, 180, 255), 'multi':(255, 255, 90)}

        pygame.draw.rect(screen, icons[self.kind], self.rect, border_radius=8)
        pygame.draw.rect(screen, (70, 70, 40), self.rect, 2, border_radius=8)

    def update(self) :
        self.y += self.fall_speed
        self.rect.y = self.y

def create_bricks() :
    colors = [(255, 90, 90), (255, 190, 90), (220, 215, 75), (90, 210, 90), (90, 180, 255), (150, 130, 230)]
    bricks = []

    for row in range(BRICK_ROWS) :
        for col in range(BRICK_COLS) :
            x = col * (BRICK_WIDTH + BRICK_GAP) + BRICK_GAP // 2
            y = row * (BRICK_HEIGHT + BRICK_GAP) + 50
            brick = Brick(x, y, colors[row % len(colors)])
            bricks.append(brick)

    return bricks

def draw_text(surf, txt, pos, size=32, color=(255, 255, 255)) :
    font = pygame.font.SysFont('arial', size)
    label = font.render(txt, True, color)
    surf.blit(label, pos)

def main() :
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Breakout Game')
    clock = pygame.time.Clock()

    paddle = Paddle()
    balls = [Ball(paddle.rect.centerx, paddle.rect.top - BALL_RADIUS)]
    bricks = create_bricks()
    powerups = []
    score, lives = 0, 3
    slow_ball_timer = 0
    running, game_over, game_clear = True, False, False

    while running :
        left = right = False

        for e in pygame.event.get() :
            if e.type == pygame.QUIT :
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] :
            left = True
        elif keys[pygame.K_RIGHT] :
            right = True
        elif keys[pygame.K_ESCAPE] :
            running = False

        if game_over or game_clear :
            if keys[pygame.K_SPACE] :
                paddle = Paddle()
                balls = [Ball(paddle.rect.centerx, paddle.rect.top - BALL_RADIUS)]
                bricks = create_bricks()
                powerups = []
                score, lives = 0, 3
                slow_ball_timer = 0
                game_over, game_clear = False, False

        if not game_over and not game_clear :
            paddle.update(left, right)

            if slow_ball_timer and pygame.time.get_ticks() > slow_ball_timer :
                for ball in balls :
                    speed = BALL_SPEED * (1 if ball.vy < 0 else -1)
                    angle = ball.vx / abs(ball.vx) if ball.vx != 0 else 1

                    ball.vy -abs(speed) if ball.vy < 0 else abs(speed)
                    ball.vx = angle * abs(speed)

                slow_ball_timer = 0

if __name__ == '__main__' :
    main()
