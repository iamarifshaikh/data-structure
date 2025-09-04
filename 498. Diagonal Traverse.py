def findDiagonalOrder():
    # mat = [[1,2,3],[4,5,6],[7,8,9]]
    # mat = [[1,2],[3,4]]
    mat = [[2,5],[8,4],[0,-1]]
    n = len(mat)
    m = len(mat[0])
    result = []

    def checkEvenOdd(i,j):
        return (i + j) % 2 == 0
    
    row = 0
    col = 0

    for _ in range(n * m):
        if checkEvenOdd(row,col):
            result.append(mat[row][col])
            if row == 0:
                if col != m - 1:
                    col += 1
                else:
                    row += 1
            elif col == m - 1:
                row += 1
            else:
                row -= 1
                col += 1
        else:
            result.append(mat[row][col])
            if col == 0:
                if row != n - 1:
                    row += 1
                else:
                    col += 1
            elif row == n - 1:
                col += 1
            else:
                row += 1
                col -= 1

    return result

print(findDiagonalOrder())