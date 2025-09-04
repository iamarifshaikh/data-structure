
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]
         ]


def isValid(board,row,col,num):
    for i in range(9):
        if board[i][col] == num:
            return False

        if board[row][i] == num:
            return False
        
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
            return False

    return True

def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                for num in "123456789":
                    if isValid(board,i,j,num):
                        board[i][j] = num
                        if solveSudoku(board) == True:
                            return True
                        else: board[i][j] = "."
                return False
    return True

solveSudoku(board)

print(board)