#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void

x, y, r = map(float, input('Введите центр и радиус окружности:').split())
p = R2Point(x, y)
f = Void(x, y, r)
try:
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}\n"
              f"perimeter in circle = {f.length()}\n")
        print()
except (EOFError, KeyboardInterrupt):
    print("\nStop")
