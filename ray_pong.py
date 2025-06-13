import pyray as pr
import pong_logic as pl

pr.init_window(pl.WINDOWWIDTH, pl.WINDOWHEIGHT, "Pong")
pr.set_target_fps(pl.FPS)

gv = pl.GameVariables()

def win_screen(pwin: bool, pnum: int) -> None:
    if pwin == True:
        if gv.replay == False:
            pr.draw_rectangle(0, 0, pl.WINDOWWIDTH, pl.WINDOWHEIGHT, pr.BLACK)
            pr.draw_text(f'Player {pnum} wins!', 200, 270, 60, pr.WHITE)
            pr.draw_text('Press "Space" to play again', 190, 340, 30, pr.WHITE)
            gv.ball.vx = 0
            gv.ball.vy = 0

def space_press() -> None:
    global gv
    if pr.is_key_down(pr.KeyboardKey.KEY_SPACE):
        gv = pl.GameVariables()

while not pr.window_should_close():

    # 1. Handle user input (update the player)

    # Player 1 movement
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

    # Player 2 movement
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


    if gv.p2s == 9:
        gv.p2win = True
        space_press()
            
    if gv.p1s == 9:
        gv.p1win = True
        space_press()

    gv.prewin_screen()

    # Toggle fullscreen
    if pr.is_key_down(pr.KeyboardKey.KEY_F):
        pr.toggle_fullscreen()

    # 2. Update the world (everything other than the player)
    gv.ball.move()
    gv.ball.colide()
    gv.ball.colide_paddles(gv.p1, gv.p2)

    # 3. Draw the world

    pr.begin_drawing()

    # Draw the dashed line
    y = 0
    for n in range(1, 14):
        pr.draw_rectangle(398, y, 4, 25, pr.BROWN)
        y += 49

    # Draw paddles, ball, and score
    pr.draw_circle_gradient( gv.ball.x, gv.ball.y, gv.ball.r, pr.YELLOW, pr.ORANGE)
    pr.draw_rectangle_gradient_h(int(gv.p1.x), int(gv.p1.y), int(gv.p1.w), int(gv.p1.h), pr.WHITE, pr.GRAY)
    pr.draw_rectangle_gradient_h(int(gv.p2.x), int(gv.p2.y), int(gv.p2.w), int(gv.p2.h), pr.WHITE, pr.GRAY)
    pr.clear_background(pr.SKYBLUE)
    pr.draw_text(f'{gv.p1s}  {gv.p2s}', 350, 32, 60, pr.WHITE)

    win_screen(gv.p1win, 1)
    win_screen(gv.p2win, 2)

    pr.end_drawing()
pr.close_window()