import pygame
import sys
import random
from pygame import Vector2

class Main :
    def __init__(self) :
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self) :
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self) :
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self) :
        if self.fruit.pos == self.snake.body[0] :
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:] :
            if block == self.fruit.pos :
                self.fruit.randomize()

    def game_over(self) :
        self.snake.reset()
        pygame.quit()
        sys.exit()

    def check_fail(self) :
        if not 0 <= self.snake.body[0].x < CELL_NUMBER or not 0 <= self.snake.body[0].y < CELL_NUMBER :
            self.game_over()

        for block in self.snake.body[1:] :
            if block == self.snake.body[0] :
                self.game_over()

    def draw_grass(self) :
        grass_color = (167, 209, 61)

        for row in range(CELL_NUMBER) :
            if row % 2 == 0 :
                for col in range(CELL_NUMBER) :
                    if col % 2 == 0 :
                        grass_rect = pygame.Rect(col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else :
                for col in range(CELL_NUMBER) :
                    if col % 2 != 0 :
                        grass_rect = pygame.Rect(col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self) :
        score_text = str(len(self.snake.body) - 3)
        score_surf = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(CELL_SIZE * CELL_NUMBER - 60)
        score_y = int(CELL_SIZE * CELL_NUMBER - 60)
        score_rect = score_surf.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,
                                apple_rect.width+score_rect.width,
                                apple_rect.height)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surf, score_rect)
        screen.blit(apple, apple_rect)

class Snake :
    def __init__(self) :
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(-1, 0)
        self.new_block = False

        self.head_up = pygame.image.load('./head_up.png').convert_alpha()
        self.head_down = pygame.image.load('./head_down.png').convert_alpha()
        self.head_right = pygame.image.load('./head_right.png').convert_alpha()
        self.head_left = pygame.image.load('./head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('./tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('./tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('./tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('./tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('./body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('./body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('./body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('./body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('./body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('./body_bl.png').convert_alpha()

        self.crunch_sound = pygame.mixer.Sound('./crunch.wav')

    def update_head_graphics(self) :
        head_relation = self.body[1] - self.body[0]

        if head_relation == Vector2(1, 0) :
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0) :
            self.head = self.head_right
        elif head_relation == Vector2(0, 1) :
            self.head = self.head_up
        elif head_relation == Vector2(0, -1) :
            self.head = self.head_down

    def update_tail_graphics(self) :
        tail_relation = self.body[-2] - self.body[-1]

        if tail_relation == Vector2(1, 0) :
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0) :
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1) :
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1) :
            self.tail = self.tail_down

    def draw_snake(self) :
#        for block in self.body :
#            block_rect = pygame.Rect(block.x*CELL_SIZE, block.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
#            pygame.draw.rect(screen, (183, 191, 122), block_rect)
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body) :
            block_rect = pygame.Rect(
                block.x * CELL_SIZE, 
                block.y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
                )

            if index == 0 :
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1 :
                screen.blit(self.tail, block_rect)
            else :
                previous_block = self.body[index+1] - block
                next_block = self.body[index-1] - block

                if previous_block.x == next_block.x :
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y :
                    screen.blit(self.body_horizontal, block_rect)
                else :
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1 :
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1 :
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1 :
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1 :
                        screen.blit(self.body_br, block_rect)

    def move_snake(self) :
        if self.new_block :
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0]+self.direction)
            self.body = body_copy
            self.new_block = False
        else :
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0]+self.direction)
            self.body = body_copy

    def add_block(self) :
        self.new_block = True

    def play_crunch_sound(self) :
        self.crunch_sound.play()

    def reset(self) :
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(-1, 0)

class Fruit :
    def __init__(self) :
        # create x and y pos
        self.randomize()

    def draw_fruit(self) :
        # draw a square
        fruit_rect = pygame.Rect(self.pos.x*CELL_SIZE, self.pos.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        #pygame.draw.rect(screen, (126, 166, 114), fruit_rect)
        screen.blit(apple, fruit_rect)

    def randomize(self) :
        self.x = random.randint(0, CELL_NUMBER-1)
        self.y = random.randint(0, CELL_NUMBER-1)
        self.pos = Vector2(self.x, self.y)

# Main program
pygame.init()
CELL_SIZE = 40
CELL_NUMBER = 20
screen = pygame.display.set_mode((CELL_NUMBER*CELL_SIZE, CELL_NUMBER*CELL_SIZE))
clock = pygame.time.Clock()
apple = pygame.image.load('./apple.png').convert_alpha()
game_font = pygame.font.Font('PoetsenOne-Regular.ttf', 20)

#fruit = Fruit()
#snake = Snake()
main = Main()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True :
    for e in pygame.event.get() :
        if e.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        if e.type == SCREEN_UPDATE :
            #snake.move_snake()
            main.update()
        if e.type == pygame.KEYDOWN :
            if e.key == pygame.K_UP :
                if main.snake.direction.y != 1 :
                    main.snake.direction = Vector2(0, -1)
            if e.key == pygame.K_DOWN :
                if main.snake.direction.y != -1 :
                    main.snake.direction = Vector2(0, 1)
            if e.key == pygame.K_LEFT :
                if main.snake.direction.x != 1 :
                    main.snake.direction = Vector2(-1, 0)
            if e.key == pygame.K_RIGHT :
                if main.snake.direction.x != -1 :
                    main.snake.direction = Vector2(1, 0)

    # Game Logic
    screen.fill((175, 215, 70))
#    fruit.draw_fruit()
#    snake.draw_snake()
    main.draw_elements()

    pygame.display.update()
    clock.tick(60)
