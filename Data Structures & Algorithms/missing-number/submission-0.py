class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for num in nums:
            res = res^num
        for num in range(0, n+1):
            res = res^num
        return res