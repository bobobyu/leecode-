class Solution:
    def countPrimes(self, n: int) -> int:
        e = [1] * n
        e[0], e[1] = 0, 0
        for i in range(2, int(n ** 0.5) + 1):
            if e[i]:
                e[i ** 2: n:i] = [0] * ((n - 1 - i * i) // i + 1)
        return sum(e)


s = Solution()
print(s.countPrimes(50))
