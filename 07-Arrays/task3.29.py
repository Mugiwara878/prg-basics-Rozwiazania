###
# Prints a 2D array (2x4) in rows and columns
#
arr = [
    [3, 7, 1, 9],
    [5, 2, 8, 4]
]

for row in arr:
    for val in row:
        print(val, end=' ')
    print()