from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}
       
        for ch in s:
            counter[ch] = counter.get(ch,0) + 1
        
        for ch in t:
            counter[ch] = counter.get(ch,0) - 1

            if counter[ch] < 0:
                return False

        return True