from typing import *


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        d = [[0 for _ in range(len(prices))] for __ in range(2)]
        d[0][0], d[1][0] = 0, (-prices[0] - fee)
        for i in range(1, len(prices)):
            d[0][i] = max(prices[i] + d[1][i - 1], d[0][i - 1])
            d[1][i] = max(-prices[i] - fee + d[0][i - 1], d[1][i - 1])
        return max(d[1][-1], d[0][-1])


Solution().maxProfit(
[1,3,7,5,10,3],
3)
