from settings import *

class Game :
    def __init__(self) :
        pygame.init()

        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Vampire Survivors')

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self) :
        while self.running :
            pass

        pygame.quit()
