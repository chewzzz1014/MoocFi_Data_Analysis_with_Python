#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, pre):
        self.pre = pre
    def write(self, s):
        print(f'{self.pre}{s}')

def main():
    pass

if __name__ == "__main__":
    main()
