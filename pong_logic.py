from dataclasses import dataclass

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