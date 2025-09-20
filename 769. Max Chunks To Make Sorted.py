def maxChunksToSorted():
    """Using Prefix Max and Suffix Min"""
    """
    arr = [2,0,1,3]
    arr = [1,2,0,3,4]
    n = len(arr)
    chunks = 0
    
    prefixMax = arr.copy()
    suffixMin = arr.copy()
    
    for i in range(1,n-1): prefixMax[i] = max(prefixMax[i],prefixMax[i-1])
    
    for i in range(n-2,-1,-1): suffixMin[i] = min(suffixMin[i],suffixMin[i+1])

    for i in range(n): 
        if i == 0 or suffixMin[i] > prefixMax[i-1]: chunks += 1
    
    return chunks"""
    
    """Using Prefix Sum"""
    """arr = [1,0,2,3,4]
    chunks = 0
    n = len(arr)

    sortedArr = arr.copy()
    sortedArr.sort()

    prefixArray = [0] * n
    prefixArray[0] = sortedArr[0]

    for i in range(1,len(sortedArr)):
        prefixArray[i] = sortedArr[i] + prefixArray[i-1]
    
    for i in range(len(arr)):
        if sum(arr[:i+1]) == prefixArray[i]:
            print(arr[:i+1],prefixArray[i])
            chunks += 1

    return chunks"""
    arr = [0,2,4,3,1,9,5,6,7,8]
    stack = []

    for i in range(len(arr)):
        while stack and stack[-1] > arr[i]
        # Case 1: Current element is larger, starts a new chunk
        # if not stack or arr[i] > stack[-1]:stack.append(arr[i])
        # else:
        #         # Case 2: Merge chunks
        #         max_element = stack[-1]
        #         while stack and arr[i] < stack[-1]:
        #             stack.pop()
        #         stack.append(max_element)

    return len(stack) 
print(maxChunksToSorted())