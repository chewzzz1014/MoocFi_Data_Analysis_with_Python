#!/usr/bin/env python3

def extract_numbers(s):
    results = []
    for x in s.split():
        try:
            results.append(int(x))
        except Exception:
            try:
                results.append(float(x))
            except Exception:
                continue
    return results


def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
