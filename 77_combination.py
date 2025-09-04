def combination():
    n = 4
    k = 2
    result = []

    def backtracking(index:int,path:list):
        if len(path) == k:
            result.append(path[:])
            return
        
        if index > n:
            return

        path.append(index)
        backtracking(index + 1, path)
        path.pop()
        backtracking(index + 1, path)

    backtracking(1,[])
    return result

result = combination()
print(result)