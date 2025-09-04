def arrangeCoins():
        n = 5
        left = 0
        right = n
        res = 0
        while left <= right:
            middle = (left + right) // 2
            summation = middle * (middle + 1) // 2
            if summation < n:
                print("Summation ",summation)
                res = middle
                # print(res)
                left = middle + 1
            else:
                right = middle - 1
        return res
result = arrangeCoins()
print(result)