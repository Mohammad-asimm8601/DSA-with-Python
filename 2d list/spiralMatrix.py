def spiralMatrix(mat):
    r = len(mat)
    c = len(mat[0])

    top = 0
    right = c - 1
    bottom = r - 1
    left = 0

    mat_list = []

    while top <= bottom and left <= right:

        # top
        for j in range(left, right + 1):
            mat_list.append(mat[top][j])
        top += 1

        # right
        for i in range(top, bottom + 1):
            mat_list.append(mat[i][right])
        right -= 1

        # bottom
        if top <= bottom:
            for j in range(right, left - 1, -1):
                mat_list.append(mat[bottom][j])
            bottom -= 1

        # left
        if left <= right:
            for i in range(bottom, top - 1, -1):
                mat_list.append(mat[i][left])
            left += 1

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
print(result)
