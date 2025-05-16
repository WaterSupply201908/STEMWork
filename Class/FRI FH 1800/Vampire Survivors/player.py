from settings import *

class Player(pygame.sprite.Sprite) :
    def __init__(self, pos, groups, collision_sprites) :
        super().__init__(groups)
        self.image = pygame.image.load(join('Image', 'Player', 'Down', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center=pos)
        self.hitbox_rect = self.rect.inflate(-60, -60)

        self.direction = pygame.Vector2(1, 0)
        self.speed = 500
        self.collision_sprites = collision_sprites

    def load_images(self) :
        self.frames = {'left':[], 'right':[], 'up':[], 'down':[]}

        for state in self.frames.keys() :
            for folder_path, sub_folders, filenames in walk(join('Image', 'Player', state)) :
                if file_names :
                    pass

    def input(self) :
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt) :
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')
        self.rect.center = self.hitbox_rect.center

    def collision(self, direction) :
        for sprite in self.collision_sprites :
            if sprite.rect.colliderect(self.hitbox_rect) :
                if direction == 'horizontal' :
                    if self.direction.x > 0 : self.rect.right = sprite.rect.left
                    if self.direction.x < 0 : self.rect.left = sprite.rect.right
                else :
                    if self.direction.y > 0 : self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0 : self.rect.top = sprite.rect.bottom

    def update(self, dt) :
        self.input()
        self.move(dt)
