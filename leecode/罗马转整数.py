class Solution:
    def romanToInt(self, s: str):
        d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
             'CM': 800, 'M': 1000}
        result = []
        for i, j in enumerate(s):
            result.append(d.get(s[i-1:i+1], d[j]))
        return sum(result)

s = Solution()
print(s.romanToInt('MCMLXXXIV'))
