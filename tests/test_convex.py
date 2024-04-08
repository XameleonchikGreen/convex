import unittest
from math import sqrt, pi
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon


class TestVoid(unittest.TestCase):

    # Инициализация (выполняется для каждого из тестов класса)
    def setUp(self):
        self.f = Void(0, 0, 1)

    # Нульугольник является фигурой
    def test_figure(self):
        self.assertIsInstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Void (нульугольник)
    def test_void(self):
        self.assertIsInstance(self.f, Void)

    # Периметр нульугольника нулевой
    def test_perimeter(self):
        self.assertEqual(self.f.perimeter(), 0.0)

    # Площадь нульугольника нулевая
    def test_area(self):
        self.assertEqual(self.f.area(), 0.0)

    # При добавлении точки нульугольник превращается в одноугольник
    def test_add(self):
        self.assertIsInstance(self.f.add(R2Point(0.0, 0.0)), Point)

    # У нульугольника нет периметра в окружности
    def test_length(self):
        self.assertEqual(self.f.length(), 0)


class TestPoint(unittest.TestCase):

    # Инициализация (выполняется для каждого из тестов класса)
    def setUp(self):
        self.f = Point(R2Point(0.0, 0.0), 0, 0, 1)

    # Одноугольник является фигурой
    def test_figure(self):
        self.assertIsInstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Point (одноугольник)
    def test_point(self):
        self.assertIsInstance(self.f, Point)

    # Периметр одноугольника нулевой
    def test_perimeter(self):
        self.assertEqual(self.f.perimeter(), 0.0)

    # Площадь одноугольника нулевая
    def test_area(self):
        self.assertEqual(self.f.area(), 0.0)

    # При добавлении точки одноугольник может не измениться
    def test_add1(self):
        self.assertIs(self.f.add(R2Point(0.0, 0.0)), self.f)

    # При добавлении точки одноугольник может превратиться в двуугольник
    def test_add2(self):
        self.assertIsInstance(self.f.add(R2Point(1.0, 0.0)), Segment)

    # У одноугольника нет периметра в окружности
    def test_length(self):
        self.assertEqual(self.f.length(), 0)


class TestSegment(unittest.TestCase):

    # Инициализация (выполняется для каждого из тестов класса)
    def setUp(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0), 0, 0, 0.5)

    # Двуугольник является фигурой
    def test_figure(self):
        self.assertIsInstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Segment (двуугольник)
    def test_segment(self):
        self.assertIsInstance(self.f, Segment)

    # Периметр двуугольника равен удвоенной длине отрезка
    def test_perimeter(self):
        self.assertAlmostEqual(self.f.perimeter(), 2.0)

    # Площадь двуугольника нулевая
    def test_area(self):
        self.assertEqual(self.f.area(), 0.0)

    # При добавлении точки двуугольник может не измениться
    def test_add1(self):
        self.assertIs(self.f.add(R2Point(0.5, 0.0)), self.f)

    # Он не изменяется в том случае, когда добавляемая точка совпадает
    # с одним из концов отрезка
    def test_add2(self):
        self.assertIs(self.f.add(R2Point(0.0, 0.0)), self.f)

    # При добавлении точки правее двуугольник может превратиться в другой
    # двуугольник
    def test_add3(self):
        self.assertIsInstance(self.f.add(R2Point(2.0, 0.0)), Segment)

    # При добавлении точки левее двуугольник может превратиться в другой
    # двуугольник
    def test_add4(self):
        self.assertIsInstance(self.f.add(R2Point(-1.0, 0.0)), Segment)

    # При добавлении точки двуугольник может превратиться в треугольник
    def test_add5(self):
        self.assertIsInstance(self.f.add(R2Point(0.0, 1.0)), Polygon)

    def test_length1(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0), 0, 0, 0.5)
        self.assertEqual(self.f.length(), 0.5)

    def test_length2(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0), 1, 0, 0.5)
        self.assertEqual(self.f.length(), 0.5)

    def test_length3(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0), 0, 0, 2)
        self.assertEqual(self.f.length(), 1)

    def test_length4(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0), 2, 2, 1)
        self.assertEqual(self.f.length(), 0)

    def test_length5(self):
        self.f = Segment(R2Point(-2, 0), R2Point(2, 0), 0, 0, 1)
        self.assertEqual(self.f.length(), 2 + pi)

    def test_length6(self):
        self.f = Segment(R2Point(-3, 0), R2Point(-3, 3), 0, 0, 3)
        self.assertEqual(self.f.length(), 0.0)

    def test_length7(self):
        self.f = Segment(R2Point(-3, -3), R2Point(0, -3), 0, 0, 3)
        self.assertEqual(self.f.length(), 0.0)


