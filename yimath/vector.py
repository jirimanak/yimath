from yimath.point import Point
import yimath.float as yif
import mpmath


class Vector(Point):

    def __init__(self, vector_params):
        Point.__init__(self, vector_params)

    @staticmethod
    def create_from_points(yif_point0: Point, yif_point1: Point):
        a = mpmath.fsub(yif_point1.x, yif_point0.x)
        b = mpmath.fsub(yif_point1.y, yif_point0.y)
        c = mpmath.fsub(yif_point1.z, yif_point0.z)
        return Vector([a, b, c])

    @staticmethod
    def convert_point(p: Point):
        return Vector(p.xyz)

    @property
    def abc(self):
        return self._params

    @property
    def a(self):
        return self._params[0]

    @property
    def b(self):
        return self._params[1]

    @property
    def c(self):
        return self._params[2]

    @staticmethod
    def from_float(fx, fy, fz):
        return Vector([yif.f2yif(fx), yif.f2yif(fy), yif.f2yif(fz)])

    def magnitude(self):
        p = mpmath.fdot(self.abc, self.abc)
        return mpmath.sqrt(p)

    def dot(self, other_vector):
        return mpmath.fdot(self.abc, other_vector.abc)

    def add(self, other_vector):
        a = mpmath.fadd(self.x, other_vector.x)
        b = mpmath.fadd(self.y, other_vector.y)
        c = mpmath.fadd(self.z, other_vector.z)
        return Vector([a, b, c])

    def sub(self, other_vector):
        a = mpmath.fsub(self.x, other_vector.x)
        b = mpmath.fsub(self.y, other_vector.y)
        c = mpmath.fsub(self.z, other_vector.z)
        return Vector([a, b, c])

    def times_scalar(self, yif_float):
        a = mpmath.fmul(self.x, yif_float)
        b = mpmath.fmul(self.y, yif_float)
        c = mpmath.fmul(self.z, yif_float)
        return Vector([a, b, c])

    def move_point(self, point):
        '''
        moves point in the direction and magnitude of this vector
        :param point: point to move yimath.Point
        :return: yipmath.Point
        '''
        a = mpmath.fadd(self.x, point.x)
        b = mpmath.fadd(self.y, point.y)
        c = mpmath.fadd(self.z, point.z)
        return Point([a, b, c])

    def cross(self, other_vector):
        # source https://en.wikipedia.org/wiki/Cross_product
        a = self
        b = other_vector

        a2b3 = mpmath.fmul(a.y, b.z)
        a3b2 = mpmath.fmul(a.z, b.y)
        a3b1 = mpmath.fmul(a.z, b.x)
        a1b3 = mpmath.fmul(a.x, b.z)
        a1b2 = mpmath.fmul(a.x, b.y)
        a2b1 = mpmath.fmul(a.y, b.x)

        c1 = mpmath.fsub(a2b3, a3b2)
        c2 = mpmath.fsub(a3b1, a1b3)
        c3 = mpmath.fsub(a1b2, a2b1)

        return Vector([c1, c2, c3])

    @staticmethod
    def cross_product(a, b):
        a2b3 = mpmath.fmul(a.y, b.z)
        a3b2 = mpmath.fmul(a.z, b.y)
        a3b1 = mpmath.fmul(a.z, b.x)
        a1b3 = mpmath.fmul(a.x, b.z)
        a1b2 = mpmath.fmul(a.x, b.y)
        a2b1 = mpmath.fmul(a.y, b.x)

        c1 = mpmath.fsub(a2b3, a3b2)
        c2 = mpmath.fsub(a3b1, a1b3)
        c3 = mpmath.fsub(a1b2, a2b1)

        return Vector([c1, c2, c3])


class HmVector:

    def __init__(self, homo_vector):
        self._params = homo_vector

    def point(self):
        if mpmath.almosteq(self._params[3], mpmath.mpf(1)):
            return Point([self._params[0], self._params[1], self._params[2]])

        return Point([
            mpmath.fdiv(self._params[0], self._params[3]),
            mpmath.fdiv(self._params[1], self._params[3]),
            mpmath.fdiv(self._params[2], self._params[3])
            ]
        )

    @property
    def xyzw(self):
        return self._params

    def vector(self):

        return Vector([
            mpmath.fdiv(self._params[0], self._params[3]),
            mpmath.fdiv(self._params[1], self._params[3]),
            mpmath.fdiv(self._params[2], self._params[3])
            ]
        )


    @staticmethod
    def from_point(point: Point):
        params = [
            point.x,
            point.y,
            point.z,
            0
        ]

        return HmVector(params)

    @staticmethod
    def from_vector(point: Vector):
        params = [
            point.x,
            point.y,
            point.z,
            0
        ]

        return HmVector(params)

    def dot(self, other_vector):
        return mpmath.fdot(self.xyzw, other_vector.xyzw)