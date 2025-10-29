import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racing Game")
clock = pygame.time.Clock()

class Car:
    def __init__(self, x, y, color, is_player=False):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 60
        self.color = color
        self.speed = 5 if not is_player else 0
        self.is_player = is_player
    
    def move(self):
        if not self.is_player:
            self.y += self.speed
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height), 2)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

def check_collision(car1, car2):
    return car1.get_rect().colliderect(car2.get_rect())

def main():
    player = Car(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT - 80, BLUE, True)
    enemy_cars = []
    score = 0
    font = pygame.font.Font(None, 36)
    road_offset = 0
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= 7
        if keys[pygame.K_RIGHT] and player.x < SCREEN_WIDTH - player.width:
            player.x += 7
        
        # Spawn enemy cars
        if random.randint(1, 20) == 1:
            enemy_x = random.randint(0, SCREEN_WIDTH - 40)
            enemy_cars.append(Car(enemy_x, -60, RED))
        
        # Move and remove enemy cars
        for enemy in enemy_cars[:]:
            enemy.move()
            if enemy.y > SCREEN_HEIGHT:
                enemy_cars.remove(enemy)
                score += 1
        
        # Check collisions
        for enemy in enemy_cars:
            if check_collision(player, enemy):
                # Game over
                game_over_text = font.render("GAME OVER!", True, RED)
                final_score_text = font.render(f"Final Score: {score}", True, BLACK)
                screen.fill(WHITE)
                screen.blit(game_over_text, (SCREEN_WIDTH//2 - 80, SCREEN_HEIGHT//2 - 50))
                screen.blit(final_score_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2))
                pygame.display.flip()
                pygame.time.wait(3000)
                running = False
        
        # Draw everything
        screen.fill(WHITE)
        
        # Draw road lines with shake effect
        road_offset += 3
        shake_x = random.randint(-2, 2)
        for i in range(0, SCREEN_HEIGHT, 40):
            line_y = (i + road_offset) % (SCREEN_HEIGHT + 40) - 40
            pygame.draw.rect(screen, YELLOW, (SCREEN_WIDTH//2 - 2 + shake_x, line_y, 4, 20))
        
        # Draw cars
        player.draw(screen)
        for enemy in enemy_cars:
            enemy.draw(screen)
        
        # Draw score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
