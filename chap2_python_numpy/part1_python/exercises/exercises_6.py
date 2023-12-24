#!/usr/bin/env python3

import sys
from functools import reduce

def file_count(filename):
    lines = []
    num_words = 0
    num_chars = 0
    with open(filename) as rf:
        lines = rf.readlines()
    for line in lines:
        words = line.split()
        num_words += len(words)
        num_chars += len(line)
    return (len(lines), num_words, num_chars)

def main():
    for filename in sys.argv[1:]:
        results = file_count(filename)
        print(f'{results[0]}\t{results[1]}\t{results[2]}\t{filename}')

if __name__ == "__main__":
    main()