class TestPolygon(unittest.TestCase):

    # Инициализация (выполняется для каждого из тестов класса)
    def setUp(self):
        self.a = R2Point(0.0, 0.0)
        self.b = R2Point(1.0, 0.0)
        self.c = R2Point(0.0, 1.0)
        self.f = Polygon(self.a, self.b, self.c, 0, 0, 1)

    # Многоугольник является фигурой
    def test_figure(self):
        self.assertIsInstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Polygon (многоугольник)
    def test_polygon1(self):
        self.assertIsInstance(self.f, Polygon)

    # Изменение порядка точек при создании объекта всё равно порождает Polygon
    def test_polygon2(self):
        self.f = Polygon(self.b, self.a, self.c, 0, 0, 1)
        self.assertIsInstance(self.f, Polygon)

    # Изменение количества вершин многоугольника
    #   изначально их три
    def test_vertexes1(self):
        self.assertEqual(self.f.points.size(), 3)

    #   добавление точки внутрь многоугольника не меняет их количества
    def test_vertexes2(self):
        self.assertEqual(self.f.add(R2Point(0.1, 0.1)).points.size(), 3)

    #   добавление другой точки может изменить их количество
    def test_vertexes3(self):
        self.assertEqual(self.f.add(R2Point(1.0, 1.0)).points.size(), 4)

    #   изменения выпуклой оболочки могут и уменьшать их количество
    def test_vertexes4(self):
        d = R2Point(0.4, 1.0)
        e = R2Point(1.0, 0.4)
        f = R2Point(0.4, 1.0)
        g = R2Point(0.4, 1.0)
        self.assertEqual(self.f.add(d).add(e).add(f).add(g).points.size(), 5)
        self.assertEqual(self.f.add(R2Point(2.0, 2.0)).points.size(), 4)

    # Изменение периметра многоугольника
    #   изначально он равен сумме длин сторон
    def test_perimeter1(self):
        self.assertAlmostEqual(self.f.perimeter(), 2.0 + sqrt(2.0))

    #   добавление точки может его изменить
    def test_perimeter2(self):
        self.assertAlmostEqual(self.f.add(R2Point(1.0, 1.0)).perimeter(), 4.0)

    # Изменение площади многоугольника
    #   изначально она равна (неориентированной) площади треугольника
    def test_area1(self):
        self.assertAlmostEqual(self.f.area(), 0.5)

    #   добавление точки может увеличить площадь
    def test_area2(self):
        self.assertAlmostEqual(self.f.add(R2Point(1.0, 1.0)).area(), 1.0)

    def test_length1(self):
        self.assertAlmostEqual(self.f.length(), 2+sqrt(2))

    def test_length2(self):
        self.a = R2Point(0.0, 0.0)
        self.b = R2Point(1.0, 0.0)
        self.c = R2Point(0.0, 1.0)
        self.f = Polygon(self.a, self.b, self.c, 1, 0, 1)
        self.assertAlmostEqual(self.f.length(), 2.81256441)

    def test_length3(self):
        self.a = R2Point(0.0, 0.0)
        self.b = R2Point(1.0, 0.0)
        self.c = R2Point(0.0, 1.0)
        self.f = Polygon(self.a, self.b, self.c, 0, 0, 0.5)
        self.assertAlmostEqual(self.f.length(),  1.7307055, 1)

    def test_length4(self):
        self.a = R2Point(0.0, 0.0)
        self.b = R2Point(1.0, 0.0)
        self.c = R2Point(0.0, 1.0)
        self.f = Polygon(self.a, self.b, self.c, 2, 2, 1)
        self.assertAlmostEqual(self.f.length(), 0)

    def test_length5(self):
        self.a = R2Point(0.0, 3)
        self.b = R2Point(-2.0, -1.5)
        self.c = R2Point(2.0, -1.5)
        self.f = Polygon(self.b, self.a, self.c, 0, 0, 2)
        self.assertAlmostEqual(self.f.length(), 12.55023811)

    def test_length6(self):
        self.a = R2Point(0.0, 3)
        self.b = R2Point(-2.0, 0)
        self.c = R2Point(0, 0)
        self.f = Polygon(self.c, self.b, self.a, 0, 0, 2)
        self.assertAlmostEqual(self.f.length(),  7.13650828)

    def test_length7(self):
        self.a = R2Point(0.0, 0.0)
        self.b = R2Point(1.0, 0.0)
        self.c = R2Point(0.0, 1.0)
        self.f = Polygon(self.a, self.b, self.c, 0, 0, 1)
        self.f.add(R2Point(0, 2))
        self.assertAlmostEqual(self.f.length(), 3.574080274)

    def test_length8(self):
        self.a = R2Point(0.0, 0.0)
        self.b = R2Point(1.0, 0.0)
        self.c = R2Point(0.0, 1.0)
        self.f = Polygon(self.a, self.b, self.c, 0, 0, 1)
        self.f.add(R2Point(2, 0))
        self.assertAlmostEqual(self.f.length(),    3.55975075)

    def test_length9(self):
        self.a = R2Point(0.0, 0.0)
        self.b = R2Point(1.0, 0.0)
        self.c = R2Point(0.0, 1.0)
        self.f = Polygon(self.a, self.b, self.c, 0, 0, 1)
        self.f.add(R2Point(2, 0))
        self.assertAlmostEqual(self.f.length(),  3.55975075)

    def test_length10(self):
        self.a = R2Point(0.0, 3)
        self.b = R2Point(-2.0, 0)
        self.c = R2Point(0, 0)
        self.f = Polygon(self.c, self.b, self.a, 0, 0, 2)
        self.f.add(R2Point(3, 0))
        self.assertAlmostEqual(self.f.length(),   9.680244924)

    def test_length11(self):
        self.a = R2Point(0.0, 3)
        self.b = R2Point(-2.0, -1.5)
        self.c = R2Point(2.0, -1.5)
        self.f = Polygon(self.b, self.a, self.c, 0, 0, 2)
        self.f.add(R2Point(0, -2))
        self.assertAlmostEqual(self.f.length(),  12.51449331)

    def test_length12(self):
        self.a = R2Point(0.0, 1)
        self.b = R2Point(1.0, 0)
        self.c = R2Point(-1.0, 0)
        self.f = Polygon(self.b, self.a, self.c, 0, 0, 2)
        self.f.add(R2Point(0, -3))
        self.f.add(R2Point(-3, 0))
        self.f.add(R2Point(3, 0))
        self.assertAlmostEqual(self.f.length(),  8.201367939)

    def test_length13(self):
        self.a = R2Point(0.0, 0)
        self.b = R2Point(0, -1)
        self.c = R2Point(-2.0, 0)
        self.f = Polygon(self.b, self.a, self.c, 0, 0, 2)
        self.f.add(R2Point(-2, -2))
        self.f.add(R2Point(-3, -4))
        self.f.add(R2Point(-5, -5))
        self.f.add(R2Point(-5, 5))
        self.f.add(R2Point(5, 5))
        self.f.add(R2Point(5, -5))
        self.assertAlmostEqual(self.f.length(),  0.0)

    def test_length14(self):
        self.a = R2Point(-3.0, 3)
        self.b = R2Point(-3, -3)
        self.c = R2Point(0, 0)
        self.f = Polygon(self.b, self.a, self.c, 3, 3, 3)
        self.f.add(R2Point(3, 1))
        self.assertAlmostEqual(self.f.length(), 6.78208884)

    def test_length15(self):
        self.a = R2Point(-3.0, 3)
        self.b = R2Point(-3, -3)
        self.c = R2Point(0, 0)
        self.f = Polygon(self.b, self.a, self.c, 3, 3, 3)
        self.f.add(R2Point(3, 0))
        self.assertAlmostEqual(self.f.length(), 5.465167227)

    def test_length16(self):
        self.a = R2Point(-4, 1)
        self.b = R2Point(2, 1)
        self.c = R2Point(-1, 6)
        self.f = Polygon(self.b, self.a, self.c, -1, -1, 3)
        self.g = Segment(self.a, self.b, -1, -1, 3)
        self.assertAlmostEqual(self.f.length(), self.g.length())

    def test_length17(self):
        self.a = R2Point(-0.5, 0)
        self.b = R2Point(0.5, 0)
        self.c = R2Point(0, -0.5)
        self.f = Polygon(self.b, self.a, self.c, 0, 0, 1)
        self.f.add(R2Point(0, 0.5))
        self.f.add(R2Point(-1, 0))
        self.f.add(R2Point(1, 0))
        self.f.add(R2Point(0, 1))
        self.f.add(R2Point(0, -1))
        self.assertAlmostEqual(self.f.length(), 4*sqrt(2))

    def test_length18(self):
        self.a = R2Point(0, 0)
        self.b = R2Point(4, 0)
        self.c = R2Point(0, -2)
        self.f = Polygon(self.b, self.a, self.c, 2, 2, 2)
        self.f.add(R2Point(2, 2))
        self.f.add(R2Point(2, 6))
        self.assertAlmostEqual(self.f.length(),  15.43361145)

    def test_length19(self):
        self.a = R2Point(0, 1)
        self.b = R2Point(4, 1)
        self.c = R2Point(0, -2)
        self.f = Polygon(self.b, self.a, self.c, 2, 2, 2)
        self.f.add(R2Point(4, -2))
        self.f.add(R2Point(2, -3))
        self.f.add(R2Point(2, 2))
        self.f.add(R2Point(2, 4))
        self.assertAlmostEqual(self.f.length(),  11.360304853)

    def test_length20(self):
        self.a = R2Point(-3, -3)
        self.b = R2Point(3, -3)
        self.c = R2Point(0, -2)
        self.f = Polygon(self.b, self.a, self.c, 0, 0, 2)
        self.f.add(R2Point(0, 0))
        self.assertAlmostEqual(self.f.length(),  4 + pi)

    def test_length21(self):
        self.a = R2Point(-3, -3)
        self.b = R2Point(3, -3)
        self.c = R2Point(0, -2)
        self.f = Polygon(self.a, self.b, self.c, 0, 0, 2)
        self.f.add(R2Point(0, 0))
        self.assertAlmostEqual(self.f.length(),  4 + pi)

    def test_length22(self):
        self.a = R2Point(5, 5)
        self.b = R2Point(3, -1)
        self.c = R2Point(-1, 3)
        self.f = Polygon(self.a, self.b, self.c, 0, 0, 2)
        self.f.add(R2Point(0, 0))
        self.f.add(R2Point(2, -2))
        self.f.add(R2Point(-2, 2))
        self.assertAlmostEqual(self.f.length(),  4 + 2*pi)

    def test_length23(self):
        self.a = R2Point(3, -3)
        self.b = R2Point(-3, -3)
        self.c = R2Point(0, -2)
        self.f = Polygon(self.a, self.b, self.c, 0, 0, 2)
        self.f.add(R2Point(0, 0))
        self.f.add(R2Point(2, 0))
        self.assertAlmostEqual(self.f.length(),  4 + 3*pi/2, 4)

    def test_length24(self):
        self.a = R2Point(0, -3)
        self.b = R2Point(-3, -3)
        self.c = R2Point(-3, 0)
        self.f = Polygon(self.a, self.b, self.c, 0, 0, 3)
        self.f.add(R2Point(-3, 3))
        self.f.add(R2Point(3, -3))
        self.f.add(R2Point(3, 0))
        self.f.add(R2Point(0, 3))
        self.assertAlmostEqual(self.f.length(),  3*sqrt(2) + 9*pi/2)
