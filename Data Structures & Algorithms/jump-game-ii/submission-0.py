class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        count = 0
        while r < n-1:
            temp = set()
            for i in range(l, r+1):
                temp.add(i + nums[i])
            l = r
            r = max(temp)
            count += 1
        return count