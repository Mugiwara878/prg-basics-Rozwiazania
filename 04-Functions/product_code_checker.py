###
# Checks if a 4-digit product code has a correct control digit
#
def is_valid(product_code):
    digits_sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    control_digit = digits_sum % 7
    return control_digit == int(product_code[3])