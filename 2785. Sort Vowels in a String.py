def sortVowels():
    s = "lEetcOde"
    s= list(s)
    vowels = {"A","a","E","e","I","i","O","o","U","u"}
    vowels_string = []

    for i in range(len(s)):
        if s[i] in vowels:
            vowels_string.append(s[i])

    vowels_string.sort()
    
    j = 0
    for i in range(len(s)):
        if s[i] in vowels:
            s[i] = vowels_string[j]
            j += 1
    
    return "".join(s)
            
print(sortVowels())