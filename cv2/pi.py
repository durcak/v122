import random
import time
import numpy as np
from decimal import Decimal, getcontext
from math    import pi


def archimedes2(_time=1., n=1000):

    # print "Calculating Pi using method of Archimedes..."
    a = 2*Decimal(3).sqrt()
    b = Decimal(3)
    n = 0

    k = 0
    start_time = time.time()

    while time.time() - start_time < _time or k < n:
        n += 1
        a = (2 * a * b) / (a + b)
        b = (a * b).sqrt()
	k += 1
    return a

def leibnitz(_time=False, n=1000):
    s = 0
    k = 0
    start_time = time.time()

    while time.time() - start_time < _time or k < n:
        s += ((-1)**k) / (2*k + 1.0)
	k += 1

    return Decimal(s * 4)


def monte_carlo(_time=False, n=1000):

    in_quarter = 0
    k          = 0
    start_time = time.time()

    while time.time() - start_time < _time or k < n:
        x, y = np.random.random(2)
        if x**2 + y**2 < 1:
            in_quarter += 1
        k += 1
    _pi = 4. * in_quarter / k
    
    return Decimal(_pi)

def error(x):
    return abs(Decimal(x) - Decimal(pi))

def str_frm(x):
    return "{0:.10f}".format(x)

if __name__ == '__main__':

    _pi = Decimal(pi)
    print "Python math module:"
    print ">>>    {}".format(_pi)

    print "Monte carlo, time: 1 sec:"
    monte_carlo = monte_carlo(_time=1)
    print ">>>    {}".format( monte_carlo )
    print "Diference: {}".format( abs(_pi - monte_carlo) )

    print "Gregory-Leibnitz, time: 1 sec:"
    leibnitz = leibnitz(_time=1)
    print ">>>    {}".format( leibnitz )
    print "Diference: {}".format( str_frm(error(leibnitz)) )

    print "Archimedes, time: 1 sec:"
    archimedes = archimedes2(_time=1)
    print ">>>    {}".format( archimedes )
    print "Diference: {}".format( abs(_pi - archimedes) )

