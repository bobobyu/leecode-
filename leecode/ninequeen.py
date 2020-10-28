class Solution:
    def nine_queen(self):
        self.result: list = []
        def check(list_:list):
            for i in range(len(list_)):
                for j in range(i+1, len(list_)):
                    if abs(i-j) == abs(list_[i]-list_[j]):
                        return False
            return True
        def dp(sol: list, layer: int = 0):
            if layer < 8:
                for i in range(8):
                    if i not in sol:
                        dp(sol + [i], layer + 1)
            else:


                if check(sol):
                    self.result.append(sol)
        dp(sol=[])
        return self.result

s = Solution()
print(len(s.nine_queen()))
