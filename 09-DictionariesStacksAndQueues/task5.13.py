###
# RPN (Reverse Polish Notation) calculator using a stack
#
import queue

stack = queue.LifoQueue()

while True:
    value = input('Enter number, operator or = : ')

    if value == '=':
        result = stack.get()
        print('Result:', result)
        break
    elif value in ['+', '-', '*', '/']:
        b = stack.get()        # drugi operand (dodany jako OSTATNI, wiec zdejmujemy go pierwszy)
        a = stack.get()        # pierwszy operand
        if value == '+':
            res = a + b
        elif value == '-':
            res = a - b
        elif value == '*':
            res = a * b
        else:
            res = a / b
        stack.put(res)         # odklada wynik z powrotem na stos
    else:
        stack.put(float(value))   # to liczba - na stos