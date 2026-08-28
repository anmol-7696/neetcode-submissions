class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = "".join(char.lower() for char in s if char.isalnum())
        
        for i in range(len(strs)):
            if strs[i] != strs[len(strs) - 1 - i]:
                return False
        return True