# Import modules
import pygame
import sys

# Define variables (Constants)
WIDTH, HEIGHT = 800, 600
BAT_WIDTH, BAT_HEIGHT = 10, 100
BALL_SIZE = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define functions

# Main Program
# Initialize pygame
pygame.init()

# Setup pygame display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Define pygame-related variables & functions
bat1_pos = [10, HEIGHT//2 - BAT_HEIGHT//2]
bat2_pos = [WIDTH-20, HEIGHT//2 - BAT_HEIGHT//2]
ball_pos = [WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2]
ball_velocity = [5, 5]

# Game loop
while True :
    # Prepare game logic
    ## Check event
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
            
    ## Check bat movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and bat1_pos[1] > 0 :
        bat1_pos[1] -= 5
    if keys[pygame.K_s] and bat1_pos[1] < HEIGHT-BAT_HEIGHT :
        bat1_pos[1] += 5
    if keys[pygame.K_UP] and bat2_pos[1] > 0 :
        bat2_pos[1] -= 5
    if keys[pygame.K_DOWN] and bat2_pos[1] < HEIGHT-BAT_HEIGHT :
        bat2_pos[1] += 5

    ## Move the ball
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    ## Check ball collision with top & bottom walls
    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT - BALL_SIZE :
        ball_velocity[1] = -ball_velocity[1]

    ## Check ball collision with bats
    if (ball_pos[0] <= bat1_pos[0] + BAT_WIDTH and 
        bat1_pos[1] < ball_pos[1] < bat1_pos[1] + BAT_HEIGHT) :
        ball_velocity[0] = -ball_velocity[0]

    if (ball_pos[0] >= bat2_pos[0] - BALL_SIZE and 
        bat2_pos[1] < ball_pos[1] < bat2_pos[1] + BAT_HEIGHT) :
        ball_velocity[0] = -ball_velocity[0]
    
    ## If ball reaches left & right walls then reset
    if ball_pos[0] < 0 or ball_pos[0] > WIDTH :
        ball_pos = [WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2]
        ball_velocity = [5 * (-1 if ball_velocity[0] > 0 else 1), ball_velocity[1]]

    ## Fill the background
    screen.fill(BLACK)

    ## Draw bats & ball
    pygame.draw.rect(screen, WHITE, (*bat1_pos, BAT_WIDTH, BAT_HEIGHT))
    pygame.draw.rect(screen, WHITE, (*bat2_pos, BAT_WIDTH, BAT_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (*ball_pos, BALL_SIZE, BALL_SIZE))

    # Update pygame display
    pygame.display.flip()

    # Set frame rate
    pygame.time.Clock().tick(60)
