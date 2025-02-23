from settings import *

class Player(pygame.sprite.Sprite) : # parent class
  # field : variable defined in a class
  # method : function defined in a class
  def __init__(self, pos, groups) :
    super().__init__(groups)
    self.image = pygame.image.load(join('Image', 'Player', 'Down', '0.png')).convert_alpha()
    self.rect = self.image.get_frect(center = pos)
