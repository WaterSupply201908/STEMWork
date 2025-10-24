import pygame, random, sys
from pygame.locals import *

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PVP Fighter")
clock = pygame.time.Clock()

# Colors
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
RED, BLUE = (255, 0, 0), (0, 0, 255)
GREEN, YELLOW = (0, 255, 0), (255, 255, 0)

# Fighter class
class Fighter:
    def __init__(self, x, y, color, controls):
        self.x, self.y = x, y
        self.width, self.height = 50, 100
        self.color = color
        self.health = 100
        self.speed = 5
        self.jump_power = 15
        self.vel_y = 0
        self.jumping = False
        self.attacking = False
        self.attack_cooldown = 0
        self.controls = controls  # [left, right, jump, attack]
        self.facing_right = (x < WIDTH // 2)
        self.score = 0

    def move(self, opponent) :
        keys = pygame.key.get_pressed()
        dx = 0

        if keys[self.controls[0]] :
            dx = -self.speed
        elif keys[self.controls[1]] :
            dx = self.speed

        if dx > 0 :
            self.facing_right = True
        elif dx < 0 :
            self.facing_right = False

        if keys[self.controls[2]] and not self.jumping :
            self.vel_y = -self.jump_power
            self.jumping = True

        self.vel_y += 1
        if self.vel_y > 10 :
            self.vel_y = 10

        self.y += self.vel_y

        if self.y + self.height >= HEIGHT - 50 :
            self.y = HEIGHT - 50 - self.height
            self.jumping = False
            self.vel_y = 0

        self.x += dx
        if self.x < 0 :
            self.x = 0
        
        if self.x + self.width > WIDTH :
            self.x = WIDTH - self.width

        if self.attack_cooldown > 0 :
            self.attack_cooldown -= 1

        if keys[self.controls[3]] and self.attack_cooldown == 0 :
            self.attacking = True
            self.attack_cooldown = 20

            attack_rect = pygame.Rect(
                self.x - 30 if not self.facing_right else self.x + self.width,
                self.y,
                30+self.width//2,
                self.height
            )

            if attack_rect.colliderect(pygame.Rect(opponent.x, opponent.y, opponent.width, opponent.height)) :
                opponent.health -= 10
                if opponent.health <= 0 :
                    self.score += 1
                    opponent.health = 100
        else :
            self.attacking = False

    def draw(self) :
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        eye_x = self.x + (30 if self.facing_right else 10)
        pygame.draw.rect(screen, WHITE, (eye_x, self.y + 20, 10, 10))

        if self.attacking :
            attack_x = self.x + self.width if self.facing_right else self.x - 30
            pygame.draw.rect(screen, YELLOW, (attack_x, self.y+20, 30, 20))

        pygame.draw.rect(screen, RED, (self.x, self.y - 20, self.width, 10))
        pygame.draw.rect(screen, GREEN, (self.x, self.y - 20, self.width * (self.health / 100), 10))

player1 = Fighter(100, HEIGHT-150, BLUE, [K_a, K_d, K_w, K_s])
player2 = Fighter(WIDTH-150, HEIGHT-150, RED, [K_LEFT, K_RIGHT, K_UP, K_DOWN])

while True :
    for event in pygame.event.get() :
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE :
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    pygame.draw.rect(screen, (50, 50, 50), (0, HEIGHT-50, WIDTH, 50))

    player1.move(player2)
    player2.move(player1)

    player1.draw()
    player2.draw()

    font = pygame.font.Font(None, 36)
    score_text = f'{player1.score} - {player2.score}'
    text = font.render(score_text, True, WHITE)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, 20))

    pygame.display.flip()
    clock.tick(60)
