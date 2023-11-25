# module docstring
'''
to calculate hypotenuse and area of triangle
'''
from math import sqrt

def hypotenuse(x1,x2):
    '''returns the length of the hypotenuse when given the lengths of two other sides of a right-angled triangle'''
    return sqrt(x1**2+x2**2)

def area(x1,x2):
    ''' returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters.'''
    return 0.5*x1*x2