#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    lines = []
    results = []
    with open(filename) as rf:
        rf.readline()
        lines = rf.readlines()
    for line in lines:
        # pattern = re.compile(r'(\d+)\s+(\d+)\s+(\d+)\s+(.+)$')
        match = re.match(r'(\d+)\s+(\d+)\s+(\d+)\s+(.+)$', line.replace('\n', ''))

        if match:
            red = match.group(1)
            green = match.group(2)
            blue = match.group(3)
            color_name = match.group(4).strip()

            formatted_string = f"{red}\t{green}\t{blue}\t{color_name}"
            results.append(formatted_string)
        else:
            print(line.replace('\n', ''))
    print(len(results))
    return results


def main():
    red_green_blue()

if __name__ == "__main__":
    main()
