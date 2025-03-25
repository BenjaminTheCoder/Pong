import pygame as pg
pg.init()
WINDOWHEIGHT = 600
WINDOWWIDTH = 800
win = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pg.display.set_caption("Pong")

#variables player 1
vel = 5


p1 = pg.Rect(5, 255, 10, 150)

#variables player 2

p2 = pg.Rect(785, 255, 10, 150)


ball = pg.Rect(400, 300, 10, 10)
bl = False
br = False
moveUpP1 = False
moveDownP1 = False
moveUpP2 = False
moveDownP2 = False
bl = True
run = True
while run:
    pg.time.delay(16)
    if bl == True:
        ball.x -= vel
    if br == True:
        ball.x += vel
    if p1.colliderect(ball):
        print("Yay!")
        bl = False
        br = True
        ball.y += vel
    if p2.colliderect(ball):
        print("Wooh!")
        bl = True
        br = False
        ball.y += vel


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
    pg.draw.rect(win, (255, 255, 255), p1)
    pg.draw.rect(win, (255, 255, 255), p2)
    pg.draw.rect(win, (255, 255, 255), ball)
    pg.display.update()
pg.quit()