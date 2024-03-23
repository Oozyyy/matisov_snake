import pygame as pg
from player import Player
from apple import Apple

green = (7, 130, 25)
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
            pg.draw.line(self.screen, green ,[0, (i + 1)*40], [800, (i + 1)*40],  1)
            pg.draw.line(self.screen, green, [(i + 1) * 40, 0], [(i+1)* 40, 800], 1) 
            
    def game(self):
        while True:
            self.draw()
            self.move()
            self.update()
            self.clock.tick(10)

    def change_pos_apple(self):
        if pg.Rect.colliderect(self.apple.apple, self.player.player) is True:
            self.apple.change_pos()
                    
    def draw(self):
        self.screen.fill(green)
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
        
        self.change_pos_apple()
        pg.display.update()
        self.apple.update()
        
        


game = Game()
game.game()


