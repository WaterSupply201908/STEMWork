from settings import *

class Player(pygame.sprite.Sprite) : # parent class
  # field : variable defined in a class
  # method : function defined in a class
  def __init__(self, pos, groups) :
    super().__init__(groups)
    self.image = pygame.image.load(join('VampireSurvivors', 'Image', 'Player', 'Down', '0.png')).convert_alpha()
    self.rect = self.image.get_frect(center = pos)

    self.direction = pygame.Vector2(1, 0)
    self.speed = 500

  def input(self) :
    keys = pygame.key.get_pressed()
    self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    self.direction = self.direction.normalize() if self.direction else self.direction

  def move(self, dt) :
    self.rect.center += self.direction * self.speed * dt
