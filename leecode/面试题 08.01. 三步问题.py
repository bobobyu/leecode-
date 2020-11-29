class Solution:
    def waysToStep(self, n: int) -> int:
        t = [1, 2, 4]
        if n <= 3:
            return t[n-1]
        else:
            t1, t2, t3 = t
            for i in range(n-3):
                t1, t2, t3 = t2, t3, (t1 + t2 + t3)%1000000007

            return t3

s = Solution()
print(s.waysToStep(900750))


'''

1

1 1
2

1 1 1
2 1
1 2
3

1 1 1 1
1 2 1
2 1 1
1 1 2
2 2
3 1
1 3

'''
