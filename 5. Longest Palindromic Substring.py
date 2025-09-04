def longestPalindrome():
    s = "aacabdkacaa"
    if not s or len(s) == 1:
        return s
    
    start, end = 0, 0
    
    def expandAroundCenter(left: int, right: int) -> (int, int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            print(s[left],left,s[right],right)
            left -= 1
            right += 1
        return left + 1, right - 1
    
    for i in range(len(s)):
        print("Iteration: ",i)
        print("Sirf i,i")
        l1, r1 = expandAroundCenter(i, i)
        print("l1: ",l1,", r1: ",r1)
        print("Sirf i,i + 1")
        l2, r2 = expandAroundCenter(i, i + 1)
        print("l2: ",l2,", r2: ",r2)
        
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2
    
    return s[start:end + 1]

longestPalindrome()