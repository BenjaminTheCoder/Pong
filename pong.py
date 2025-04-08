import pygame as pg
from dataclasses import dataclass
pg.init()
WINDOWHEIGHT = 600
WINDOWWIDTH = 800
win = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
FPS = 15
clock = pg.time.Clock()

pg.display.set_caption("Pong")

@dataclass
class Ball:
    x: float
    y: float
    r: float
    vx: float
    vy: float

    def colide(self) -> None:
        pass    
        # if self.x >= WINDOWWIDTH - self.r:
        #     self.x = WINDOWWIDTH - self.r
        #     self.vx *= -1
        # elif self.x <= self.r:
        #     self.x = self.r
        #     self.vx *= -1

        # if self.y >= WINDOWHEIGHT - self.r:
        #     self.y = WINDOWHEIGHT - self.r
        #     self.vy *= -1
        # elif self.y <= self.r:
        #     self.y = self.r
        #     self.vy *= -1


    def colide_paddles(self, p1: pg.Rect, p2: pg.Rect) -> None:
        if self.x == p1.x + p1.w:
            self.vx *= -1
        if self.x == p2.x:
            self.vx *= -1

        

    def move(self) -> None:
        self.x += self.vx
        # self.y += self.vy


#variables player 1
vel = 5

p1 = pg.Rect(20, 255, 10, 150)

#variables player 2

p2 = pg.Rect(770, 255, 10, 150)

ball1 = Ball(400, 300, 15, 5, 5)

bl = False
br = False
moveUpP1 = False
moveDownP1 = False
moveUpP2 = False
moveDownP2 = False
bl = True
run = True
while run:
    ball1.move()
    ball1.colide()
    ball1.colide_paddles(p1, p2)



    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

#player 1
    if keys[pg.K_w]:
        p1.y -= vel
        moveUpP1 = True
    if keys[pg.K_s]:
        p1.y += vel
        moveDownP1 = True
    if p1.bottom<WINDOWHEIGHT:
        p1.y += vel
    if p1.top>0:
        p1.y -= vel    


#player 2
    if keys[pg.K_UP]:
        p2.y -= vel
        moveUpP2 = True
    if keys[pg.K_DOWN]:
        p2.y += vel
        moveDownP2 = True
    if p2.bottom<WINDOWHEIGHT:
        p2.y += vel
    if p2.top>0:
        p2.y -= vel    

    print(ball1.x)

    win.fill((0, 0, 0))
    pg.draw.rect(win, (255, 255, 255), p1)
    pg.draw.rect(win, (255, 255, 255), p2)
    pg.draw.circle(win, (0, 255, 255), (ball1.x, ball1.y), ball1.r)
    pg.display.update()
    clock.tick(FPS)
pg.quit()