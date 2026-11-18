###
# Calculates x to the power of n (recursively)
#
def power(x, n):
    if n == 1:
        return x
    return x * power(x,n-1)