def uniquePaths():
    m = 2
    n = 1
    grid = [[1 if j == 0 or i == 0 else 0 for j in range(n)]for i in range(m)]

    for row in range(1, m):
        for col in range(1, n):
            grid[row][col] = grid[row-1][col] + grid[row][col-1]
    return grid[-1][-1]
    # grid = [["" for j in range(n)]for i in range(m)]
    # print(grid)
    # count = 0
    # def backtracking(row,col):
    #     nonlocal count
    #     if row == m and col == n:
    #         count +=1
    #         return

    #     if row != m: 
    #         backtracking(row + 1,col)
    #     if col != n: 
    #         backtracking(row,col + 1)
    
    # backtracking(1,1)
    # return count

result = uniquePaths()
print(result)