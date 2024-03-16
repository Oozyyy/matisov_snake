import pygame as pg
from player import Player
from apple import Apple

green = (5, 161, 33)
black = (0, 0, 0)
class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 800))  
        #self.screen.fill(black)
        self.back_surf = pg.image.load('sources/background.jpg')
        self.clock = pg.time.Clock()
        self.player = Player(self.screen)
        self.apple = Apple(self.screen)       
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
            
    
            pg.draw.line(self.screen, green ,[0, (i + 1)*40], [800, (i + 1)*40],  3)
            pg.draw.line(self.screen, green, [(i + 1) * 40, 0], [(i+1)* 40, 800], 3) 
            
    
         

    def game(self):
        while True:
            self.draw()
            self.move()
            self.update()
            self.clock.tick(10)


            
            
            


    def draw(self):
        self.screen.blit(self.back_surf, (0,0))
        self.draw_lines()
        self.player.draw()
        self.apple.draw()

      
    def move(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()      
        keys = pg.key.get_pressed()
        self.player.move(keys)

        
    def update(self):
        pg.display.update()
        self.apple.update()

game = Game()
game.game()

