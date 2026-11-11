###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
# Type temperature in C 
C = float(input("Type c: "))
# calculate Kelvin
K = C + 273.15
# calculate Fahrenheit
F = C * 9/5 + 32
# print results
print(f"C: {C} | K: {K} | F: {F}")