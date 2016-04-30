from decimal   import *
from math      import log, factorial
from itertools import product

context = Context(prec=49)

def p(x, a):
# calculates x**a

    result = 1
    for i in xrange(a):
        result *= x

    return result

def gcd_modulo(a, b):

    steps = 0
    while a % b != 0:
        tmp = a
        a   = b
        b   = tmp % b

        steps +=1

    return b

def root(S, n=2, eps=0.0001):
# calculates n-th root of S with eps precision
    if n <= 1: return S
    
    #Decimal(S)

    xi_next = S
    xi = S
    
    while True:
	xi = xi_next
        xi_next = ((n-1) * xi + S/p(xi, (n-1)))/n  #Newtonova (Babylonska) metoda

	if ((xi - xi_next) < eps):
	    break

    return Decimal(xi_next)


def fraction(y):
# return y as fraction
    
    int_part = int(y)
    decimal  = str( y - int_part )[2:]
    if not decimal:
        decimal = 0
        denom   = 1
    else:
        denom   = p(10, len( decimal ))
    decimal  = int( decimal )
    numer    = int_part * denom + decimal
    modul    = gcd_modulo(numer, denom)

    return numer / modul, denom / modul



def newtons_method(x, y):

    exp, rot = fraction(y)
    result = root(x, rot)
    if result == None:
        return None
    result = p(result, exp)

    return result

def taylor_series(x, y, n=10):

    logar  = log(x)
    result = 0

    for k in xrange(n):
        result += (p(logar, k) * p(y,k)) / factorial(k)

    return Decimal( result )


if __name__ == '__main__':

    x = 255
    y = 1.5

    print "To Calculate: {0}^{1}".format(x, y)
    print "     Python:    %f" % x ** y
    print "     Taylor:    %f" % taylor_series(x, y)
    print "     Newtons:   %f" % newtons_method(x, y)  #najpomalsia metoda

    x = 255
    y = 0.5

    print "To Calculate: {0}^{1}".format(x, y)
    print "     Python:    %f" % x ** y
    print "     Taylor:    %f" % taylor_series(x, y)
    print "     Newtons:   %f" % newtons_method(x, y)
    
