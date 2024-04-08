import unittest
from snippet import Snippet
from r2point import R2Point
from math import sqrt, pi


class TestSnippet(unittest.TestCase):

    def setUp(self):
        self.sn = Snippet(R2Point(0, 0), R2Point(0, 4))

    def test_length1(self):
        self.assertAlmostEqual(Snippet(R2Point(0, 0), R2Point(0, 1)).length(),
                               1.0)

    def test_length2(self):
        self.assertAlmostEqual(Snippet(R2Point(0, 0), R2Point(1, 1)).length(),
                               2)

    def test_arc_length1(self):
        self.assertAlmostEqual(Snippet(R2Point(1, 0),
                                       R2Point(0, 1)).arc_length(1), pi / 2)

    def test_arc_length2(self):
        self.assertAlmostEqual(Snippet(R2Point(-1, 0),
                                       R2Point(0, -1)).arc_length(1), pi / 2)

    def test_clever_dist1(self):
        self.assertAlmostEqual(Snippet(R2Point(1, 0),
                                       R2Point(0, 1)).clever_dist(1), sqrt(2))

    def test_clever_dist2(self):
        self.assertAlmostEqual(Snippet(R2Point(1, 0, arc=True),
                                       R2Point(0, 1,))
                               .clever_dist(1), pi / 2)

    def test_intersection1(self):
        self.assertFalse(self.sn.intersection(2, -1, 1))

    def test_intersection2(self):
        self.assertAlmostEqual(self.sn.intersection(1, 1, 1)[0].x, 0)
        self.assertAlmostEqual(self.sn.intersection(1, 1, 1)[0].y, 1)

    def test_intersection3(self):
        self.assertAlmostEqual(self.sn.intersection(0, 0, 1)[0].x, 0)
        self.assertAlmostEqual(self.sn.intersection(0, 0, 1)[0].y, 1)

    def test_intersection4(self):
        self.assertAlmostEqual(self.sn.intersection(0, 2, 1)[0].x, 0)
        self.assertAlmostEqual(self.sn.intersection(0, 2, 1)[0].y, 1)
        self.assertAlmostEqual(self.sn.intersection(0, 2, 1)[1].x, 0)
        self.assertAlmostEqual(self.sn.intersection(0, 2, 1)[1].y, 3)

    def test_intersection5(self):
        self.assertAlmostEqual(self.sn.intersection(0, 4, 1)[0].x, 0)
        self.assertAlmostEqual(self.sn.intersection(0, 4, 1)[0].y, 3)

    def test_intersection6(self):
        self.assertFalse(self.sn.intersection(0, 6, 1))

    def test_intersection7(self):
        self.assertFalse(self.sn.intersection(1, 6, 1))
