import pygame as pg
from player import Player

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 800))  #screen_size
        
        self.back_surf = pg.image.load('sources/background.jpg')
        self.clock = pg.time.Clock()
        self.player = Player(self.screen)
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
    
    def draw_lines(self):  
        for i in range(10):
            
           
            pg.draw.line(self.screen, 'white',[0, (i + 1)*80], [800, (i + 1)*80],  3)
            pg.draw.line(self.screen, 'white', [(i + 1) * 80, 0], [(i+1)* 80, 800], 3)
       
           
            


    def game(self):
        while True:
            self.draw()
            self.move()
            self.update()
            self.clock.tick(30)

    def draw(self):
        self.screen.blit(self.back_surf, (0,0))
        self.draw_lines()
        self.player.draw()
    def move(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        
        keys = pg.key.get_pressed()
        self.player.move(keys)

    def update(self):
        pg.display.update()
        
    

    
    
    

game = Game()
game.game()
