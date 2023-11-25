#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    results = []
    with open(filename) as rf:
        for line in rf:
            parsed_line = line.replace('\n', '')
            found = re.findall(r"[rwx-]*\s*\d\s*\w*\s*\w*-\w*\s*(\d+)\s*(\w{,3})\s*(\d+)\s(\d+):(\d+)\s*([A-Za-z0-9-._]+)", parsed_line)
            for t in found:
                results.append(t)
    return results

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
