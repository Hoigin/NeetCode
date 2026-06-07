from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return math.inf
            min_coins = math.inf
            for coin in coins:
                res = dfs(rem-coin)
                if res != math.inf:
                    min_coins = min(min_coins, 1+res)
            return min_coins
        res = dfs(amount)
        return res if res != math.inf else -1