#!/usr/bin/env python3

def find_matching(L, pattern):
    results = []
    for idx, ele in enumerate(L):
        if pattern in ele:
            results.append(idx)
    return results

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
