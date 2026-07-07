class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            tank = gas[i]
            for j in range(n+1):
                idx = (i + j) % n
                tank -= cost[idx]
                if tank < 0:
                    break
                tank += gas[(idx + 1) % n]
                if j == n:
                    return i
        return -1