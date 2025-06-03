from settings import *
from player import Player
from sprites import *
from random import randint
from pytmx.util_pygame import load_pygame
from groups import AllSprites

class Game :
    def __init__(self) :
        pygame.init()

        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Vampire Survivors')

        self.clock = pygame.time.Clock()
        self.running = True
        self.load_image()

        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()

        self.setup()

        self.can_shoot = True
        self.shoot_time = 0
        self.gun_cooldown = 100

    def setup(self) :
        map = load_pygame(join('Data', 'Maps', 'world.tmx'))
    
        for x, y, image in map.get_layer_by_name('Ground').tiles() :
            Sprite((x*TILE_SIZE, y*TILE_SIZE), image, self.all_sprites)

        for obj in map.get_layer_by_name('Objects') :
            CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        for obj in map.get_layer_by_name('Collisions') :
            CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), (self.collision_sprites))

        for obj in map.get_layer_by_name('Entities') :
            if obj.name == 'Player' :
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)
                self.gun = Gun(self.player, self.all_sprites)

    def load_image(self) :
        self.bullet_surf = pygame.image.load(join('Image', 'Gun', 'bullet.png')).convert_alpha()

    def input(self) :
        if pygame.mouse.get_pressed()[0] and self.can_shoot :
            pos = self.gun.rect.center + self.gun.player_direction * 50
            Bullet(self.bullet_surf, pos,
                   self.gun.player_direction, (self.all_sprites, self.bullet_sprites))
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def gun_timer(self) :
        if not self.can_shoot :
            if pygame.time.get_ticks() - self.shoot_time >= self.gun_cooldown :
                self.can_shoot = True

    def run(self) :
        while self.running :
            dt = self.clock.tick() / 1000

            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    self.running = False

            # Game logic
            self.gun_timer()
            self.input()
            self.all_sprites.update(dt)

            self.display_surface.fill('black')
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()

        pygame.quit()

# Main Program
game = Game()
game.run()
