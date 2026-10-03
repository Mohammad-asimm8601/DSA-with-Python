# Brute force
def markInfinity(matrix, row, col):
    r = len(matrix)
    c = len(matrix[0])

    for i in range(r):
        if matrix[i][col] !=0:
            matrix[i][col] = float("inf")

    for j in range(c):
        if matrix[row][j] !=0:
            matrix[row][j] = float("inf")

def setZeros1(mat):
    r = len(mat)
    c = len(mat[0])

    for i in range(r):
        for j in range(c):
            if mat[i][j] == 0:
                markInfinity(mat, i, j)

    for i in range(r):
        for j in range(c):
            if mat[i][j] == float("inf"):
                mat[i][j] = 0

    return mat

def printMat(mat):
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            print(mat[row][col], end=" ")
        print()


def setZeros2(mat):
    r = len(mat)
    c = len(mat[0])

    row_track = [0]*r
    col_track = [0]*c

    for i in range(r):
        for j in range(c):
            if mat[i][j] == 0:
                row_track[i] = -1
                col_track[j] = -1

    for i in range(r):
        for j in range(c):
            if row_track[i]== -1 or col_track[j] == -1:
                mat[i][j] = 0

    return mat

def setZeros3(mat):
    r = len(mat)
    c = len(mat[0])

    first_row_zero = False
    first_col_zero = False

    for j in range(c):
        if mat[0][j] == 0:
            first_row_zero = True

    for i in range(r):
        if mat[i][0] == 0:
            first_col_zero = True

    for i in range(1, r):
        for j in range(1, c):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0

    for i in range(1, r):
        for j in range(1, c):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0

    if first_row_zero:
        for j in range(c):
            mat[0][j] = 0

    if first_col_zero:
        for i in range(c):
            mat[i][0] = 0

    return mat


matrix = [[7, 9, 2, 3], [20, 8, 0, 10], [29, 0, -10, 5], [4, 14, 6, 7]]
# result = setZeros1(matrix) # Brute force solution 
# result = setZeros2(matrix) # optimize solution 
result = setZeros3(matrix) # more optimize solution 
printMat(result)