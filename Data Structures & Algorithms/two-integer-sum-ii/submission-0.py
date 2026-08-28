class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
       
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in map:
                return [map[complement] + 1, i + 1]
            map[numbers[i]] = i
        return [1]