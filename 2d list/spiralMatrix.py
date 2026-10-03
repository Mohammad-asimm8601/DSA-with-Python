def spiralMatrix(mat):
    r = len(mat)
    c = len(mat[0])

    top = 0
    right = c - 1
    bottom = r - 1
    left = 0

    mat_list = []

    # top
    for j in range(c - 1):
        mat_list.append(2)
    top += 1

    return mat_list


matrix = [
    [1, 2, 3, 4, 5, 6],
    [20, 21, 22, 23, 24, 7],
    [19, 32, 33, 34, 25, 8],
    [18, 31, 36, 35, 26, 9],
    [17, 30, 29, 28, 27, 10],
    [16, 15, 14, 13, 12, 11],
]

result = spiralMatrix(matrix)
print(matrix)