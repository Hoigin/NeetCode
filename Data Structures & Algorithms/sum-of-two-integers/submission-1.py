class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF
        for i in range(32):
            abit = (a >> i) & 1
            bbit = (b >> i) & 1
            bit = abit ^ bbit ^ carry
            carry = (abit + bbit + carry) >= 2
            if bit:
                res |= (1 << i)
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        return res