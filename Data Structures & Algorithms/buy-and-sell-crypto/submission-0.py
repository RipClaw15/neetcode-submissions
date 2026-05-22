class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_d = 0
        for i,vi in enumerate(prices):
            for j,vj in enumerate(prices):
                if i == j or j < i:
                    continue
                if vj - vi > max_d:
                    max_d = vj - vi
        return max_d