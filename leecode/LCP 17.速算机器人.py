class Solution:
    def calculate(self, s: str) -> int:
        x: int = 1
        y: int = 0
        calculate_pattern: dict = {'A': lambda x: 2 * x + y,
                                   'B': lambda y: 2 * y + x, }
        for i in s:
            if i=='A':
                x = calculate_pattern[i](x)
            else:
                y = calculate_pattern[i](y)
        return x+y

s = Solution()
print(s.calculate('ABA'))
