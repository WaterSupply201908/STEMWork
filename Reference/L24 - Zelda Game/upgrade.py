import pygame
from settings import *

class Upgrade:
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.attribute_num = len(player.stats)
        self.attribute_name = list(player.stats.keys())
        self.max_values = list(player.max_stats.values())
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

        #item size
        self.height = self.display_surface.get_size()[1] * 0.8
        self.width = self.display_surface.get_size()[0] // 6
        self.create_items()

        #selection
        self.selection_index = 0
        self.selection_time = None
        self.can_move = True

    def display(self):
        self.input()
        self.selection_cooldown()

        for index, item in enumerate(self.item_list):
            name = self.attribute_name[index]
            value = self.player.get_value_by_index(index)
            max_value = self.max_values[index]
            cost = self.player.get_cost_by_index(index)
            item.display(self.display_surface,self.selection_index,name,value,max_value,cost)


    def create_items(self):
        self.item_list = []

        for item in range(self.attribute_num):
            full_width = self.display_surface.get_size()[0]
            increment = full_width // self.attribute_num
            left = (item * increment) + (increment - self.width) // 2

            top = self.display_surface.get_size()[1] * 0.1

            #create object
            item = Item(left,top,self.width,self.height,item,self.font)
            self.item_list.append(item)

    def input(self):
        keys = pygame.key.get_pressed()
        if self.can_move:
            if keys[pygame.K_RIGHT] and self.selection_index < self.attribute_num - 1:
                self.selection_index += 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_LEFT] and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_SPACE]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                self.item_list[self.selection_index].trigger(self.player)

    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_move = True

class Item:
    def __init__(self,l,t,w,h,i,font):
        self.rect = pygame.Rect(l,t,w,h)
        self.index = i
        self.font = font

    def display_names(self,surface,name,cost,selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR
        #title
        title_surf = self.font.render(name,False, color)
        title_rect = title_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,20))
        #cost
        cost_surf = self.font.render(str(int(cost)), False, color)
        cost_rect = cost_surf.get_rect(midbottom = self.rect.midbottom + pygame.math.Vector2(0,-20))
        #draw
        surface.blit(title_surf,title_rect)
        surface.blit(cost_surf,cost_rect)

    def display_bar(self,surface,value,max_value,selected):

        #drawing setup
        top = self.rect.midtop + pygame.math.Vector2(0,60)
        bottom = self.rect.midbottom + pygame.math.Vector2(0,-60)
        color = BAR_COLOR_SELECTED if selected else BAR_COLOR

        #bar setup
        full_height = bottom[1] - top[1]
        relative_num = (value / max_value) * full_height
        value_rect = pygame.Rect(top[0] - 15 , bottom[1] - relative_num , 30, 10)

        #draw elements
        pygame.draw.line(surface,color,top,bottom,5)
        pygame.draw.rect(surface,color,value_rect)

    def trigger(self,player):
        upgrade_attribute = list(player.stats.keys())[self.index]

        if player.exp >= player.upgrade_cost[upgrade_attribute]:
            player.exp -= player.upgrade_cost[upgrade_attribute]
            player.stats[upgrade_attribute] *= 1.2
            player.upgrade_cost[upgrade_attribute] *= 1.4
        
        if player.stats[upgrade_attribute] > player.max_stats[upgrade_attribute]:
            player.stats[upgrade_attribute] = player.max_stats[upgrade_attribute]

    def display(self,surface,selection_num,name,value,max_value,cost):
        if self.index == selection_num:
            pygame.draw.rect(surface,UPGRADE_BG_COLOR_SELECTED,self.rect)
            pygame.draw.rect(surface,UI_BORDER_COLOR,self.rect,4)
        else:
            pygame.draw.rect(surface,UI_BG_COLOR,self.rect)
            pygame.draw.rect(surface,UI_BORDER_COLOR,self.rect,4)
        self.display_names(surface,name,cost,self.index == selection_num)
        self.display_bar(surface,value,max_value,self.index == selection_num)