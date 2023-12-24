#!/usr/bin/env python3

import re
from datetime import datetime


def file_listing(filename="src/listing.txt"):
    lines = []
    results = []
    with open(filename) as rf:
        lines = rf.readlines()
    for line in lines:
        parsed_line = line.replace('\n', '')
        match = re.match(r'^\s*([^\s]+)\s+(\d+)\s+([^\s]+)\s+([^\s]+)\s+(\d+)\s+([a-zA-Z]+)\s+(\d+)\s+(\d+:\d+)\s+(.*)$', parsed_line)
        if match:
            size = int(match.group(5))
            month = match.group(6)
            day = int(match.group(7))
            hour, minute = map(int, match.group(8).split(':'))
            filename = match.group(9)
            # month_number = datetime.strptime(month, '%b').month
            results.append((size, month, day, hour, minute, filename))
    return results

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
