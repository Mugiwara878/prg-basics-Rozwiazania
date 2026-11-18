###
# Returns the acronym of a text (first letters of all words)
#
def acronym(name):
    words = name.split()
    result = ''
    for word in words:
        result += word[0]
    return result