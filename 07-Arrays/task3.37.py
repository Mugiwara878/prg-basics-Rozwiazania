###
# Transposes a matrix
#
def transpose_matrix(m):
    rows = len(m)                      # ile wierszy ma oryginalna macierz
    cols = len(m[0])                   # ile kolumn ma oryginalna macierz
    result = [[0]*rows for i in range(cols)]   # nowa macierz: rozmiar ZAMIENIONY (cols wierszy, rows kolumn)
    for i in range(rows):              # i = wiersz w ORYGINALE
        for j in range(cols):          # j = kolumna w ORYGINALE
            result[j][i] = m[i][j]     # wartość z (wiersz i, kolumna j) ląduje w (wiersz j, kolumna i) - zamienione!
    return result

def print_matrix(matrix):
    for row in matrix:
        print(*row)

m1 = [[1,2,3],[4,5,6],[7,8,9]]
print_matrix(transpose_matrix(m1))
print()
m2 = [[1,2,3,4,5],[6,7,8,9,0]]
print_matrix(transpose_matrix(m2))
print()
m3 = [[5,6,7,8]]
print_matrix(transpose_matrix(m3))