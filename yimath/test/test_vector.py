import unittest
from yimath.vector import Vector
from yimath.point import Point



class TestVector(unittest.TestCase):

    def test_vector_magnitude(self):

        p0 = Point.from_float(-14.7, 26.4, 18.2)
        p1 = Point.from_float(26.47, 76.42, 108.2)

        vec = Vector.create_from_points(p0, p1)

        print(vec)
        self.assertAlmostEqual(41.17, float(vec.a), 2)
        self.assertAlmostEqual(50.02, float(vec.b), 2)
        self.assertAlmostEqual(90.00, float(vec.c), 2)

        mag = vec.magnitude()
        print(mag)
        self.assertAlmostEqual(110.891700771519, float(mag), 12)

        vec = Vector.from_float(0.0027, 10705, 90.00004)
        mag = vec.magnitude()
        self.assertAlmostEqual(10705.378321535736, float(mag), 12)

    def test_vector_dot(self):

        v0 = Vector.from_float(-14.7, 26.4, 18.2)
        v1 = Vector.from_float(26.47, 76.42, 108.2)

        vec_dot = v0.dot(v1)
        print(vec_dot)
        self.assertAlmostEqual(3597.619, float(vec_dot), 12)


    def test_cross_product(self):

        v0 = Vector.from_float(-14.7, 26.4, 18.2)
        v1 = Vector.from_float(26.47, 76.42, 108.2)

        vec_cross = v0.cross(v1)
        # print(vec_cross)

        self.assertAlmostEqual(1465.636, vec_cross.a)
        self.assertAlmostEqual(2072.294, vec_cross.b)
        self.assertAlmostEqual(-1822.182, vec_cross.c)

        v0 = Vector.from_float(-1, -2, 3)
        v1 = Vector.from_float(4, 0, -8)

        vec_cross = v0.cross(v1)
        # print(vec_cross)

        self.assertAlmostEqual(16, vec_cross.a)
        self.assertAlmostEqual(4, vec_cross.b)
        self.assertAlmostEqual(8, vec_cross.c)

