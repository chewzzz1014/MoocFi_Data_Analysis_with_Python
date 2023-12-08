#!/usr/bin/env python3

class Rational(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}/{self.y}'

    def __hash__(self):
        return self.value

    def __add__(self, value2):
        return self.value + value2

    def __sub__(self, value2):
        return self.value - value2

    def __mul__(self, value2):
        return self.value * value2

    def __truediv__(self, value2):
        return self.value / value2

    def __eq__(self, value2):
        return self.value == value2

    def __ge__(self, value2):
        return self.value >= value2

    def __le__(self, value2):
        return self.value <= value2


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