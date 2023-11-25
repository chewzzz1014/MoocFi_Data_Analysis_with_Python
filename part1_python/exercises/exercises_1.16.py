#!/usr/bin/env python3

def transform(s1, s2):
    return [x*y for x,y in zip(map(int,s1.split()), map(int, s2.split()))]

def main():
    pass

if __name__ == "__main__":
    main()