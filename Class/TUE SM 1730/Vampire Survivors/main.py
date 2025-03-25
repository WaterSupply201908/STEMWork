from settings import *
from player import Player
from sprites import *
from random import randint

class Game :
    def __init__(self) :
        pygame.init()

        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Vampire Survivors')

        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.player = Player((400, 300), self.all_sprites, self.collision_sprites)

        for i in range(6) :
            x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
            w, h = randint(60, 100), randint(50, 120)
            CollisionSprite((x, y), (w, h), (self.all_sprites, self.collision_sprites))

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
