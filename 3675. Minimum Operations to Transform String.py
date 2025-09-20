def minOperations():
    s = "sb"
    ans = 0    
    for c in range(len(s)):
        ans = max(ans,26 - (ord(s[c]) - ord('a')) % 26)
        
    return ans
print(minOperations())

# print(ord("s")- ord('a'))
# print(ord("n")- ord('a'))