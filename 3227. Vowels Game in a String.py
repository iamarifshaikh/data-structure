from collections import Counter

def doesAliceWin():
    s = "leetcoder"
    vowels = {"a","e","i","o","u"}
    
    dictionary = Counter()
    
    for i in range(len(s)):
        if s[i] in vowels:
            if s[i] not in dictionary:
                dictionary[s[i]] = 1
            else:
                dictionary[s[i]] += 1
    
    if dictionary: return True
    else: return False

doesAliceWin()