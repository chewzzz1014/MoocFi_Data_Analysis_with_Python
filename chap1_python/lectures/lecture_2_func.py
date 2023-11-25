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


# map function
# a list and a function as parameters, and it returns a new list whose elements are elements of the original list transformed by the parameter function.
def double(x):
    return 2*x
L=[12,4,-1]
print(list(map(double, L)))

# convert all values in list into int
s="12 43 64 6"
L=s.split()        # The split method of the string class, breaks the string at whitespaces
                   # to a list of strings.
print(L)
print(sum(map(int, L)))  # The int function converts a string to an integer


# lambda function
L=[2,3,5]
print(list(map(lambda x : 2*x+x**2, L)))


