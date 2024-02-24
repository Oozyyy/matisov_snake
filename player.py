import pygame as pg



class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x = 150
        self.y = 150
    def draw(self):
        #pg.draw.circle(self.screen, 'white', (self.x, self.y), 10)
        pg.draw.rect(self.screen, 'White' ,(self.x, self.y, 30, 30))

    def move(self, keys):
        if keys[pg.K_w]:
            self.y -= 10
        elif keys[pg.K_s]:
            self.y += 10
        elif keys[pg.K_a]:
            self.x -= 10
        elif keys[pg.K_d]:
            self.x += 10
        
    def update(self):
        pass