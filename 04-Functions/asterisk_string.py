def asterisk_string(n):
    result = ''
    for i in range(n):
        result += '*'
        if i < n - 1:
            result += '/'
    return result