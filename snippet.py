from r2point import R2Point
from math import sqrt, acos


class Snippet:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        x1 = self.point1.x
        x2 = self.point2.x
        y1 = self.point1.y
        y2 = self.point2.y
        return (x1 - x2)**2 + (y1 - y2)**2

    def arc_length(self, r):
        h = self.length()
        return r*acos(round((2*r**2 - h)/2/r**2, 4))

    def clever_dist(self, r):
        if self.point1.arc:
            return self.arc_length(r)
        else:
            return sqrt(self.length())

    def intersection(self, x_c, y_c, r):
        x1 = self.point1.x
        x2 = self.point2.x
        y1 = self.point1.y
        y2 = self.point2.y
        x_vector = x2 - x1
        y_vector = y2 - y1
        a = x_vector*x_vector + y_vector*y_vector
        b = x_vector*(x1 - x_c) + y_vector*(y1 - y_c)
        c = (x1 - x_c)**2 + (y1 - y_c)**2 - r*r
        d = b**2 - a*c
        if d < 0:
            return []
        elif d == 0:
            if 0 < -b/a < 1:
                return [R2Point(x1 + x_vector*(-b/a),
                                y1 + y_vector*(-b/a), arc=True, contact=True)]
            else:
                return []
        else:
            t1 = (-b - sqrt(d))/a
            t2 = (-b + sqrt(d))/a
            if 0 < t1 < 1:
                if 0 < t2 < 1:
                    point1 = R2Point(x1 + x_vector*t1, y1 + y_vector*t1)
                    point2 = R2Point(x1 + x_vector*t2, y1 + y_vector*t2,
                                     arc=True)
                    return [point1, point2]
                else:
                    return [R2Point(x1 + x_vector*t1, y1 + y_vector*t1)]
            else:
                if 0 < t2 < 1:
                    return [R2Point(x1 + x_vector*t2, y1 + y_vector*t2,
                                    arc=True)]
                else:
                    return []


if __name__ == "__main__":  # pragma: no cover
    while True:
        Snip = Snippet(R2Point(0, 0), R2Point(0, 4))
        x, y, r = map(int, input().split())
        print(Snip.intersection(x, y, r))
