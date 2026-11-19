###
# Creates a 2D array filled with zeros
#
def create_2d_arr(x, y):
    arr = []                    # pusta lista na całą tablicę 2D
    for i in range(x):          # dla każdego z x wierszy...
        row = []                # ...tworzymy nowy, pusty wiersz
        for j in range(y):      # dla każdej z y kolumn w tym wierszu...
            row.append(0)       # ...dokładamy zero
        arr.append(row)         # gotowy wiersz dokładamy do całej tablicy
    return arr

arr = create_2d_arr(3, 5)
for row in arr:
    print(row)