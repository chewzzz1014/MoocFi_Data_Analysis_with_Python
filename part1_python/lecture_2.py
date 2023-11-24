# argument packing: packs all given positional args into tuple t
# happens in params list of func
def sum_of_squares(*t):
    "Computes the sum of squares of arbitrary number of arguments"
    s=0
    for x in t:
        s += x**2
    return s
print(sum_of_squares(-2))
print(sum_of_squares(-2,4,5))


# argument unpacking: reverse of argument packing
# happens where the function is called
lst=[1,5,8]
print("With list unpacked as arguments to the functions:", sum_of_squares(*lst))
# print(sum_of_squares(lst))    # Does not work correctly


# named argument
def named(a, b, c):
    print("First:", a, "Second:", b, "Third:", c)
named(5, c=7, b=8)


