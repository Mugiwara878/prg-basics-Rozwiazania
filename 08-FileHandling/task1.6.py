###
# Reads from file, prints countries sorted alphabetically
#
def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()
    return content

file_content = read_from_file('countries.txt')
file_lines = file_content.splitlines()

for line in sorted(file_lines):
    print(line)