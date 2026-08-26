class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        buy_price = prices[0]
        for i in prices:
            if max_p < i - buy_price:
                max_p = i - buy_price
            if i < buy_price:
                buy_price = i
        return max_p