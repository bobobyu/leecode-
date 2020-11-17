class Solution:
    def sortArrayByParityII(self, A: list) -> list:
        even: list = [i for i in A if not i % 2]
        odd: list = [i for i in A if i % 2]
        res = []
        for i in zip(even, odd):
            res.append(i[0])
            res.append(i[1])
        return res
s = Solution()
print(s.sortArrayByParityII([4,2,5,7]))