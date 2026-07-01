class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for i in range(len(s)):
            map[s[i]] = i
        for i in range(len(t)):
            if t[i] not in map:
                return False
        return True