# Реализовать класс Rational рациональных чисел с арифметическими операциями +, -, *, /.
# Арифметика также должна работать с аргументами типа целых чисел.
# Пример использования: 4 - (Rational(1, 3)*3 + 1)/Rational(2)

from math import gcd

class Rational:
    def __init__(self, numerator, denominator=1):
        d = gcd(numerator, denominator)
        self._numerator = numerator // d
        self._denominator = denominator // d

    def __add__(self, other):
        if isinstance(other, int):
            return self.__add__(Rational(other))
        elif isinstance(other, Rational):
            new_numerator = self._numerator * other._denominator + self._denominator * other._numerator
            new_denominator = self._denominator * other._denominator
            d = gcd(new_numerator, new_denominator)
            new_numerator //= d
            new_denominator //= d
            return Rational(new_numerator, new_denominator)
        else:
            raise TypeError

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            return self.__add__(-other)
        return self.__add__(Rational(-other._numerator, other._denominator))

    def __rsub__(self, other):
        return Rational(-self._numerator, self._denominator).__add__(other)

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__mul__(Rational(other))
        elif isinstance(other, Rational):
            new_numerator = self._numerator * other._numerator
            new_denominator = self._denominator * other._denominator
            d = gcd(new_numerator, new_denominator)
            new_numerator //= d
            new_denominator //= d
            return Rational(new_numerator, new_denominator)
        else:
            raise TypeError

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return self.__mul__(Rational(1, other))
        return self.__mul__(Rational(other._denominator, other._numerator))

    def __rtruediv__(self, other):
        return Rational(self._denominator, self._numerator).__mul__(other)

    def __str__(self):
        if self._denominator == 1:
            return str(self._numerator)
        elif self._denominator == -1:
            return str(-self._numerator)
        return str(self._numerator) + '/' + str(self._denominator)
