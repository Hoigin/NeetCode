class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums)-k+1):
            window = []
            for j in range(k):
                heapq.heappush(window, -nums[i+j])
            res.append(-heapq.heappop(window))
        return res