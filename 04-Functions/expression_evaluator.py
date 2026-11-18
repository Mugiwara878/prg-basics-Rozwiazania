###
# Evaluates a simple expression with single-digit numbers and +/- operators
#
def evaluate(expression):
    result = int(expression[0])
    i = 1
    while i < len(expression):
        operator = expression[i]
        number = int(expression[i+1])
        if operator == '+':
            result += number
        else:
            result -= number
        i += 2
    return result