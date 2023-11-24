# 1.4
for i in range(1, 11):
    j = i
    while j<=i*10:
        print(f'{j:4}', end='')
        j += i
    print()

# 1.5
for i in range(1,7):
    for j in range(1,7):
        if i+j != 5:
            continue
        else:
            print(f'({i},{j})')

# 1.6
def triple(n):
    return n*3

def square(n):
    return n**2

def main():
    for i in range(1,11):
        t = triple(i)
        s = square(i)
        if s>t:
            break
        print(f'triple({i})=={t} square({i})=={s}')