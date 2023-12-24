#!/usr/bin/env python3

class Rational(object):
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError('Denominator cannot be zero')
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __hash__(self):
        return self.value

    def __add__(self, value2):
        return Rational(self.numerator * value2.denominator + value2.numerator * self.denominator,
                        self.denominator * value2.denominator)

    def __sub__(self, value2):
        return Rational(self.numerator * value2.denominator - value2.numerator * self.denominator,
                        self.denominator * value2.denominator)

    def __mul__(self, value2):
        return Rational(self.numerator * value2.numerator, self.denominator * value2.denominator)

    def __truediv__(self, value2):
        if value2.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        return Rational(self.numerator * value2.denominator, self.denominator * value2.numerator)

    def __eq__(self, value2):
        return (self.numerator == value2.numerator) and (self.denominator == value2.denominator)

    def __ge__(self, value2):
        return (self.numerator * value2.denominator) >= (value2.numerator * self.denominator)

    def __gt__(self, value2):
        return (self.numerator * value2.denominator) > (value2.numerator * self.denominator)

    def __le__(self, value2):
        return (self.numerator * value2.denominator) <= (value2.numerator * self.denominator)

    def __lt__(self, value2):
        return (self.numerator * value2.denominator) < (value2.numerator * self.denominator)


def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1 * r2)
    print(r1 / r2)
    print(r1 + r2)
    print(r1 - r2)
    print(Rational(1, 2) == Rational(2, 4))
    print(Rational(1, 2) > Rational(2, 4))
    print(Rational(1, 2) < Rational(2, 4))


if __name__ == "__main__":
    main()
