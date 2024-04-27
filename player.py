snake_color = (172, 194, 10)

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x_player = 85
        self.y_player = 85
        self.ver = "DOWN"
        self.rect = None
        self.cound = 0
        self.last_move = [self.x_player, self.y_player]
        self.tail = [self.last_move]
        self.change_block = 0
             
    def draw(self):
        self.player = pg.draw.rect(self.screen, snake_color ,(self.x_player, self.y_player, 30, 30))
        if len(self.tail) > 1:
            self.draw_tail()
            
    
    def draw_tail(self):
        for i in range(len(self.tail)):
            pg.draw.rect(self.screen, snake_color, [self.tail[i][0],self.tail[i][1],30,30])

    def move(self, keys):
        self.last_move = self.tail[-1]
        self.tail[0] = [self.x_player, self.y_player]
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
    def update_tail(self):
        if len(self.tail) > 2:
            for i in reversed(range(len(self.tail))):
                self.tail[i] = self.tail[i - 1]
    def add_block(self):
        self.tail.append(self.last_move)

    def update(self):
        self.update_tail()
             
             
