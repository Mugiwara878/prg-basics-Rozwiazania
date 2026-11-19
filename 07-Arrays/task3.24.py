###
# Returns a randomly selected array element
#
import random

def rand_elem(array):
    return array[random.randint(0, len(array)-1)]

arr = [10, 20, 30, 40, 50]
for i in range(5):
    print(rand_elem(arr))
# print()
# for i in range(5):
#     print(random.choice(arr))
# print()
# for i in range(5):
#     print(random.choice(arr), end=" ")