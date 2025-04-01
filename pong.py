import pygame as pg
from dataclasses import dataclass

pg.init()
WINDOWHEIGHT = 600
WINDOWWIDTH = 800
win = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pg.display.set_caption("Pong")

@dataclass
class Ball:
    x: float
    y: float
    r: float
    vx: float
    vy: float

    def edges(self) -> None:
        if self.x >= WINDOWWIDTH - self.r:
            self.x = WINDOWWIDTH - self.r
            self.vx *= -1
        elif self.x <= self.r:
            self.x = self.r
            self.vx *= -1

        if self.y >= WINDOWHEIGHT - self.r:
            self.y = WINDOWHEIGHT - self.r
            self.vy *= -1
        elif self.y <= self.r:
            self.y = self.r
            self.vy *= -1

    def move(self) -> None:
        self.x += self.vx
        self.y += self.vy


#variables player 1
vel = 5

p1 = pg.Rect(5, 255, 10, 150)

#variables player 2

p2 = pg.Rect(785, 255, 10, 150)

ball1 = Ball(400, 300, 50, 0.05, 0.05)
ball2 = Ball(400, 300, 25, 0.05, 0.1)


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
    ball1.edges()
    ball2.move()
    ball2.edges()
    # pg.time.delay(16)
    # if bl == True:
    #     ball.x -= vel
    # if br == True:
    #     ball.x += vel
    # if p1.colliderect(ball):
    #     print("Yay!")
    #     bl = False
    #     br = True
    #     ball.y += vel
    # if p2.colliderect(ball):
    #     print("Wooh!")
    #     bl = True
    #     br = False
    #     ball.y += vel


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

    win.fill((0, 0, 0))
    #pg.draw.rect(win, (255, 255, 255), p1)
    #pg.draw.rect(win, (255, 255, 255), p2)
    pg.draw.circle(win, (255, 0, 0), (ball1.x, ball1.y), ball1.r)
    pg.draw.circle(win, (0, 0, 255), (ball2.x, ball2.y), ball2.r)
    pg.display.update()
pg.quit()