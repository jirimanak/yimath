import mpmath
import yimath.base.float as yif


class Point:

    def __init__(self, mpf_x, mpf_y, mpf_z):

        self._mpf_x = mpf_x
        self._mpf_y = mpf_y
        self._mpf_z = mpf_z

    @staticmethod
    def from_float(fx, fy, fz):
        return Point(yif.f2yif(fx), yif.f2yif(fy), yif.f2yif(fz))


