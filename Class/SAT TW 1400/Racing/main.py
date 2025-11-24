import pygame, random, sys

pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
WHITE, BLACK, RED, GREEN, BLUE, YELLOW = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")
clock = pygame.time.Clock()

class Car :
    def __init__(self, x, y, color, isplayer=False) :
        self.x = x
        self.y = y
        self.color = color
        self.width = 40
        self.height = 60
        self.isplayer = isplayer
        self.speed = 5 if not isplayer else 0

    def move(self) :
        if not self.isplayer :
            self.y += self.speed

    def draw(self, surface) :
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height), 2)

    def get_rect(self) :
        return pygame.Rect(self.x, self.y, self.width, self.height)
   
def check_collision(car1, car2) :
    return car1.get_rect().colliderect(car2.get_rect())

def main() :
    player = Car(WIDTH // 2 - 20, HEIGHT - 80, BLUE, True)
    enemies = []
    score = 0
    font = pygame.font.Font(None, 36)
    road_offset = 0

    running = True
    while running :
        # Handle events
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0 :
            player.x -= 7
        elif keys[pygame.K_RIGHT] and player.x < WIDTH - player.width :
            player.x += 7

        # Spawn enemies
        if random.randint(1, 20) == 1 :
            enemy_x = random.randint(0, WIDTH - 40)
            enemies.append(Car(enemy_x, -60, RED))

        # Handle enemy cars
        for enemy in enemies :
            enemy.move()

            if enemy.y > HEIGHT :
                enemies.remove(enemy)
                score += 1

        # Check collisions
        for enemy in enemies :
            if check_collision(player, enemy) :
                # Game over
                game_over_text =font.render('GAME OVER!', True, RED)
                final_score_text = font.render(f'Score: {score}', True, BLACK)

                screen.fill(WHITE)
                screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 50))
                screen.blit(final_score_text, (WIDTH // 2 - 100, HEIGHT // 2))
                pygame.display.flip()
                pygame.time.wait(3000)
                running = False

        # Draw everything
        screen.fill(WHITE)

        # Draw road
        road_offset += 3
        shake_x = random.randint(-2, 2)
        for i in range(0, HEIGHT, 40) :
            line_y = (i + road_offset) % (HEIGHT+40) - 40
            pygame.draw.rect(screen, YELLOW, (WIDTH // 2 - 2 + shake_x, line_y, 4, 20))

        # Draw cars
        player.draw(screen)
        for enemy in enemies :
            enemy.draw(screen)

        # Display score
        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__" :
    main()
