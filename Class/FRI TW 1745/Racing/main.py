import pygame, random, sys

pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
RED, BLUE, GREEN, YELLOW = (255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")
clock = pygame.time.Clock()

# class
class Car:
    def __init__(self, x, y, color, isPlayer=False) :
        self.x = x
        self.y = y
        self.color = color
        self.isPlayer = isPlayer
        self.width = 40
        self.height = 60
        self.speed = 5 if not isPlayer else 0

    def move(self) :
        if not self.isPlayer :
            self.y += self.speed

    def draw(self, surface) :
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height), 2)

    def getRect(self) :
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
def main() :
    playerCar = Car(WIDTH//2-20, HEIGHT-80, BLUE, True)
    enemyCars = []
    score = 0
    font = pygame.font.Font(None, 36)
    roadOffset = 0

    running = True
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and playerCar.x > 0 :
            playerCar.x -= 5
        elif keys[pygame.K_RIGHT] and playerCar.x < WIDTH - playerCar.width :
            playerCar.x += 5

        if random.randint(1, 20) == 1 :
            enemyX = random.randint(0, WIDTH-40)
            enemyCars.append(Car(enemyX, -60, RED))

        for enemy in enemyCars :
            enemy.move()
            if enemy.y > HEIGHT :
                enemyCars.remove(enemy)
                score += 1

        for enemy in enemyCars :
            if playerCar.getRect().colliderect(enemy.getRect()) :
                gameOverText = font.render("Game Over!", True, RED)
                finalScoreText = font.render(f"Final Score: {score}", True, BLACK)

                screen.fill(WHITE)
                screen.blit(gameOverText, (WIDTH//2-80, HEIGHT//2-50))
                screen.blit(finalScoreText, (WIDTH//2-100, HEIGHT//2))

                pygame.display.flip()
                pygame.time.delay(3000)
                running = False

        screen.fill(WHITE)

        roadOffset += 3
        shakeX = random.randint(-2, 2)
        for i in range(0, HEIGHT, 40) :
            lineY = (i + roadOffset) % (HEIGHT + 40) - 40
            pygame.draw.rect(screen, YELLOW, (WIDTH//2 - 2 + shakeX, lineY, 4, 20))

        playerCar.draw(screen)
        for enemy in enemyCars :
            enemy.draw(screen)

        scoreText = font.render(f"Score: {score}", True, BLACK)
        screen.blit(scoreText, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__" :
    main()
