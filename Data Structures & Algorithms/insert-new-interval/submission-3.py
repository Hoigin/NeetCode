class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        # 1. 添加所有在 newInterval 之前的区间
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
            
        # 2. 合并所有与 newInterval 重叠的区间
        # 只要当前区间的开始小于等于 newInterval 的结束，说明存在重叠
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        
        # 3. 添加剩余的区间
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result