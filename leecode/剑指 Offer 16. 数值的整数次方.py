class Solution:
    def myPow(self, x: float, n: int) -> float:
        def descending_power(x, n) -> float:
            if n == 0:
                return 1
            if n == 1:
                return x
            if n == -1:
                return 1/x
            if n & 1:
                y = descending_power(x, (n - (1 if n > 0 else -1)) >> 1)
                return (y * y * x) if n > 0 else y * y * (1/x)
            else:
                y = descending_power(x, n >> 1)
                return (y * y) if n > 0 else y * y

        return descending_power(x=x, n=n)


s = Solution()
import time

a = time.time()
print(s.myPow(2, -3))
