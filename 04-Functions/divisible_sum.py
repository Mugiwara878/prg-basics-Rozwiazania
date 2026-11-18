###
# Returns the sum of numbers in range <x,y> divisible by 2 and 3 but not by 4
#
def divisible_sum(x, y):
    total = 0
    for i in range(x, y+1):
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
            total += i
    return total