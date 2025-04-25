from settings import *

class Player(pygame.sprite.Sprite) :
    def __init__(self, pos, groups) :
        super().__init__(groups)
        self.image = pygame.image.load(join('Image', 'Player', 'Down', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center=pos)

        self.direction = pygame.Vector2(1, 0)
        self.speed = 500

    def input(self) :
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])

    def move(self, dt) :
        self.rect.center += self.direction * self.speed * dt
