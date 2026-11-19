###
# Calculates the array and the arithmetic mean using a while loop
#
arr = [15,8,31,47,2,19]
print('Array:', arr)
total = 0
i = 0
while i < len(arr):
    total += arr[i]
    i += 1
mean = total / len(arr)
print(f'Mean: {mean}')