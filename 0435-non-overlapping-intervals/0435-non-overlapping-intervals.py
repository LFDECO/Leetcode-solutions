class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count=0
        intervals.sort(key=lambda x: x[1])
        last=intervals[0]
        i=1
        while i<len(intervals):
            if last[1]<=intervals[i][0]:
                last=intervals[i]
                i+=1
            else:
                count+=1
                i+=1
        return count

