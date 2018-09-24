import graphics
from graphics import *
import time

class GameBoard():
    def __init__(self):
        self.size = 90
        self.stroke = 5
        self.w = self.size * 5
        self.h = self.size * 5
        self.win = GraphWin("/rl/tic-tac-toe", self.w, self.h)
        self.clear()

    def line(self,xyxy):
        rect = Rectangle(Point(xyxy[0], xyxy[1]), Point(xyxy[2],xyxy[3]))
        rect.setFill('black')
        rect.draw(self.win)

    def clear(self):
        rect = Rectangle(Point(0,0), Point(self.w, self.h))
        rect.setFill('white')
        rect.draw(self.win)
        self.line([self.size * 2, self.size, self.size * 2 + self.stroke, self.size * 4])
        self.line([self.size * 3, self.size, self.size * 3 + self.stroke, self.size * 4])
        self.line([self.size, self.size * 2, self.size * 4, self.size * 2 + self.stroke])
        self.line([self.size, self.size * 3, self.size * 4, self.size * 3 + self.stroke])
        time.sleep(0.2)

    def x(self,row,col):
        a = Point((row+1)*self.size + self.stroke*3,(col+1)*self.size + self.stroke*2)
        b = Point(a.getX()-self.stroke,a.getY()+self.stroke)
        c = Point(a.getX()+self.size-self.stroke*4,a.getY()+self.size-self.stroke*4)
        d = Point(c.getX()-self.stroke,c.getY()+self.stroke)
        poly = Polygon([a,b,d,c])
        poly.setFill('red')
        poly.draw(self.win)
        e = Point(c.getX(),b.getY())
        f = Point(d.getX(),a.getY())
        g = Point(b.getX(),c.getY())
        h = Point(a.getX(),d.getY())
        poly = Polygon([e,f,g,h])
        poly.setFill('red')
        poly.draw(self.win)

    def o(self,row,col):
        center = Point((row+1)*self.size + self.size * 0.5 + self.stroke//2,(col+1)*self.size + self.size * 0.5 + self.stroke//2)
        outer = Circle(center, self.size//3)
        outer.setFill('blue')
        outer.draw(self.win)
        inner = Circle(center, self.size//4.5)
        inner.setFill('white')
        inner.draw(self.win)
