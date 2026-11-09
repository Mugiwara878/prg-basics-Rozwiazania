###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)
print(f"side a {a}")
print(f"side b {b}")
print(f"length of the diagonal: √({a}**2 + {b}**2) = {round(diagonal,2)}")