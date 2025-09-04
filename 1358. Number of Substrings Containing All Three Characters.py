def numberOfSubstrings() -> int:
    s = "abcabc"
    hashtable = {}
    left = 0

    for right in range(len(s)):
        if s[right] not in hashtable:
            hashtable[s[right]] = 1
        else: hashtable[s[right]] += 1
        print(hashtable)

numberOfSubstrings()