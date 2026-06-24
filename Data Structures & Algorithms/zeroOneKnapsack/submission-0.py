class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        cache = [[-1] * (M + 1) for _ in range(N)]
        return self.helper(0, profit, weight, capacity, cache)
    
    def helper(self, i, profit, weight, capacity, cache):
        if i == len(profit):
            return 0
        
        if cache[i][capacity] != -1:
            return cache[i][capacity]

        cache[i][capacity] = self.helper(i + 1, profit, weight, capacity, cache)

        newcap = capacity - weight[i]
        if newcap >= 0:
            p = profit[i] + self.helper(i + 1, profit, weight, newcap, cache)
            cache[i][capacity] = max(cache[i][capacity], p)

        return cache[i][capacity]

