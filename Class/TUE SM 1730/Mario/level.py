from settings import *

class Level :
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def run(self) :
        self.display_surface.fill('gray')
