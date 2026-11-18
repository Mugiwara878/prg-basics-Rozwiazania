###
# Calculates the sum of natural numbers from 1 to n (recursively)
#
def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n-1)