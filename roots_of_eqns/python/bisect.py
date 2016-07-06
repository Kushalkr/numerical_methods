## module bisect
''' root = bisect(f, a, b, switch=0, epsilon = 1.0e-9)
    Finds a root of f(x) by bisection.
    The root must be bracketed in (x1, x2).
    Setting switch = 1 returns root = None if
    f(x) increases as a result of bisection
'''

from math import log, ceil

def bisect(f,x1,x2,switch=0, epsilon=1.e-9):
    f1 = f(x1)
    if f1 == 0.0 : return x1
    f2 = f(x2)
    if f2 == 0.0 : return x2

    if f1*f2 > 0.0 : print('Root is not bracketed') ; exit
    n = int(ceil(log((x2 - x1)/epsilon)/log(2.0)))
    for i in range(n):
        x3 = 0.5 * (x1 + x2); f3 = f(x3)
        if switch == 1 and (abs(f3) > abs(f1)) \
                and (abs(f3) > abs(f2)):
                    return None
        if f3 == 0.0 : return f3
        if f2 * f3 < 0.0:
            x1 = x3 ; f1 = f3
        else:
            x2 = x3 ; f2 = f3
    return (x1 + x2) / 2.0
