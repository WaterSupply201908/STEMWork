import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Paddle and Ball positions
paddle1_pos = [10, HEIGHT // 2 - PADDLE_HEIGHT // 2]
paddle2_pos = [WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2]
ball_pos = [WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2]
ball_velocity = [5, 5]

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_pos[1] > 0:
        paddle1_pos[1] -= 5
    if keys[pygame.K_s] and paddle1_pos[1] < HEIGHT - PADDLE_HEIGHT:
        paddle1_pos[1] += 5
    if keys[pygame.K_UP] and paddle2_pos[1] > 0:
        paddle2_pos[1] -= 5
    if keys[pygame.K_DOWN] and paddle2_pos[1] < HEIGHT - PADDLE_HEIGHT:
        paddle2_pos[1] += 5

    # Move the ball
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Ball collision with top and bottom walls
    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT - BALL_SIZE:
        ball_velocity[1] = -ball_velocity[1]

    # Ball collision with paddles
    if (ball_pos[0] <= paddle1_pos[0] + PADDLE_WIDTH and 
        paddle1_pos[1] < ball_pos[1] < paddle1_pos[1] + PADDLE_HEIGHT):
        ball_velocity[0] = -ball_velocity[0]

    if (ball_pos[0] >= paddle2_pos[0] - BALL_SIZE and 
        paddle2_pos[1] < ball_pos[1] < paddle2_pos[1] + PADDLE_HEIGHT):
        ball_velocity[0] = -ball_velocity[0]

    # Reset the ball if it goes out of bounds
    if ball_pos[0] < 0 or ball_pos[0] > WIDTH:
        ball_pos = [WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2]
        ball_velocity = [5 * (-1 if ball_velocity[0] > 0 else 1), ball_velocity[1]]

    # Fill the background
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (*paddle1_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (*paddle2_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (*ball_pos, BALL_SIZE, BALL_SIZE))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)
