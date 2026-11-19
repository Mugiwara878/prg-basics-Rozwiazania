###
# Calculates the array and the arithmetic mean using a for loop
#
arr = [15,8,31,47,2,19]
print('Array:', arr)
total = 0
for val in arr:
    total += val
mean = total / len(arr)
print(f'Mean: {mean}')