#!/usr/bin/env python3

# TODO
import re

def red_green_blue(filename="src/rgb.txt"):
    results = []
    with open(filename) as rf:
        rf.readline()
        for line in rf.readlines():
            parsed_line = line.replace('\n', '')
            found = re.findall(f"\s*(\d+){1,3}\s*([A-Za-z0-9]+)", parsed_line)
            print(found)


def main():
    red_green_blue()

if __name__ == "__main__":
    main()
