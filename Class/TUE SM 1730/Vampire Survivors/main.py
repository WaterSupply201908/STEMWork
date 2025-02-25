from settings import *
from player import Player

class Game :
    def __init__(self) :
        pygame.init()

        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Vampire Survivors')

        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = pygame.sprite.Group()
        self.player = Player((400, 300), self.all_sprites)

    def run(self) :
        while self.running :
            dt = self.clock.tick() / 1000

            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    self.running = False

            # Game logic
            self.all_sprites.update(dt)

            self.display_surface.fill('black')
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()

# Main Program
game = Game()
game.run()
