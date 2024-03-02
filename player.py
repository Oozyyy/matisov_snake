import pygame as pg

snake_color = (141, 204, 33)

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x = 190
        self.y = 190
        self.ver = "DOWN"
    def draw(self):
        pg.draw.rect(self.screen, snake_color ,(self.x, self.y, 30, 30))

    def move(self, keys):
        if keys[pg.K_s]:
            self.ver = "DOWN"

        if keys[pg.K_w]:
           self.ver = "UP"

        if keys[pg.K_d]:
           self.ver = "RIGHT"
    
        if keys[pg.K_a]:
           self.ver = "LEFT"
           
        match self.ver:
               case "DOWN":
                   self.y += 80
               case "UP":
                   self.y -= 80
               case "RIGHT":
                   self.x += 80
               case "LEFT":
                   self.x -= 80
               


            
                         

    def update(self):
        pass  
