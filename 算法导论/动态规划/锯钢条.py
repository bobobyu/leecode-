class CUT_ROD:
    def __init__(self):
        self.prices_list: list = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        self.memory_dict: dict = {}
        self.MEMORY_LIST: list = [0] * (len(self.prices_list) + 1)
        self.SOLUTION:list = [0]  * (len(self.prices_list)+1)
        self.cost:int = 2


    def CUT_ROD(self,length:int)->int:
        if length == 0:
            return 0
        max_prices:float = -float('inf')
        for i in range(1, length+1):
            max_prices = max(max_prices, self.prices_list[i-1]+self.CUT_ROD(length - i))
        return int(max_prices)
    
    def CUT_ROD_MEMORY(self,length:int)->int:
        if length == 0:
            return 0
        prices = -float('inf')
        for i in range(1, length+1):
            if self.memory_dict.get(length - i):
                prices = max(prices, self.prices_list[i-1] + self.memory_dict[length-i])
            else:
                prices = max(prices, self.prices_list[i-1] + self.CUT_ROD_MEMORY(length - i))
        self.memory_dict[i] = prices
        print(self.memory_dict)
        return prices
    
    
    def CUT_ROD_MEMORY_II(self)->int:
        for i in range(1, len(self.prices_list)+1):
            prices = -float('inf')
            for j in range(1, i+1):
                prices = max(prices, self.prices_list[j-1]+self.MEMORY_LIST[i - j])
            self.MEMORY_LIST[i] = prices
        print(self.MEMORY_LIST)
        return self.MEMORY_LIST[-1]

    def CUT_ROD_MEMORY_PRINT_SOLUTION(self)->int:
        for i in range(1, len(self.prices_list)+1):
            prices = -float('inf')
            for j in range(1, i+1):
                if prices < self.prices_list[j-1]+self.MEMORY_LIST[i - j]:
                    prices = self.prices_list[j-1]+self.MEMORY_LIST[i - j]
                    self.SOLUTION[i] = j
            self.MEMORY_LIST[i] = prices
        print(self.MEMORY_LIST)
        print(self.SOLUTION)
        return self.MEMORY_LIST[-1]
    def CUT_ROD_WITH_COST(self):
        for i in range(1, len(self.prices_list)):
            prices = -float('inf')
            for j in range(1 ,i+1):
                if i!=j:
                    prices = max(prices, self.prices_list[j]+self.MEMORY_LIST[j - i] - self.cost)
                    continue
                prices = max(prices, self.prices_list[j] + self.MEMORY_LIST[j - i])# 长度相同等于没切，不用加上切割成本
            self.MEMORY_LIST[i] = prices

# CUT_ROD(10)
# CUT_ROD_MEMORY(10)
# CUT_ROD_MEMORY_II(10)
s = CUT_ROD()
s.CUT_ROD_MEMORY_PRINT_SOLUTION()



# print(CUT_ROD(10))