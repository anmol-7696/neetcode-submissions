class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        res = [0] * n

        for i in range(n):
            count = 0
            for j in range(i+1, n):
                count += 1
                if temp[j] > temp[i]:
                    res[i] = count
                    break
        
        return res
