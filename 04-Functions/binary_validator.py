###
# Checks if a string is a valid binary number
#
def is_binary(binary_number):
    for char in binary_number:
        if char == '0' or char == '1':
             bin = True   
        else:
            return False
        
    return bin
