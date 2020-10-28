class Solution:
    def climbStairs(self, n: int) -> int:
        self.count = 1
        num2 = n // 2
        def dp(n):
            if n == 1 or n == 0:
                return 1
            return n * dp(n-1)
        for i in range(1, num2 + 1):
            pos = n - i
            self.count += dp(pos)/((dp(i))*dp(pos-i))
        return int(self.count)



s = Solution()
print(s.climbStairs(4))
