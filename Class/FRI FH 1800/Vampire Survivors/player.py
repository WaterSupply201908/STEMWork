from settings import *

class Player(pygame.sprite.Sprite) :
    def __init__(self, pos, groups, collision_sprites) :
        super().__init__(groups)
        self.load_images()
        self.state, self.frame_index = 'down', 0
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
                if filenames :
                    for filename in sorted(filenames, key=lambda name : int(name.split('.')[0])) :
                        full_path = join(folder_path, filename)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)

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

    def animate(self, dt) :
        # get state
        if self.direction.x != 0 :
            if self.direction.x > 0 :
                self.state = 'right'
            else :
                self.state = 'left'
        if self.direction.y != 0 :
            if self.direction.y > 0 :
                self.state = 'down'
            else :
                self.state = 'up'

        # animate
        if self.direction :
            self.frame_index += 5*dt
        else :
            self.frame_index = 0

        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]

    def update(self, dt) :
        self.input()
        self.move(dt)
        self.animate(dt)
