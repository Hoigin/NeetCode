class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if intervals[-1][1] < newInterval[0]:
            intervals.append(newInterval)
            return intervals
        n = len(intervals)
        result = []
        i = 0
        while i < n:
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
                i += 1
            elif intervals[i][1] == newInterval[0]:
                result.append(intervals[i])
                result[-1][1] = newInterval[1]
                i += 1
                break
            else:
                result.append(newInterval)
                result[-1][0] = min(newInterval[0], intervals[i][0])
                break
        while i < n:
            if intervals[i][0] <= newInterval[1]:
                if intervals[i][1] > newInterval[1]:
                    result[-1][1] = intervals[i][1]
                i += 1
            else:
                result.append(intervals[i])
                i += 1
        return result