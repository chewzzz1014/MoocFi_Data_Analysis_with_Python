#!/usr/bin/env python3
from functools import reduce

def sum_equation(L):
    if len(L)==0:
        return '0 = 0'
    return f'{" + ".join(list(map(str,L)))} = {reduce(lambda x,y:x+y, L, 0)}'

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
