import pygame
import sys
import random

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

enemy_pos = [WIDTH, random.randint(50, HEIGHT - 50)]
food_pos = [random.randint(WIDTH, WIDTH + 100), random.randint(50, HEIGHT - 100)]

speed = 15
score = 0

def draw_text(text, font, color, x, y) :
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

def game_over_screen() :
    while True :
        screen.fill(BG_COLOR)
        mouse_pos = pygame.mouse.get_pos()

        exit_rect = pygame.Rect(100, HEIGHT-100, 40, 20)
        restart_rect = pygame.Rect(WIDTH-180, HEIGHT-100, 80, 20)

        if exit_rect.collidepoint(mouse_pos) :
            pygame.draw.rect(screen, LIGHT_GREY, exit_rect)
        else :
            pygame.draw.rect(screen, DARK_GREY, exit_rect)

        if restart_rect.collidepoint(mouse_pos) :
            pygame.draw.rect(screen, LIGHT_GREY, restart_rect)
        else :
            pygame.draw.rect(screen, DARK_GREY, restart_rect)

        draw_text('GAME OVER', font_medium, WHITE, WIDTH//2-150, HEIGHT//2-50)
        draw_text('Exit', font_tiny, WHITE, exit_rect.x+5, exit_rect.y)
        draw_text('Restart', font_tiny, WHITE, restart_rect.x+10, restart_rect.y)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if exit_rect.collidepoint(event.pos) :
                    pygame.quit()
                    sys.exit()
                elif restart_rect.collidepoint(event.pos) :
                    main_game()

        pygame.display.update()
        clock.tick(60)

def main_game() :
    global speed, score
    lead_x_local = lead_x
    lead_y_local = lead_y
    enemy = enemy_pos[:]
    food = food_pos[:]
    speed_local = speed
    score_local = score

    running = True
    while running :
        screen.fill(BG_COLOR)
        clock.tick(speed_local)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] :
            lead_y_local -= 10
        if keys[pygame.K_DOWN] :
            lead_y_local += 10

        pygame.draw.rect(screen, (c1, c2, c3), (0, 0, WIDTH, 40))
        pygame.draw.rect(screen, (c3, c2, c1), (0, HEIGHT-40, WIDTH, 40))

        player_rect = pygame.Rect(lead_x_local, lead_y_local, player_size, player_size)
        pygame.draw.rect(screen, player_color, player_rect)

        if enemy[0] > 0 :
            enemy[0] -= 10
        else :
            enemy[0] = WIDTH
            enemy[1] = random.randint(obstacle_size, HEIGHT-obstacle_size)

        if food[0] > 0 :
            food[0] -= 10
        else :
            food[0] = WIDTH + 100
            food[1] = random.randint(obstacle_size, HEIGHT-obstacle_size)

        enemy_rect = pygame.Rect(enemy[0], enemy[1], obstacle_size, obstacle_size)
        food_rect = pygame.Rect(food[0], food[1], obstacle_size, obstacle_size)
        pygame.draw.rect(screen, RED, enemy_rect)
        pygame.draw.rect(screen, BLUE, food_rect)

        if player_rect.colliderect(enemy_rect) :
            game_over_screen()

        if player_rect.colliderect(food_rect) :
            food[0] = WIDTH + 100
            food[1] = random.randint(obstacle_size, HEIGHT-obstacle_size)
            score_local += 1
            speed_local = min(speed_local+1, 60)

        if lead_y_local <= 38 or lead_y_local >= HEIGHT-38 or food[0] <= 0 :
            game_over_screen()

        draw_text(f'Score: {score_local}', font_small, WHITE, WIDTH-120, HEIGHT-40)

        pygame.display.update()

def intro_screen() :
    colox_c1 = 0
    colox_c2 = 0

    button_x = 300
    button_y = 290
    button_width = 100
    button_height = 40

    running = True
    while running :
        screen.fill(BG_COLOR)
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN :
                start_rect = pygame.Rect(button_x, button_y, button_width, button_height)
                exit_rect = pygame.Rect(button_x, button_y + 70, button_width, button_height)
                if start_rect.collidepoint(event.pos) :
                    main_game()
                elif exit_rect.collidepoint(event.pos) :
                    pygame.quit()
                    sys.exit()

        colox_c1 = (colox_c1 + 1) % 255
        colox_c2 = (colox_c2 + 1) % 255
        side_color = (c2, colox_c1, colox_c2)
        pygame.draw.rect(screen, side_color, (0, 0, 40, HEIGHT))
        pygame.draw.rect(screen, side_color, (WIDTH - 40, 0, 40, HEIGHT))

        start_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        exit_rect = pygame.Rect(button_x, button_y + 70, button_width, button_height)

        for rect in [start_rect, exit_rect] :
            if rect.collidepoint(mouse_pos) :
                pygame.draw.rect(screen, LIGHT_GREY, rect)
            else:
                pygame.draw.rect(screen, DARK_GREY, rect)

        draw_text('Start', font_small, WHITE, button_x + 10, button_y + 5)
        draw_text('Exit', font_small, WHITE, button_x + 10, button_y + 75)

        colox_color = (c1, colox_c1, colox_c2)
        draw_text('Colox', font_small, colox_color, WIDTH // 2 - 30, 50)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__" :
    intro_screen()
