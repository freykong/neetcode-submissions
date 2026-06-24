class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n, m = len(profit), capacity
        cache = [[-1] * (m + 1) for _ in range(n)]

        return self.helper(0, profit, weight, capacity, cache)

    def helper(self, i, profit, weight, capacity, cache):
        if i == len(profit):
            return 0
        
        if cache[i][capacity] != -1:
            return cache[i][capacity]
        
        cache[i][capacity] = self.helper(i + 1, profit, weight, capacity, cache)

        if capacity - weight[i] >= 0:
            newp = profit[i] + self.helper(i, profit, weight, capacity - weight[i], cache)
            cache[i][capacity] = max(cache[i][capacity], newp)
        
        return cache[i][capacity]

