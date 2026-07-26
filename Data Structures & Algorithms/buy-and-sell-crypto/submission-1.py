class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        price = prices[0]
        for i in prices:
            if price < i:
                if max_p < i - price:
                    max_p = i - price
            if i < price:
                price = i
        return max_p