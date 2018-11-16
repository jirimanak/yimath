import mpmath


def f2yif(float_number):
    s = format(float_number, '.60f' )
    return mpmath.mpf(s)






