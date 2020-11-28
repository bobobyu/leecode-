class Solution:
    def fib(self, n: int) -> int:
        t1 = 0
        t2 = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        for _ in range(n - 1):
            t1, t2 = t2, (t1 + t2) % (1e9 + 7)
        return int(t2)


s = Solution()
print(s.fib(45))
