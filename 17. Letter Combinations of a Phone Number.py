def letterCombination():
    combination = []
    dial_pad = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    digits = "234"

    def backtracking(start,path):
        if len(path) == len(digits):
            combination.append("".join(path))
            return

        for i in range(start,len(digits)):
            for j in range(len(dial_pad[digits[start]])):
                path.append(dial_pad[digits[start]][j])
                backtracking(start+1,path)
                path.pop()

    backtracking(0,[])
    return combination

result = letterCombination()
# print(result)

# dial_pad = {"2":"abc","3":"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
# digits = "23"
# print(dial_pad[digits[0]])
