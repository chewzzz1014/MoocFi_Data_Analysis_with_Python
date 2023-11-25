# TODO
def detect_ranges(L):
    sorted_L = sorted(L)
    pair_begin = 0
    pair_end = 0
    for i in range(1, len(sorted_L)):
        if pair_begin == 0:
           pass

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
