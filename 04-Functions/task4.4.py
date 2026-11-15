###
# Calculates the sum of the digits in a number
#
i = 0
number = abs(int(input("Enter a number: ")))
num = str(number)
def sum_digits(num):
    result = 0
    for i in range(0,len(num)):
        num1 = num[i]
        result += int(num1) 
        i += 1 
    return result
        

print(sum_digits(num)) 

