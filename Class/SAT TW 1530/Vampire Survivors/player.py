from settings import *

class Player(pygame.sprite.Sprite) :
    def __init__(self, pos, groups, collision_sprites) :
        super().__init__(groups)

        self.image = pygame.image.load(join('images', 'player', 'down', '0.png')).convert_alpha()
        self.rect = self.image.get_rect(center = pos)

        self.direction = pygame.math.Vector2(1, 0)
        self.speed = 500
        self.collision_sprites = collision_sprites

    def input(self) :
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def collision(self, direction) :
        pass

    def move(self, dt) :
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')

    def update(self, dt) :
        self.input()
        self.move(dt)
