def generateParenthesis():
    n = 3
    parenthesis = []
    def backtracking(open,close,string):
        if open == n and close == n:
            parenthesis.append(string)
            return
        
        if open != n: backtracking(open + 1,close,string + "(")
        if close != n and open > close: backtracking(open,close + 1,string + ")")

    backtracking(0,0,"")
    print(parenthesis)
generateParenthesis()