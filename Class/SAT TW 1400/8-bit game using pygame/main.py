import pygame, random, sys

pygame.init()
WIDTH, HEIGHT = 720, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
DARK_GREY = (100, 100, 100)
LIGHT_GREY = (169, 169, 169)
BG_COLOR = (65, 25, 64)

COLOR_CHOICES = [RED, GREEN, BLUE]
player_color = random.choice(COLOR_CHOICES)

c1 = random.randint(125, 255)
c2 = random.randint(0, 255)
c3 = random.randint(0, 255)

# Fonts
font_small = pygame.font.SysFont('Corbel', 35)
font_medium = pygame.font.SysFont('Corbel', 60)
font_tiny = pygame.font.SysFont('Corbel', 25)

lead_x = 40
lead_y = HEIGHT // 2
player_size = 40
obstacle_size = 50

enemy_pos = [WIDTH, random.randint(50, HEIGHT - obstacle_size - 50)]
food_pos = [random.randint(WIDTH, WIDTH+100), random.randint(50, HEIGHT - obstacle_size - 50)]

score = 0
speed = 15

def draw_text(text, font, color, x, y) :
  surface = font.render(text, True, color)
  screen.blit(surface, (x, y))

def intro_screen() :
  running = True

  while running :
    screen.fill(BG_COLOR)

    for event in pygame.event.get() :
      if event.type == pygame.QUIT :
        pygame.quit()
        sys.exit()

# Main
if __name__ == "__main__" :
  intro_screen()
