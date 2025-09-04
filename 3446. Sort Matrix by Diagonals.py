def sortMatrix():
    grid = [
        [1,7,3],
        [9,8,2],
        [4,5,6]
    ]

    n = len(grid)

    for i in range(n):
        temp = [grid[i+j][j] for j in range(n-i)]
        temp.sort(reverse=True)
        for j in range(n-i):
            grid[i+j][j] = temp[j]

    for i in range(1,n):
        temp = [grid[j][j+i] for j in range(n-i)]
        temp.sort()
        for j in range(n - i):
            grid[j][j+i] = temp[j]

sortMatrix()