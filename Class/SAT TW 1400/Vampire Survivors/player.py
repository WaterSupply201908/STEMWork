from settings import *

class Player(pygame.sprite.Sprite) : # parent class
  # field : variable defined in a class
  # method : function defined in a class
  def __init__(self, pos, groups, collision_sprites) :
    super().__init__(groups)
    self.image = pygame.image.load(join('VampireSurvivors', 'image', 'player', 'down', '0.png')).convert_alpha()
    self.rect = self.image.get_frect(center = pos)
    self.hitbox_rect = self.rect.inflate(-40, 0)

    self.direction = pygame.Vector2(1, 0)
    self.speed = 500
    self.collision_sprites = collision_sprites

  def input(self) :
    keys = pygame.key.get_pressed()
    self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    self.direction = self.direction.normalize() if self.direction else self.direction

  def collision(self, direction) :
    for sprite in self.collision_sprites :
      if sprite.rect.colliderect(self.hitbox_rect) :
        if direction == 'horizontal' :
          if self.direction.x > 0 :
            self.hitbox_rect.right = sprite.rect.left
          if self.direction.x < 0 :
            self.hitbox_rect.left = sprite.rect.right
        else :
          if self.direction.y > 0 :
            self.hitbox_rect.bottom = sprite.rect.top
          if self.direction.y < 0 :
            self.hitbox_rect.top = sprite.rect.bottom
    
  def move(self, dt) :
    self.hitbox_rect.x += self.direction.x * self.speed * dt
    self.collision('horizontal')
    self.hitbox_rect.y += self.direction.y * self.speed * dt
    self.collision('vertical')
    self.rect.center = self.hitbox_rect.center

  def update(self, dt) :
    self.input()
    self.move(dt)
