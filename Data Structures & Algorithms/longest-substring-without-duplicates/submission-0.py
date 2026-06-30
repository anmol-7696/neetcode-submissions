class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            map  = {}
            
            for j in range(i,n):
                if s[j] in map:
                    break
                else:
                    map[s[j]] = j
                res = max(res,len(map))
        return res
