###
# Swaps the first and last column of a 3x5 2D array
#
arr = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

print('Before:')
for row in arr:
    print(row)

for row in arr:                      # kolumny trzeba zamieniać w KAŻDYM wierszu osobno
    row[0], row[-1] = row[-1], row[0]

print('After:')
for row in arr:
    print(row)