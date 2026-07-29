class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window, res = [], []
        start = 0
        for i, num in enumerate(nums):
            heapq.heappush(window, (-num, i))
            while i == start + k -1:
                maxNum, index = window[0]
                if start <= index < start + k:
                    res.append(-maxNum)
                    start += 1
                else:
                    heapq.heappop(window)
        return res