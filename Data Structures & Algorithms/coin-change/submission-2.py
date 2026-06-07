from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        least = math.inf
        @cache
        def dfs(i, current_sum, num_coins, least):
            if i >= n or current_sum > amount:
                return least
            if current_sum == amount and num_coins < least:
                return num_coins
            return min(dfs(i, current_sum+coins[i], num_coins+1, least), dfs(i+1, current_sum, num_coins, least))
        least = dfs(0, 0, 0, least)
        return least if least != math.inf else -1