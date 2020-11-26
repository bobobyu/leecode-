from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_list: List[int] = []
        i: int = 1
        while i < len(prices):
            sheet_profit: int = 0
            while i < len(prices) and prices[i] >= prices[i - 1]:
                sheet_profit += prices[i] - prices[i - 1]
                if prices[i] < prices[i - 1]:
                    break
                i += 1
            profit_list.append(sheet_profit)
            i += 1
        x = 0
        print(profit_list)
        if not profit_list:
            return 0
        for _ in range(2):
            x += max(profit_list)
            profit_list.remove(max(profit_list))
            if not profit_list:
                return x
        return x


s = Solution()
s.maxProfit([1, 2, 4,
             2, 5, 7,
             2, 4, 9,
             0])
