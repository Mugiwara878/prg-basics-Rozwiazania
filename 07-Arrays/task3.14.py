###
# Prints all unique elements in an array
#
arr = [2, 3, 2, 5, 8, 1, 9, 8]
print('Array:', end=' ')
for val in arr:
    print(val, end=' ')
print()
print('Unique elements:', end=' ')
for val in arr:
    if arr.count(val) == 1:
        print(val, end=' ')