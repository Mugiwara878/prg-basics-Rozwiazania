###
# Prints the array in reverse order
#
arr = [15,8,31,47,2,19]
print('existed array:', end=' ')
for val in arr:
    print(val, end=' ')
print()
print('reverse array:', end=' ')
for val in arr[::-1]:
    print(val, end=' ')