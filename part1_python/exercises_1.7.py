#!/usr/bin/env python3

import math

def triangle(b,h):
    return b*h*0.5

def rectangle(w,h):
    return w*h

def circle(r):
    return math.pi * r**2

def main():
    # enter you solution here
    shape = input('Choose a shape (triangle, rectangle, circle):\n')
    while shape != '':
        if shape == 'triangle':
            base = float(input('Give base of the triangle:'))
            height = float(input('Give height of the triangle:'))
            print(f'The area is {triangle(base, height):.6f}')
        elif shape == 'rectangle':
            width = float(input('Give width of the rectangle:'))
            height = float(input('Give height of the rectangle:'))
            print(f'The area is {rectangle(width, height):.6f}')
        elif shape == 'circle':
            radius = float(input('Give radius of the circle:'))
            print(f'The area is {circle(radius):.6f}')
        else:
            print('Unknown shape!')
        shape = input('Choose a shape (triangle, rectangle, circle):\n')


if __name__ == "__main__":
    main()
