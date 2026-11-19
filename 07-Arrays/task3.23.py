###
# Checks if the first array is a subset of the second
#
def is_subset(arr1, arr2):
    for val in arr1:
        if val not in arr2:
            return False
    return True

a = [2, 4, 6]
b = [1, 2, 3, 4, 5, 6, 7]
print(f'{a} is subset of {b}: {is_subset(a, b)}')

c = [2, 4, 9]
print(f'{c} is subset of {b}: {is_subset(c, b)}')