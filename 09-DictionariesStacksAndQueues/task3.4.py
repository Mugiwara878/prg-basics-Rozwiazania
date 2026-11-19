###
# Converts a decimal number to binary using a stack
#
import queue

def decimal_to_binary(number):
    stack = queue.LifoQueue()
    while number > 0:
        remainder = number % 2
        stack.put(remainder)
        number = number // 2

    binary = ""
    while not stack.empty():
        binary += str(stack.get())
    return binary

n = 18
print('Natural number:', n)
print('Binary number:', decimal_to_binary(n))