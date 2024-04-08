#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon


def void_draw(self, tk, p, r):
    tk.draw_circle(p, r)


def point_draw(self, tk, p, r):
    tk.draw_circle(p, r)
    tk.draw_point(self.p)


def segment_draw(self, tk, p, r):
    tk.draw_circle(p, r)
    tk.draw_line(self.p, self.q)


def polygon_draw(self, tk, p, r):
    tk.draw_circle(p, r)
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)


tk = TkDrawer()
x, y, r = map(float, input('Введите центр и радиус окружности:').split())
p = R2Point(x, y)
f = Void(x, y, r)
tk.clean()
f.draw(tk, p, r)

try:
    while True:
        f = f.add(R2Point())
        tk.clean()
        f.draw(tk, p, r)
        print(f"S = {f.area()}, P = {f.perimeter()}\n"
              f"perimeter in circle = {f.length()}\n")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
