from dataclasses import dataclass, field

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
FPS = 30

@dataclass
class Rect:
    x: int
    y: int
    w: int
    h: int

@dataclass
class Ball:
    x: int
    y: int
    r: int
    vx: int
    vy: int

    def colide(self) -> None:   
        if self.y >= WINDOWHEIGHT - self.r:
            self.y = WINDOWHEIGHT - self.r
            self.vy *= -1
        if self.y <= self.r:
            self.y = self.r
            self.vy *= -1


    def colide_paddles(self, p1: Rect, p2: Rect) -> None:
        if self.x < (p1.x + p1.w + self.r) and self.x > (p1.x + self.r) and self.y > p1.y and self.y < p1.y + p1.h:
            self.vx *= -1
        if self.x > (p2.x - self.r) and self.x < (p2.x + p2.w - self.r)  and self.y > p2.y and self.y < p2.y + p2.h:
            self.vx *= -1


    def move(self) -> None:
        self.x += -self.vx
        self.y += -self.vy

@dataclass
class GameVariables: 
    replay: bool = False
    p1win: bool = False
    p2win: bool = False
    run: bool = True
    vel: int = 5
    p1s: int = 0
    p2s: int = 0
    p1: Rect = field(default_factory=lambda: Rect(20, 255, 10, 100))
    p2: Rect = field(default_factory=lambda: Rect(770, 255, 10, 100))
    ball: Ball = field(default_factory=lambda:Ball(400, 300, 20, 7, 7))

    def prewin_screen(self) -> None:
        if self.ball.x <= 0:
            self.p2s += 1
            self.reset_ball()
        if self.ball.x >= 800:
            self.p1s += 1
            self.reset_ball()

    def reset_ball(self) -> None:
        self.ball.x = 400
        self.ball.y = 300
        self.ball.vx *= -1
        self.ball.vy *= -1
    