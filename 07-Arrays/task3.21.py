###
# Prints the number of elements greater than a given value
#
arr = [12.5, 7.3, 20.1, 3.8, 15.6, 9.2]
value = float(input('Enter value: '))
count = 0
for val in arr:
    if val > value:
        count += 1
print(f'Number of elements greater than {value}: {count}')