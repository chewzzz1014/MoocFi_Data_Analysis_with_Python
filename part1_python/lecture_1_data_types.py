# data type: int, float, complex, str, bool
i=5
f=1.5
b = i==4
print("Result of the comparison:", b)
c=0+2j                                 # Note that j denotes the imaginary unit of complex numbers.
print("Complex multiplication:", c*c)
s="conca" + "tenation"
print(s)

# characters <-> binary
b="ä".encode("utf-8")     # Convert character(s) to a sequence of bytes
print(b)                  # Prints bytes in hexadecimal notation
print(list(b))            # Prints bytes in decimal notation
bytes.decode(b, "utf-8")  # convert sequence of bytes to character(s)

# string interpolation
print('%i plus %i is equal to %i' % (1,2,3)) # i for integer, f for float...
print('{} plus {} is equal to {}'.format(1,2,3))
print(f'{1} plus {3} is equal to {4}')

# number of decimals
print("%.1f %.2f %.3f" % (1.6, 1.7, 1.8))               # Old style
print("{:.1f} {:.2f} {:.3f}".format(1.6, 1.7, 1.8))     # newer style
print(f"{1.6:.1f} {1.7:.2f} {1.8:.3f}")                 # f-string


