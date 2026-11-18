###
# Returns True if password is at least 6 chars and each char is unique
#
def is_valid(password):
    if len(password) < 6:
        return False
    for char in password:
        if password.count(char) > 1:
            return False
    return True