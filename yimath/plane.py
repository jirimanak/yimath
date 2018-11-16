import mpmath
from yimath.point import Point
from yimath.vector import Vector
from yimath.point import HmPoint


class Plane:

    def __init__(self, plane_params):

        self._params = plane_params

    @property
    def abcd(self):
        return self._params

    @property
    def nv(self):
        return Vector(self._params[:3])

    @property
    def d(self):
        return self._params[3:]

    @staticmethod
    def create_from_point_vector(normal_vector: Vector, point: Point):
        d = normal_vector.dot(Vector.convert_point(point))
        plane_params = [normal_vector.x, normal_vector.y, normal_vector.z, mpmath.fneg(d)]
        return Plane(plane_params)


    @staticmethod
    def create_from_3points(points):
        vec_a = Vector.create_from_points(points[0], points[1])
        vec_b = Vector.create_from_points(points[0], points[2])
        normal_vector = vec_a.cross(vec_b)
        d = normal_vector.dot(Vector.convert_point(points[2]))
        plane_params = [normal_vector.a, normal_vector.b, normal_vector.c, mpmath.fneg(d)]
        return Plane(plane_params)

    def point_plane_distance(self, point: Point):
        '''
        calculates point distance from the plane
        :param point: list or numpy array
        :return: err, distance
        distance = (a*x0 + b*y0 + c*z0 + d)/ sqrt(a**2 + b**2 + c**2)
        '''

        numerator = mpmath.fdot(self.abcd, HmPoint.from_point(point).xyzw)
        denominator = mpmath.sqrt(self.nv.dot(self.nv))
        distance = numerator/denominator

        return distance
