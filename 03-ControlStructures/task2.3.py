###
number1 = int(input("Type a number: "))
number2 = int(input("Type a number: "))
operator = input("choose operator: '+' '-' '/' '*' ")

if operator == "+":
    result = number1+number2
elif  operator == "-":
    result = number1-number2
elif  operator == "/":
    result = number1/number2
elif  operator == "*":
    result = number1*number2


print(f'{number1} {operator} {number2} = {result}')