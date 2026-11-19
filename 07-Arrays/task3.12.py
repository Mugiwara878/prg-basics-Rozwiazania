###
# Prints numbers from the first array that do not appear in the second array
#
arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

for val in arr1:
    if val not in arr2:
        print(val, end=' ')