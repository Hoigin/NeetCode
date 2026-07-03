class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda t: t[0])
        n = len(intervals)
        result = [intervals[0]]
        i = 1
        Count = 0
        preEnd = result[-1][1]
        while i < n:
            if preEnd <= intervals[i][0]:
                result.append(intervals[i])
                preEnd = intervals[i][1]
            else:
                Count += 1
                if preEnd > intervals[i][1]:
                    result.pop()
                    result.append(intervals[i])
                    preEnd = intervals[i][1]
            i += 1
        return Count
