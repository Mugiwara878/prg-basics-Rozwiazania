###
# Converts a 2D array into a 1D array
#
def flatten(arr_2d):
    result = []
    for row in arr_2d:
        for val in row:
            result.append(val)
    return result

print(flatten([[2,3],[1,5]]))
print(flatten([[5,0,3,7,5],[9,0,9,1,2]]))
print(flatten([[2,1],[3,5],[7,4],[2,6]]))