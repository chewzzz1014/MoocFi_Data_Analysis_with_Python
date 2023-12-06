#!/usr/bin/env python3

import sys
from functools import reduce
from statistics import stdev

def summary(filename):
    numbers = []
    with open(filename) as rf:
        lines = list(map(lambda x:x.replace('\n', ''),rf))
        numbers = [float(x) for x in lines if x.strip() != '' and not x.isalpha()]
    total = reduce(lambda a, b: a+b, numbers)
    avg = total/len(numbers)
    std_dev = stdev(numbers)
    return (total, avg, std_dev)

def main():
    for filename in sys.argv[1:]:
    # for filename in ['./src/example3.txt']:
        results = summary(filename)
        print(f'File: {filename} Sum: {results[0]:.6} Average: {results[1]:6} Stddev: {results[2]:.6}')


if __name__ == "__main__":
    main()
