###
import math
# Calculation of circle area and circumference
#

# determine radius and PI values
radius = int(input("Type radius: "))
pi = math.pi
# calculate area
area = pi * radius**2
# calculate circumference
circumference = 2*pi*radius
# print results
print(f"area = {area}")
print(f"circumference = {circumference}")
