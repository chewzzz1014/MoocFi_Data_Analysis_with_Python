#!/usr/bin/env python3

import sys
from functools import reduce

def file_count(filename):
    num_lines = 0
    num_words = 0
    num_chars = 0
    with open(filename) as rf:
        num_lines += len(list(rf))
        for line in rf:
            if line.replace('\n','').strip() != '':
                num_words += len(line.split())
                num_chars += sum(list(map(lambda x:len(x),line.replace('\n', '').split())))
    return (num_lines, num_words, num_chars)

def main():
    for filename in sys.argv[1:]:
        results = file_count(filename)
        print(f'{results[0]}\t{results[1]}\t{results[2]}\t{filename}')

if __name__ == "__main__":
    main()
