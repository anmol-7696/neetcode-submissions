class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sorted_nums = sorted(nums)
        res = []

        for i in range(n):
            
            # to avoid duplicates
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            # remaining logic
            j = i + 1
            k = n - 1

            while (j < k):
                total = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
                    k -= 1
                # to avoid duplicates
                    while(j<k and sorted_nums[j] == sorted_nums[j-1]):
                        j += 1
                    while(j < k and sorted_nums[k] == sorted_nums[k+1]):
                        k -= 1
        
        return res