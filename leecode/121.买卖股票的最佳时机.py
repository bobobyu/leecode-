class Solution:
    def maxProfit(self, prices: list) -> int:
        min_price = prices[0]
        max_profit  = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
s =Solution()
print(s.maxProfit([7,1,5,3,6,4]))