from settings import *

class Player(pygame.sprite.Sprite) :
  def __init__(self, pos, groups) :
    super().__init__(groups)
