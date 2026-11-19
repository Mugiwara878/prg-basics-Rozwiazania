###
# Counts lines, characters and words in a text file
#
try:
    file_name = input('File name: ')
    with open(file_name, 'r') as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()

    print('Number of lines:', len(lines))
    print('Number of characters:', len(content))
    print('Number of words:', len(words))
except FileNotFoundError:
    print(f'File {file_name} does not exist.')