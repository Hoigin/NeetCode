class Solution:
    def isHappy(self, n: int) -> bool:
        store = []
        while n != 1 and n not in store:
            store.append(n)
            n = sum([int(x)**2 for x in list(str(n))])
        return True if n==1 else False