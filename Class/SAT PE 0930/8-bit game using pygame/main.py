import pygame, random, sys

pygame.init()
WIDTH, HEIGHT = 720, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
DARK_GREY = (100, 100, 100)
LIGHT_GREY = (169, 169, 169)
BG_COLOR = (65, 25, 64)
color_choices = [RED, GREEN, BLUE]

c1 = random.randint(125, 255)
c2 = random.randint(0, 255)
c3 = random.randint(0, 255)

player_color = random.choice(color_choices)

font_small = pygame.font.SysFont('Corbel', 35)
font_medium = pygame.font.SysFont('Corbel', 60)
font_tiny = pygame.font.SysFont('Corbel', 25)

lead_x = 40
lead_y = HEIGHT // 2
player_size = 40
obstacle_size = 50

enemy_pos = [WIDTH, random.randint(50, HEIGHT - obstacle_size)]
food_pos = [random.randint(WIDTH, WIDTH + 100), random.randint(50, HEIGHT - obstacle_size * 2)]

speed = 15
score = 0

def draw_text(text, font, color, x, y) :
  pass

def intro_screen() :
  colox_c1, colox_c2 = 0, 0
  button_x, button_y = 300, 290
  button_width, button_height = 100, 40
  running = True

  while running :
    screen.fill(BG_COLOR)

    for event in pygame.event.get() :
      if event.type == pygame.QUIT :
        pygame.quit()
        sys.exit()

    colox_c1 = (colox_c1 + 1) % 256
    colox_c2 = (colox_c2 + 1) % 256
    side_color = (c2, colox_c1, colox_c2)
    pygame.draw.rect(screen, side_color, (0, 0, 40, HEIGHT))
    pygame.draw.rect(screen, side_color, (WIDTH-40, 0, 40, HEIGHT))

    start_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    exit_rect = pygame.Rect(button_x, button_y+70, button_width, button_height)

    mouse_pos = pygame.mouse.get_pos()

    for rect in [start_rect, exit_rect] :
      if rect.collidepoint(mouse_pos) :
        pygame.draw.rect(screen, LIGHT_GREY, rect)
      else :
        pygame.draw.rect(screen, DARK_GREY, rect)

    draw_text('Start', font_small, WHITE, button_x+10, button_y+5)
    draw_text('Exit', font_small, WHITE, button_x+10, button_y+75)

    colox_color = (c1, colox_c1, colox_c2)
    draw_text('Colox', font_small, colox_color, WIDTH//2-30, 50)

    pygame.display.update()
    clock.tick(60)
  
# Main program
if __name__ == "__main__" :
  intro_screen()
