import pyray as pr
from dataclasses import dataclass
WINDOWHEIGHT = 600
WINDOWWIDTH = 800
pr.init_window(WINDOWWIDTH, WINDOWHEIGHT, "Pong")
FPS = 30
pr.set_target_fps(FPS)
p1s = 0
p2s = 0

@dataclass
class Ball:
    x: int
    y: int
    r: int
    vx: int
    vy: int

    def colide(self) -> None:   
        if self.x >= WINDOWWIDTH - self.r:
            self.x = WINDOWWIDTH - self.r
            self.vx *= -1
        elif self.x <= self.r:
            self.x = self.r
            self.vx *= -1

        if self.y >= WINDOWHEIGHT - self.r:
            self.y = WINDOWHEIGHT - self.r
            self.vy *= -1
        if self.y <= self.r:
            self.y = self.r
            self.vy *= -1


    def colide_paddles(self, p1: pr.Rectangle, p2: pr.Rectangle) -> None:
        if self.x < (p1.x + p1.width + self.r) and self.x > (p1.x + self.r) and self.y > p1.y and self.y < p1.y + p1.height:
            self.vx *= -1
        if self.x > (p2.x - self.r) and self.x < (p2.x + p2.width - self.r)  and self.y > p2.y and self.y < p2.y + p2.height:
            self.vx *= -1


        

    def move(self) -> None:
        self.x += -self.vx
        self.y += -self.vy

vel = 5

p1 = pr.Rectangle(20, 255, 10, 100)


p2 = pr.Rectangle(770, 255, 10, 100)

ball1 = Ball(400, 300, 20, 7, 7)

black_screen = pr.Rectangle(0, 0, 800, 600)

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
    #player 1
    if pr.is_key_down(pr.KeyboardKey.KEY_W):
        p1.y -= vel
    if pr.is_key_down(pr.KeyboardKey.KEY_S):
        p1.y += vel
    if p1.y-p1.height<WINDOWHEIGHT:
        p1.y += vel
    if p1.y>0:
        p1.y -= vel    
    if pr.is_key_down(pr.KeyboardKey.KEY_A):
        p1.x -= vel
    if pr.is_key_down(pr.KeyboardKey.KEY_D):
        p1.x += vel
    if p1.x<0:
       p1.x += vel
    if p1.x+p1.width>400:
       p1.x -= vel

    if pr.is_key_down(pr.KeyboardKey.KEY_UP):
        p2.y -= vel
    if pr.is_key_down(pr.KeyboardKey.KEY_DOWN):
        p2.y += vel
    if p2.y-p2.height<WINDOWHEIGHT:
        p2.y += vel
    if p2.y+ p2.height>0:
        p2.y -= vel    
    if pr.is_key_down(pr.KeyboardKey.KEY_LEFT):
        p2.x -= vel
    if pr.is_key_down(pr.KeyboardKey.KEY_RIGHT):
        p2.x += vel
    if p2.x<0:
       p2.x += vel
    if p2.x<WINDOWWIDTH:
       p2.x += vel
    if p2.x+p2.width>419:
       p2.x -= vel  


    ball1.move()
    ball1.colide()
    ball1.colide_paddles(p1, p2)
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    pr.draw_circle_gradient( ball1.x, ball1.y, ball1.r, pr.WHITE, pr.GRAY)
    pr.draw_rectangle(int(p1.x), int(p1.y), int(p1.width), int(p1.height), pr.WHITE)
    pr.draw_rectangle(int(p2.x), int(p2.y), int(p2.width), int(p2.height), pr.WHITE)
    pr.end_drawing()
pr.close_window()