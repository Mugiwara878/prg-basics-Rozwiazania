###
# Reads from file, line by line, prints numbered list
#
with open('countries.txt', 'r') as file:
    counter = 1
    for line in file:
        print(f'{counter}. {line}', end="")
        counter += 1