def searchMatrix():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 40
    left = 0
    right = len(matrix) * len(matrix[0]) - 1    
    column = len(matrix[0])
    
    while left <= right:
        middle = (left + right) // 2
        row = middle // column
        col = middle % column
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            right = middle - 1
        else:
            left = middle + 1 
    return False
    
result = searchMatrix()
print(result)