###
# Returns the sum of repeated digits in a number
#
def sum_repeated(number):
    number = str(number)
    sum = 0
    for char in number:
        if number.count(char) > 1:
            sum += int(char)
    return sum