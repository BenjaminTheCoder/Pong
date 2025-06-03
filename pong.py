import pygame as pg
import pong_logic as pl

pg.init()

win = pg.display.set_mode((pl.WINDOWWIDTH, pl.WINDOWHEIGHT))
clock = pg.time.Clock()

font = pg.font.SysFont('Arial', 60)

gv = pl.GameVariables()

while gv.run:
    keys =pg.key.get_pressed()
    

    if keys[pg.K_w]:
        gv.p1.y -= gv.vel
    if keys[pg.K_s]:
        gv.p1.y += gv.vel
    if gv.p1.y + gv.p1.h <= pl.WINDOWHEIGHT:
        gv.p1.y += gv.vel
    if gv.p1.y>0:
        gv.p1.y -= gv.vel    
    if keys[pg.K_a]:
        gv.p1.x -= gv.vel
    if keys[pg.K_d]:
        gv.p1.x += gv.vel
    if gv.p1.x<0:
       gv.p1.x += gv.vel
    if gv.p1.x + gv.p1.w >= 400:
       gv.p1.x -= gv.vel
    # player 2
    if keys[pg.K_UP]:
        gv.p2.y -= gv.vel
    if keys[pg.K_DOWN]:
        gv.p2.y += gv.vel
    if gv.p2.y + gv.p2.h <= pl.WINDOWHEIGHT:
        gv.p2.y += gv.vel
    if gv.p2.y >= 0:
        gv.p2.y -= gv.vel    
    if keys[pg.K_LEFT]:
        gv.p2.x -= gv.vel
    if keys[pg.K_RIGHT]:
        gv.p2.x += gv.vel
    if gv.p2.x < 0:
       gv.p2.x += gv.vel
    if gv.p2.x < pl.WINDOWWIDTH:
       gv.p2.x += gv.vel
    if gv.p2.x + gv.p2.w > 419:
       gv.p2.x -= gv.vel  

    #print(pl.ball1.x)




    gv.ball1.move()
    gv.ball1.colide()
    gv.ball1.colide_paddles(gv.p1, gv.p2)
    if gv.ball1.x <= 0:
        gv.p2s += 1
        gv.ball1.x = 400
        gv.ball1.y = 300
        gv.ball1.vx *= -1
        gv.ball1.vy *= -1
    if gv.ball1.x >= 800:
        gv.p1s += 1
        gv.ball1.x = 400
        gv.ball1.y = 300
        gv.ball1.vx *= -1
        gv.ball1.vy *= -1
    if gv.p2s == 9:
        gv.p2win = True
        if keys[pg.K_SPACE]:
            gv.ball1.move()
            gv.p1s = 0
            gv.p2s = 0
            gv.replay = True
            net = pl.Rect(398, 0, 4, 600)
            gv.p1 = pl.Rect(20, 255, 10, 100)
            gv.p2 = pl.Rect(770, 255, 10, 100)
            gv.ball1 = pl.Ball(400, 300, 20, 7, 7)
            gv.p1win = False
            gv.p2win = False
            bl = True
            run = True
    if gv.p1s == 9:
        gv.p1win = True
        if keys[pg.K_SPACE]:
            gv.ball1.move()
            gv.p1s = 0
            gv.p2s = 0
            gv.replay = True
            net = pl.Rect(398, 0, 4, 600)
            gv.p1 = pl.Rect(20, 255, 10, 100)
            gv.p2 = pl.Rect(770, 255, 10, 100)
            gv.ball1 = pl.Ball(400, 300, 20, 7, 7)
            gv.p1win = False
            gv.p2win = False
            bl = True
            run = True
        gv.replay = False
    if gv.p1s == 9:
        gv.p1win = True

    if gv.p2s == 9:
        gv.p2win = True

    for event in pg.event.get():
        if event.type == pg.QUIT:
            gv.run = False
            

    win.fill((0, 0, 0))
    pg.draw.rect(win, (100, 0, 0), (gv.p1.x, gv.p1.y, gv.p1.w, gv.p1.h))
    pg.draw.rect(win, (255, 255, 0), (gv.p2.x, gv.p2.y, gv.p2.w, gv.p2.h))
    y = 0
    for n in range(1, 14):
        pg.draw.rect(win, (255, 255, 255), (398, y, 4, 25))
        y += 49



    pg.draw.circle(win, (190, 188, 188), (gv.ball1.x, gv.ball1.y), gv.ball1.r)
            
    score = font.render(f'{gv.p1s}  {gv.p2s}', True, (255, 255, 255))
    win.blit(score, (360, 32))
    p1Win = font.render('Player 1 wins!', True, (255, 255, 255))
    p2Win = font.render('Player 2 wins!', True, (255, 255, 255))
    winL2 = font.render('Press "Space" to play again', True, (255, 255, 255))

    if gv.p1win == True:
        if gv.replay == False:
            win.fill((0, 0, 0))
            win.blit(p1Win, (260, 270))
            win.blit(winL2, (100, 320))
            gv.ball1.vx = 0
            gv.ball1.vy = 0
    if gv.p2win == True:
        if gv.replay == False:
            win.fill((0, 0, 0))
            win.blit(p2Win, (260, 270))
            win.blit(winL2, (100, 320))
            gv.ball1.vx = 0
            gv.ball1.vy = 0
    # print('pl.ball1', pl.ball1)
    # print('pl.p2', pl.p2)
    # print()
    pg.display.update()
    clock.tick(pl.FPS)
pg.quit()