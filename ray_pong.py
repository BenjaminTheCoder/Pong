import pyray as pr
from dataclasses import dataclass
import pong_logic as pl


pr.init_window(pl.WINDOWWIDTH, pl.WINDOWHEIGHT, "Pong")
pr.set_target_fps(pl.FPS)
p1s = 0
p2s = 0



vel = 5

p1 = pl.Rect(20, 255, 10, 100)


p2 = pl.Rect(770, 255, 10, 100)

ball1 = pl.Ball(400, 300, 20, 7, 7)

black_screen = pl.Rect(0, 0, 800, 600)

replay = False
moveUpP1 = False
moveDownP1 = False
moveUpP2 = False
moveDownP2 = False
p1win = False
p2win = False
bl = True
run = True

while not pr.window_should_close():

    if p2s == 9:
        p2win = True
        if pr.is_key_down(pr.KeyboardKey.KEY_SPACE):
            ball1.move()
            p1s = 0
            p2s = 0
            replay = False
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
        if pr.is_key_down(pr.KeyboardKey.KEY_SPACE):
            ball1.move()
            p1s = 0
            p2s = 0
            replay = False
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
            replay = False
    if p1s == 9:
        p1win = True

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

    #player 1
    if pr.is_key_down(pr.KeyboardKey.KEY_W):
        p1.y -= vel
    if pr.is_key_down(pr.KeyboardKey.KEY_S):
        p1.y += vel
    if p1.y+p1.h<=pl.WINDOWHEIGHT:
        p1.y += vel
    if p1.y>0:
        p1.y -= vel    
    if pr.is_key_down(pr.KeyboardKey.KEY_A):
        p1.x -= vel
    if pr.is_key_down(pr.KeyboardKey.KEY_D):
        p1.x += vel
    if p1.x<0:
       p1.x += vel
    if p1.x+p1.w>=400:
       p1.x -= vel
    # player 2
    if pr.is_key_down(pr.KeyboardKey.KEY_UP):
        p2.y -= vel
    if pr.is_key_down(pr.KeyboardKey.KEY_DOWN):
        p2.y += vel
    if p2.y+p2.h<=pl.WINDOWHEIGHT:
        p2.y += vel
    if p2.y>=0:
        p2.y -= vel    
    if pr.is_key_down(pr.KeyboardKey.KEY_LEFT):
        p2.x -= vel
    if pr.is_key_down(pr.KeyboardKey.KEY_RIGHT):
        p2.x += vel
    if p2.x<0:
       p2.x += vel
    if p2.x<pl.WINDOWWIDTH:
       p2.x += vel
    if p2.x+p2.w>419:
       p2.x -= vel  




    pr.begin_drawing()
    y = 0
    for n in range(1, 14):
        pr.draw_rectangle(398, y, 4, 25, pr.BROWN)
        y += 49
    pr.draw_circle_gradient( ball1.x, ball1.y, ball1.r, pr.YELLOW, pr.ORANGE)
    pr.draw_rectangle_gradient_h(int(p1.x), int(p1.y), int(p1.w), int(p1.h), pr.WHITE, pr.GRAY)
    pr.draw_rectangle_gradient_h(int(p2.x), int(p2.y), int(p2.w), int(p2.h), pr.WHITE, pr.GRAY)
    pr.clear_background(pr.SKYBLUE)
    pr.draw_text(f'{p1s}  {p2s}', 350, 32, 60, pr.WHITE)




    if p1win == True:
        if replay == False:
            pr.draw_rectangle(0, 0, pl.WINDOWWIDTH, pl.WINDOWHEIGHT, pr.BLACK)
            pr.draw_text('Player 1 wins!', 200, 270, 60, pr.WHITE)
            pr.draw_text('Press "Space" to play again', 190, 340, 30, pr.WHITE)
            ball1.vx = 0
            ball1.vy = 0
    if p2win == True:
        if replay == False:
            pr.draw_rectangle(0, 0, pl.WINDOWWIDTH, pl.WINDOWHEIGHT, pr.BLACK)
            pr.draw_text('Player 2 wins!', 200, 270, 60, pr.WHITE)
            pr.draw_text('Press "Space" to play again', 190, 340, 30, pr.WHITE)
            ball1.vx = 0
            ball1.vy = 0
    ball1.move()
    ball1.colide()
    ball1.colide_paddles(p1, p2)
    # pr.begin_drawing()
    # pr.clear_background(pr.BLACK)
    # pr.draw_text(f'{p1s}  {p2s}', 350, 32, 60, pr.WHITE)
    # pr.draw_circle_gradient( ball1.x, ball1.y, ball1.r, pr.WHITE, pr.GRAY)
    # pr.draw_rectangle(int(p1.x), int(p1.y), int(p1.w), int(p1.h), pr.WHITE)
    # pr.draw_rectangle(int(p2.x), int(p2.y), int(p2.w), int(p2.h), pr.WHITE)
    # pr.end_drawing()
    pr.end_drawing()
pr.close_window()