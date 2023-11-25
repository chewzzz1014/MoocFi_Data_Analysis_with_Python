#!/usr/bin/env python3

def reverse_dictionary(d):
    results = {}
    for k,v in d.items():
        print(v)
        for word in v:
            if word in results:
                results[word].append(k)
            else:
                results[word] = [k]
    return results

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
