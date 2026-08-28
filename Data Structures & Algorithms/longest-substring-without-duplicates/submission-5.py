class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = {}
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] in index and index[s[right]] >= left:
                left = index[s[right]] + 1
            index[s[right]] = right
            res = max(res, right - left + 1)
        return res