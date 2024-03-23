import pygame as pg


snake_color = (8, 161, 31)

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x_player = 85
        self.y_player = 85
        self.ver = "DOWN"
             
    def draw(self):
        self.player = pg.draw.rect(self.screen, snake_color ,(self.x_player, self.y_player, 30, 30))

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
                   self.y_player += 40
               case "UP":
                   self.y_player -= 40
               case "RIGHT":
                   self.x_player += 40
               case "LEFT":
                   self.x_player -= 40
    
  


    def update(self):
        pass
             
