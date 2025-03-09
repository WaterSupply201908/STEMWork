from settings import *

class CollisionSprite(pygame.sprite.Sprite) :
  def __init__(self, pos, size, groups) :
    super().__init__(groups)
