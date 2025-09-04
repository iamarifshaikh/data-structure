def isValidSudoku():
    board = [
        [".",".",".",".",".",".",".",".","2"],
        ["2",".",".","5",".",".",".",".","8"],
        ["9",".",".","1","3",".",".",".","."],
        [".",".",".",".",".",".","8",".","2"],
        [".",".",".",".",".",".",".",".","."],
        [".","2",".",".",".","9",".",".","."],
        ["7","9",".",".",".",".","2",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".","8","3",".","1"]
        ]

    grid = [
        (0,0),(0,3),(0,6),
        (3,0),(3,3),(3,6),
        (6,0),(6,3),(6,6)
    ]

    for tup in range(len(grid)):
        row = grid[tup][0]
        col = grid[tup][1]

        hashtable = {}
        for i in range(row,row+3):
            for j in range(col,col+3):
                if board[i][j] != "." and board[i][j] in hashtable: 
                    return False
                else:
                    if board[i][j] != ".": 
                        hashtable[board[i][j]] = (i,j)
        
    for i in range(9):
        hashtable = {}
        for j in range(9): 
            if board[j][i] != "." and board[j][i] in hashtable:
                return False
            else: 
                if board[j][i] != ".":
                    hashtable[board[j][i]] = (j,i)
        print("Col:", i, hashtable)

    # check rows
    for i in range(9):
        hashtable = {}
        for j in range(9):
            if board[i][j] != "." and board[i][j] in hashtable:
                print("False Row")
                return False
            else:
                if board[i][j] != ".":
                    hashtable[board[i][j]] = (i,j)
        print("Row:", i, hashtable)

    return True

print(isValidSudoku())