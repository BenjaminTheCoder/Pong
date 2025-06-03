import pyray as pr
import pong_logic as pl

pr.init_window(pl.WINDOWWIDTH, pl.WINDOWHEIGHT, "Pong")
pr.set_target_fps(pl.FPS)

gv = pl.GameVariables()

while not pr.window_should_close():

    if gv.p2s == 9:
        gv.p2win = True
        if pr.is_key_down(pr.KeyboardKey.KEY_SPACE):
            gv.ball1.move()
            gv.p1s = 0
            gv.p2s = 0
            gv.replay = False
            gv.p1 = pl.Rect(20, 255, 10, 100)
            gv.p2 = pl.Rect(770, 255, 10, 100)
            gv.ball1 = pl.Ball(400, 300, 20, 7, 7)
            moveUpP1 = False
            moveDownP1 = False
            moveUpP2 = False
            moveDownP2 = False
            gv.p1win = False
            gv.p2win = False
            bl = True
            run = True
    if gv.p1s == 9:
        gv.p1win = True
        if pr.is_key_down(pr.KeyboardKey.KEY_SPACE):
            gv.ball1.move()
            gv.p1s = 0
            gv.p2s = 0
            gv.replay = False
            gv.p1 = pl.Rect(20, 255, 10, 100)
            gv.p2 = pl.Rect(770, 255, 10, 100)
            gv.ball1 = pl.Ball(400, 300, 20, 7, 7)
            moveUpP1 = False
            moveDownP1 = False
            moveUpP2 = False
            moveDownP2 = False
            gv.p1win = False
            gv.p2win = False
            bl = True
            run = True
            gv.replay = False
    if gv.p1s == 9:
        gv.p1win = True

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

    #player 1
    if pr.is_key_down(pr.KeyboardKey.KEY_W):
        gv.p1.y -= gv.vel
    if pr.is_key_down(pr.KeyboardKey.KEY_S):
        gv.p1.y += gv.vel
    if gv.p1.y + gv.p1.h <= pl.WINDOWHEIGHT:
        gv.p1.y += gv.vel
    if gv.p1.y > 0:
        gv.p1.y -= gv.vel    
    if pr.is_key_down(pr.KeyboardKey.KEY_A):
        gv.p1.x -= gv.vel
    if pr.is_key_down(pr.KeyboardKey.KEY_D):
        gv.p1.x += gv.vel
    if gv.p1.x < 0:
       gv.p1.x += gv.vel
    if gv.p1.x + gv.p1.w>=400:
       gv.p1.x -= gv.vel
    # player 2
    if pr.is_key_down(pr.KeyboardKey.KEY_UP):
        gv.p2.y -= gv.vel
    if pr.is_key_down(pr.KeyboardKey.KEY_DOWN):
        gv.p2.y += gv.vel
    if gv.p2.y + gv.p2.h <= pl.WINDOWHEIGHT:
        gv.p2.y += gv.vel
    if gv.p2.y>=0:
        gv.p2.y -= gv.vel    
    if pr.is_key_down(pr.KeyboardKey.KEY_LEFT):
        gv.p2.x -= gv.vel
    if pr.is_key_down(pr.KeyboardKey.KEY_RIGHT):
        gv.p2.x += gv.vel
    if gv.p2.x < 0:
       gv.p2.x += gv.vel
    if gv.p2.x < pl.WINDOWWIDTH:
       gv.p2.x += gv.vel
    if gv.p2.x + gv.p2.w > 419:
       gv.p2.x -= gv.vel  




    pr.begin_drawing()
    y = 0
    for n in range(1, 14):
        pr.draw_rectangle(398, y, 4, 25, pr.BROWN)
        y += 49
    pr.draw_circle_gradient( gv.ball1.x, gv.ball1.y, gv.ball1.r, pr.YELLOW, pr.ORANGE)
    pr.draw_rectangle_gradient_h(int(gv.p1.x), int(gv.p1.y), int(gv.p1.w), int(gv.p1.h), pr.WHITE, pr.GRAY)
    pr.draw_rectangle_gradient_h(int(gv.p2.x), int(gv.p2.y), int(gv.p2.w), int(gv.p2.h), pr.WHITE, pr.GRAY)
    pr.clear_background(pr.SKYBLUE)
    pr.draw_text(f'{gv.p1s}  {gv.p2s}', 350, 32, 60, pr.WHITE)




    if gv.p1win == True:
        if gv.replay == False:
            pr.draw_rectangle(0, 0, pl.WINDOWWIDTH, pl.WINDOWHEIGHT, pr.BLACK)
            pr.draw_text('Player 1 wins!', 200, 270, 60, pr.WHITE)
            pr.draw_text('Press "Space" to play again', 190, 340, 30, pr.WHITE)
            gv.ball1.vx = 0
            gv.ball1.vy = 0
    if gv.p2win == True:
        if gv.replay == False:
            pr.draw_rectangle(0, 0, pl.WINDOWWIDTH, pl.WINDOWHEIGHT, pr.BLACK)
            pr.draw_text('Player 2 wins!', 200, 270, 60, pr.WHITE)
            pr.draw_text('Press "Space" to play again', 190, 340, 30, pr.WHITE)
            gv.ball1.vx = 0
            gv.ball1.vy = 0
    gv.ball1.move()
    gv.ball1.colide()
    gv.ball1.colide_paddles(gv.p1, gv.p2)
    # pr.begin_drawing()
    # pr.clear_background(pr.BLACK)
    # pr.draw_text(f'{pl.p1s}  {pl.p2s}', 350, 32, 60, pr.WHITE)
    # pr.draw_circle_gradient( pl.ball1.x, pl.ball1.y, pl.ball1.r, pr.WHITE, pr.GRAY)
    # pr.draw_rectangle(int(pl.p1.x), int(pl.p1.y), int(pl.p1.w), int(pl.p1.h), pr.WHITE)
    # pr.draw_rectangle(int(pl.p2.x), int(pl.p2.y), int(pl.p2.w), int(pl.p2.h), pr.WHITE)
    # pr.end_drawing()
    pr.end_drawing()
pr.close_window()