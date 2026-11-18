###
# Returns the n-th prime number
#

def is_prime(num):
    if num < 2:
        return False
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    number = 1
    while count < n:
        number += 1
        if is_prime(number):
            count += 1
    return number