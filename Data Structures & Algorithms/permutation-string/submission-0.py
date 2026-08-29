class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        freq1 = [0] * 26
        freq2 = [0] * 26

        # calculate freq for the first window
        for i in range(n1):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1
        
        if freq1 == freq2:
            return True

        for i in range(n1,n2):
            right = i
            left = i - n1

            freq2[ord(s2[right]) - ord('a')] += 1
            freq2[ord(s2[left]) - ord('a')] -= 1

            if freq1 == freq2:
                return True
        
        return False