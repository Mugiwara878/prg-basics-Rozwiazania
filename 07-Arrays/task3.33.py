###
# Finds the smallest and largest values in a 2D array, and their position
#
arr = [[-38, 19], [5,40], [-7,11], [29,16]]

min_val = arr[0][0]       # start: zakładamy że pierwsza komórka to min/max
max_val = arr[0][0]
min_pos = (0,0)            # zapamiętujemy też POZYCJĘ (wiersz, kolumna)
max_pos = (0,0)

for i in range(len(arr)):          # i = numer wiersza
    for j in range(len(arr[i])):   # j = numer kolumny w tym wierszu
        if arr[i][j] < min_val:
            min_val = arr[i][j]
            min_pos = (i,j)
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            max_pos = (i,j)

print(f'Min value: {min_val} at position {min_pos}')
print(f'Max value: {max_val} at position {max_pos}')