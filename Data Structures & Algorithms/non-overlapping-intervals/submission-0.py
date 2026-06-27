class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = -1
        for j in range(len(intervals)-1):
            if intervals[j][0] < intervals[j+1][1]:
                count+=1
        return count
