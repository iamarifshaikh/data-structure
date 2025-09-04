def setZeroes():
    matrix = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]

    no_of_row = len(matrix)
    no_of_col = len(matrix[0])

    first_row_zero = any(row == 0 for row in matrix[0])
    first_col_zero = any(matrix[row][0] == 0 for row in range(no_of_row))
    
    for row in range(1,no_of_row):
        for col in range(1,no_of_col):
            if matrix[row][col] == 0:
                matrix[0][col] = matrix[row][0] = 0 

    for row in range(1,no_of_row):
        for col in range(1,no_of_col):
            if matrix[row][0] == 0 or matrix[0][col] == 0:
                matrix[row][col] = 0

    if first_col_zero:
        for row in range(no_of_row):
            matrix[row][0] = 0
    
    if first_row_zero:
        for col in range(no_of_col):
            matrix[0][col] == 0

    print(matrix)

setZeroes()