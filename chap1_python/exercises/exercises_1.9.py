# 1.9
#!/usr/bin/env python3

def merge(L1, L2):
    results = []
    current_L1 = 0
    current_L2 = 0
    while len(results)<len(L1)+len(L2):
        if current_L1<len(L1):
            if current_L2<len(L2) and (L1[current_L1]>L2[current_L2]):
                results.append(L2[current_L2])
                current_L2 += 1
            else:
                results.append(L1[current_L1])
                current_L1 += 1
        if current_L2<len(L2):
            if current_L1<len(L1) and (L2[current_L2]>L1[current_L1]):
                results.append(L1[current_L1])
                current_L1 += 1
            else:
                results.append(L2[current_L2])
                current_L2 += 1
        print(current_L1, current_L2)
    return results

def main():
    L1 = [14, 73, 32, 63]
    L2 = [40,52, 90, 0]
    print(merge(sorted(L1), sorted(L2)))

if __name__ == "__main__":
    main()