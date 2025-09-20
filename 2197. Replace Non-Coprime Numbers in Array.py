import math

def replaceNonCoprimes():
    nums = [54395,31,31]
    new_num = []
    i = 0
    last_merged = -1
    while i < len(nums)-1: 
        lowest_factor = math.gcd(nums[i],nums[i+1])
        if lowest_factor > 1:
            lcm = math.lcm(nums[i],nums[i+1])
            new_num.append(lcm)
            
            if i + 1 < len(nums):
                j = i + 2
            else: 
                break

            while j < len(nums):
                if math.gcd(new_num[-1],nums[j]) > 1:
                    last_merged = nums[j]
                    new_num[-1] = math.lcm(new_num[-1],nums[j])
                else:
                    last_element = nums[j]
                    break
                j += 1
            i = j
        else:
            new_num.append(nums[i])
            i += 1
    
    if last_merged != nums[-1] and math.gcd(nums[-1],new_num[-1]) == 1:
        new_num.append(nums[-1])

    return new_num

print(replaceNonCoprimes())
# print(math.gcd(517,11),math.lcm(517,11))
# print(math.gcd(121,517),math.lcm(121,517))
# print(math.gcd(3,5687),math.lcm(3,5687))
# print(math.gcd(5687,517),math.lcm(5687,517))
# print(math.gcd(51,3),math.lcm(51,3))
# print(math.gcd(121,11),math.lcm(121,11))
# print(math.gcd(517,3),math.lcm(517,3))
print(math.gcd(31,31),math.lcm(31,31))