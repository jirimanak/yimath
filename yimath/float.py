import mpmath


class Float:

    def __init__(self):
        self._value = mpmath.mpf(0)


def f2yif(float_number):
    s = format(float_number, '.60f' )
    return mpmath.mpf(s)


def to_string(yif):
    return mpmath.nstr(yif, 25)

