import unittest
import mpmath
from yimath.vector import Vector
from yimath.point import Point
from yimath.line import Line




class TestLine(unittest.TestCase):

    def test_point_distance(self):
        l0 = [-1000000, -1000000, 0]
        l1 = [10, 10, 0]
        p = [0, 0, 5]


        yif_l0 = Point.from_float_array(l0)
        yif_l1 = Point.from_float_array(l1)
        yif_p = Point.from_float_array(p)

        dist = Line.distance_from_point(yif_l0, yif_l1, yif_p)
        print("1:", dist)

        dist = Line.distance_from_point2(yif_l0, yif_l1, yif_p)
        print("2:", dist)

        dist = Line.distance_from_point3(yif_l0, yif_l1, yif_p)
        print("3:", dist)

        dist = Line.distance_from_point4(yif_l0, yif_l1, yif_p)
        print("4:", dist)

    def test_point_distance2(self):
        l0 = [0, 6, 12]
        l1 = [-10, 54, -89]
        p = [14, 15, 16]

        yif_l0 = Point.from_float_array(l0)
        yif_l1 = Point.from_float_array(l1)
        yif_p = Point.from_float_array(p)

        dist = Line.distance_from_point(yif_l0, yif_l1, yif_p)
        print("1:", dist)

        dist = Line.distance_from_point2(yif_l0, yif_l1, yif_p)
        print("2:", dist)

        dist = Line.distance_from_point3(yif_l0, yif_l1, yif_p)
        print("3:", dist)

        dist = Line.distance_from_point4(yif_l0, yif_l1, yif_p)
        print("4:", dist)



    def test_point_distance3(self):
        l0 = [25.4925, 329.2269, 169.1376]
        l1 = [202.1582, 261.3284, 412.7597]
        p = [110755170867147.1094, -42566904002934.5469, 152731380625929.8750]

        mpmath.mp.prec = 100
        print(mpmath.mp)

        yif_l0 = Point.from_float_array(l0)
        yif_l1 = Point.from_float_array(l1)
        yif_p = Point.from_float_array(p)

        result = 42658653.78327434466453717114365169359092936

        dist = Line.distance_from_point(yif_l0, yif_l1, yif_p)
        print("1:", dist)

        dist = Line.distance_from_point3(yif_l0, yif_l1, yif_p)
        print("3:", dist)

        dist = Line.distance_from_point4(yif_l0, yif_l1, yif_p)
        print("4:", dist)

    def test_point_distance6(self):
        l0 = [-4, -5, -1]
        l1 = [-1, -4, 0]
        p = [-6, 1, 21]

        mpmath.mp.prec = 50
        print(mpmath.mp)
        dist_result = mpmath.fmul(mpmath.mpf(4), mpmath.sqrt(mpmath.mpf(30)))
        print("expected = ", dist_result)
        yif_l0 = Point.from_float_array(l0)
        yif_l1 = Point.from_float_array(l1)
        yif_p = Point.from_float_array(p)

        dist = Line.distance_from_point(yif_l0, yif_l1, yif_p)
        print("1:", dist)

        dist = Line.distance_from_point3(yif_l0, yif_l1, yif_p)
        print("3:", dist)

        dist = Line.distance_from_point4(yif_l0, yif_l1, yif_p)
        print("4:", dist)


    def test_point_distance8(self):
        l0 = [1.264231338144258, 337.7670806560546, 126.46027048778166]
        l1 = [165.5963173389248, 245.54391399241658, 4.000000000000013]
        p = [30404953447469.33, -17063259874381.307, -22657771308926.742]

        mpmath.mp.prec = 400
        print(mpmath.mp)

        yif_l0 = Point.from_float_array(l0)
        yif_l1 = Point.from_float_array(l1)
        yif_p = Point.from_float_array(p)

        result = 42658653.78327434466453717114365169359092936

        dist = Line.distance_from_point(yif_l0, yif_l1, yif_p)
        print("1:", dist)

        dist = Line.distance_from_point3(yif_l0, yif_l1, yif_p)
        print("3:", dist)

        dist = Line.distance_from_point4(yif_l0, yif_l1, yif_p)
        print("4:", dist)