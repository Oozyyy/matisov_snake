import pygame as pg
from player import Player
from apple import Apple

green = (7, 130, 25)
black = (0, 0, 0)
HEIGHT = 800
WEIGHT = 800
game_over =True
class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 800))
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
        
        for i in range(20):
            pg.draw.line(self.screen, black ,[0, (i + 1)*40], [800, (i + 1)*40],  1)
            pg.draw.line(self.screen, black, [(i + 1) * 40, 0], [(i+1)* 40, 800], 1) 
            
    def game(self):
        while True:
            while not self.finish():
                self.draw()
                self.move()
                self.update()
                self.clock.tick(10)
               
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
        
        #self.change_pos_apple()
        pg.display.update()
        if self.Apple.update():
            self.player.add_block()
        self.player.update()
        
        
        
game = Game()
game.game()


