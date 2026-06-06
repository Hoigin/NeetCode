from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, holding):
            if i >= n:
                return 0
            skip = dfs(i+1, holding)
            if holding:
                sell_now_revenue = dfs(i+2, not holding) + prices[i]
                return max(sell_now_revenue, skip)
            else:
                buy_now_revenue = dfs(i+1, not holding) - prices[i]
                return max(buy_now_revenue, skip)
        return dfs(0, False)
     
