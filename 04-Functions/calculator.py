###
# Performs an arithmetic operation based on the operator string
#
def calculate(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '%':
        return number1 % number2
    elif operator == '**':
        return number1 ** number2