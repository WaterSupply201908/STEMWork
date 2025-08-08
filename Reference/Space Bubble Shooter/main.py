import pygame, random, math

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Bubble Shooter")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Colors
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), 
          (255, 0, 255), (0, 255, 255), (255, 165, 0), (128, 0, 128)]
FLAMES = [(255, 165, 0), (255, 215, 0), (255, 69, 0)]

# Player ship
class Ship:
    def __init__(self):
        self.x, self.y = WIDTH // 2, HEIGHT - 40
        self.speed = 5
        
    def draw(self):
        # Ship body
        pygame.draw.polygon(screen, WHITE, [(self.x, self.y), 
                           (self.x - 20, self.y + 30), (self.x + 20, self.y + 30)])
        # Thruster flames
        pygame.draw.polygon(screen, random.choice(FLAMES), [(self.x, self.y + 30),
                           (self.x - 10, self.y + 40), (self.x + 10, self.y + 40)])
        
    def move(self, direction):
        if direction == "left" and self.x > 20: self.x -= self.speed
        if direction == "right" and self.x < WIDTH - 20: self.x += self.speed

# Laser shots
class Laser:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.speed, self.active = 7, True
        
    def update(self):
        self.y -= self.speed
        if self.y < 0: 
            self.active = False
            
    def draw(self):
        pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x, self.y + 15), 3)

# Bubbles
class Bubble:
    def __init__(self):
        self.reset()
        
    def update(self):
        self.y += self.speed
        if self.y > HEIGHT + self.radius: self.reset()
            
    def reset(self):
        self.radius = random.randint(15, 30)
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(-100, -20)
        self.speed = random.uniform(1.0, 3.0)
        self.color = random.choice(COLORS)
        
    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        # Shine effect
        pygame.draw.circle(screen, WHITE, (int(self.x - self.radius//3), 
                          int(self.y - self.radius//3)), self.radius//5)

# Game initialization
ship = Ship()
lasers, bubbles, explosions = [], [Bubble() for _ in range(8)], []
score, game_over = 0, False

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                lasers.append(Laser(ship.x, ship.y))
            if event.key == pygame.K_r and game_over:
                ship, lasers = Ship(), []
                bubbles = [Bubble() for _ in range(8)]
                explosions, score, game_over = [], 0, False
    
    # Draw background
    screen.fill(BLACK)
    for _ in range(50): # Stars
        pygame.draw.circle(screen, WHITE, (random.randint(0, WIDTH), 
                          random.randint(0, HEIGHT)), 1)
    
    # Move ship
    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT]: ship.move("left")
        if keys[pygame.K_RIGHT]: ship.move("right")
        
        # Update game objects
        for laser in lasers[:]:
            laser.update()
            if not laser.active: lasers.remove(laser)
        
        for bubble in bubbles:
            bubble.update()
            # Bubble-ship collision
            if math.sqrt((bubble.x - ship.x)**2 + (bubble.y - ship.y)**2) < bubble.radius + 20:
                game_over = True
                break
        
        # Laser-bubble collisions
        for laser in lasers[:]:
            for bubble in bubbles:
                if math.sqrt((bubble.x - laser.x)**2 + (bubble.y - laser.y)**2) < bubble.radius and laser.active:
                    bubble.reset()
                    lasers.remove(laser)
                    score += 10
                    break
    
    # Draw everything
    for obj in bubbles + lasers: obj.draw()
    if not game_over: ship.draw()
    
    # Draw score and game over
    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
    if game_over:
        screen.blit(font.render("GAME OVER! Press R to Restart", True, WHITE), 
                   (WIDTH//2 - 180, HEIGHT//2))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
