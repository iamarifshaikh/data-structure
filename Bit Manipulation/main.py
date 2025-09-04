nums = [1, 2, 3, 4, 5]
ans = 0

for num in nums:
    # print(bin(num))
    ans ^= num
    print("{:b} {:d} {:d}".format(num,num,ans))  