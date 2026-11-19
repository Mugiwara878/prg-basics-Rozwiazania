###
# Sorts three arrays using bubble sort
#
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr1 = [5,2,9,1,7]
arr2 = [-3,8,-1,0,4]
arr3 = [100,20,50,10,80]

print(bubble_sort(arr1))
print(bubble_sort(arr2))
print(bubble_sort(arr3))