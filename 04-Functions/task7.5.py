import range_checker

number = int(input("Enter your number: "))
x = int(input("Enter x: "))
y = int(input("Enter y: "))

print(f'Number {number} in the range <{x},{y}>: {"yes" if range_checker.in_range(number, x, y) else "no"}')