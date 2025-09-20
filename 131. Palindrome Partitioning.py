def partition():
    s = "aab"
    result = []
    
    def backtracking(index,string,palindrome):
        if string != "" and string != string[::-1]:
            return
        
        if string != "" and string == string[::-1]: 
            palindrome.append(string)

        if len(s) <= index:
            result.append(palindrome)
            return
        
        if index < len(s) - 1:
            backtracking(index + 1,s[index+1],palindrome)
        else: backtracking(index + 1,"",palindrome)

        backtracking(index + 1,string + s[index],palindrome)

    backtracking(0,s[0],[])
    return result

print(partition())