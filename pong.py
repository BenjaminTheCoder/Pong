import pygame as pg
from dataclasses import dataclass
import pong_logic as pl

pg.init()

win = pg.display.set_mode((pl.WINDOWWIDTH, pl.WINDOWHEIGHT))
clock = pg.time.Clock()
p1s = 0
p2s = 0
pg.display.set_caption("Pong")


    
#variables player 1
vel = 5

# net1 = pg.Rect(398, 0, 4, 25)
# net2 = pg.Rect(398, 50, 4, 25)
# net3 = pg.Rect(398, 100, 4, 25)
# net4 = pg.Rect(398, 150, 4, 25)
# net5 = pg.Rect(398, 200, 4, 25)
# net6 = pg.Rect(398, 250, 4, 25)
# net7 = pg.Rect(398, 300, 4, 25)
# net8 = pg.Rect(398, 350, 4, 25)
# net9 = pg.Rect(398, 400, 4, 25)
# net10 = pg.Rect(398, 450, 4, 25)
# net11 = pg.Rect(398, 500, 4, 25)
# net12 = pg.Rect(398, 550, 4, 25)
# net13 = pg.Rect(398, 595, 4, 25)



p1 = pl.Rect(20, 255, 10, 100)

#variables player 2

p2 = pl.Rect(770, 255, 10, 100)

ball1 = pl.Ball(400, 300, 20, 7, 7)

black_screen = pg.Rect(0, 0, 800, 600)

font = pg.font.SysFont('Arial', 60)

replay = False
moveUpP1 = False
moveDownP1 = False
moveUpP2 = False
moveDownP2 = False
p1win = False
p2win = False
bl = True
run = True
while run:
    keys =pg.key.get_pressed()
    

    if keys[pg.K_w]:
        p1.y -= vel
    if keys[pg.K_s]:
        p1.y += vel
    if p1.y+p1.h<=pl.WINDOWHEIGHT:
        p1.y += vel
    if p1.y>0:
        p1.y -= vel    
    if keys[pg.K_a]:
        p1.x -= vel
    if keys[pg.K_d]:
        p1.x += vel
    if p1.x<0:
       p1.x += vel
    if p1.x+p1.w>=400:
       p1.x -= vel
    # player 2
    if keys[pg.K_UP]:
        p2.y -= vel
    if keys[pg.K_DOWN]:
        p2.y += vel
    if p2.y+p2.h<=pl.WINDOWHEIGHT:
        p2.y += vel
    if p2.y>=0:
        p2.y -= vel    
    if keys[pg.K_LEFT]:
        p2.x -= vel
    if keys[pg.K_RIGHT]:
        p2.x += vel
    if p2.x<0:
       p2.x += vel
    if p2.x<pl.WINDOWWIDTH:
       p2.x += vel
    if p2.x+p2.w>419:
       p2.x -= vel  

    #print(ball1.x)




    ball1.move()
    ball1.colide()
    ball1.colide_paddles(p1, p2)
    if ball1.x <= 0:
        p2s += 1
        ball1.x = 400
        ball1.y = 300
        ball1.vx *= -1
        ball1.vy *= -1
    if ball1.x >= 800:
        p1s += 1
        ball1.x = 400
        ball1.y = 300
        ball1.vx *= -1
        ball1.vy *= -1
    if p2s == 9:
        p2win = True
        if keys[pg.K_SPACE]:
            ball1.move()
            p1s = 0
            p2s = 0
            replay = True
            net = pl.Rect(398, 0, 4, 600)
            p1 = pl.Rect(20, 255, 10, 100)
            p2 = pl.Rect(770, 255, 10, 100)
            ball1 = pl.Ball(400, 300, 20, 7, 7)
            moveUpP1 = False
            moveDownP1 = False
            moveUpP2 = False
            moveDownP2 = False
            p1win = False
            p2win = False
            bl = True
            run = True
    if p1s == 9:
        p1win = True
        if keys[pg.K_SPACE]:
            ball1.move()
            p1s = 0
            p2s = 0
            replay = True
            net = pl.Rect(398, 0, 4, 600)
            p1 = pl.Rect(20, 255, 10, 100)
            p2 = pl.Rect(770, 255, 10, 100)
            ball1 = pl.Ball(400, 300, 20, 7, 7)
            p1win = True
            moveUpP1 = False
            moveDownP1 = False
            moveUpP2 = False
            moveDownP2 = False
            p1win = False
            p2win = False
            bl = True
            run = True
        replay = False
    if p1s == 9:
        p1win = True

    if p2s == 9:
        p2win = True

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    win.fill((0, 0, 0))
    pg.draw.rect(win, (100, 0, 0), (p1.x, p1.y, p1.w, p1.h))
    pg.draw.rect(win, (255, 255, 0), (p2.x, p2.y, p2.w, p2.h))
    y = 0
    for n in range(1, 14):
        pg.draw.rect(win, (255, 255, 255), (398, y, 4, 25))
        y += 49



    pg.draw.circle(win, (190, 188, 188), (ball1.x, ball1.y), ball1.r)
            
    score = font.render(f'{p1s}  {p2s}', True, (255, 255, 255))
    win.blit(score, (360, 32))
    p1Win = font.render('Player 1 wins!', True, (255, 255, 255))
    p2Win = font.render('Player 2 wins!', True, (255, 255, 255))
    winL2 = font.render('Press "Space" to play again', True, (255, 255, 255))

    if p1win == True:
        if replay == False:
            pg.draw.rect(win, (0, 0, 0), black_screen)
            win.blit(p1Win, (260, 270))
            win.blit(winL2, (100, 320))
            ball1.vx = 0
            ball1.vy = 0
    if p2win == True:
        if replay == False:
            pg.draw.rect(win, (0, 0, 0), black_screen)
            win.blit(p2Win, (260, 270))
            win.blit(winL2, (100, 320))
            ball1.vx = 0
            ball1.vy = 0
    # print('ball1', ball1)
    # print('p2', p2)
    # print()
    pg.display.update()
    clock.tick(pl.FPS)
pg.quit()