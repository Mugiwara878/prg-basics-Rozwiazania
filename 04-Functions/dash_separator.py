###
# Returns text with all characters separated by a dash sign
#
def dash_separate(text):
    if text == '':
        return ''
    result = text[0]
    for char in text[1:]:
        result += '-' + char
    return result