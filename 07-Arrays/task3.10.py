###
# Prints array values graphically using asterisks
#
def star(n):
    return '*' * n

arr = [2,6,4,9,7]
for val in arr:
    print(f'{val}: {star(val)}')