###
# Functions to read any data type from the keyboard
#
def input_string(message):
    a = input(message)
    return a

def input_integer(message):
    a = int(input(message))
    return a

def input_real(message):
    a = float(input(message))
    return a

def input_boolean(message):
    answer = input(message)
    a = answer == 'y' or answer == 'Y' 
    return a