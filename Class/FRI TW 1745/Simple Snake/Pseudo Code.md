# Modules

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Snake properties

# Food properties

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop variable
game_over = False

# Main game loop
while True :
    # Handle event queue
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()

    # Handle key presses for snake direction

    # Move the snake

    # Insert new head at the front of the snake

    # Create Rect objects for the snake's head and the food

    # Check if the snake eats food using colliderect
    # Remove the tail segment if no food is eaten

    # Check for collisions (walls or itself)

    # Draw everything
    screen.fill(BLACK)

    # Draw food

    # Draw snake

    # Draw score

    # Check for game over

    # Update everything
    pygame.display.flip()
    clock.tick(snake_speed)
