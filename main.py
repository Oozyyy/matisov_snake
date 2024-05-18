import pygame as pg
from player import Player
from apple import Apple
from database import dataBase

green = (7, 130, 25)
black = (0, 0, 0)
HEIGHT = 800
WEIGHT = 1200
game_over =True

class Game:
    def __init__(self, nick_name):
        self.nickename = nick_name
        self.database = dataBase()
        pg.init()
        self.screen = pg.display.set_mode((1200, 800))
        self.player = Player(self.screen)
        self.Apple = Apple(self.screen, self.player)         
        self.clock = pg.time.Clock()
           
        massive = [[0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0]]
    
    def draw_lines (self):  
        
        for i in range(30):
            pg.draw.line(self.screen, black ,[0, (i + 1)*40], [1200, (i + 1)*40],  1)
            pg.draw.line(self.screen, black, [(i + 1) * 40, 0], [(i+1)* 40, 800], 1) 
            
    def game(self):
        while not self.finish():
            self.draw()
            self.move()
            self.update()
            self.clock.tick(10)
        self.database.reg(self)
        self.game_ower_screen(self.database.getDb())
        self.database.close()
               
    def draw(self):
        self.screen.fill(green)
        self.draw_lines()
        self.player.draw()
        self.Apple.draw()
                
    def move(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()      
        keys = pg.key.get_pressed()
        self.player.move(keys)

    def finish(self):
        return self.player.x_player >= WEIGHT or self.player.x_player < 0 or self.player.y_player >= HEIGHT or self.player.y_player < 0
       
    def update(self):     
        
        pg.display.update()
        if self.Apple.update():
            self.player.add_block()
        self.player.update()

name = input()              
game = Game(name)
game.game()

