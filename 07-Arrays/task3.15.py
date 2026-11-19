###
# Checks if a given number is present in an array
#
def occurs(number, array):
    return number in array

array = [15, 38, 7, 23, 14]
number = int(input('Number: '))
print('Array:', array)
print(f'Result: number {number} {"appears" if occurs(number,array) else "does not appear"} in the array')