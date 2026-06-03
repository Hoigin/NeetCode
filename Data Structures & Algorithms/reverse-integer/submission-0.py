class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if x >= 0:
            s = s[::-1]
        else:
            s = "-" + s[:0:-1]
        res = int(s)
        return res if -2**31 < res < 2**31-1 else 0