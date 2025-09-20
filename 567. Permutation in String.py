from collections import Counter

def checkInclusion():
    s1 = "ab"
    s2 = "eidbaooo"
    left = 0
    s1_table = Counter(s1)
    s2_table = Counter() 

    for right in range(len(s2)):
        s2_table[s2[right]] = s2_table.get(s2[right], 0 ) + 1
        if right - left + 1 >= len(s1):
            if s1_table == s2_table: return True
            s2_table[s2[left]] -= 1
            if s2_table[s2[left]] <= 0: del s2_table[s2[left]]
            left += 1

    return False

print(checkInclusion())

s1 = {"a","b","c"}
s2 = {"b","d","c"}