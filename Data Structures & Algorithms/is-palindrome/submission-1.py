class Solution:
    def isAlphaNum(self,c):
        return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for ch in s:
            if self.isAlphaNum(ch):
                newS += ch.lower()
        print(newS)
        i ,j = 0, len(newS)-1

        while i < j:
            if newS[i] != newS[j]:
                return False
            else:
                i += 1
                j -= 1

        return True

        