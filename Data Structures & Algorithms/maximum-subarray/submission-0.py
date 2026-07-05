class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, currSub = nums[0], 0
        for num in nums:
            if currSub < 0:
                currSub = 0
            currSub += num
            maxSub = max(maxSub, currSub)
        return maxSub