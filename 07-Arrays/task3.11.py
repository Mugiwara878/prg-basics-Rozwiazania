###
# Checks if two arrays are the same
#
def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

test_pairs = [
    (["water","book","sky"], ["water","book","sky"]),
    ([True,False], [True,False,True]),
    ([5,3,1], [5,3,1]),
    ([3,2,1], [3,2])
]
for a1, a2 in test_pairs:
    print('Array1:', a1)
    print('Array2:', a2)
    result = 'arrays are the same' if compare(a1,a2) else 'arrays are different'
    print('Comparison:', result)