#!/usr/bin/env python3

def file_extensions(filename):
    no_extensions = []
    has_extensions = {}
    with open(filename) as rf:
        for line in rf:
            parsed_line = line.replace('\n', '')
            if parsed_line != '':
                x = parsed_line.split('.')
                if len(x) == 1:
                    no_extensions.append(x[0])
                else:
                    if x[-1] in has_extensions:
                        has_extensions[x[-1]].append(parsed_line)
                    else:
                        has_extensions[x[-1]] = [parsed_line]
    return (no_extensions, has_extensions)

def main():
    results = file_extensions('src/filenames.txt')
    print(f'{len(results[0])} files with no extension')
    for k,v in results[1]:
        print(f'{k} {len(v)}')

if __name__ == "__main__":
    main()