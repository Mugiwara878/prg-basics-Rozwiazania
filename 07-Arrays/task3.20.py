import MyArrays

numbers = [7,3,8,5,2]
print('Numbers:', ','.join(str(n) for n in numbers))
print('Second largest number:', MyArrays.second_largest(numbers))
print('Median:', MyArrays.median(numbers))
minmax = MyArrays.min_max_array(numbers)
print(f'Smallest and largest number: {minmax[0]},{minmax[1]}')
print('Numbers as a string:', MyArrays.array_to_string(numbers))