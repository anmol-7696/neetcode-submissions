class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            strs = "".join(char.lower() for char in s if char.isalnum())
            
            for i in range(len(strs)):
                if strs[i] != strs[len(strs) - 1 - i]:
                    return False
            return True
        
        res = ""

        for i in range(len(s)):
            for j in range(i,len(s)):
                aux = s[i:j+1]
                if isPalindrome(aux) and len(aux) >= len(res):
                    res = aux
        return res

        