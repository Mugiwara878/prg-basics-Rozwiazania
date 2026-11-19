###
# Makes a copy of a text file
#
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

with open(original_file, 'r') as file:
    content = file.read()           # czytamy CAŁĄ zawartość oryginału naraz

with open(target_file, 'w') as file:
    file.write(content)             # i zapisujemy ją do nowego pliku