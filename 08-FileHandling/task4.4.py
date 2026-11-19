###
# Prints the file 5 lines at a time, waiting for Enter between batches
#
with open('it_company.csv', 'r') as file:
    lines = file.readlines()        # czyta WSZYSTKIE linie naraz, jako listę stringów

i = 0
while i < len(lines):
    print(lines[i], end="")
    i += 1
    if i % 5 == 0:                   # co 5 linii - przerwa
        input('Press Enter key...')

print()