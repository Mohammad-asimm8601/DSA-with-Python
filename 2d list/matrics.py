def printMat(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols): 
            print(matrix[row][col], end=" ")
        print()

def printUpperTriangle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            if col >= row:
                print(matrix[row][col], end=" ")
            else:
                print("*", end=" ")
        print()

def printLowerTriangle(matrix):
    rows = len(matrix) 
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            if col <= row:
                print(matrix[row][col], end=" ")
            else:
                print("*", end=" ")
        print()

def transpose(matrix):
    rows = len(matrix) 
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(row+1, cols):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        

matrix = [[5, 20, 3], [7, -10, 9], [1, -52, 6]]

# printMat(matrix)
# printUpperTriangle(matrix)
printLowerTriangle(matrix)