from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def dfs(i, current_sum):
            if current_sum == amount:
                return 1
            if current_sum > amount or i >= n:
                return 0
            take = dfs(i, current_sum+coins[i])
            skip = dfs(i+1, current_sum)
            return take+skip
        return dfs(0, 0)