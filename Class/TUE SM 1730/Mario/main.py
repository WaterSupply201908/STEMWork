from settings import *
import sys
from level import Level

WIDTH, HEIGHT = 600, 500

class Game :
    def __init__(self) :
        pygame.init()
        self.display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Super World')

    def run(self) :
        while True :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    pygame.quit()
                    sys.exit()
