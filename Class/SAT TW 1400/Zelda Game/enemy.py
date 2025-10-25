import pygame
from settings import *
from entity import Entity
from support import import_folder

class Enemy(Entity) :
    def __init__(self, monster_name, pos, groups) :
        super().__init__(groups)
        self.sprite_type = 'enemy'

        self.image_graphics(monster_name)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

    def image_graphics(self, name) :
        self.animations = {'idle' : [], 'move' : [], 'attack' : []}
        main_path = f'../graphics/monsters/{name}/'

        for animation in self.animations.keys() :
            self.animations[animation] = import_folder(main_path + animation)
