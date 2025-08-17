import pygame as pg
import pong_logic as pl

pg.init()

win = pg.display.set_mode((pl.WINDOWWIDTH, pl.WINDOWHEIGHT))
pg.display.set_caption("Pygame Pong")
clock = pg.time.Clock()

font = pg.font.SysFont('Arial', 60)

gv = pl.GameVariables()

def draw_win_screen(pWin: pg.Surface) -> None:
    if gv.replay == False:
        win.fill((0, 0, 0))
        win.blit(pWin, (260, 270))
        win.blit(winL2, (100, 320))
        gv.ball.vx = 0
        gv.ball.vy = 0

def space_press(keys: pg.key.ScancodeWrapper) -> None:
    global gv
    if keys[pg.K_SPACE]:
        gv = pl.GameVariables()

while gv.run:

    # 1. Handle user input
    keys = pg.key.get_pressed()

    # Toggle fullscreen
    if keys[pg.K_f]:
        pg.display.toggle_fullscreen()
    
    # Player 1 movement
    if keys[pg.K_w]:
        gv.p1.y -= gv.vel
    if keys[pg.K_s]:
        gv.p1.y += gv.vel
    if gv.p1.y + gv.p1.h <= pl.WINDOWHEIGHT:
        gv.p1.y += gv.vel
    if gv.p1.y > 0:
        gv.p1.y -= gv.vel    
    if keys[pg.K_a]:
        gv.p1.x -= gv.vel
    if keys[pg.K_d]:
        gv.p1.x += gv.vel
    if gv.p1.x < 0:
       gv.p1.x += gv.vel
    if gv.p1.x + gv.p1.w >= 400:
       gv.p1.x -= gv.vel
    
    # Player 2 movement
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
    if gv.p2.x < pl.WINDOWWIDTH:
       gv.p2.x += gv.vel
    if gv.p2.x + gv.p2.w > 419:
       gv.p2.x -= gv.vel  

    gv.prewin_screen()
    
    if gv.p2s == 9:
        gv.p2win = True
        space_press(keys)

    if gv.p1s == 9:
        gv.p1win = True
        space_press(keys)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            gv.run = False
            

    # 2. Update the world (everything other than the player)
    gv.ball.move()
    gv.ball.colide()
    gv.ball.colide_paddles(gv.p1, gv.p2)

    # 3. Draw the world
    win.fill((135, 206, 235))

    # Draw the paddles
    pg.draw.rect(win, (255, 255, 255), (gv.p1.x, gv.p1.y, gv.p1.w, gv.p1.h))
    pg.draw.rect(win, (255, 255, 255), (gv.p2.x, gv.p2.y, gv.p2.w, gv.p2.h))
    
    # Draw the dashed line
    y = 0
    for n in range(1, 14):
        pg.draw.rect(win, (150, 85, 85), (398, y, 4, 25))
        y += 49

    # Draw the ball
    pg.draw.circle(win, (255, 201, 34), (gv.ball.x, gv.ball.y), gv.ball.r)

    # Draw the score        
    score = font.render(f'{gv.p1s}  {gv.p2s}', True, (255, 255, 255))
    win.blit(score, (360, 32))

    # Draw win screen
    p1Win = font.render('Player 1 wins!', True, (255, 255, 255))
    p2Win = font.render('Player 2 wins!', True, (255, 255, 255))
    winL2 = font.render('Press "Space" to play again', True, (255, 255, 255))

    if gv.p1win == True:
        draw_win_screen(p1Win)
    if gv.p2win == True:
        draw_win_screen(p2Win)

    pg.display.update()
    clock.tick(pl.FPS)

pg.quit()