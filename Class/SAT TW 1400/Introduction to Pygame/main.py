from random import randint, choice
from sys import exit

import pygame


class Player(pygame.sprite.Sprite) :

    def __init__(self) :
        super().__init__()

        player_walk_1 = pygame.image.load('player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('jump.png').convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))

        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('jump.mp3')
        self.jump_sound.set_volume(0.1)

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity

        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1

            if self.player_index >= len(self.player_walk):
                self.player_index = 0

            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            self.frames = [fly_frame_1, fly_frame_2]

            y_pos = 210
        else:
            self.frames = [snail_frame_1, snail_frame_2]

            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

def display_score() :
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f"Score: {current_time}", False, 'Black')
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)

    return current_time

def obstacle_movement(obstacle_list) :
    if obstacle_list :
        for obstacle_rect in obstacle_list :
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300 :
                screen.blit(snail_surface, obstacle_rect)
            else :
                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else :
        return []

def collision(player, obstacles) :
    if obstacles :
        for obstacle_rect in obstacles :
            if player.colliderect(obstacle_rect) :
                return False

    return True

def collision_sprite() :
    if pygame.sprite.spritecollide(player.sprite, Obstacle_group, True) :
        Obstacle_group.empty()

        return False
    else :
        return True

def player_animation():
    pass


# Main Program
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 50)

sky_surface = pygame.image.load('Sky.png').convert()
ground_surface = pygame.image.load('ground.png').convert()

snail_frame_1 = pygame.image.load('snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('snail2.png').convert_alpha()
snail_frame = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frame[snail_frame_index]

fly_frame_1 = pygame.image.load('Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('Fly2.png').convert_alpha()
fly_frame = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frame[fly_frame_index]

player_walk_1 = pygame.image.load('player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('jump.png').convert_alpha()

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

game_active = False
start_time = 0
score = 0

bg_music = pygame.mixer.Sound('music.wav')
bg_music.set_volume(0.1)
bg_music.play(loops=-1)

player_stand = pygame.image.load('player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 320))

player = pygame.sprite.GroupSingle()
player.add(Player())

Obstacle_group = pygame.sprite.Group()

obstacle_time = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_time, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
            elif e.type == obstacle_time:
                Obstacle_group.add(
                    Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
            elif e.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surface = snail_frame[snail_frame_index]
            elif e.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surface = fly_frame[fly_frame_index]  # ***
        else:
            if e.type == pygame.KEYDOWN and e.type == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(text_surface, (300, 50))
        score = display_score()
        #pygame.draw.rect(screen, '#C0E8EC', score_rect)
        #pygame.draw.rect(screen, '#C0E8EC', score_rect,10)
        #screen.blit(score_surface,score_rect)

    else:
        screen.fill(94, 129, 162)
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f'Your score: {score}', False,
                                         (111, 96, 169))
        screen.blit(game_name, game_name_rect)
#        screen.blit(game_message, game_message_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print('jump')
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 300:
        player_rect.bottom = 300
#    if snail_rect.collidedict(player_rect) :
#        game_active = False
#    else :
#        screen.fill('Yellow')
#       screen.bilt(player_stand, player_stand_rect)
#        pygame.quit
#        exit()
#    screen.blit(player_surface, player_rect)

#    if player_rect.collidedict({tuple(snail_rect), 0}) :
#     print("Yes")

    pygame.display.update()
    clock.tick(60)
