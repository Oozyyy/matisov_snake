import pygame as pg
import random
from player import Player


apple_color = (224, 11, 11)
dis_width = 800
dis_height = 800
snake_block = 20

class Apple:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.spawn_x = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
        self.spawn_y = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

    def spawn(self):
        if self.apple.colliderect(self.player.player):
            self.spawn_x = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            self.spawn_y = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            return True
        return False

        
    def draw(self):
        #self.apple = pg.draw.rect(self.screen, apple_color ,[self.spawn_x, self.spawn_y, 25, 25 ])
        
        self.apple = pg.draw.circle(self.screen, apple_color ,(self.spawn_x, self.spawn_y),15)
        
                      

    def update(self):
        return self.spawn()
   
   
