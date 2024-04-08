from deq import Deq
from r2point import R2Point
from snippet import Snippet


class Figure:
    """ Абстрактная фигура """

    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0

    def length(self):
        return 0.0


class Void(Figure):
    """ "Hульугольник" """

    def __init__(self, x_c, y_c, r):
        self.x_c = x_c
        self.y_c = y_c
        self.r = r

    def add(self, p):
        return Point(p, self.x_c, self.y_c, self.r)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p, x_c, y_c, r):
        self.p = p
        self.x_c = x_c
        self.y_c = y_c
        self.r = r

    def add(self, q):
        return self if self.p == q else Segment(self.p, q,
                                                self.x_c, self.y_c, self.r)


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q, x_c, y_c, r):
        self.p, self.q = p, q
        self.x_c = x_c
        self.y_c = y_c
        self.r = r

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r, self.x_c, self.y_c, self.r)
        elif r.is_inside(self.p, self.q):
            return self
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q, self.x_c, self.y_c, self.r)
        else:
            return Segment(self.p, r, self.x_c, self.y_c, self.r)

    def length(self):
        if ((self.p.x - self.x_c) ** 2 + (self.p.y - self.y_c) ** 2
                <= self.r * self.r):
            if ((self.q.x - self.x_c) ** 2 + (self.q.y - self.y_c) ** 2
                    <= self.r * self.r):
                return self.p.dist(self.q)
            else:
                t = Snippet(self.p, self.q).intersection(
                    self.x_c, self.y_c, self.r)
                if t:
                    return self.p.dist(t[0])
                else:
                    return 0.0
        else:
            if ((self.q.x - self.x_c) ** 2 + (self.q.y - self.y_c) ** 2
                    <= self.r * self.r):
                t = Snippet(self.p, self.q).intersection(
                    self.x_c, self.y_c, self.r)
                if t:
                    return self.p.dist(t[0])
                else:
                    return 0.0
            else:
                t = Snippet(self.p, self.q).intersection(
                    self.x_c, self.y_c, self.r)
                if len(t) == 2:
                    p1 = t[0]
                    p2 = t[1]
                    return p1.dist(p2) + Snippet(p1, p2).arc_length(self.r)
                else:
                    return 0.0


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c, x_c, y_c, r):
        self.points = Deq()
        self.points.push_first(b)

        self.x_c = x_c
        self.y_c = y_c
        self.r = r
        self.circle_points = Deq()

        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)

            if (c.x - x_c) ** 2 + (c.y - y_c) ** 2 <= r * r:
                if (c.x - x_c) ** 2 + (c.y - y_c) ** 2 == r * r:
                    c.arc = True
                self.circle_points.push_first(c)
            for x in Snippet(c, b).intersection(self.x_c, self.y_c, r):
                c.arc = False
                self.circle_points.push_first(x)

            if (b.x - x_c) ** 2 + (b.y - y_c) ** 2 <= r * r:
                c.arc = False
                if (b.x - x_c) ** 2 + (b.y - y_c) ** 2 == r * r:
                    b.arc = True
                self.circle_points.push_first(b)
            for x in Snippet(b, a).intersection(self.x_c, self.y_c, r):
                b.arc = False
                self.circle_points.push_first(x)

            if (a.x - x_c) ** 2 + (a.y - y_c) ** 2 <= r * r:
                b.arc = False
                if (a.x - x_c) ** 2 + (a.y - y_c) ** 2 == r * r:
                    a.arc = True
                self.circle_points.push_first(a)
            for x in Snippet(a, c).intersection(self.x_c, self.y_c, r):
                a.arc = False
                self.circle_points.push_first(x)

            if (c.x - x_c) ** 2 + (c.y - y_c) ** 2 <= r * r:
                a.arc = False
        else:
            self.points.push_last(a)
            self.points.push_first(c)

            if (a.x - x_c) ** 2 + (a.y - y_c) ** 2 <= r * r:
                if (a.x - x_c) ** 2 + (a.y - y_c) ** 2 == r * r:
                    a.arc = True
                self.circle_points.push_first(a)
            for x in Snippet(a, b).intersection(self.x_c, self.y_c, r):
                a.arc = False
                self.circle_points.push_first(x)

            if (b.x - x_c) ** 2 + (b.y - y_c) ** 2 <= r * r:
                a.arc = False
                if (b.x - x_c) ** 2 + (b.y - y_c) ** 2 == r * r:
                    b.arc = True
                self.circle_points.push_first(b)
            for x in Snippet(b, c).intersection(self.x_c, self.y_c, r):
                b.arc = False
                self.circle_points.push_first(x)

            if (c.x - x_c) ** 2 + (c.y - y_c) ** 2 <= r * r:
                b.arc = False
                if (c.x - x_c) ** 2 + (c.y - y_c) ** 2 == r * r:
                    c.arc = True
                self.circle_points.push_first(c)
            for x in Snippet(c, a).intersection(self.x_c, self.y_c, r):
                c.arc = False
                self.circle_points.push_first(x)

            if (a.x - x_c) ** 2 + (a.y - y_c) ** 2 <= r * r:
                c.arc = False

        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._area = abs(R2Point.area(a, b, c))
        self._perm = 0.0

        for i in range(0, self.circle_points.size() - 1):
            p1 = self.circle_points.array[i]
            p2 = self.circle_points.array[i + 1]
            self._perm += Snippet(p1, p2).clever_dist(self.r)

        if self.circle_points.size() > 1:
            p1 = self.circle_points.last()
            p2 = self.circle_points.first()
            self._perm += Snippet(p1, p2).clever_dist(self.r)

    def perimeter(self):
        return self._perimeter

    def area(self):
        return self._area

    def length(self):
        # for p in self.circle_points.array:
        #     print(p.x, p.y, p.arc)
        return self._perm

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())
            if self.circle_points.array:
                self.circle_points.push_last(self.circle_points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            self._perimeter -= self.points.first().dist(self.points.last())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))
            last = Snippet(self.points.first(), self.points.last())
            mas_last = last.intersection(self.x_c, self.y_c, self.r)
            del_last = len(mas_last)
            if del_last > 0:
                if mas_last[0] in self.circle_points:
                    while not (mas_last[0] == self.circle_points.last()):
                        self.circle_points.push_last(
                            self.circle_points.pop_first())
            # else:
            #     if self.points.first() in self.circle_points:
            #         while not (self.points.first() ==
            #                    self.circle_points.first()):
            #             self.circle_points.push_last(
            #                 self.circle_points.pop_first())
            if self.circle_points.array:
                self._perm -= (Snippet(self.circle_points.last(),
                                       self.circle_points.first()).
                               clever_dist(self.r))
            if del_last == 2:
                if self.circle_points.size() > 2:
                    p1 = self.circle_points.pop_last()
                    p2 = self.circle_points.last()
                    self._perm -= Snippet(p2, p1).clever_dist(self.r)
                    p1 = self.circle_points.pop_last()
                    p2 = self.circle_points.last()
                    self._perm -= Snippet(p2, p1).clever_dist(self.r)
                else:
                    p1 = self.circle_points.pop_last()
                    p2 = self.circle_points.pop_last()
                    self._perm -= Snippet(p2, p1).clever_dist(self.r)
            elif del_last == 1:
                if self.circle_points.size() > 1:
                    p1 = self.circle_points.pop_last()
                    p2 = self.circle_points.last()
                    self._perm -= Snippet(p2, p1).clever_dist(self.r)
                else:
                    self.circle_points.pop_first()

            # удаление освещённых рёбер из начала дека

            # print()
            # for p in self.circle_points.array:
            #     print(p.x, p.y, p.arc)
            # print(self._perm)
            # print()

            p = self.points.pop_first()
            # print(p.x, p.y)
            while t.is_light(p, self.points.first()):
                # print("Deleting from begin")
                self._perimeter -= p.dist(self.points.first())
                self._area += abs(R2Point.area(t, p, self.points.first()))

                if self.circle_points.array:
                    sn = Snippet(self.points.first(), p)
                    mas = sn.intersection(self.x_c, self.y_c, self.r)
                    del_first = len(mas)
                    if p in self.circle_points:
                        del_first += 1
                    if self.circle_points.size() > 2:
                        for i in range(0, del_first):
                            p1 = self.circle_points.pop_first()
                            p2 = self.circle_points.first()
                            self._perm -= (Snippet(p1, p2).
                                           clever_dist(self.r))
                    elif self.circle_points.size() == 2:
                        p1 = self.circle_points.pop_first()
                        p2 = self.circle_points.pop_first()
                        self._perm -= (Snippet(p2, p1).
                                       clever_dist(self.r))
                        self._perm -= (Snippet(p1, p2).
                                       clever_dist(self.r))
                        if self._perm < 0:
                            self._perm = 0.0
                    else:
                        self.circle_points.pop_first()
                p = self.points.pop_first()
            self.points.push_first(p)

            # print()
            # for p in self.circle_points.array:
            #     print(p.x, p.y, p.arc)
            # print(self._perm)
            # print()

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            # print(p.x, p.y)
            while t.is_light(self.points.last(), p):
                # print("Deleting from end")
                self._perimeter -= p.dist(self.points.last())
                self._area += abs(R2Point.area(t, p, self.points.last()))

                if self.circle_points.array:
                    sn = Snippet(p, self.points.last())
                    mas = sn.intersection(self.x_c, self.y_c, self.r)
                    del_last = len(mas)
                    if p in self.circle_points:
                        del_last += 1

                    if self.circle_points.size() > 2:
                        for i in range(0, del_last):
                            p1 = self.circle_points.pop_last()
                            p2 = self.circle_points.last()
                            self._perm -= (Snippet(p2, p1).
                                           clever_dist(self.r))
                    elif self.circle_points.size() == 2:
                        p1 = self.circle_points.pop_last()
                        p2 = self.circle_points.pop_last()
                        self._perm -= (Snippet(p2, p1).
                                       clever_dist(self.r))
                        self._perm -= (Snippet(p1, p2).
                                       clever_dist(self.r))
                        if self._perm < 0:
                            self._perm = 0.0
                    else:
                        self.circle_points.pop_last()

                p = self.points.pop_last()
            self.points.push_last(p)

            # print()
            # for p in self.circle_points.array:
            #     print(p.x, p.y, p.arc)
            # print(self._perm)
            # print()

            # добавление двух новых рёбер
            self._perimeter += (t.dist(self.points.first()) +
                                t.dist(self.points.last()))
            if self.circle_points.array:
                sn1 = Snippet(self.points.first(), t)
                mas1 = sn1.intersection(self.x_c, self.y_c, self.r)
                sn2 = Snippet(t, self.points.last())
                mas2 = sn2.intersection(self.x_c, self.y_c, self.r)

                for x in mas1:
                    self._perm += Snippet(
                        x, self.circle_points.first()).clever_dist(self.r)
                    self.circle_points.push_first(x)

                if ((t.x - self.x_c) ** 2 + (t.y - self.y_c) ** 2
                        <= self.r * self.r):
                    fir = self.points.first()
                    if ((t.x - self.x_c) ** 2 + (t.y - self.y_c) ** 2
                            == self.r * self.r and
                            (fir.x - self.x_c) ** 2 + (fir.y - self.y_c) ** 2
                            > self.r * self.r):
                        t.arc = True
                    fir = self.points.last()
                    if ((t.x - self.x_c) ** 2 + (t.y - self.y_c) ** 2
                            == self.r * self.r and
                            (fir.x - self.x_c) ** 2 + (fir.y - self.y_c) ** 2
                            > self.r * self.r):
                        t.arc = True
                    if mas1:
                        t.arc = False
                    self._perm += Snippet(
                        t, self.circle_points.first()).clever_dist(self.r)
                    self.circle_points.push_first(t)

                for x in mas2:
                    self._perm += Snippet(
                        x, self.circle_points.first()).clever_dist(self.r)
                    self.circle_points.push_first(x)

                ls = self.circle_points.last()
                if ((ls.x - self.x_c) ** 2 + (ls.y - self.y_c) ** 2
                        == self.r * self.r):
                    if mas2 and not mas2[0].contact:
                        ls.arc = False
                    else:
                        if ((t.x - self.x_c) ** 2 + (t.y - self.y_c) ** 2
                                <= self.r * self.r and
                                ls == self.points.last()):
                            ls.arc = False
                        else:
                            ls.arc = True

                self._perm += Snippet(
                    self.circle_points.last(),
                    self.circle_points.first()).clever_dist(self.r)
            else:
                if ((t.x - self.x_c) ** 2 + (t.y - self.y_c) ** 2
                        <= self.r * self.r):
                    if ((t.x - self.x_c) ** 2 + (t.y - self.y_c) ** 2
                            == self.r * self.r):
                        t.arc = True
                    self.circle_points.push_first(t)
                for x in (Snippet(self.points.first(), t).
                          intersection(self.x_c, self.y_c, self.r)):
                    self.circle_points.push_first(x)
                for x in (Snippet(t, self.points.last()).
                          intersection(self.x_c, self.y_c, self.r)):
                    t.arc = False
                    self.circle_points.push_last(x)

                for i in range(0, self.circle_points.size() - 1):
                    p1 = self.circle_points.array[i]
                    p2 = self.circle_points.array[i + 1]
                    self._perm += Snippet(p1, p2).clever_dist(self.r)

                if self.circle_points.size() > 1:
                    p1 = self.circle_points.last()
                    p2 = self.circle_points.first()
                    self._perm += Snippet(p1, p2).clever_dist(self.r)
            self.points.push_first(t)
            if (self._perm < 0.05 or
                    all(p.arc for p in self.circle_points.array)):
                self._perm = 0.0
            if all((p.x - self.x_c) ** 2 + (p.y - self.y_c) ** 2 <= self.r ** 2
                   for p in self.points.array):
                self._perm = self._perimeter

        return self


if __name__ == "__main__":  # pragma: no cover
    f = Void(0, 0, 1)
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)
