class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()
        res = []

        current_start, current_end = intervals[0]

        for start, end in intervals[1:]:
            if start <= current_end:
                current_end = max(current_end, end)
            else:
                res.append([current_start, current_end])
                current_start, current_end = start, end

        res.append([current_start, current_end])
        return res
