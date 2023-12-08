#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    results = []
    m = a.shape[1]
    for row in range(0,a.shape[0]):
        results.append(a[row,:].reshape(1,m))
    return results

def get_column_vectors(a):
    results = []
    n = a.shape[0]
    a = a.transpose()
    for col in range(0,a.shape[0]):
        results.append(a[col,:].reshape(n,1))
    return results

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
