###
# Prints file names whose extension has exactly 4 characters
#
with open('files.txt', 'r') as file:
    for line in file:
        line = line.strip()           # usuwa białe znaki (np. \n) z końca linii
        if line == '':
            continue                  # pomija puste linie (jak ta na końcu pliku)
        extension = line.split('.')[-1]   # dzieli po kropce, bierze OSTATNI fragment = rozszerzenie
        if len(extension) == 4:
            print(line)