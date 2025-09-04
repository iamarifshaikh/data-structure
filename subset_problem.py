def subset():
    arr = [3, 34, 4, 12, 5, 2]
    target = 9

    dp = [[False] *  (target + 1) for _ in range(len(arr) + 1)]
    
    row = len(dp)
    col = len(dp[0])

    for r in range(row):
        dp[r][0] = True

    for j in range(1, target + 1):
        dp[0][j] = False

    for r in range(1,row):
        for c in range(1,col):
            if arr[r-1] <= c:
                dp[r][c] = dp[r-1][c] or dp[r-1][c-arr[r-1]]
                if r == 3  and c == 1: 
                    print([c-arr[r-1]])
                    print("yeh huit hua")
                    break 
            else: dp[r][c] = dp[r-1][c]
            # print(dp)
    # def recursion(ind,remaining,arr):
    #     if remaining == 0:
    #         return True
        
    #     if ind == len(arr):
    #         return False
        
    #     if arr[ind] <= target:
    #         return (recursion(ind + 1,remaining - arr[ind],arr) or recursion(ind + 1,remaining,arr))
    #     else:
    #         return recursion(ind + 1,remaining,arr)


    # print(recursion(0,0,arr))

subset()