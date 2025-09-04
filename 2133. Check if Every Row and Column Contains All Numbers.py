def checkValid():
    matrix = [[1,1,1],[3,1,2],[2,3,1]]
    for row in range(len(matrix)):
        if len(set(matrix[row])) != len(matrix[row]):
            return False

    for row in range(len(matrix)):
        seen_col = set()
        for col in range(len(matrix[row])):
            if matrix[col][row] not in seen_col:
                seen_col.add(matrix[col][row])
            else:
                return False

    return True 

result = checkValid()
print(result)