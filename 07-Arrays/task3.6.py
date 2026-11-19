###
# Finds max and min without using built-in functions
#
arr = [-15,8,-31,47,-2,19]
max_val = arr[0]
min_val = arr[0]
for val in arr:
    if val > max_val:
        max_val = val
    if val < min_val:
        min_val = val
print(f'Max: {max_val}, Min: {min_val}')