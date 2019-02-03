import numbers
import numpy
import scipy.signal

class TransferFunction(scipy.signal.TransferFunction, scipy.signal.lti):
    def __neg__(self):
        return TransferFunction(-self.num, self.den)

    def __add__(self, rhs):
        if isinstance(rhs, numbers.Number):
            return TransferFunction(numpy.polyadd(self.num, self.den * rhs), self.den)
        if isinstance(rhs, scipy.signal.TransferFunction):
            numer = numpy.polyadd(numpy.polymul(self.num, rhs.den), numpy.polymul(self.den, rhs.num))
            denom = numpy.polymul(self.den, rhs.den)
            return TransferFunction(numer, denom)
        raise TypeError

    def __sub__(self, rhs):
        if isinstance(rhs, numbers.Number):
            return TransferFunction(numpy.polyadd(self.num,-self.den * rhs), self.den)
        if isinstance(rhs, scipy.signal.TransferFunction):
            numer = numpy.polyadd(numpy.polymul(self.num, rhs.den), -numpy.polymul(self.den, rhs.num))
            denom = numpy.polymul(self.den, rhs.den)
            return TransferFunction(numer, denom)
        raise TypeError

    def __rsub__(self, lhs):
        if isinstance(lhs, numbers.Number):
            return TransferFunction(numpy.polyadd(-self.num, self.den * lhs), self.den)
        if isinstance(lhs, scipy.signal.TransferFunction):
            numer = numpy.polyadd(numpy.polymul(lhs.num, self.den), -numpy.polymul(self.num, lhs.den))
            denom = numpy.polymul(self.den, lhs.den)
            return TransferFunction(numer, denom)
        raise TypeError

    def __mul__(self, rhs):
        if isinstance(rhs, numbers.Number):
            return TransferFunction(self.num * rhs, self.den)
        if isinstance(rhs, scipy.signal.TransferFunction):
            numer = numpy.polymul(self.num, rhs.num)
            denom = numpy.polymul(self.den, rhs.den)
            return TransferFunction(numer, denom)
        raise TypeError

    def __div__(self, rhs):
        if isinstance(rhs, numbers.Number):
            return TransferFunction(self.num, self.den * rhs)
        if isinstance(rhs, scipy.signal.TransferFunction):
            numer = numpy.polymul(self.num, rhs.den)
            denom = numpy.polymul(self.den, rhs.num)
            return TransferFunction(numer, denom)
        raise TypeError

    def __rdiv__(self, lhs):
        if isinstance(lhs, numbers.Number):
            return TransferFunction(lhs * self.den, self.num)
        if isinstance(lhs, scipy.signal.TransferFunction):
            numer = numpy.polymul(self.den, lhs.num)
            denom = numpy.polymul(self.num, lhs.den)
            return TransferFunction(numer, denom)
        raise TypeError

    def __pow__(self, rhs):
        if isinstance(rhs, numbers.Integral) and rhs >= 0:
            numer = numpy.polynomial.polynomial.polypow(self.num[::-1], rhs)
            denom = numpy.polynomial.polynomial.polypow(self.den[::-1], rhs)
            return TransferFunction(numer[::-1], denom[::-1])
        raise TypeError

    def __or__(self, rhs):
        return 1/(1/self + 1/rhs)

    __radd__ = __add__
    __rmul__ = __mul__
    __truediv__ = __div__
    __rtruediv__ = __rdiv__
    __ror__ = __or__

def Z_R(value):
    return TransferFunction([value],[1.])

def Z_C(value):
    return TransferFunction([1.],[value,0])

def Z_L(value):
    return TransferFunction([value,0.],[1.])

s = TransferFunction([1., 0], [1.])
