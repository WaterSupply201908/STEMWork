from settings import *

class Player(pygame.sprite.Sprite) :
    def __init__(self, pos, groups, collision_sprites) :
        super().__init__(groups)

        self.image = pygame.Surface((48, 56))
        self.image.fill('Red')
        self.rect = self.image.get_frect(topleft=pos)

        self.direction = vector()
        self.speed = 200

        self.collision_sprites = collision_sprites

    def input(self) :
        keys = pygame.key.get_pressed()
        input_vector = vector(0, 0)

        if keys[pygame.K_RIGHT] :
            input_vector.x += 1
        elif keys[pygame.K_LEFT] :
            input_vector.x -= 1

        if input_vector :
            self.direction.x = input_vector.normalize().x
        else :
            self.direction.x = input_vector.x

    def collision(self, axis) :
        for sprite in self.collision_sprites :
            if sprite.rect.colliderect(self.rect) :
                if axis == 'horizontal' :
                    if self.rect.left <= sprite.rect.right :
                        self.rect.left = sprite.rect.right

                    if self.rect.right >= sprite.rect.left :
                        self.rect.right = sprite.rect.left

    def move(self, dt) :
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')

    def update(self, dt) :
        self.input()
        self.move(dt)
