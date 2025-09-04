def replace_with_rank():
        arr = [20, 15, 26, 2, 98, 6]
        num_to_indices = {k: [] for k in sorted(set(arr))}
        

        for i, num in enumerate(arr):
            num_to_indices[num].append(i)
        rank = 1
        
        for num in num_to_indices.keys():
            for index in num_to_indices[num]:
                arr[index] = rank
            rank += 1
        return arr
        
replace_with_rank()