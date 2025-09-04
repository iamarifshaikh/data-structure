def findAnagrams():
   s = "cbaebabacd"
   p = "abc"
   k = len(p) - 1

   freqP = [0] * 26
   freqS = [0] * 26

   for char in p:
       freqP[ord(char) - ord('a')] += 1
   
   result = []
   left = 0
   
   for right in range(len(s)):
       freqS[ord(s[right]) - ord('a')] += 1
       
       if (right - left + 1) > k:
            if freqS == freqP:
               result.append(left)
            freqS[ord(s[left]) - ord('a')] -= 1
            left += 1
   return result

findAnagrams()