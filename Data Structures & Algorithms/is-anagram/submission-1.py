from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # dict_one = {}
        # dict_two = {}
        # for r in range(len(s)):

        #     dict_one[s[r]] = dict_one.get(s[r],0) + 1
        #     dict_two[t[r]] = dict_two.get(t[r],0) + 1
           
            
        return Counter(t) == Counter(s)