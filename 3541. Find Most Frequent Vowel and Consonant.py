from collections import Counter

def maxFreqSum():
    s = "successes"
    mp = Counter(s)
    vowel = max((mp[ch] for ch in mp if ch in "aeiou"), default=0)
    consonant = max((mp[ch] for ch in mp if ch not in "aeiou"), default=0)
    return vowel + consonant

maxFreqSum()