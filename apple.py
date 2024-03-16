import pygame as pg
import random

apple_color = (224, 11, 11)

class Apple:
    def __init__(self, screen):
        self.screen = screen
        

        self.x = random.randint(0,800) 
        self.y = random.randint(0,800) 

        
    def draw(self):
        pg.draw.circle(self.screen, apple_color ,(self.x // 40 * 40 + 20, self.y // 40 * 40 + 20), 15)    
    def update(self):
        pass       
   
