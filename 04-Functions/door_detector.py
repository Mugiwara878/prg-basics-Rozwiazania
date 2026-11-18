###
# Returns True if at least 3 people were in the room at the same time
#
def at_least_three(detector):
    count = 0
    max_count = 0
    for char in detector:
        if char == '+':
            count += 1
        elif char == '-':
            count -= 1
        if count > max_count:
            max_count = count
    return max_count >= 3