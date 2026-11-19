###
# Reverses a string using a stack
#
import queue

def reverse_string(text):
    stack = queue.LifoQueue()
    for char in text:
        stack.put(char)              # wrzuc kazdy znak na stos

    result = ''
    while not stack.empty():
        result += stack.get()        # zdejmuj - LIFO odwraca kolejnosc!
    return result

text = input('Enter text: ')
print('Reversed:', reverse_string(text))