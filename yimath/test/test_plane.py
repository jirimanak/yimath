import unittest
from yimath.vector import Vector
from yimath.point import Point
from yimath.plane import Plane


class TestPlane(unittest.TestCase):

    def test_distance_form_plane(self):

        p0 = [3, -6, -1]
        p1 = [25, 30, 3]
        p2 = [-10, 40, 80]

        v0 = [40, 40, 40]
        v1 = [-40, -40, -40]

        yif_p0 = Point.from_float_array(p0)
        yif_p1 = Point.from_float_array(p1)
        yif_p2 = Point.from_float_array(p2)
        yif_v0 = Point.from_float_array(v0)
        yif_v1 = Point.from_float_array(v1)

        pp = Plane.create_from_3points([yif_p0, yif_p1, yif_p2])

        dist = pp.point_plane_distance(yif_v0)
        print("dist = ", dist)
        self.assertAlmostEqual(dist, 21.452232579, 8)
        dist = pp.point_plane_distance(yif_v1)
        print("dist = ", dist)
        self.assertAlmostEqual(dist, -31.274805223, 8)

