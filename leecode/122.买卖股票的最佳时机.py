class Solution:
    def maxProfit(self, prices: list) -> int:
        purchase_time: int = 0
        sale_time :int = 1
        income:int = 0
        while prices[purchase_time] > prices[sale_time]:
            purchase_time += 1
            sale_time += 1
            if sale_time >= len(prices):
                return 0
        print(purchase_time, sale_time)
        while sale_time < len(prices):
            while prices[purchase_time] >= prices[sale_time]:
                sale_time += 1
                if sale_time == len(prices) - 1:
                    print('a')
                    return income + max(0, prices[sale_time] - prices[purchase_time])
            income += prices[sale_time] - prices[purchase_time]
            print(purchase_time, sale_time, income)
            purchase_time = sale_time + 1
            sale_time += 2
        return income

s = Solution()
print(s.maxProfit([1,2,3,4,5]))
