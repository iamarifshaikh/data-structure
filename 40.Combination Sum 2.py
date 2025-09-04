def combinationSum():
    candidates = [10,1,2,7,6,1,5]
    target = 8
    candidates.sort()
    print(candidates)
    result = []
    
    def backtracking(index,combination,target):
        if target == 0:
            result.append(combination[:])
            return
        
        if target < 0 or index >= len(candidates): return

        # for i in range(index,len(candidates)):
        #     if i > index and candidates[i] == candidates[i - 1]:
        #         continue
        #     combination.append(candidates[i])
        #     backtracking(i + 1,combination,target - candidates[i])
        #     combination.pop()

        # combination.append(candidates[index])
        # backtracking(index + 1,combination,target - candidates[index])
        # combination.pop()

        # next_index = index + 1
        # while next_index < len(candidates) and candidates[index] == candidates[next_index]:
        #     next_index += 1
        # backtracking(next_index,combination,target)

    backtracking(0,[],target)
    return result

result = combinationSum()
print(result)