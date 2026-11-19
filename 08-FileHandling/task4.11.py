###
# Calculates, prints, and saves integers 1-100 with their 2nd and 3rd powers
#
with open('powers.txt', 'w') as file:
    for i in range(1, 101):
        line = f"{i},{i**2},{i**3}"
        print(line)
        file.write(line + '\n')