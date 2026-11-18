###
# Sums the even or odd digits of a number, depending on the 'even' parameter
#
def digit_sum(number, even):
    number = str(number)
    sum = 0
    for char in number:
        digit_is_even = int(char) % 2 == 0
        if digit_is_even == even:
            sum += int(char)
    return sum


