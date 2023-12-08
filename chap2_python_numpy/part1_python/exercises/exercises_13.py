#!/usr/bin/env python3

import numpy as np

def diamond(n):
    unit = np.eye(n, dtype=int)
    first_unit = np.concatenate((unit[::-1][:,:n-1],unit), axis=1)
    second_unit = np.concatenate((unit[:,:n-1],unit[::-1]), axis=1)
    return np.concatenate((first_unit[:n-1,:], second_unit))

def main():
    print(diamond(3))

if __name__ == "__main__":
    main()