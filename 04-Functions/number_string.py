###
# Returns numbers from 1 to n as a single string
#
def number_string(n):
    result = ''
    for i in range(1, n+1):
        result += str(i)
    return result