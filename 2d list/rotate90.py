def transpose(mat):
    r = len(mat)
    c = len(mat[0])

    for i in range(r):
        for j in range(i+1, c):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

def rotate90(mat):
    transpose(mat)

    r = len(mat)
    c = len(mat[0])

    for i in range(r):
        left = 0
        right = c-1
        while(left < right):
            mat[i][left], mat[i][right] = mat[i][right], mat[i][left]
            left += 1
            right -= 1
    

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
rotate90(matrix)
print(matrix)

