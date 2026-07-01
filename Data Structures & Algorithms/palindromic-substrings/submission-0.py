class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(s):
            strs = "".join(char.lower() for char in s if char.isalnum())
            
            for i in range(len(strs)):
                if strs[i] != strs[len(strs) - 1 - i]:
                    return False
            return True
        
        count = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if isPalindrome(s[i:j+1]) and s[i:j+1]:
                    count += 1
        return count