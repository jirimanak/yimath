import yimath.float as yif
import mpmath


class Point:

    def __init__(self, point_params):
        self._params = point_params

    @property
    def x(self):
        return self._params[0]

    @property
    def y(self):
        return self._params[1]

    @property
    def z(self):
        return self._params[2]

    @property
    def xyz(self):
        return self._params

    @staticmethod
    def from_float(fx, fy, fz):
        return Point([yif.f2yif(fx), yif.f2yif(fy), yif.f2yif(fz)])

    @staticmethod
    def from_float_array(f_array):
        return Point([yif.f2yif(f_array[0]), yif.f2yif(f_array[1]), yif.f2yif(f_array[2])])

    def __str__(self):
        s = ""
        s += "["
        s += yif.to_string(self.x) + ", "
        s += yif.to_string(self.y) + ", "
        s += yif.to_string(self.z)
        s += "]"
        return s


class HmPoint:

    def __init__(self, homo_point):
        self._params = homo_point

    @property
    def xyzw(self):
        return self._params

    def point(self):
        if mpmath.almosteq(self._params[3], mpmath.mpf(1)):
            return Point([self._params[0], self._params[1], self._params[2]])

        return Point([
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
            1
        ]

        return HmPoint(params)
