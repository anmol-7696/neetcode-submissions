class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        print(sortedNums)
        count = 1
        for i in range(1,len(nums)):
            if sortedNums[i] != sortedNums[i-1] + 1:
                continue
            else:
                count+=1
        return count