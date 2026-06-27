class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        ind = 0
        len_intervals = len(intervals)
        start, end = newInterval[0],newInterval[1]
        while ind < len_intervals and start > intervals[ind][1]:
            res.append(intervals[ind])
            ind += 1
        while ind < len_intervals and end >= intervals[ind][0]:
            start = min(intervals[ind][0],start)
            end = max(intervals[ind][1],end)
            ind+=1
        res.append([start,end])
        while ind < len_intervals:
            res.append(intervals[ind])
            ind+=1
        return res