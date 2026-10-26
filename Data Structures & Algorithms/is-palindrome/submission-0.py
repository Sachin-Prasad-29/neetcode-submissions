import re

class Solution:

    def remove_non_alpha(self,s:str) -> str:
        return re.sub(r'[^A-Za-z0-9]','',s).lower()
    
    def isPalindrome(self, s: str) -> bool:
        
        s = self.remove_non_alpha(s)
        i = 0
        j = len(s) - 1
        while i < j:
            print(s[i], s[j])
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
            