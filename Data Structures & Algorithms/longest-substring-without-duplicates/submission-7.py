class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset = set()
        l = res = 0
        for r in range(len(s)):
            while s[r] in subset:
                subset.remove(s[l])
                l += 1
            subset.add(s[r])
            res = max(res, r-l+1)
        return res