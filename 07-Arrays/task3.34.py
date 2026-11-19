###
# Swaps the first and last row of a 3x5 2D array
#
arr = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

print('Before:')
for row in arr:
    print(row)

arr[0], arr[-1] = arr[-1], arr[0]   # ta sama "jednoczesna zamiana" co wcześniej, tylko całych wierszy

print('After:')
for row in arr:
    print(row)