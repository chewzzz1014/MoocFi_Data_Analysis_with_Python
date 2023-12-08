#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    results = []
    for row in range(0, a.shape[0]):
        results.append(np.array(a[row,:]))
    return results

def get_columns(a):
    results = []
    a = a.transpose()
    for col in range(0, a.shape[0]):
        results.append(np.array(a[col,:]))
    return results

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()