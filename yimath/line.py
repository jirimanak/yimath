from yimath.vector import Vector
from yimath.point import Point
from yimath.plane import Plane

import mpmath


class Line:

    def __init__(self, point_xyz, vector_abc):
        self.xyz = point_xyz
        self.abc = vector_abc

    @staticmethod
    def create_from_points(p0: Point, p1: Point):
        a_vec = Vector.create_from_points(p0, p1)
        return Line(p0, a_vec)


    @staticmethod
    def distance_from_point(l0: Point, l1: Point, p: Point):
        '''
        source: http://mathworld.wolfram.com/Point-LineDistance3-Dimensional.html
        condition: distance l0, l1 can't be zero
        :param l0:
        :param l1:
        :param p:
        :return:
        '''

        vec0 = Vector.create_from_points(l0, p)
        print("vec0", vec0 )
        vec1 = Vector.create_from_points(l1, p)
        print("vec1", vec1)

        vec2 = Vector.create_from_points(l0, l1)
        print("vec2", vec2)
        vec_cx = vec0.cross(vec1)
        print("vec_cx", vec_cx)

        num_sq = vec_cx.dot(vec_cx)
        den_sq = vec2.dot(vec2)
        print("N:", num_sq)
        print("D:", den_sq)

        dist_sq = mpmath.fdiv(num_sq, den_sq)

        return mpmath.sqrt(dist_sq)


    @staticmethod
    def distance_from_point3(l0: Point, l1: Point, p: Point):
        '''
        http://mathworld.wolfram.com/Point-LineDistance3-Dimensional.html
        :param l0:
        :param l1:
        :param p:
        :return:
        '''

        vec_v = Vector.create_from_points(l0, p)
        vec_w = Vector.create_from_points(l1, p)
        vec_x = Vector.create_from_points(l0, l1)
        c = vec_v.cross(vec_w)
        nom_sq = c.dot(c)
        den_sq = vec_x.dot(vec_x)
        dist = mpmath.sqrt(mpmath.fdiv(nom_sq, den_sq))
        return dist


    @staticmethod
    def distance_from_point4(l0: Point, l1: Point, p: Point):
        '''

        :param l0:
        :param l1:
        :param p:
        :return:
        '''
        vec_nv = Vector.create_from_points(l0, l1)
        plane0 = Plane.create_from_point_vector(vec_nv, p)
        plane1 = Plane.create_from_3points([l0, l1, p])
        vec_nv2 = plane1.nv.cross(plane0.nv)
        plane2 = Plane.create_from_point_vector(vec_nv2, l0)
        dist = plane2.point_plane_distance(p)
        return dist
