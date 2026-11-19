###
# Creates and prints identity matrices
#
def identity_matrix(n):
    matrix = [[0]*n for i in range(n)]
    for i in range(n):
        matrix[i][i] = 1          # przekątna = 1,
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(*row)               # rozpakowuje listę jako osobne argumenty print

print_matrix(identity_matrix(3))
print()
print_matrix(identity_matrix(5))
print()
print_matrix(identity_matrix(8))