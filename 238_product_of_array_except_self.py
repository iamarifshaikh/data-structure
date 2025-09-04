def productExceptSelf():
    nums = [-1,1,0,-3,3]
    n = len(nums)
    output = [1] * n

    left = 1
    for l in range(len(nums)):
        output[l] *= left
        left *= nums[l]
    
    right = 1 
    for r in range(len(nums)-1,-1,-1):
        output[r] *= right
        right *= nums[r]
    
    print(output)
         
productExceptSelf()