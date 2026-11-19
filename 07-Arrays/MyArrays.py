###
# Module with array utility functions
#
def second_largest(arr):
    sorted_arr = sorted(arr)
    return sorted_arr[-2]

def max_min_diff(arr):
    return max(arr) - min(arr)

def median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 1:
        return sorted_arr[n//2]
    else:
        return (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2

def min_max_array(arr):
    return [min(arr), max(arr)]

def array_to_string(arr):
    result = str(arr[0])
    for val in arr[1:]:
        result += '-' + str(val)
    return result