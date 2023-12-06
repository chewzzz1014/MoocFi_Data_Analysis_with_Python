#!/usr/bin/env python3

def word_frequencies(filename):
    results = {}
    lines = []
    with open(filename) as rf:
        lines = rf.readlines()
    for line in lines:
        if line.strip() != '':
            parsed_line = line.replace('\n', '').split()
            words = map(lambda x : x.strip("""!"#$%&'()*,-./:;?@[]_"""), parsed_line)
            for word in words:
                if word not in results:
                    results[word] = 1
                else:
                    results[word] += 1
    return results

def main():
    pass

if __name__ == "__main__":
    main()
