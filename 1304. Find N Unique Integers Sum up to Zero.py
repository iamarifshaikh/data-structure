def sumZero():
    n = 4
    start = -(n // 2)
    result = [0] * n
    
    for i in range(n):
        result.extend([i, -i])
        # if n % 2 == 0 and start == 0:
        #     result[i] = start + 1
        #     start = start + 2
        # else:
        #     result[i] = start
        #     start = start + 1
    return result
print(sumZero())